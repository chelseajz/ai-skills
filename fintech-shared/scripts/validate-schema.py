#!/usr/bin/env python3
"""
Phase 间 JSON 文件 Schema 校验
在每步开始前验证中间文件的结构完整性，防止下游静默失败。
"""

import json
import sys
import os
from pathlib import Path

BASE_DIR = Path(os.path.expanduser("~/.claude/fintech-reports"))
LOGS_DIR = BASE_DIR / "logs"
CONFIG_PATH = Path(__file__).parent.parent / "fintech-shared" / "config.json"


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在: {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失败: {path} — {e}")
        return None


def validate_phase3(data):
    """验证 Phase 3 输出（phase3-unique-events.json）"""
    errors = []
    required_top = ["target_month", "total_events", "events"]
    for key in required_top:
        if key not in data:
            errors.append(f"缺少顶层字段: {key}")
    if errors:
        return errors

    if not isinstance(data["events"], list):
        errors.append("events 必须是数组")
        return errors

    if len(data["events"]) == 0:
        print("⚠️  events 为空数组（本月无事件）")
        return errors

    event_required = ["title", "date", "url"]
    for i, event in enumerate(data["events"][:5]):  # 抽检前 5 条
        for key in event_required:
            if key not in event:
                errors.append(f"事件[{i}] 缺少字段: {key}")
        if "date" in event:
            d = str(event["date"])
            if len(d) < 8 or d.count("-") < 2:
                errors.append(f"事件[{i}] 日期格式异常: {d}")
        if "url" in event:
            if not str(event["url"]).startswith("http"):
                errors.append(f"事件[{i}] URL 不是有效 http 链接: {event['url']}")
    if len(data["events"]) > 5:
        print(f"  （抽检前 5/{len(data['events'])} 条事件，其余跳过）")
    return errors


def validate_phase4(data):
    """验证 Phase 4 输出（phase4-scored-events.json）"""
    errors = []
    required_top = ["target_month", "total_events", "events"]
    for key in required_top:
        if key not in data:
            errors.append(f"缺少顶层字段: {key}")
    if errors:
        return errors

    if not isinstance(data["events"], list):
        errors.append("events 必须是数组")
        return errors

    for i, event in enumerate(data["events"][:5]):
        if "score" not in event:
            errors.append(f"事件[{i}] 缺少 score 字段")
        elif not isinstance(event["score"], (int, float)):
            errors.append(f"事件[{i}] score 不是数字: {event['score']}")
        if "score_reasons" not in event:
            errors.append(f"事件[{i}] 缺少 score_reasons 字段（不可追溯）")
        elif not isinstance(event["score_reasons"], dict):
            errors.append(f"事件[{i}] score_reasons 不是对象")
    return errors


def validate_phase2_batch(data, batch_label):
    """验证单个 Phase 2 Batch 文件"""
    errors = []
    required_top = ["batch", "queries_executed", "results", "all_events", "sentinel"]
    for key in required_top:
        if key not in data:
            errors.append(f"Batch {batch_label} 缺少字段: {key}")
    if not isinstance(data.get("results"), list):
        errors.append(f"Batch {batch_label} results 必须是数组")
    if not isinstance(data.get("all_events"), list):
        errors.append(f"Batch {batch_label} all_events 必须是数组")
    return errors


def validate_phase2_aggregated(data):
    """验证 Phase 2 聚合文件（phase2-secondary-sources.json）"""
    errors = []
    required_top = ["target_month", "total_queries_executed", "results", "all_events"]
    for key in required_top:
        if key not in data:
            errors.append(f"缺少顶层字段: {key}")
    if errors:
        return errors

    expected = 128
    actual = data.get("total_queries_executed", 0)
    if actual < expected:
        errors.append(f"查询数不足: {actual}/{expected}（部分 Agent 可能失败）")
    if not isinstance(data.get("all_events"), list):
        errors.append("all_events 必须是数组")
    return errors


def validate_phase1(data):
    """验证 Phase 1 输出（phase1-primary-sources.json）"""
    errors = []
    if not isinstance(data, dict):
        errors.append("phase1 文件必须是 JSON 对象")
        return errors
    # 允许纯 events 数组格式或带 sources 的对象格式
    if "events" in data:
        if not isinstance(data["events"], list):
            errors.append("events 必须是数组")
    elif "sources" in data:
        for source_name, source_data in data["sources"].items():
            if not isinstance(source_data.get("events", []), list):
                errors.append(f"sources.{source_name}.events 必须是数组")
    return errors


SCHEMAS = {
    "phase1": validate_phase1,
    "phase2_batch": validate_phase2_batch,
    "phase2": validate_phase2_aggregated,
    "phase3": validate_phase3,
    "phase4": validate_phase4,
}


def main():
    if len(sys.argv) < 3:
        print("用法: python validate-schema.py <phase> <path> [batch_label]")
        print("示例: python validate-schema.py phase3 ~/.claude/fintech-reports/logs/phase3-unique-events.json")
        print("示例: python validate-schema.py phase2_batch ~/.claude/fintech-reports/logs/phase2-batch-1-2.json batch-1-2")
        sys.exit(1)

    phase = sys.argv[1]
    path = Path(sys.argv[2]).expanduser()
    batch_label = sys.argv[3] if len(sys.argv) > 3 else ""

    if phase not in SCHEMAS:
        print(f"❌ 未知阶段: {phase}（可选: {', '.join(SCHEMAS.keys())}）")
        sys.exit(1)

    data = load_json(path)
    if data is None:
        sys.exit(1)

    validator = SCHEMAS[phase]
    if phase == "phase2_batch":
        errors = validator(data, batch_label)
    else:
        errors = validator(data)

    if errors:
        print(f"❌ {path.name} schema 校验失败:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"✅ {path.name} schema 校验通过")
        if isinstance(data, dict):
            if "total_events" in data:
                print(f"  事件数: {data['total_events']}")
            elif "total_queries_executed" in data:
                print(f"  查询数: {data['total_queries_executed']}/128")
            elif "events" in data and isinstance(data["events"], list):
                print(f"  事件数: {len(data['events'])}")
            elif "all_events" in data and isinstance(data["all_events"], list):
                print(f"  事件数: {len(data['all_events'])}")
        sys.exit(0)


if __name__ == "__main__":
    main()
