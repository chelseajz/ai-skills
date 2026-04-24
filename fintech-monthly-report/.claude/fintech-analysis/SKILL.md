---
name: fintech-analysis
version: "2.0"
description: Fintech 月报分析阶段 — Phase 4-5（信源分级评分 → 深度分析 → 趋势判断 + 跨月趋势追踪续接）
argument-hint: "YYYY年MM月"
user-invocable: true
model: opus
effort: high
context: fork
allowed-tools: WebSearch, WebFetch, Read, Write, Bash
---

# Fintech 月报分析 Skill

> **职责**：对搜索到的事件进行六维评分，对高评分事件进行六维度深度分析，生成趋势判断和非共识观察。
>
> **前置条件**：必须先执行 `/fintech-research` 完成搜索。
>
> **输入**：`/fintech-analysis 2026年4月`
> **输入数据**：`~/.claude/fintech-reports/logs/phase3-unique-events.json`
> **输出**：`phase4-scored-events.json` + `phase5-analysis.md` + `data/trend-tracker.json`

---

## Phase 0: 初始化

### 步骤 1: 解析参数

从参数中提取目标年月：`YYYY`、`MM`、`month_cn`

### 步骤 2: 验证数据文件存在

```bash
ls ~/.claude/fintech-reports/logs/phase3-unique-events.json
```
- 不存在 → 报错"请先执行 `/fintech-research {YYYY}年{MM}月` 完成搜索"

### 步骤 3: 读取关键知识文件

```python
# 信源分类与评分规则
read("../../reference/02-source-classification.md")
# 深度分析规则（六维度框架）
read("../../reference/03-phase5-deep-analysis.md")
# 咨询级分析方法论（框架选择、What-Why-So What、证据分级、红队审查）
read("../../reference/09-analysis-methodology.md")
# 核心玩家图谱
read("../../knowledge-base/core-players.md")
# 护城河分析框架
read("../../knowledge-base/methodology/moat-analysis.md")
# 字节财经业务线
read("../../knowledge-base/bytedance-finance.md")
# 竞品详细档案（按需读取）
read("../../knowledge-base/competitors/{stripe,ant-group,tencent-fintech,paypal,sea-group}.md")
# 公司追踪格式规则（P2 新增）
read("../../reference/10-company-tracking.md")
```

### 步骤 4.5: 读取上期公司追踪数据（P2 新增）

```python
tracker_path = Path("~/.claude/fintech-reports/data/company-tracker.json").expanduser()
if tracker_path.exists():
    previous_company_tracker = json.loads(tracker_path.read_text())
    # 提取上月各公司财务指标和趋势状态
    for company in previous_company_tracker.get("companies", []):
        company["last_metrics"] = company.get("financial_metrics", {})
else:
    previous_company_tracker = {}
```

### 步骤 4: 读取跨月趋势追踪文件（P0 改进）

```python
import json
from pathlib import Path

trend_path = Path("~/.claude/fintech-reports/data/trend-tracker.json").expanduser()
if trend_path.exists():
    trend_tracker = json.loads(trend_path.read_text())
    # 上期趋势状态
    previous_trends = trend_tracker.get("trends", [])
    # 检查每条趋势的证伪条件是否已触发
    for trend in previous_trends:
        trend["status"] = check_falsification(trend)  # Strengthen/Weaken/Falsified/Unchanged
else:
    previous_trends = []
    trend_tracker = {}
```

**证伪条件检查逻辑**：
```python
def check_falsification(trend):
    """基于当月最新事实检查证伪条件"""
    falsification_condition = trend.get("falsification_condition", "")
    prediction = trend.get("prediction", "")

    # 搜索当月是否出现了证伪条件描述的事件
    results = WebSearch(falsification_condition + " 2026年4月")
    if results:
        return "Falsified"

    # 搜索是否有支持预测的新事件
    results = WebSearch(prediction + " latest")
    if results:
        return "Strengthen"

    return "Unchanged"
```

---

## Phase 4: 信源分级与评分

### 步骤 1: 读取事件数据

```python
events = read("~/.claude/fintech-reports/logs/phase3-unique-events.json")["events"]
```

### 步骤 2: 信源分级

按 `../../reference/02-source-classification.md` 中的规则：

```python
for event in events:
    event.source_level = classify_source(event.url, event.title)  # 1-4
```

### 步骤 3: 读取咨询框架

```python
# 读取咨询级分析框架（已内置于 reference/09-analysis-methodology.md）
read("../../reference/09-analysis-methodology.md")
# 读取 Fintech 专用维度（支付/数字银行/嵌入式金融/稳定币）
# 见 reference/09-analysis-methodology.md 第一节"分析框架选择矩阵"
```

在 Phase 5 深度分析时，为每个焦点事件选择 1-2 个咨询分析框架（SWOT/PESTEL/Porter's Five Forces/VRIO/Gartner Hype Cycle 等），标注 `[分析框架：XXX]`，框架选择参考 `../../reference/09-analysis-methodology.md` 的分析框架选择矩阵。

### 步骤 4: 六维评分（含 reason 字段 + 咨询框架预标注）

```python
for event in events:
    score = 0
    reasons = {}  # P1 改进：每个维度记录评分原因

    # 维度 1: 信源可信度（规则化）
    source_score = {1: 25, 2: 20, 3: 15, 4: 10}[event.source_level]
    score += source_score
    reasons["source_credibility"] = {
        "score": source_score,
        "reason": f"{event.source_level}级信源 ({event.get('source', 'unknown')})"
    }

    # 维度 2: 时间紧迫性（规则化）
    if event.date.month == target_month:
        score += 10
        reasons["timeliness"] = {"score": 10, "reason": f"本月事件 ({event.date})"}
    elif event.date.month == target_month - 1:
        score += 5
        reasons["timeliness"] = {"score": 5, "reason": f"上月事件 ({event.date})"}
    else:
        score += 3
        reasons["timeliness"] = {"score": 3, "reason": f"更早事件 ({event.date})"}

    # 维度 3: 信息独特性（模型判断 + reason）
    uniqueness_score, uniqueness_reason = judge_uniqueness(event)
    score += uniqueness_score
    reasons["uniqueness"] = {"score": uniqueness_score, "reason": uniqueness_reason}

    # 维度 4: 战略相关性（模型判断 + reason）
    relevance_score, relevance_reason = judge_relevance(event)
    score += relevance_score
    reasons["relevance"] = {"score": relevance_score, "reason": relevance_reason}

    # 维度 5: 影响持续性（模型判断 + reason）
    sustainability_score, sustainability_reason = judge_sustainability(event)
    score += sustainability_score
    reasons["sustainability"] = {"score": sustainability_score, "reason": sustainability_reason}

    # 维度 6: 市场热度（模型判断 + reason）
    popularity_score, popularity_reason = judge_popularity(event)
    score += popularity_score
    reasons["popularity"] = {"score": popularity_score, "reason": popularity_reason}

    # P1 改进：跨信号放大 bonus
    if event.get("cross_signal_amplified", False):
        score += 5
        reasons["cross_signal"] = {"score": 5, "reason": "多信源重合发现，可信度更高"}

    # P0-4: 维度 7: 市场热度评分（基于搜索热度 + 来源扩散度）
    popularity_heat = calculate_heat_score(event)
    score += popularity_heat
    reasons["market_heat"] = {
        "score": popularity_heat,
        "reason": popularity_heat_reason(event)
    }

    event.score = score
    event.score_reasons = reasons  # 可追溯的评分原因
```

**市场热度计算规则**（P0-4 新增）：
- 搜索结果数量：该事件标题/关键词在 WebSearch 中返回的结果数 → 0-10 条=1分, 11-50条=2分, 50-200条=3分, 200+条=4分
- 来源扩散度：该事件被多少个独立一级信源报道 → 1家=1分, 2家=2分, 3家=3分, 4+家=4分
- 满分 8 分，两项相加

### 步骤 4: 分级

- **≥80 分**：焦点事件（深度分析）
- **60-79 分**：关注事件（简要提及）
- **<60 分**：不进入正文

### 步骤 5: 保存评分结果

```json
{
  "target_month": "{YYYY}-{MM}",
  "total_events": <count>,
  "focus_events": <count of ≥80>,
  "watch_events": <count of 60-79>,
  "events": [
    {
      "title": "...",
      "date": "...",
      "url": "...",
      "score": XX,
      "score_reasons": {
        "source_credibility": {"score": 25, "reason": "一级信源 (HKMA)"},
        "timeliness": {"score": 10, "reason": "本月事件 (2026-04-10)"},
        ...
      },
      "source_level": N,
      "source": "...",
      ...
    }
  ]
}
```

**输出**：`~/.claude/fintech-reports/logs/phase4-scored-events.json`

---

## Phase 5: 深度分析

### 步骤 1: 筛选高价值事件

```python
focus_events = [e for e in events if e.score >= 80]
watch_events = [e for e in events if 60 <= e.score < 80]
```

### 步骤 2: 焦点事件深度分析（每个 ≥80 分事件必须完成 6 个维度）

**分析前准备（每个焦点事件）**：
1. **选择分析框架**：从 `../../reference/09-analysis-methodology.md` 的框架矩阵中选择 1-2 个最相关框架，标注 `[分析框架：XXX]`
2. **提出初始假设**：1 句话假设该事件的战略含义，标注 `[假设] XXX`

**严格按照 `../../reference/03-phase5-deep-analysis.md` 中的六维度框架执行**：

#### 维度 1: 信号（事实层）
- 1-2 句话客观描述核心事实
- 引用原文 quote（外文：英文原文 + 中文翻译；中文：直接引用）
- 标注炒作/真实判断：【实质落地】/【明确规划】/【概念阶段】/【炒作信号】
- **每个关键数据标注证据等级**（A-D），见 `../../reference/09-analysis-methodology.md`

#### 维度 2: 背景脉络 + 护城河分析 + Gartner 技术成熟度
- 历史脉络 + 竞品横向对比（3-5 家直接竞品）
- 护城河变化：加深了哪条护城河？从什么强度到什么强度？
- 参考 `../../knowledge-base/methodology/moat-analysis.md`
- **P2-2: Gartner 技术成熟度标注**：对涉及新兴技术/产品的事件，标注其在 Gartner Hype Cycle 中的阶段：
  - `【技术触发期】` — 概念刚提出，尚未产品化（如 2025 年初 Agentic Payment）
  - `【期望膨胀期】` — 媒体大量报道，实际落地有限（炒作信号高发区）
  - `【泡沫破裂低谷期】` — 热度骤降但仍在发展
  - `【稳步爬升期】` — 产品真实商用，用户可感知
  - `【生产成熟期】` — 成为行业标准（如移动支付）
  - 判断依据：商用时间 + 用户规模 + 竞品跟进数

#### 维度 3: 影响评估（量化 + 二阶影响）
- 行业格局影响 + TAM/TAM-at-risk 数字估算
- 二阶影响推导：一阶 → 二阶 → 三阶
- **对字节财经各产品的影响（强制）**：抖音支付/放心借/月付/TikTok Shop支付/抖音保险/香港SVF
  - 竞争压力等级 + 可借鉴点 + 字节优势 + 行动建议

#### 维度 4: 趋势预判
- 明确方向：加速/放缓/转向/伪趋势
- 3-6 个月具体预测 + 信心等级 + 证伪条件
- **证伪条件必须基于最新事实**：写证伪条件前，必须先搜索该趋势最新进展
- **趋势类判断必须执行假设驱动分析**（提出假设 → 找支持证据 → 找反驳证据 → 验证结论）

#### 维度 5: 缺口与机会 + 竞争窗口期
- 市场盲区 + 非共识观点（市场共识 → 我的判断 → 验证信号）
- 窗口期判断：进入/退出 + 剩余时间 + 关闭信号

#### 维度 6: 行动建议
- 具体可执行动作 + 优先级（P0/P1/P2）+ 关联字节产品

**每个维度必须遵循 "What → Why → So What" 论证结构**，见 `../../reference/09-analysis-methodology.md` 第二节。

### 步骤 3: 关注事件简要分析

对每个 60-79 分事件：
- 事件核心事实（1 句话）
- 为什么值得关注（1-2 句话）
- 与哪些焦点事件相关

### 步骤 4: 跨事件关联分析

- 至少做 1 条因果链推导
- 关联分析必须指向至少 1 条趋势判断
- 区分"相关性"和"因果性"（使用 SVO 句型）

### 步骤 5: 趋势判断与非共识观察

#### 趋势判断（3-5 条）

**P0 改进：先检查上期趋势状态**

```python
# 续接上期趋势
for prev_trend in previous_trends:
    status = prev_trend["status"]  # Strengthen/Weaken/Falsified/Unchanged

    if status == "Falsified":
        # 证伪了：说明该趋势不成立，不再作为核心趋势
        record_falsified_trend(prev_trend)
    elif status == "Strengthen":
        # 加强了：该趋势是本月最重要的方向
        promote_to_top_trend(prev_trend)
    elif status == "Weaken":
        # 减弱了：仍然提及但降级
        include_as_secondary(prev_trend)
    else:
        # 未变化：保持跟踪
        include_trend(prev_trend)

# 再识别本月新增趋势
new_trends = identify_new_trends(focus_events, cross_event_links)
```

每条趋势必须：
- 有明确方向（"X 将加速/放缓/转向"）
- 有至少 2 个事件作为论据支撑
- 给出可验证的时间窗口
- 标注趋势阶段：萌芽期 / 加速期 / 成熟期 / 衰退期
- 竞争格局重塑分析（点名 2-3 家具体公司）
- **P2-1: 头部玩家份额变化标注**：趋势中必须提及该赛道头部玩家本月是否有份额/用户规模/营收的变化，标注"XX 份额从 A%→B%"或"无显著变化"
- **P2-1: 护城河移动分析**：趋势中涉及的头部玩家，其护城河本月是加深还是被侵蚀？标注 `[护城河→加深/→持平/→侵蚀]`
- 趋势间相互作用（至少 2-3 条）
- **证伪条件**：具体事件 + 时间窗口（用于下月自动检查）

#### 非共识观察（3-5 条）

每条必须：
1. **市场共识**：主流观点
2. **我的判断**：为什么不同
3. **支撑论据**：至少 2 个数据/事件
4. **证伪条件**：什么信号证明我错了
5. **对字节启示**：具体业务线 + 行动建议

### 步骤 6: 咨询报告融合

对每个焦点事件，检查 Phase 2 中 Batch 11 找到的咨询报告，如有则引用佐证。

### 步骤 7: 假设验证 + 红队审查（P0 新增）

对分析开始时提出的每个初始假设，执行假设验证流程，见 `../../reference/03-phase5-deep-analysis.md`。

执行红队审查（5 项）：
1. 最强反驳 — 分析中最薄弱的论据是什么？
2. 遗漏检查 — 哪些关键玩家/事件/数据可能被遗漏？
3. 方向性错误风险 — 结论方向（加速/放缓/转向）有无反向可能？
4. 字节偏差检查 — 是否高估了某些影响或低估了某些威胁？
5. 数据时效性 — 引用数据是否过时？

### 步骤 8: P2-3 字节战略对标分析（新增）

对每个焦点事件（≥80 分），增加"字节 vs 竞品"对标分析：
1. **竞品当前能力**：该事件主体（如 Stripe/PayPal/Ant）在该赛道的能力水平
2. **字节对应业务线现状**：字节现有业务线在该赛道的能力对比
3. **差距评估**：领先 / 持平 / 落后（落后时必须标注具体差距维度）
4. **追赶窗口期**：预计需要多长时间能追平或形成差异化优势
5. **参考竞品详细档案**：从 `../../knowledge-base/competitors/` 读取对应竞品档案获取对比数据

### 步骤 8.5: P2-4 头部公司追踪分析（新增）

> 读取 Phase 2.5 的公司研究数据，为每家追踪公司生成简要分析卡片。

```python
# 读取公司研究数据
company_data = read("~/.claude/fintech-reports/logs/phase2.5-company-research.json")
# 读取公司追踪格式规则
read("../../reference/10-company-tracking.md")
# 读取上期 company-tracker.json
previous_tracker = read("~/.claude/fintech-reports/data/company-tracker.json")
```

**对每家追踪公司执行**：

1. **读取 Phase 2.5 数据**：获取该公司的财务指标、月度事件、战略焦点
2. **读取上月数据对比**：与上月 company-tracker.json 中该公司数据对比，标注趋势变化
3. **检查本月事件关联**：该公司是否有 ≥80 分事件，如有则引用而非重复分析
4. **护城河月度评估**：基于本月事件评估该公司护城河变化（加深/持平/侵蚀）
5. **对字节相关性**：更新该公司对字节各业务线的影响评估

**输出格式**（写入 phase5-analysis.md 的公司追踪部分）：

```markdown
## 头部公司追踪

### {公司名称}（{赛道}）

**业务表现**：
- {关键指标}：{数值}（同比 {变化}）→ 【{趋势方向}】
- {最新财报季度}：{简要总结}

**本月重大事件**：
- {事件 1}（{日期}）— {一句话摘要}
- 如该公司有 ≥80 分事件，引用事件分析链接，不重复

**战略要点**：
- {战略动向 1}
- {战略动向 2}

**护城河变化**：→ {加深/持平/侵蚀}
- {具体维度变化}

**对字节启示**：
- {战略启示}
```

**筛选规则**：
- 有本月重大事件或财报的公司 → 完整展示
- 连续 2 个月无重大事件的公司 → 缩减为 1 行简表
- 财报季优先展示最新财务数据

**更新 company-tracker.json**：
```python
# 合并本期数据到 tracker
for company in company_data["companies"]:
    update_company_tracker(company, previous_tracker)

# 保存更新后的 tracker
write(updated_tracker, "~/.claude/fintech-reports/data/company-tracker.json")
```

---

### 步骤 9: 假设验证 + 红队审查（P0 新增）

```python
trend_tracker = {
    "last_updated": "{YYYY}-{MM}-15",  # 月中日期
    "month": "{YYYY}-{MM}",
    "trends": [
        {
            "name": "趋势名称",
            "direction": "加速/放缓/转向/伪趋势",
            "stage": "萌芽期/加速期/成熟期/衰退期",
            "confidence": "高/中/低",
            "verification_date": "YYYY-MM",  # 预计验证时间
            "falsification_condition": "什么事件出现意味着判断错误",
            "supporting_events": ["事件1 URL", "事件2 URL"],
            "last_status": "Strengthen/Weaken/Falsified/Unchanged",
            "bytedance_implication": "对字节财经的战略启示"
        }
    ]
}
write(trend_tracker, "~/.claude/fintech-reports/data/trend-tracker.json")
```

**输出**：`~/.claude/fintech-reports/logs/phase5-analysis.md`
**附加输出**：`~/.claude/fintech-reports/data/trend-tracker.json`

---

## 质量门（完成后自检）

在输出前，逐项检查：
- [ ] 每个焦点事件标注了分析框架（至少 1 个）
- [ ] 每个焦点事件提出了初始假设并给出验证结论
- [ ] 每个维度遵循 "What → Why → So What" 结构（不缺 So What）
- [ ] 关键主张标注了证据等级（A-D）
- [ ] 非共识观点满足至少一项标准（忽略关键变量/相反判断/利好隐患/利空机会）
- [ ] 趋势判断有竞争格局重塑 + 趋势间相互作用
- [ ] 红队审查 5 项已完整输出
- [ ] trend-tracker.json 已更新

如有任一检查不通过，必须修复后再输出。

---

## 完成后提示

```
✅ Analysis 阶段完成！

分析统计：
- 焦点事件（≥80分）：X 个（已完整深度分析）
- 关注事件（60-79分）：X 个
- 趋势判断：X 条
- 非共识观察：X 条
- 跨月趋势追踪：X 条续接，X 条新识别

输出文件：
- ~/.claude/fintech-reports/logs/phase4-scored-events.json（含评分原因追溯）
- ~/.claude/fintech-reports/logs/phase5-analysis.md
- ~/.claude/fintech-reports/data/trend-tracker.json

下一步请执行报告生成：
/fintech-report-gen {YYYY}年{MM}月
```
