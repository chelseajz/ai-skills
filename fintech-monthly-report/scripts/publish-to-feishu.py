#!/usr/bin/env python3
"""
飞书文档发布脚本 — 将 Fintech 月报发布到飞书云文档

用法:
    python publish-to-feishu.py YYYYMM [--folder-token TOKEN] [--title "自定义标题"]

流程:
    1. 获取/刷新 Feishu Tenant Access Token
    2. 读取 Markdown 报告
    3. 创建飞书文档
    4. 将 Markdown 内容转换为飞书文档块并写入
    5. 输出文档 URL

依赖:
    - FEISHU_APP_ID / FEISHU_APP_SECRET 环境变量
    - lark-cli 或 curl
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# ===== 配置 =====
BASE_DIR = Path(os.path.expanduser("~/.claude/fintech-reports"))
OUTPUT_DIR = BASE_DIR / "output"
TOKEN_CACHE_FILE = BASE_DIR / "data" / ".feishu-token-cache.json"

# 飞书应用凭证（从环境变量读取，或 fallback 到 skill 定义中的值）
FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID", "cli_a94e2de491b8dcb3")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET", "3E18dhBDvPmNrCI820YiAhWFDnyIxqTs")


def log(msg):
    print(f"[feishu] {msg}")


def get_token():
    """获取 Feishu Tenant Access Token，带缓存"""
    # 尝试读取缓存
    if TOKEN_CACHE_FILE.exists():
        try:
            cache = json.loads(TOKEN_CACHE_FILE.read_text())
            if time.time() < cache.get("expires_at", 0):
                log(f"使用缓存 Token (剩余 {int(cache['expires_at'] - time.time())}s)")
                return cache["token"]
        except (json.JSONDecodeError, KeyError):
            pass

    # 请求新 Token
    log("请求新 Tenant Access Token...")
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-X", "POST",
                "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
                "-H", "Content-Type: application/json",
                "-d", json.dumps({
                    "app_id": FEISHU_APP_ID,
                    "app_secret": FEISHU_APP_SECRET
                })
            ],
            capture_output=True, text=True, timeout=30
        )
        resp = json.loads(result.stdout)
        if resp.get("code") != 0:
            raise RuntimeError(f"获取 Token 失败: {resp}")

        token = resp["tenant_access_token"]
        expires_in = resp.get("expire", 7200)

        # 缓存 Token（提前 5 分钟过期）
        TOKEN_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        cache = {
            "token": token,
            "expires_at": time.time() + expires_in - 300
        }
        TOKEN_CACHE_FILE.write_text(json.dumps(cache))
        log(f"Token 已获取，有效期 {expires_in}s")
        return token

    except subprocess.TimeoutExpired:
        raise RuntimeError("请求 Token 超时")
    except FileNotFoundError:
        raise RuntimeError("curl 未安装，无法请求 Token")


def feishu_api(method, path, token, data=None):
    """通用飞书 API 调用（通过 lark-cli 或 curl）"""
    headers = {"Authorization": f"Bearer {token}"}

    try:
        # 优先使用 lark-cli
        cmd = [
            os.path.expanduser("~/.local/bin/lark-cli"),
            "api", method, path,
            "--format", "json"
        ]
        if data:
            cmd.extend(["--data", json.dumps(data, ensure_ascii=False)])

        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=60,
            env={**os.environ, "HOME": os.path.expanduser("~")}
        )
        resp = json.loads(result.stdout)
        if resp.get("code") != 0:
            raise RuntimeError(f"API 调用失败 {method} {path}: {resp}")
        return resp
    except (FileNotFoundError, Exception):
        # Fallback 到 curl
        url = f"https://open.feishu.cn{path}"
        curl_cmd = ["curl", "-s", "-X", method, url,
                    "-H", f"Authorization: Bearer {token}",
                    "-H", "Content-Type: application/json"]
        if data:
            curl_cmd.extend(["-d", json.dumps(data, ensure_ascii=False)])

        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=60)
        resp = json.loads(result.stdout)
        if resp.get("code") != 0:
            raise RuntimeError(f"API 调用失败 {method} {path}: {resp}")
        return resp


# ===== Markdown → Feishu Block 转换 =====

def parse_markdown_to_blocks(md_content):
    """将 Markdown 内容解析为飞书文档块列表"""
    blocks = []
    lines = md_content.split("\n")
    current_list = []
    in_code_block = False
    code_content = []
    code_lang = ""

    for line in lines:
        # 代码块处理
        if line.strip().startswith("```"):
            if in_code_block:
                # 代码块结束
                if code_content:
                    blocks.append({
                        "block_type": 14,  # Code
                        "code": {
                            "elements": [{"text": "\n".join(code_content)}],
                            "style": {"language": code_lang or "text"}
                        }
                    })
                in_code_block = False
                code_content = []
                code_lang = ""
            else:
                # 代码块开始
                lang = line.strip().replace("```", "").strip()
                in_code_block = True
                code_lang = lang
            continue

        if in_code_block:
            code_content.append(line)
            continue

        # 标题
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = min(len(heading_match.group(1)), 6)
            text = heading_match.group(2).strip()
            blocks.append({
                "block_type": 2,  # Heading
                "heading": {
                    "elements": [{"text": text}],
                    "level": level
                }
            })
            continue

        # 分隔线
        if re.match(r'^---+\s*$', line):
            blocks.append({
                "block_type": 6,  # Hr
                "hr": {}
            })
            continue

        # 引用块
        quote_match = re.match(r'^>\s*(.*)', line)
        if quote_match:
            blocks.append({
                "block_type": 4,  # Quote
                "quote": {
                    "elements": [{"text": quote_match.group(1)}]
                }
            })
            continue

        # 无序列表
        list_match = re.match(r'^[-*]\s+(.+)$', line)
        if list_match:
            current_list.append(list_match.group(1))
            continue
        else:
            if current_list:
                blocks.append({
                    "block_type": 12,  # Bullet
                    "bullet": {
                        "elements": [{"text": ", ".join(current_list)}]
                    }
                })
                current_list = []

        # 有序列表
        ol_match = re.match(r'^\d+\.\s+(.+)$', line)
        if ol_match:
            blocks.append({
                "block_type": 13,  # Ordered
                "ordered": {
                    "elements": [{"text": ol_match.group(1)}]
                }
            })
            continue

        # 空行
        if not line.strip():
            continue

        # 普通文本（支持基本 Markdown 格式）
        elements = parse_inline_markdown(line)
        if elements:
            blocks.append({
                "block_type": 1,  # Text
                "text": {
                    "elements": elements
                }
            })

    # 处理未闭合的列表
    if current_list:
        blocks.append({
            "block_type": 12,
            "bullet": {
                "elements": [{"text": ", ".join(current_list)}]
            }
        })

    return blocks


def parse_inline_markdown(text):
    """解析行内 Markdown 格式（粗体、斜体、代码、链接）"""
    elements = []
    # 简单的行内解析：按 ** 分割粗体
    parts = re.split(r'(\*\*[^*]+\*\*|`[^`]+`|[^*`]+)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            elements.append({"text": part[2:-2], "text_style": {"bold": True}})
        elif part.startswith("`") and part.endswith("`"):
            elements.append({"text": part[1:-1], "text_style": {"inline_code": True}})
        else:
            # 处理斜体 *text*
            sub_parts = re.split(r'(\*[^*]+\*)', part)
            for sp in sub_parts:
                if not sp:
                    continue
                if sp.startswith("*") and sp.endswith("*"):
                    elements.append({"text": sp[1:-1], "text_style": {"italic": True}})
                else:
                    elements.append({"text": sp})
    return elements if elements else [{"text": text}]


# ===== 文档操作 =====

def create_document(token, title):
    """创建飞书文档"""
    log(f"创建文档: {title}")
    resp = feishu_api(
        "POST",
        "/open-apis/docx/v1/documents",
        token,
        data={"title": title}
    )
    doc = resp["data"]["document"]
    doc_id = doc["document_id"]
    log(f"文档已创建: {doc_id}")
    return doc_id


def get_root_block_id(token, doc_id):
    """获取文档根块 ID"""
    resp = feishu_api(
        "GET",
        f"/open-apis/docx/v1/documents/{doc_id}/blocks/root",
        token
    )
    return resp["data"]["block"]["block_id"]


def append_blocks(token, doc_id, parent_block_id, blocks):
    """批量追加块到文档"""
    # 飞书 API 支持一次追加多个块
    children = []
    for block in blocks:
        child = {"block_type": block["block_type"]}
        # 根据 block_type 添加对应字段
        for key, value in block.items():
            if key != "block_type":
                child[key] = value
        children.append(child)

    resp = feishu_api(
        "POST",
        f"/open-apis/docx/v1/documents/{doc_id}/blocks/{parent_block_id}/children",
        token,
        data={"children": children}
    )
    return resp["data"]


def publish_report(yyyy, mm, custom_title=None, folder_token=None):
    """主发布流程"""
    # 1. 读取 Markdown 报告
    md_path = OUTPUT_DIR / f"fintech-report-{yyyy}{mm}.md"
    if not md_path.exists():
        print(f"错误: Markdown 报告不存在: {md_path}")
        print("请先完成报告生成阶段。")
        sys.exit(1)

    md_content = md_path.read_text(encoding="utf-8")
    log(f"读取报告: {md_path.name} ({len(md_content)} 字符)")

    # 2. 获取 Token
    token = get_token()

    # 3. 创建文档
    title = custom_title or f"全球金融科技月度报告 {yyyy}年{int(mm)}月"
    doc_id = create_document(token, title)

    # 4. 获取根块 ID
    root_block_id = get_root_block_id(token, doc_id)

    # 5. 解析并追加块
    # 分批追加（飞书 API 单次最多 50 块）
    blocks = parse_markdown_to_blocks(md_content)
    log(f"解析到 {len(blocks)} 个文档块")

    batch_size = 50
    total_batches = (len(blocks) + batch_size - 1) // batch_size
    for i in range(0, len(blocks), batch_size):
        batch = blocks[i:i + batch_size]
        batch_num = i // batch_size + 1
        log(f"写入第 {batch_num}/{total_batches} 批 ({len(batch)} 块)")
        append_blocks(token, doc_id, root_block_id, batch)

    # 6. 输出文档 URL
    doc_url = f"https://bytedance.larkoffice.com/docx/{doc_id}"
    print()
    print("=" * 60)
    print(f"飞书文档发布完成!")
    print(f"标题: {title}")
    print(f"文档: {doc_url}")
    print(f"块数: {len(blocks)}")
    print("=" * 60)

    return doc_url


def main():
    # 解析参数
    args = sys.argv[1:]
    yyyy_mm = None
    custom_title = None
    folder_token = None

    i = 0
    while i < len(args):
        if args[i] == "--folder-token" and i + 1 < len(args):
            folder_token = args[i + 1]
            i += 2
        elif args[i] == "--title" and i + 1 < len(args):
            custom_title = args[i + 1]
            i += 2
        elif yyyy_mm is None:
            yyyy_mm = args[i]
            i += 1
        else:
            i += 1

    if not yyyy_mm:
        print("用法: python publish-to-feishu.py YYYYMM [--title '标题'] [--folder-token TOKEN]")
        print("示例: python publish-to-feishu.py 202604")
        sys.exit(1)

    yyyy = yyyy_mm[:4]
    mm = yyyy_mm[4:]

    try:
        publish_report(yyyy, mm, custom_title, folder_token)
    except Exception as e:
        print(f"\n发布失败: {e}")
        print("\n提示: 请检查")
        print("  1. FEISHU_APP_ID / FEISHU_APP_SECRET 环境变量是否正确")
        print("  2. 飞书应用权限是否包含 docx:document:write")
        print("  3. lark-cli 是否正常工作 (~/.local/bin/lark-cli --version)")
        sys.exit(1)


if __name__ == "__main__":
    main()
