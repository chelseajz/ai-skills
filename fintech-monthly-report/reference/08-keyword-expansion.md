# 关键词展开映射表

> 用于 Phase 2 搜索。当某个查询返回空结果时，按此表展开变体关键词。

## 核心概念展开

| 原始概念 | 展开变体 |
|---------|---------|
| 支付 | payment, checkout, settlement, clearing, acquiring, gateway |
| 消费金融 | consumer finance, consumer lending, personal loan, BNPL, buy now pay later, credit |
| 数字银行 | digital bank, neobank, challenger bank, online banking, virtual bank |
| 稳定币 | stablecoin, USDC, USDT, EURC, algorithmic stablecoin, regulated stablecoin |
| AI 金融 | AI finance, AI lending, AI risk control, AI payment, agentic payment, machine learning fraud |
| 保险科技 | insurtech, digital insurance, embedded insurance, usage-based insurance |
| 加密支付 | crypto payment, blockchain payment, Web3 payment, on-chain settlement |
| 跨境支付 | cross-border payment, remittance, international transfer, correspondent banking |
| 监管 | regulation, regulatory, compliance, license, framework, directive, enforcement |
| 并购 | acquisition, merger, M&A, acquire, invest, funding round, valuation |

## 公司名展开

| 公司 | 展开变体（英文） | 展开变体（中文） |
|------|-----------------|-----------------|
| Stripe | Stripe, Stripe Press, Stripe Atlas | Stripe |
| PayPal | PayPal, Venmo, PayPal Holdings | PayPal, 贝宝 |
| Visa | Visa, Visa Inc, V | Visa |
| Mastercard | Mastercard, MasterCard, MA | Mastercard, 万事达 |
| Ant Group | Ant Group, Ant Financial, Alipay | 蚂蚁集团, 蚂蚁金服, 支付宝 |
| Tencent | Tencent, WeChat Pay, Tenpay | 腾讯, 微信支付, 财付通 |
| Block | Block Inc, Square, Afterpay | Block, Square |
| Adyen | Adyen | Adyen |
| Circle | Circle, USDC, Centre | Circle, USDC |
| Revolut | Revolut | Revolut |
| Klarna | Klarna, BNPL | Klarna |
| Nubank | Nubank, Nu Holdings | Nubank |
| 富途 | Futu, Moomoo | 富途, moomoo |
| 同花顺 | Hithink Flush, 同花顺 | 同花顺 |
| 众安 | ZhongAn, ZA Bank, ZA Online | 众安, 众安银行, 众安在线 |

## 使用方式

```python
def expand_keywords(query, target_month):
    """如果查询包含概念词，展开为多个变体"""
    expanded = [query]
    for concept, variants in KEYWORD_MAP.items():
        if concept in query:
            for v in variants:
                expanded.append(query.replace(concept, v))
    return expanded
```

## 回退策略

当搜索结果为空时，按以下顺序回退：

1. **阶段 1**：使用展开变体，限定目标月份
2. **阶段 2**：去掉时间限定，只搜"概念 + 公司"关键词
3. **阶段 3**：只搜概念词 + "latest developments 2026"
