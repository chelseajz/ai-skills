# 头部公司追踪模块（Key Companies Tracking）

> 用于每月追踪 ~15 家高优先级 Fintech 公司的业务表现和战略动态。
> 历史报告格式参考：Global Fintech 观察_25 年 6 月 → Key Companies 章节。

---

## 1. 追踪公司清单

从 `../knowledge-base/core-players.md` 中选取 **高优先级 + 最高优先级** 公司：

| # | 公司 | 赛道 | 优先级 | 必查指标 |
|:-:|------|------|:------:|----------|
| 1 | Stripe | 支付清结算 | 最高 | 交易规模、新产品、合作生态 |
| 2 | Visa | 支付清结算 | 高 | 交易笔数/金额、Tap to Pay、收购 |
| 3 | Mastercard | 支付清结算 | 高 | 交易增长、One Credential |
| 4 | PayPal | 支付清结算 | 高 | TPV、Venmo 货币化、Braintree |
| 5 | Adyen | 支付清结算 | 高 | 净收入、全球化扩张 |
| 6 | Block (Square/Cash App) | 支付+数字银行 | 高 | GPV、Cash App 毛利、Square GPV |
| 7 | 蚂蚁集团（支付宝） | 支付+消金 | 高 | 用户规模、新产品、海外扩张 |
| 8 | Nubank | 数字银行 | 高 | 累计/活跃用户、收入、净利润、信贷质量 |
| 9 | Revolut | 数字银行 | 高 | 用户数、收入、盈利、新市场 |
| 10 | Affirm | BNPL | 高 | GMV、收入、Take Rate、商户数 |
| 11 | Klarna | BNPL+支付 | 高 | GMV、收入、Take Rate、上市进展 |
| 12 | Apple Pay | 支付平台 | 中 | Apple Pay 用户、Apple PayLater/BNPL、NFC 开放 |
| 13 | 腾讯金融科技（微信支付） | 支付 | 高 | 交易规模、新产品、合规进展 |
| 14 | Circle | 稳定币 | 高 | USDC 市值、监管牌照、合作生态 |
| 15 | Xendit | 东南亚支付 | 高 | 交易规模、新市场、融资 |

**动态调整规则**：
- 每月可根据当月重大事件临时加入 1-3 家公司（如某公司发布重大产品、IPO、收购）
- 被加入临时名单的公司需在下月评估是否加入固定名单
- 固定名单每季度回顾一次

---

## 2. 数据追踪结构（company-tracker.json）

```json
{
  "last_updated": "2026-04-15",
  "month": "2026-04",
  "companies": [
    {
      "name": "Stripe",
      "track": "支付清结算",
      "priority": "highest",
      "financial_metrics": {
        "last_reported_quarter": "2025-Q4",
        "revenue": null,
        "revenue_yoy_growth": null,
        "transaction_volume": "1.4万亿美金 (2024全年)",
        "transaction_volume_yoy": "+38%",
        "gross_profit": null,
        "net_income": null,
        "key_metric_name": "收单交易规模",
        "key_metric_value": "1.4万亿美金",
        "key_metric_yoy": "+38%",
        "other_metrics": {
          "研发投入占比": "远高于同规模企业"
        }
      },
      "monthly_events": [
        {
          "date": "2026-04-10",
          "title": "发布 Agentic Payment 框架",
          "url": "https://stripe.com/...",
          "summary": "联合 OpenAI 发布 AI 代理原生支付框架",
          "event_type": "product_launch",
          "score": 95
        }
      ],
      "strategic_focus": [
        "AI + 支付（Agent Toolkit、MCP Server）",
        "稳定币（收购 Bridge、稳定币账户）",
        "全球化（新兴市场扩张）"
      ],
      "moat_changes": {
        "month": "2026-04",
        "changes": [
          {
            "dimension": "技术壁垒",
            "direction": "加深",
            "from": "高",
            "to": "很高",
            "reason": "连续6年高研发投入，AI 50 强企业全部使用 Stripe"
          }
        ]
      },
      "competitive_position": {
        "vs_peers": "领先",
        "peer_comparison": "交易增速高于 Worldpay，与 Adyen 相当，全球化优于 Worldpay",
        "market_share_trend": "上升"
      },
      "bytedance_relevance": {
        "relevance_level": "高",
        "affected_products": ["抖音支付", "TikTok Shop 支付"],
        "key_takeaways": "AI 支付框架可能成为行业标准，字节需评估跟进时机",
        "gap_assessment": "字节在收单技术层面落后 Stripe，需关注其 Agentic Payment 方案"
      }
    }
  ]
}
```

---

## 3. 报告输出格式

### 在 Markdown 报告中的位置

位于"趋势判断"和"非共识观察"之间，作为独立章节：

```markdown
---

## 头部公司追踪

> 本月追踪 {N} 家公司，{M} 家有重大事件更新

### {公司名称}（{赛道}）

**业务表现**：
- {关键指标 1}：{数值}（同比 {变化}）
- {关键指标 2}：{数值}（同比 {变化}）
- {最新财报季度}：{简要总结}

**本月重大事件**：
- {事件 1}（{日期}）— {一句话摘要}
- {事件 2}（{日期}）— {一句话摘要}

**战略要点**：
- {战略动向 1}
- {战略动向 2}

**竞争格局变化**：
- {护城河变化}
- {市场份额变化}

**对字节启示**：
- {战略启示}

---

### {公司 2}...
```

### 筛选规则

**当月无重大事件的公司**：
- 如果连续 2 个月无重大事件，缩减为 1 行简表
- 如果有季度财报发布，即使无其他事件也完整展示
- 财报季优先展示最新财务数据

**报告长度控制**：
- 事件 ≤ 15 条：所有公司完整展示
- 事件 15-30 条：有重大事件的公司完整展示，无重大事件的缩为简表
- 事件 > 30 条：只展示 Top 5 有重大事件的公司，其余归档到附录

---

## 4. 搜索策略（Phase 2.5）

### 公司专属查询模板

每家公司使用以下查询模板：

| 查询模板 | 示例 |
|---------|------|
| `{公司名} {YYYY} {MM} earnings` | `Stripe 2026 April earnings financial results` |
| `{公司名} {YYYY} quarterly results` | `Nubank 2026 Q1 quarterly results` |
| `{公司名} {YYYY} announcement` | `Visa 2026 April announcement` |
| `{公司名} {YYYY} product launch` | `PayPal 2026 April product launch` |
| `{公司名} acquisition {YYYY}` | `Block acquisition 2026` |
| `{公司名} CEO interview {YYYY}` | `Stripe CEO interview 2026` |
| `{公司中文名} 最新动态 {YYYY}` | `蚂蚁集团 最新动态 2026` |
| `{公司名} revenue {YYYY}` | `Revolut revenue 2026` |

### 一级信源优先

- **财报**：直接从公司 IR 网站或 SEC EDGAR 获取
- **官方博客**：公司 Newsroom/Blog
- **CEO 发言**：官方新闻稿或经核实的媒体报道

### 中文公司特殊处理

对于蚂蚁集团、腾讯金融科技等中文公司：
- 使用中文关键词搜索
- 优先从公司官网/官方微信公众号获取信息
- 财报数据可参考上市公司公告

---

## 5. 跨月对比规则

### 财务指标追踪

对每家公司的关键财务指标进行跨月追踪：

| 指标 | 追踪方式 |
|------|---------|
| 交易规模 | 季度更新，月间标注趋势方向 |
| 用户数 | 季度更新，月间标注趋势方向 |
| 收入 | 季度更新，月间标注趋势方向 |
| 净利润 | 季度更新，月间标注趋势方向 |
| Take Rate | 季度计算，标注变化 |

### 趋势状态标记

每次更新时标记趋势状态：
- `【上升】` — 指标环比/同比改善
- `【持平】` — 指标无明显变化
- `【下降】` — 指标环比/同比恶化
- `【新高】` — 创历史新高
- `【暂无数据】` — 当月无最新数据

---

## 6. 截图/图片引用

历史报告中大量使用截图佐证，当前 Skill 需支持：

1. **截图 URL 引用**：如果事件原文包含截图/图表，保留原图 URL 并在报告中以 `![描述](URL)` 格式引用
2. **关键数据截图**：对于财报数据、产品截图等重要信息，尽可能保留原始截图链接
3. **图片质量要求**：仅引用清晰的、信息量大的截图，避免装饰性图片

```markdown
**{事件描述}**：

![事件截图](原始图片URL)
*截图来源：{来源名称}*
```

---

## 7. 与事件驱动分析的协同

公司追踪模块与现有事件驱动分析的关系：

| 维度 | 事件驱动分析 | 公司追踪模块 |
|------|-------------|-------------|
| 触发条件 | 搜索发现的高评分事件 | 固定公司名单定期更新 |
| 深度 | ≥80 分事件才有六维度深度分析 | 所有追踪公司都有简要更新 |
| 视角 | 事件为中心 | 公司为中心 |
| 互补性 | 覆盖突发/偶发事件 | 覆盖持续/系统性变化 |
| 交叉引用 | 公司追踪中的重大事件引用事件驱动分析结果 | 事件驱动分析中标注涉及的公司 |

**协同规则**：
1. 如果某公司在本月有 ≥80 分事件，该事件在公司追踪卡片中简要引用，不重复完整分析
2. 如果某公司无重大事件但有财报发布，以财报数据为主展示
3. 公司追踪卡片中不重复事件驱动分析的完整六维度，只做概要引用