---
name: fintech-monthly-report
version: "4.2-orchestrator"
description: Fintech 月报编排器 — 协调三个子 skill 完成搜索、分析、报告生成全流程
argument-hint: "YYYY年MM月 [--checkpoint|-c]"
user-invocable: true
model: opus
effort: high
context: isolated
allowed-tools: WebSearch, WebFetch, Read, Bash, Write, Skill
---

# Fintech 月报编排器 Skill

> **本 skill 是三个子 skill 的编排入口，不直接执行搜索/分析/生成。**
>
> **子 skill**：
> - `/fintech-research` — Phase 1-3（纯搜索，支持并行 + 两阶段抓取 + 跨信号放大）+ Phase 2.5（头部公司追踪）
> - `/fintech-analysis` — Phase 4-5（评分 + 深度分析 + 跨月趋势追踪续接 + 头部公司分析）
> - `/fintech-report-gen` — Phase 6-8（Markdown + HTML + 校验 + 动态折叠）+ Phase 9（飞书发布）
>
> **路径配置**：所有共享文件（knowledge-base / reference / scripts / examples）位于本 skill 根目录下，子 skill 通过 `../../` 相对路径引用。本 skill 为完整自包含包，可直接打包参赛。

---

## 执行模式

### 模式一：full（完整流程，默认）

```
/fintech-monthly-report 2026年4月
```
无模式参数时默认 full 模式。**全自动执行，三步连续运行，无需人工干预。**

**执行流程**：
1. 调用 `/fintech-research 2026年4月` → 等待完成
2. 自动验证 `phase3-unique-events.json` schema：`python3 scripts/validate-schema.py phase3 ~/.claude/fintech-reports/logs/phase3-unique-events.json`
3. 调用 `/fintech-analysis 2026年4月` → 等待完成
4. 自动验证 `phase4-scored-events.json` schema：`python3 scripts/validate-schema.py phase4 ~/.claude/fintech-reports/logs/phase4-scored-events.json`
5. 自动调用 `/fintech-report-gen 2026年4月` → 等待完成
6. 输出最终报告路径和校验结果

### 模式二：checkpoint（人工检查点模式）

```
/fintech-monthly-report 2026年4月 --checkpoint
```
或
```
/fintech-monthly-report 2026年4月 -c
```

**执行流程**：
1. 调用 `/fintech-research 2026年4月` → 等待完成
2. 自动验证 `phase3-unique-events.json` schema
3. 自动调用 `/fintech-analysis 2026年4月` → 等待完成
4. 自动验证 `phase4-scored-events.json` schema
5. **暂停，提示用户检查结果**
6. 用户确认后，手动调用 `/fintech-report-gen 2026年4月`

> **为什么需要 checkpoint 模式？**：分析结果需要人工审阅确认方向后再决定生成报告，避免错误的分析被直接发布。full 模式适合已知数据质量好的月份，checkpoint 模式适合需要人工介入的月份。

### 模式三：report（仅报告生成）

```
/fintech-monthly-report 2026年4月 report
```

**执行流程**：
- 验证 `phase4-scored-events.json` 和 `phase5-analysis.md` 存在
- 调用 `/fintech-report-gen 2026年4月`
- 适用于分析阶段已完成、重新生成报告或修复报告格式的场景

### 模式四：search（仅搜索）

```
/fintech-monthly-report 2026年4月 search
```

**执行流程**：
- 调用 `/fintech-research 2026年4月`
- 完成后提示执行分析

## 各子 skill 职责概览

| 子 Skill | 职责 | 输入 | 输出 | 核心改进 |
|---------|------|------|------|---------|
| `/fintech-research` | 搜索 + 聚合 + 去重 + 公司追踪 | 年月参数 | `phase3-unique-events.json` + `phase2.5-company-research.json` | 4 Agent 并行 + 两阶段抓取 + 跨信号放大 + **头部公司追踪** |
| `/fintech-analysis` | 评分 + 深度分析 + 趋势判断 | `phase3-unique-events.json` + `phase2.5-company-research.json` | `phase4-scored-events.json` + `phase5-analysis.md` + `company-tracker.json` | 跨月趋势追踪续接 + 评分原因追溯 + **头部公司分析** |
| `/fintech-report-gen` | Markdown + HTML + 校验 + 飞书发布 | 全部分析数据 | `.md` + `.html` 报告 + 飞书文档链接 | 动态折叠策略 + 飞书自动发布 + **头部公司追踪章节** |

## 数据流

```
/fintech-research
  ↓ phase3-unique-events.json
  ↓ phase2.5-company-research.json（P2 新增：头部公司追踪）
  ↓ phase2-secondary-sources.json
  ↓ phase1-primary-sources.json

/fintech-analysis
  ↓ 读取 phase3 + phase2.5 + trend-tracker.json + company-tracker.json（跨月续接）
  ↓ phase4-scored-events.json（含评分原因）
  ↓ phase5-analysis.md（含头部公司追踪分析）
  ↓ data/trend-tracker.json（更新后）
  ↓ data/company-tracker.json（更新后，P2 新增）

/fintech-report-gen
  ↓ 读取 phase3 + phase4 + phase5 + phase2.5 + company-tracker
  ↓ output/fintech-report-{YYYYMM}.md（含头部公司追踪章节）
  ↓ output/fintech-report-{YYYYMM}.html
```

## 中间检查点

三步之间的数据通过 JSON 文件传递，每步完成后自动运行 schema 校验脚本。校验失败时停止流程并报错。

full 模式下自动连续运行；checkpoint 模式在分析完成后暂停等待人工确认。

## 数据契约

各阶段间通过 JSON 文件传递数据，结构由 `scripts/validate-schema.py` 定义和校验。如果校验失败，下游不会执行，避免静默错误。

## 改进点汇总（v4.1）

| 改进 | 阶段 | 说明 |
|------|------|------|
| 全自动 full 模式 | orchestrator | 三步连续运行无需人工介入，用 `--checkpoint` 启用人工检查点 |
| JSON schema 校验 | orchestrator + 全局 | 每步完成后自动校验中间文件结构，校验失败则停止流程 |
| 路径集中管理 | 全局 | 所有共享文件位于 skill 根目录，子 skill 通过 `../../` 引用；参赛包自包含 |
| context: isolated | orchestrator | 编排器不继承上下文，减少上下文窗口消耗 |
| Agent 失败容错 | research | 4 Agent 并行，单 Agent 失败自动 fallback 到串行执行 |
| 两阶段搜索 | research | 先扫标题再抓全文，节省 30-50% token |
| 跨信号放大 | research | 多信源重合事件自动提分 |
| 关键词展开映射 | research | 空结果自动展开变体，减少查询跳过 |
| 评分原因追溯 | analysis | 每个维度带 reason 字段，可追溯 |
| 跨月趋势追踪 | analysis | trend-tracker.json 续接上期，自动检查证伪 |
| 四态信号追踪 | analysis | Strengthen/Weaken/Falsified/Unchanged |
| 动态折叠策略 | report-gen | 事件过多时自动压缩，保持可读性 |
| 通用事件模板 | report-gen | 减少 SKILL.md 冗余 |
| 反幻觉规则 | 全局 | 禁止截断时间戳/禁止虚假因果/空结果不编造 |
