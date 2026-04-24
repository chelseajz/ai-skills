#!/usr/bin/env python3
"""
质量校验自动化脚本 - 确保报告生成完整
检查项：
1. Markdown 报告完整性检查
2. HTML 占位符完整性检查
3. 事件数量检查
4. 抽检 URL 可访问性
"""

import json
import sys
import os
import re
import subprocess
from pathlib import Path

# 配置
BASE_DIR = Path(os.path.expanduser("~/.claude/fintech-reports"))
OUTPUT_DIR = BASE_DIR / "output"
LOGS_DIR = BASE_DIR / "logs"

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def check_markdown_report(yyyy, mm):
    """检查 Markdown 报告"""
    md_path = OUTPUT_DIR / f"fintech-report-{yyyy}{mm}.md"
    if not md_path.exists():
        return False, [f"❌ Markdown 文件不存在: {md_path}"]

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = []
    all_passed = True

    # 1. 检查必要章节
    required_sections = [
        ("包含核心结论", "## 核心结论" in content or "Executive Summary" in content),
        ("包含宏观指标", "## 全球宏观指标" in content or "Mermaid" in content),
        ("包含核心拐点分析", "## 核心拐点" in content or "深度分析" in content),
        ("包含趋势判断", "## 趋势判断" in content or "非共识观察" in content),
        ("包含信源统计", "## 信源质量统计" in content),
        ("包含字节财经竞争态势总结", "字节财经月度竞争态势总结" in content or "竞争态势总结" in content or "威胁与机会矩阵" in content),
    ]

    for name, passed in required_sections:
        if not passed:
            checks.append(f"❌ 缺失章节: {name}")
            all_passed = False
        else:
            checks.append(f"✅ {name}")

    # 2. 检查占位符
    placeholders = ["[待填写]", "TODO", "{{", "}}"]
    for ph in placeholders:
        if ph in content:
            checks.append(f"❌ 发现未替换占位符: {ph}")
            all_passed = False

    # 3. 检查最小长度
    if len(content) < 2000:
        checks.append(f"⚠️  报告过短 ({len(content)} 字符)，可能内容不完整")

    return all_passed, checks

def check_html_report(yyyy, mm):
    """检查 HTML 报告 - 确保所有占位符都被替换"""
    html_path = OUTPUT_DIR / f"fintech-report-{yyyy}{mm}.html"
    if not html_path.exists():
        return False, [f"❌ HTML 文件不存在: {html_path}"]

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = []
    all_passed = True

    # 查找所有占位符 {{...}}
    placeholder_pattern = r'{{[^}]+}}'
    placeholders = re.findall(placeholder_pattern, content)

    if placeholders:
        unique_ph = list(set(placeholders))
        all_passed = False
        if len(unique_ph) <= 10:
            checks.append(f"❌ 发现 {len(unique_ph)} 个未替换占位符: {', '.join(unique_ph)}")
        else:
            checks.append(f"❌ 发现 {len(unique_ph)} 个未替换占位符: {', '.join(unique_ph[:10])}")
            checks.append(f"   ...还有 {len(unique_ph) - 10} 个未列出")
    else:
        checks.append("✅ 所有占位符已替换")

    # 检查年月替换
    expected = f"{yyyy}年{int(mm)}月"
    if expected not in content:
        checks.append(f"❌ 年月未正确替换，未找到: {expected}")
        all_passed = False
    else:
        checks.append(f"✅ 年月正确替换: {expected}")

    # 检查中文内容（事件标题中是否包含中文）
    # 提取所有事件标题
    event_titles = re.findall(r'<div class="event-title">.*?</div>', content)
    if event_titles:
        # 检查是否有纯英文标题（不含任何中文字符）
        pure_en_titles = []
        for t in event_titles:
            clean = re.sub(r'<[^>]+>', '', t).strip()
            # 检查是否包含中文字符
            if not re.search(r'[\u4e00-\u9fff]', clean):
                pure_en_titles.append(clean[:80])
        if pure_en_titles:
            checks.append(f"❌ 发现 {len(pure_en_titles)} 个纯英文事件标题（应翻译为中文）")
            for t in pure_en_titles[:3]:
                checks.append(f"   示例: {t}")
            all_passed = False
        else:
            checks.append("✅ 所有事件标题均包含中文")
    else:
        checks.append("⚠️  未找到事件标题（可能结构不同）")

    # 检查重点事件引言
    focus_event_count = 0
    phase3_path = LOGS_DIR / "phase3-unique-events.json"
    if phase3_path.exists():
        phase3 = load_json(phase3_path)
        if phase3 and 'events' in phase3:
            focus_event_count = sum(1 for e in phase3['events'] if e.get('score', 0) >= 80)

    if focus_event_count > 0:
        quote_blocks = re.findall(r'<div class="quote-block', content)
        if len(quote_blocks) < focus_event_count:
            checks.append(f"⚠️  重点事件引言不足：应有 {focus_event_count} 个引言，仅找到 {len(quote_blocks)} 个")
        else:
            checks.append(f"✅ 重点事件引言数量达标（{len(quote_blocks)} 个，应 ≥ {focus_event_count}）")

    # 检查关键 JS 函数是否存在（防止 JS 错误导致功能失效）
    if 'function switchTab' in content:
        if 'event.target' in content and 'function switchTab(tabId) {' in content:
            # 检查是否使用了废弃的 event.target 而没有传参
            if re.search(r'function switchTab\(tabId\)\s*\{[^}]*event\.target', content):
                checks.append("❌ switchTab 函数使用了废弃的 event.target，Tab 切换将失效")
                all_passed = False
            else:
                checks.append("✅ switchTab 函数签名正确")
        else:
            checks.append("✅ switchTab 函数存在")

    if 'function initWorldMap' in content:
        if 'typeof d3' in content or 'typeof d3' in content:
            checks.append("✅ initWorldMap 包含 D3.js 可用性检查")
        else:
            checks.append("⚠️  initWorldMap 缺少 D3.js 可用性检查（CDN 被屏蔽时地图将崩溃）")

    return all_passed, checks

def check_event_counts():
    """检查事件数量"""
    phase3 = LOGS_DIR / "phase3-unique-events.json"
    if not phase3.exists():
        return False, ["❌ phase3-unique-events.json 不存在"]

    data = load_json(phase3)
    if not data or 'events' not in data:
        return False, ["❌ phase3 文件格式错误"]

    events = data['events']
    checks = []
    all_passed = True

    total = len(events)
    primary = sum(1 for e in events if e.get('source_level', 99) == 1)

    checks.append(f"📊 总事件数: {total}")
    checks.append(f"📊 一级信源: {primary}")

    if total < 10:
        checks.append("⚠️  总事件数过少 (< 10)，报告可能内容不足")
        # 不失败，但警告
    if primary < 3:
        checks.append("⚠️  一级信源过少 (< 3)，可能遗漏重要监管动态")
        # 不失败，但警告

    return all_passed, checks

def check_trend_tracker():
    """检查趋势追踪文件是否已更新"""
    data_dir = BASE_DIR / "data"
    trend_path = data_dir / "trend-tracker.json"
    if not trend_path.exists():
        return True, ["⚠️  trend-tracker.json 不存在（首次运行或跨月追踪未启用）"]
    data = load_json(trend_path)
    if not data or 'trends' not in data:
        return False, ["❌ trend-tracker.json 格式错误"]
    trend_count = len(data.get('trends', []))
    return True, [f"✅ trend-tracker.json 已更新 ({trend_count} 条趋势)"]

def check_phase_logs():
    """检查各阶段日志是否都生成"""
    required_logs = [
        "phase1-primary-sources.json",
        "phase2-secondary-sources.json",
        "phase3-unique-events.json",
        "phase4-scored-events.json",
        "phase5-analysis.md",
    ]

    checks = []
    all_passed = True

    for log_file in required_logs:
        path = LOGS_DIR / log_file
        if not path.exists():
            checks.append(f"❌ 缺失阶段日志: {log_file}")
            all_passed = False
        elif path.stat().st_size == 0:
            checks.append(f"❌ 阶段日志为空: {log_file}")
            all_passed = False
        else:
            checks.append(f"✅ {log_file} 已生成 ({path.stat().st_size} 字节)")

    # 额外检查：Phase 2 搜索结果数量
    phase2_path = LOGS_DIR / "phase2-secondary-sources.json"
    if phase2_path.exists():
        data = load_json(phase2_path)
        if data and 'results' in data:
            count = len(data['results'])
            queries_expected = 128
            checks.append(f"📊 Phase 2 搜索结果数: {count}/{queries_expected} 个查询")
            if count < queries_expected:
                checks.append(f"⚠️  仅完成 {count}/{queries_expected} 个搜索，有查询被跳过")
                # 不失败，但警告

    return all_passed, checks

def sample_url_checks(yyyy, mm, sample_size=10):
    """抽检 URL 可访问性"""
    md_path = OUTPUT_DIR / f"fintech-report-{yyyy}{mm}.md"
    if not md_path.exists():
        return True, [f"⚠️  无法抽检: Markdown 不存在"]

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取所有 URL
    urls = re.findall(r'https?://[^\s\)\]]+', content)
    if not urls:
        return True, ["⚠️  未找到 URL 抽检"]

    import random
    sample = random.sample(urls, min(sample_size, len(urls)))

    checks = []
    failed = 0

    for url in sample:
        try:
            result = subprocess.run(
                ['curl', '-I', '-s', '-m', '10', url],
                capture_output=True,
                timeout=15
            )
            if result.returncode == 0 and result.stdout:
                first_line = result.stdout.decode('utf-8', errors='ignore').split('\n')[0]
                if '200' in first_line or '201' in first_line or '301' in first_line or '302' in first_line:
                    checks.append(f"✅ {url[:60]}... → {first_line.strip()}")
                else:
                    checks.append(f"⚠️  {url[:60]}... → {first_line.strip()}")
            else:
                checks.append(f"⚠️  {url[:60]}... → 连接失败")
        except Exception as e:
            checks.append(f"⚠️  {url[:60]}... → {str(e)[:50]}")

    return True, checks

def main():
    # 获取年月参数
    if len(sys.argv) != 2:
        print("用法: python validate-report.py YYYYMM")
        print("示例: python validate-report.py 202604")
        sys.exit(1)

    yyyymm = sys.argv[1]
    yyyy = yyyymm[:4]
    mm = yyyymm[4:]

    print("=" * 60)
    print(f"Fintech 月报质量校验 - {yyyy}年{int(mm)}月")
    print("=" * 60)

    # 依次执行各项检查
    all_checks_passed = True

    print("\n📋 阶段日志检查:")
    print("-" * 60)
    passed, checks = check_phase_logs()
    for check in checks:
        print(f"  {check}")
    all_checks_passed = all_checks_passed and passed

    print("\n📄 Markdown 报告检查:")
    print("-" * 60)
    passed, checks = check_markdown_report(yyyy, mm)
    for check in checks:
        print(f"  {check}")
    all_checks_passed = all_checks_passed and passed

    print("\n🌐 HTML 报告检查:")
    print("-" * 60)
    passed, checks = check_html_report(yyyy, mm)
    for check in checks:
        print(f"  {check}")
    all_checks_passed = all_checks_passed and passed

    print("\n🔢 事件数量统计:")
    print("-" * 60)
    passed, checks = check_event_counts()
    for check in checks:
        print(f"  {check}")
    # 数量检查只是警告，不影响整体结果

    print("\n🔍 URL 抽检:")
    print("-" * 60)
    passed, checks = sample_url_checks(yyyy, mm)
    for check in checks:
        print(f"  {check}")

    print("\n📈 趋势追踪检查:")
    print("-" * 60)
    passed, checks = check_trend_tracker()
    for check in checks:
        print(f"  {check}")
    # 趋势追踪只是警告，不影响整体结果

    print("\n" + "=" * 60)
    if all_checks_passed:
        print("✅ 所有强制检查通过！")
        sys.exit(0)
    else:
        print("❌ 存在检查失败，请修复问题后重新生成")
        sys.exit(1)

if __name__ == "__main__":
    main()
