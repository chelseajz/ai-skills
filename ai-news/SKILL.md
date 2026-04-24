---
name: ai-news
version: "1.0.0"
description: AI 行业新闻聚合 — 从 18 个精选源（15 RSS + 3 WebSearch）抓取，覆盖大模型发布、研究突破、产品更新、中国 AI 实验室
homepage: https://github.com/tensakulabs/ai-news-skill
user-invocable: true
model: opus
effort: medium
context: fork
allowed-tools: WebFetch, WebSearch, Read, Write, Bash
---

# AI News Skill

从 18 个精选源（15 RSS + 3 WebSearch）抓取 AI 行业新闻，覆盖主要实验室的模型发布（GPT、Claude、Gemini、Grok、GLM、Llama）和中国 AI 实验室（智谱、DeepSeek、百度、阿里）的重要新闻。

## Feeds

### 聚合器（每日/每周摘要）
| 名称 | URL |
|------|-----|
| TLDR AI | https://tldr.tech/ai/rss |
| Hacker News | https://news.ycombinator.com/rss |
| The Decoder | https://the-decoder.com/feed/ |
| Last Week in AI | https://lastweekin.ai/feed |
| Marktechpost | https://www.marktechpost.org/feed/ |

### 实验室博客
| 名称 | URL |
|------|-----|
| Anthropic News | https://www.anthropic.com/news.xml |
| Claude Blog | https://blog.claude.ai/rss |
| Anthropic Red Team | https://www.anthropic.com/research.xml |
| OpenAI Research | https://openai.com/research/rss |
| xAI News | https://x.ai/blog/rss |
| Google AI | https://blog.google/technology/ai/rss/ |
| Claude Code Changelog | https://docs.anthropic.com/en/release-notes/api-changelog.xml |

### AI 编程工具
| 名称 | URL |
|------|-----|
| Cursor Blog | https://www.cursor.com/blog/rss.xml |
| Windsurf Blog | https://windsurf.com/blog/rss.xml |
| Ollama Blog | https://ollama.com/blog/rss.xml |

### 中国 AI 实验室（WebSearch 补充）
| 名称 | 抓取方式 | 搜索词 |
|------|----------|--------|
| DeepSeek | WebSearch | "DeepSeek 最新 发布" OR "deepseek release" |
| 智谱 AI | WebSearch | "智谱 AI" OR "zhipuai" 最新 |
| 百度 AI | WebSearch | "百度 AI" OR "baidu AI" 发布 |
| 阿里达摩院 | WebSearch | "达摩院" OR "damo academy" 最新 |

## Instructions

### Step 0: 幂等检查

如果用户要求保存且文件已存在（当日），直接返回缓存内容，注明 `(Cached — run with --regenerate to refresh)`。

### Step 1: 加载配置

读取 feeds.json（如果存在，用于覆盖上述默认配置）。

### Step 2: 并行抓取

使用 WebFetch 并行抓取所有 RSS 源：

```
WebFetch(url: "<rss_url>", prompt: "Extract all items. For each item return: title, link, pubDate, description")
```

优先抓取聚合器信源。

### Step 2.5: 中国 AI 实验室补充搜索

对每个中国 AI 实验室源执行 WebSearch：

```
WebSearch(query: "DeepSeek 最新 发布", allowed_domains: ["36kr.com", "jiemian.com", "huxiu.com"])
WebSearch(query: "智谱 AI 最新", allowed_domains: ["36kr.com", "jiemian.com", "huxiu.com"])
```

将搜索结果与 RSS 结果合并，进行去重和分类。

### Step 3: 解析 RSS

从 XML 中提取 `<item>` 或 `<entry>` 元素：
- 标题：`<title>`
- 链接：`<link>`
- 日期：`<pubDate>` 或 `<published>`
- 摘要：`<description>` 或 `<summary>`

### Step 4: 时间过滤

计算 `cutoff = 当前时间 - 86400 秒（24小时）`。排除早于 cutoff 的条目。

周报模式（用户说 "week" 或 "last 7 days"）：使用 604800 秒。

### Step 5: 去重

同一故事可能出现在多个源。去重规则：
1. 精确标题匹配 → 合并
2. 标题相似度 >80% → 合并
3. 同 URL → 保留信息量最大的版本

保留优先级最高的源版本。

### Step 6: 分类

| 类别 | 关键词 |
|------|--------|
| 模型发布 | release, launch, announce, 模型名（GPT, Claude, Gemini, Grok, GLM, Llama） |
| 研究 | paper, research, study, benchmark |
| 行业 | funding, acquisition, hire, layoff, IPO |
| 产品 | feature, update, API, pricing |
| 观点 | think, believe, future, prediction |

### Step 7: 格式化输出

```markdown
# AI News Briefing
**日期:** YYYY-MM-DD
**信源:** N 个源已检查
**时间范围:** 过去 24 小时

---

## 模型发布
1. **[标题](链接)** — 一句话摘要。来源
2. ...

## 研究
1. **[标题](链接)** — 一句话摘要。来源
...

## 行业
...

## 产品更新
...

---

**覆盖缺口:** 中国 AI 实验室（智谱、DeepSeek、百度、阿里）不发布 RSS。请手动检查重大发布。
```

### Step 8: 错误处理

某个源抓取失败：
- 记录错误
- 继续处理其余源
- 在输出中标注失败源
