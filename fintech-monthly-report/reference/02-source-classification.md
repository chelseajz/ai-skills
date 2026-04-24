# 信源分类与评分规则

> 用于 Phase 2 信源分级 + Phase 4 信源分级与六维评分。执行时引用本文件。

## 信源分级规则

按以下顺序匹配（第一个匹配即停止）：

### 一级信源（source_level = 1）：监管机构、央行、政府官方

以下机构名称或域名匹配即判定：

**机构名**：HKMA, Fed, ECB, PBC, MAS, OCC, FDIC, PRA, FCA, HM Treasury, US Treasury, SEC, CFTC, FINMA, BaFin, AMF, BoE, NIST, IMF, World Bank, BIS, FATF, SFC

**域名**：hkma.gov.hk, federalreserve.gov, ecb.europa.eu, pbc.gov.cn, mas.gov.sg, sec.gov, gov.cn

### 二级信源（source_level = 2）：上市公司/大厂官网新闻室、顶级通讯社

**机构名**：Stripe, Ant Group, Visa, Mastercard, PayPal, Adyen, Block, Klarna, Revolut, Coinbase, Circle, Tether, Binance, Plaid, Airwallex, Checkout.com, Affirm, SoFi, Robinhood, Nubank, Chime, Razorpay, Grab, MoMo, VNPay, SeaMoney, ShopeePay, GoPay, Tencent, UnionPay, 连连支付, PingPong, 富途, 老虎证券, 同花顺, 东方财富, 众安在线, ZA Bank, Lemonade, FWD Group

**域名**：reuters.com, bloomberg.com, wsj.com, ft.com, cnbc.com, apnews.com, stripe.com, adyen.com, paypal.com

### 三级信源（source_level = 3）：科技媒体、行业垂直媒体、国内Fintech公众号

**域名**：techcrunch.com, theblock.co, coindesk.com, theinformation.com, fintechfutures.com, paymentsdive.com, secu.org, 36kr.com, pingwest.com, ifanr.com, genspark.com

**公众号/自媒体**：支付之家、移动支付网、消金江湖、零壹财经、新流财经、镭财传媒、支付通

### 四级信源（source_level = 4）：自媒体、博客、社区、未明确来源

不匹配以上任何级别的默认值。

**平台**：微信公众号（无转载）、小红书、Twitter/X、YouTube、Bilibili、知乎、个人博客

## 六维评分规则

### 评分维度

| 维度 | 权重 | 满分 | 评分方式 |
|------|------|------|----------|
| 信源可信度 | 25% | 25 | **规则化**：一级25/二级20/三级15/四级10 |
| 时间紧迫性 | 10% | 10 | **规则化**：本月=10/上月-1=5/更早=3 |
| 信息独特性 | 25% | 25 | 模型判断：独家25/增量20/整合15/已知10 |
| 战略相关性 | 25% | 25 | 模型判断：直接25/间接15/弱相关5 |
| 影响持续性 | 10% | 10 | 模型判断：长期10/中期7/短期3 |
| 市场热度 | 5% | 5 | 模型判断：高5/中3/低1 |

### 分级筛选

- **≥80分**：重点事件（深度分析）
- **60-79分**：关注事件（简要提及）
- **<60分**：不进入正文

## 信源追溯规范

每条事件必须包含：
1. `source` — 来源名称（如"香港金管局"）
2. `source_url` — 原始链接或存档链接
3. `source_level` — 1/2/3/4 级
4. `date` — 首次发布日期
5. `access_status` — 完整/摘要/付费墙

**来源不明处理**：无法确认来源 → 剔除该事件；仅有摘要 → 标注「[付费墙/仅获摘要]」

## 原文引用规范

**外文原文（需翻译）**：
```markdown
> **原文引用**
>
> "英文原文内容..."
>
> *【译】中文翻译内容...*
>
> — 发言人, 职位, 机构. [来源](URL)
```

**中文原文（直接引用）**：
```markdown
> **原文引用**
>
> 中文原文内容...
>
> — 发言人, 职位, 机构. [来源](URL)
```
