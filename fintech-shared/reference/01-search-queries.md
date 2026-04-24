# 搜索任务清单（128 个查询，必须全部执行）

> 搜索清单基于 `core-players.md` 整理，**包含所有中优先级及以上公司**，确保完整覆盖

> ⚠️ 注意：即使前一个查询没结果，也要继续执行下一个查询

## 查询格式说明

- **占位符替换**：`{YYYY}` → 年份数字（如 2026），`{MM}` → 月份数字（如 04），`{年}年{月}月` → 中文格式（如 2026年4月）
- **语言规则**：国际公司用英文关键词，中国公司用中文关键词
- **失败回退**：无结果时尝试 `base_variants` 和 `topic_variants` 关键词变体（见 SKILL.md Phase 2.1）

---

## Batch 1: 支付与清结算（27 个查询）

> ⚠️ 国际公司使用英文关键词，中国公司使用中文关键词

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | 蚂蚁集团 | `蚂蚁集团 金融科技 {年}年{月}月` | CN | 高 |
| 1a | 支付宝 | `支付宝 新动态 发布 {年}年{月}月` | CN | 高 |
| 2 | Visa | `Visa news press release {YYYY} {MM}` | EN | 高 |
| 3 | Mastercard | `Mastercard news announcement {YYYY} {MM}` | EN | 中 |
| 3a | Worldpay | `Worldpay news announcement acquisition {YYYY} {MM}` | EN | 高 |
| 4 | American Express | `American Express Amex news {YYYY} {MM}` | EN | 中 |
| 5 | PayPal | `PayPal news announcement {YYYY} {MM}` | EN | 高 |
| 5a | Venmo | `Venmo news product update {YYYY} {MM}` | EN | 中 |
| 6 | Adyen | `Adyen news announcement {YYYY} {MM}` | EN | 高 |
| 7 | Stripe | `Stripe news announcement launch {YYYY} {MM}` | EN | ⭐最高 |
| 8 | Block | `Block Inc Square news {YYYY} {MM}` | EN | 高 |
| 9 | X (Twitter) Pay | `X Twitter Pay news announcement {YYYY} {MM}` | EN | 中 |
| 10 | FIS | `FIS fintech news {YYYY} {MM}` | EN | 中 |
| 11 | Global Payments | `Global Payments news {YYYY} {MM}` | EN | 中 |
| 12 | 腾讯金融 | `腾讯金融科技 微信支付 {年}年{月}月` | CN | 高 |
| 13 | 中国银联 | `中国银联 新动态 {年}年{月}月` | CN | 高 |
| 14 | Klarna | `Klarna news BNPL {YYYY} {MM}` | EN | 高 |
| 15 | Wise | `Wise cross-border payment news {YYYY} {MM}` | EN | 中 |
| 16 | Checkout.com | `Checkout.com news announcement {YYYY} {MM}` | EN | 中 |
| 17 | Rapyd | `Rapyd payment news {YYYY} {MM}` | EN | 中 |
| 18 | Marqeta | `Marqeta news announcement {YYYY} {MM}` | EN | 中 |
| 19 | 连连支付 | `连连支付 中国 {年}年{月}月` | CN | 中 |
| 20 | PingPong | `PingPong 跨境支付 {年}年{月}月` | CN | 中 |
| 21 | 微信 | `微信 支付 新功能 场景拓展 {年}年{月}月` | CN | 高 |
| 22 | Remitly | `Remitly cross-border remittance news {YYYY} {MM}` | EN | 中 |
| 23 | Shift4 Payments | `Shift4 Payments news {YYYY} {MM}` | EN | 中 |
| 24 | StoneCo | `StoneCo Brazil payment news {YYYY} {MM}` | EN | 中 |
| 25 | PagSeguro/PagBank | `PagSeguro PagBank Brazil news {YYYY} {MM}` | EN | 中 |
| 26 | Flywire | `Flywire cross-border payment news {YYYY} {MM}` | EN | 中 |
| 27 | Payoneer | `Payoneer cross-border B2B payment news {YYYY} {MM}` | EN | 中 |

## Batch 2: 支付与清结算 - 区域（8 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | Grab Financial | `Grab Financial news {YYYY} {MM}` | EN | 高 |
| 2 | GoPay Gojek | `GoPay Gojek Indonesia news {YYYY} {MM}` | EN | 高 |
| 3 | ShopeePay Sea | `ShopeePay SeaMoney news {YYYY} {MM}` | EN | 高 |
| 4 | MoMo Vietnam | `MoMo Vietnam payment news {YYYY} {MM}` | EN | 高 |
| 5 | VNPay | `VNPay Vietnam fintech news {YYYY} {MM}` | EN | 高 |
| 6 | PhonePe | `PhonePe India payment news {YYYY} {MM}` | EN | 中 |
| 7 | Razorpay | `Razorpay India news {YYYY} {MM}` | EN | 中 |
| 8 | Airwallex | `Airwallex cross-border payment news {YYYY} {MM}` | EN | 高 |

## Batch 3: 消费金融（17 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | 蚂蚁消金 | `蚂蚁消金 {年}年{月}月` | CN | 高 |
| 1a | 花呗 | `花呗 新动态 {年}年{月}月` | CN | 高 |
| 1b | 借呗 | `借呗 新动态 {年}年{月}月` | CN | 高 |
| 2 | 招联消费金融 | `招联消费金融 新闻 {年}年{月}月` | CN | 高 |
| 3 | 马上消费金融 | `马上消费金融 {年}年{月}月` | CN | 高 |
| 4 | 京东消费金融 | `京东消费金融 白条 {年}年{月}月` | CN | 高 |
| 5 | 美团金融 | `美团金融 月付 {年}年{月}月` | CN | 高 |
| 6 | 度小满 | `度小满 AI 风控 {年}年{月}月` | CN | 高 |
| 7 | Akulaku | `Akulaku Indonesia BNPL news {YYYY} {MM}` | EN | 高 |
| 8 | WeLend 香港 | `WeLend Hong Kong digital lending {YYYY} {MM}` | EN | 高 |
| 9 | Affirm | `Affirm BNPL news {YYYY} {MM}` | EN | 高 |
| 10 | SoFi | `SoFi personal loan news {YYYY} {MM}` | EN | 中 |
| 11 | LendingClub | `LendingClub news {YYYY} {MM}` | EN | 中 |
| 12 | 京东科技 | `京东科技 供应链金融 {年}年{月}月` | CN | 中 |
| 13 | Dave | `Dave app banking overdraft news {YYYY} {MM}` | EN | 中 |
| 14 | Oportun Financial | `Oportun Financial personal loan news {YYYY} {MM}` | EN | 中 |
| 15 | Pagaya | `Pagaya AI credit lending news {YYYY} {MM}` | EN | 中 |
| 16 | Upbound | `Upbound lease payment news {YYYY} {MM}` | EN | 中 |
| 17 | Credit Acceptance | `Credit Acceptance auto lending news {YYYY} {MM}` | EN | 中 |

## Batch 4: 数字银行（13 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | Nubank | `Nubank Brazil digital bank news {YYYY} {MM}` | EN | 高 |
| 2 | Chime | `Chime digital bank news {YYYY} {MM}` | EN | 中 |
| 3 | Revolut | `Revolut banking news {YYYY} {MM}` | EN | 高 |
| 4 | N26 | `N26 Germany digital bank news {YYYY} {MM}` | EN | 中 |
| 5 | Starling Bank | `Starling Bank UK news {YYYY} {MM}` | EN | 中 |
| 6 | Mercury | `Mercury banking US news {YYYY} {MM}` | EN | 中 |
| 7 | ZA Bank 香港 | `ZA Bank 众安银行 {年}年{月}月` | CN | 高 |
| 8 | 天星银行 | `天星银行 香港 {年}年{月}月` | CN | 高 |
| 9 | SeaBank | `SeaBank Indonesia news {YYYY} {MM}` | EN | 高 |
| 10 | Xendit | `Xendit Indonesia payment news {YYYY} {MM}` | EN | 高 |
| 11 | TNG FinTech | `TNG FinTech Hong Kong news {YYYY} {MM}` | EN | 中 |
| 12 | Alkami Technology | `Alkami Technology digital banking news {YYYY} {MM}` | EN | 中 |
| 13 | Blend Labs | `Blend Labs mortgage banking news {YYYY} {MM}` | EN | 中 |

## Batch 5: 财富科技与券商（9 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | Robinhood | `Robinhood news {YYYY} {MM}` | EN | 中 |
| 2 | 富途 | `富途 互联网券商 {年}年{月}月` | CN | 高 |
| 3 | 老虎证券 | `老虎证券 {年}年{月}月` | CN | 中 |
| 4 | 东方财富 | `东方财富 {年}年{月}月` | CN | 中 |
| 5 | 同花顺 | `同花顺 {年}年{月}月` | CN | 高 |
| 6 | Betterment | `Betterment robo-advisor news {YYYY} {MM}` | EN | 中 |
| 7 | Envestnet | `Envestnet wealth management news {YYYY} {MM}` | EN | 中 |
| 8 | Wealthsimple | `Wealthsimple Canada investment news {YYYY} {MM}` | EN | 中 |
| 9 | Tigo Energy | `Tigo Energy investment platform news {YYYY} {MM}` | EN | 中 |
| 10 | Cboe Global Markets | `Cboe Global Markets exchange news {YYYY} {MM}` | EN | 中 |

## Batch 6: 区块链与稳定币（8 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | Circle | `Circle USDC stablecoin news {YYYY} {MM}` | EN | 高 |
| 2 | Tether | `Tether USDT news {YYYY} {MM}` | EN | 中 |
| 3 | Coinbase | `Coinbase news {YYYY} {MM}` | EN | 中 |
| 4 | Binance | `Binance compliance news {YYYY} {MM}` | EN | 中 |
| 5 | Ripple | `Ripple XRP news {YYYY} {MM}` | EN | 中 |
| 6 | Fireblocks | `Fireblocks crypto custody news {YYYY} {MM}` | EN | 中 |
| 7 | Chainalysis | `Chainalysis blockchain analysis news {YYYY} {MM}` | EN | 中 |
| 8 | BVNK | `BVNK stablecoin crypto bank news {YYYY} {MM}` | EN | 低 |

## Batch 7: AI+金融 与 企业服务（8 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | Plaid | `Plaid financial API news {YYYY} {MM}` | EN | 高 |
| 2 | Upstart | `Upstart AI lending news {YYYY} {MM}` | EN | 中 |
| 3 | 蚂蚁万相 灵犀 | `蚂蚁集团 AI 金融 {年}年{月}月` | CN | 高 |
| 4 | 度小满 | `度小满 AI 风控 {年}年{月}月` | CN | 高 |
| 5 | Socure | `Socure AI identity verification news {YYYY} {MM}` | EN | 中 |
| 6 | Figure Technologies | `Figure Technologies blockchain lending news {YYYY} {MM}` | EN | 中 |
| 7 | Toast | `Toast restaurant POS payment news {YYYY} {MM}` | EN | 中 |
| 8 | BlackLine | `BlackLine financial close automation news {YYYY} {MM}` | EN | 中 |

## Batch 8: 保险科技（6 个查询）

| # | 公司 | 查询 | 语言 | 优先级 |
|---|------|------|------|--------|
| 1 | 蚂蚁保 | `蚂蚁保 保险 {年}年{月}月` | CN | 高 |
| 2 | 众安在线 | `众安在线 保险科技 {年}年{月}月` | CN | 高 |
| 3 | Lemonade | `Lemonade insurtech news {YYYY} {MM}` | EN | 中 |
| 4 | FWD Group | `FWD Group Hong Kong insurance news {YYYY} {MM}` | EN | 高 |
| 5 | Snapsheet | `Snapsheet digital claims insurtech news {YYYY} {MM}` | EN | 中 |
| 6 | Better Holdings | `Better Holdings insurtech news {YYYY} {MM}` | EN | 中 |

## Batch 9: 主题搜索（6 个查询）

| # | 查询 | 语言 |
|---|------|------|
| 1 | `Agentic Payment {YYYY} {MM}` | EN |
| 2 | `AI fintech news {YYYY} {MM}` | EN |
| 3 | `stablecoin regulation news {YYYY} {MM}` | EN |
| 4 | `稳定币 监管 {年}年{月}月` | CN |
| 5 | `金融科技 融资 {年}年{月}月` | CN |
| 6 | `CBDC central bank digital currency {YYYY} {MM}` | EN/CN |

## Batch 10: 融资与并购 + 新产品发布（8 个查询）

| # | 查询 | 语言 |
|---|------|------|
| 1 | `fintech payment acquisition deal {YYYY} {MM}` | EN |
| 2 | `payment fintech merger acquisition M&A {YYYY} {MM}` | EN |
| 3 | `fintech new product launch framework {YYYY} {MM}` | EN |
| 4 | `payment protocol framework announcement {YYYY} {MM}` | EN |
| 5 | `fintech startup raises funding round {YYYY} {MM}` | EN |
| 6 | `金融科技 融资 收购 投资 {年}年{月}月` | CN |
| 7 | `payment company new feature product launch {YYYY} {MM}` | EN |
| 8 | `稳定币 融资 收购 牌照 {年}年{月}月` | CN |

## Batch 11: 行业深度报告与咨询报告（8 个查询）

> 当本月涉及重要趋势时，必须搜索顶级咨询公司的行业报告

| # | 查询 | 语言 |
|---|------|------|
| 1 | `KPMG global fintech report {YYYY}` | EN |
| 2 | `McKinsey fintech payments digital banking report {YYYY}` | EN |
| 3 | `BCG Bain fintech stablecoin AI payment report {YYYY}` | EN |
| 4 | `PwC fintech digital assets crypto report {YYYY}` | EN |
| 5 | `Deloitte fintech banking payments report {YYYY}` | EN |
| 6 | `Forrester Gartner fintech payment trend report {YYYY}` | EN |
| 7 | `世界银行 IMF fintech 数字支付 报告 {年}年` | CN |
| 8 | `艾瑞咨询 亿欧 金融科技 行业报告 {年}年` | CN |

## Batch 12: 监管执法与处罚（6 个查询）

| # | 查询 | 语言 |
|---|------|------|
| 1 | `fintech penalty fine enforcement regulator {YYYY} {MM}` | EN |
| 2 | `payment company regulatory penalty fine {YYYY} {MM}` | EN |
| 3 | `crypto exchange fine penalty SEC enforcement {YYYY} {MM}` | EN |
| 4 | `央行 罚款 处罚 支付 金融科技 {年}年{月}月` | CN |
| 5 | `fintech license revoked suspended regulator {YYYY} {MM}` | EN |
| 6 | `PBOC HKMA MAS fintech enforcement action penalty {YYYY} {MM}` | EN |

## Batch 13: 产品级功能发布（竞品动态追踪）

> 查询设计基于字节财经实际业务线（抖音支付、放心借、月付、TikTok Shop支付、保险经纪、香港SVF）

| # | 查询 | 语言 | 对标字节业务 |
|---|------|------|-------------|
| 1 | `支付宝 新功能 产品 更新 {年}年{月}月` | CN | 抖音支付 |
| 2 | `支付宝 AI智能体 智能助理 金融 {年}年{月}月` | CN | AI金融 |
| 3 | `微信 碰一下 支付 新场景 拓展 {年}年{月}月` | CN | 抖音支付线下 |
| 4 | `花呗 借呗 新产品 功能更新 {年}年{月}月` | CN | 放心借/月付 |
| 5 | `美团月付 美团借钱 新功能 {年}年{月}月` | CN | 月付/放心借 |
| 6 | `京东白条 京东金融 新产品 {年}年{月}月` | CN | 月付/放心借 |
| 7 | `TikTok Shop payment checkout new feature {YYYY} {MM}` | EN | TikTok Shop支付 |
| 8 | `Shopify Shop Pay checkout payment update {YYYY} {MM}` | EN | TikTok Shop支付 |
| 9 | `Amazon Pay Buy with Prime checkout {YYYY} {MM}` | EN | TikTok Shop支付 |
| 10 | `Klarna BNPL new product feature {YYYY} {MM}` | EN | 月付/BNPL |
| 11 | `SeaMoney SeaBank new product feature {YYYY} {MM}` | EN | TikTok Shop东南亚 |
| 12 | `Grab Financial GrabPay new feature {YYYY} {MM}` | EN | 东南亚支付 |
| 13 | `GoPay Gojek financial product update {YYYY} {MM}` | EN | 东南亚支付 |
| 14 | `Kredivo Atome BNPL Southeast Asia {YYYY} {MM}` | EN | 东南亚BNPL |
| 15 | `Affirm BNPL new merchant feature {YYYY} {MM}` | EN | 月付/BNPL |
| 16 | `Stripe new product feature launch {YYYY} {MM}` | EN | 支付基础设施 |
| 17 | `PayPal new product Venmo feature {YYYY} {MM}` | EN | 跨境支付 |
| 18 | `Adyen new payment method feature {YYYY} {MM}` | EN | 支付基础设施 |
| 19 | `AI financial assistant AI lending AI risk control {YYYY} {MM}` | EN | AI金融 |
| 20 | `Apple Pay new feature launch {YYYY} {MM}` | EN | 支付 |
| 21 | `Google Pay Google Wallet update {YYYY} {MM}` | EN | 支付 |
| 22 | `Meta AI shopping mode Instagram Facebook {YYYY} {MM}` | EN | 社交电商+支付 |
| 23 | `蚂蚁保 保险科技 新产品 {年}年{月}月` | CN | 保险经纪 |
| 24 | `众安在线 互联网保险 新产品 {年}年{月}月` | CN | 保险经纪 |
| 25 | `ZA Bank 众安银行 香港 新产品 {年}年{月}月` | CN | 香港出海 |

**总共：128 个查询必须全部执行**
