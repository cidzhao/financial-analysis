# CRCL Key Financial Analysis Notes

本文总结此前围绕 Circle Internet Group, Inc. (`CRCL`) 财报和业务模型讨论出的关键结论。主要参考 Circle 2025 Q2/Q3/Q4、2026 Q1 earnings releases、SEC 10-Q/10-K，以及 Circle/BlackRock/Fed 官方公开信息。

## 1. 核心收入结构

CRCL 的收入分为两大块：

- `Reserve income`: USDC/EURC 储备资产产生的利息、股息和货币基金收益。这是目前绝对核心收入来源。
- `Other revenue`: 除储备收益外的平台和服务收入，包括 `subscription and services revenue`、`transaction revenue` 和其他服务收入。

`Other revenue` 具体包括：

- 集成服务和维护服务收入。
- 基金管理费，例如 USYC 相关管理费。
- 按时间或按用户授权的服务费。
- 稳定币和 USYC 赎回费。
- 区块链奖励收入。
- 使用 Circle 基础设施处理数字资产交易的费用，例如 CCTP 相关交易基础设施收入。
- 非经常性服务费和部分已停止 legacy products 的收入。

截至 2026 Q1，`Other revenue` 仍然较小：

```text
2026 Q1 Reserve income: 652.508M
2026 Q1 Other revenue:   41.625M
2026 Q1 Total revenue:  694.133M
Other revenue 占比约 6.0%
```

因此，CRCL 目前仍主要是储备收益驱动的公司，`Other revenue` 是证明其不只是“吃利息”的重要增长项。

## 2. Operating Income From Continuing Operations

`Operating income from continuing operations` 是持续经营业务的营业利润，不包括非经营性项目、所得税和终止经营业务。

公式为：

```text
Operating income from continuing operations
= Total revenue and reserve income
- Total distribution, transaction and other costs
- Total operating expenses
```

以 2026 Q1 为例：

```text
694.133M - 406.781M - 242.350M = 45.002M
```

## 3. USDC In Circulation: End vs Average

`USDC in Circulation, end of period` 是期末某一天的流通 USDC 余额，是时点数。

`USDC in Circulation, average of period` 是整个季度或期间的平均流通余额，是期间平均数。

分析储备收入时，应优先看 `average of period`，因为储备资产是整个季度持续产生收益，而不是只在期末一天产生收益。

## 4. 分销成本与 Coinbase

Circle 的商业模式最核心的压力来自高额分销成本。USDC 储备收益并不是 Circle 全部留下，必须分给 Coinbase、Binance 和其他战略分销伙伴。

2026 Q1 数据：

```text
Reserve income                         652.5M
Distribution and transaction costs      405.4M
Coinbase distribution costs             330.6M
```

比例约为：

```text
Distribution and transaction costs / Reserve income = 62.1%
Coinbase costs / Reserve income = 50.7%
Coinbase costs / Distribution and transaction costs = 81.6%
```

所以，“63% 全部分给 Coinbase”并不准确。更准确地说，2026 Q1 分销及交易成本约等于储备收入的 62%，其中 Coinbase 一项约等于储备收入的 51%。这仍然非常高，说明 Coinbase 是 CRCL 利润质量的关键约束。

更应关注 `RLDC`：

```text
RLDC = Total revenue and reserve income - distribution, transaction and other costs
```

2026 Q1：

```text
Total revenue and reserve income     694.1M
Distribution/transaction/other costs  406.8M
RLDC                                  287.4M
RLDC margin                           41.4%
```

CRCL 的业务不是没有价值，而是总收入看起来很大，真正留下来的收入池明显小很多。

## 5. 2026 Q1 是否亏损

2026 Q1 没有亏损，是盈利的：

```text
Operating income from continuing operations    45.0M
Net income from continuing operations          55.2M
Net income attributable to common stockholders 55.3M
Basic EPS                                      0.23
Diluted EPS                                    0.21
```

但利润率较低，且比 2025 Q3/Q4 明显回落，主要原因是：

- 储备收益率下降。
- 期间平均 USDC 流通量环比下降。
- 分销成本仍然很高。
- 上市后继续扩团队、合规、Arc、CPN、USYC 等投入，运营费用较高。

## 6. 2025 Q2 Compensation Expenses 异常高的原因

2025 Q2 `Compensation expenses` 为 503.392M，明显高于其他季度。主要原因不是现金工资暴涨，而是 IPO 触发的一次性股权激励费用。

拆分：

```text
2025 Q2 Compensation expenses         503.392M
其中 Stock-based compensation expense 434.966M
占比约 86.4%
```

Circle IPO 前发放的部分 RSU 同时满足两个条件后才能确认费用：

- `service condition`: 员工服务期条件。
- `liquidity-event related performance condition`: 流动性事件条件，即 IPO/上市交易。

2025 年 6 月 CRCL 在 NYSE 上市后，流动性事件条件满足，公司一次性确认约 423.8M 的 stock-based compensation expense，涉及约 9.5M 股 Class A common stock 归属，其中约 4.0M 股用于税款预扣。

剔除股权激励后：

```text
Q2 compensation expenses - stock-based compensation
= 503.392M - 434.966M
= 68.426M
```

这更接近常态薪酬水平。

## 7. Q3 2025 Income Tax Expense 为负的原因

2025 Q3 `Income tax expense (benefit)` 为 `(61.294M)`，括号表示负数，即所得税收益，不是税费支出。

计算关系：

```text
Net income before income taxes       153.091M
Less: Income tax expense (benefit)   (61.294M)
Net income                           214.385M
```

因为税项是负数：

```text
153.091M - (-61.294M) = 214.385M
```

Circle 披露该所得税收益主要来自：

- 股权激励费用相关税务影响。
- 研发税收抵免。
- 近期美国税法变化影响。

这不一定代表收到现金退税，更多是 GAAP 下确认的税收收益、递延税项和税收抵免影响。

## 8. Other Income (Expense), Net

`Other income (expense), net` 是营业利润之后、税前利润之前的非经营性收益或费用净额。

它不同于 `Other revenue`。主要包括：

- 可转换债务、warrant liability、embedded derivatives 的公允价值变动。
- 公司现金利息收入。
- 数字资产和战略投资的已实现/未实现收益或损失。
- 外汇损益。
- 其他非经营性项目。

2025 Q2 为负，主要因为股价上涨导致可转换债务等金融工具公允价值上升，形成非现金费用。Q2 release 披露 IPO 相关非现金影响合计 591M，其中包括：

- 424M stock-based compensation related to IPO vesting conditions。
- 167M increase in fair value of convertible debt caused by share price increase。

## 9. Diluted EPS 为什么不能直接用净利润除以 diluted shares

2025 Q4：

```text
Net income attributable to common stockholders = 133.416M
Diluted weighted-average shares                = 267.804M
直接相除                                      ≈ 0.50
Reported diluted EPS                           = 0.43
```

直接相除对不上，因为 diluted EPS 不是简单用这两行相除。Circle 使用 two-class method，并且 diluted EPS 会考虑潜在普通股转换、warrants、unvested awards、convertible securities 等对分子和分母的影响。

2025 Q3/Q4 还涉及 convertible debt、warrant liability、embedded derivatives 公允价值变动，diluted EPS 的分子/分母可能需要按 if-converted 或稀释假设调整。earnings release 没有给完整 EPS bridge，因此只能确认机制，不能仅凭摘要表复算出 0.43。

## 10. 股数是否还会变化

会。CRCL 未来总股数大概率仍会变化，尤其是 Class A common stock outstanding 和 diluted shares。

2026 Q1 10-Q：

```text
Class A issued and outstanding: 228.9M
Class B issued and outstanding: 18.7M
合计实际已发行流通股数: 约 247.6M

Basic weighted-average shares:   244.038M
Diluted weighted-average shares: 266.687M
```

潜在变化来源：

- RSU 归属和结算。
- 员工或高管期权行权。
- warrants 行权。
- 可转债转换。
- 未来再融资或股票并购。
- Class B 转 Class A，不改变总股数，但会改变流通盘和投票权结构。

估值时不应只看 basic shares，应重点看 diluted weighted-average shares 或 fully diluted share count。

## 11. 储备资产是否全部买国债

不是。USDC 储备不是 100% 直接买美国国债。

2026 Q1 10-Q 披露的 USDC 储备构成：

```text
Cash 银行现金             10.658B
Circle Reserve Fund      66.467B
合计                     77.125B
```

比例约为：

```text
Circle Reserve Fund: 约 86%
银行现金: 约 14%
```

Circle Reserve Fund 是 BlackRock 管理的政府货币市场基金，持有：

- 3 个月以内美国国债。
- 隔夜美国国债回购。
- 现金。

因此更准确的表述是：Circle 储备主要投向短期美债相关高流动性资产，但不是全部直接买国债。

## 12. 储备资产平均年化收益率

2026 Q1：

```text
Reserve income              652.508M
Average USDC in circulation 75.2B
季度收益率                  652.508M / 75.2B ≈ 0.87%
年化                         ≈ 3.5%
```

Circle 披露的 `Reserve Return Rate` 为 3.5%。

BlackRock USDXX 页面显示截至 2026-06-24，Circle Reserve Fund 的 `7 Day SEC Yield` 为 3.58%。

但 Circle 自己扣除分销成本后的留存收益率明显更低。2026 Q1：

```text
Reserve income                         652.5M
Distribution and transaction costs      405.4M
扣除后剩余                             247.1M
```

按平均 USDC 75.2B 年化：

```text
247.1M / 75.2B * 4 ≈ 1.3%
```

所以：

```text
储备资产毛收益率: 约 3.5%
Circle 扣除分销成本后的净留存: 约 1.3% - 1.5%
```

## 13. 美联储利率和 CRCL 利率敏感性

截至 2026-06-25，最新 FOMC 决议显示联邦基金目标利率区间为：

```text
3.50% - 3.75%
```

CRCL 对利率高度敏感，因为储备资产主要是短期美元利率资产。降息会降低 reserve income，加息会提高 reserve income。

Circle 2026 Q1 10-Q 给出的敏感性测算，以 2026 年 3 月平均收益率 3.49% 为基准，假设 USDC 流通规模和储备配置不变：

```text
+200 bps: reserve income +1.546B/年, distribution costs +769M/年, 留存约 +777M/年
+100 bps: reserve income +773M/年,  distribution costs +384M/年, 留存约 +389M/年
-100 bps: reserve income -773M/年,  distribution costs -384M/年, 留存约 -389M/年
-200 bps: reserve income -1.546B/年, distribution costs -769M/年, 留存约 -777M/年
```

换算成 25bp：

```text
每加息 25bp:
Reserve income 约 +193M/年
扣除分销成本后的 Circle 留存约 +97M/年

每降息 25bp:
Reserve income 约 -193M/年
扣除分销成本后的 Circle 留存约 -97M/年
```

这只是静态测算。实际影响还取决于 USDC 流通量变化、用户行为、分销协议、储备配置和短端利率曲线。

## 14. 综合判断

CRCL 不是简单的“业务糟糕”，但其利润质量确实受两个核心因素限制：

- 分销伙伴尤其 Coinbase 分走大量储备收益。
- 储备收益高度依赖美联储短端利率。

看多逻辑：

- USDC 流通规模增长。
- Other revenue 增长。
- CPN、Arc、USYC、CCTP 等平台化收入拓展。
- 稳定币监管清晰后，合规发行商可能受益。

看空逻辑：

- Coinbase 分润过高。
- 降息周期压低储备收益。
- 竞争加剧可能导致更多分销激励。
- 股权激励和扩张费用仍会压制 GAAP 利润。
- 总收入看起来很大，但 RLDC 才是更接近 Circle 自己可留存的收入池。

因此，分析 CRCL 应重点关注：

```text
USDC average circulation
Reserve return rate
Distribution and transaction costs
RLDC and RLDC margin
Other revenue growth
Operating expenses
Diluted shares
Fed rate path
```

## 15. 主要参考来源

- Circle 2025 Q2/Q3/Q4 earnings releases.
- Circle 2026 Q1 earnings release.
- Circle 2025 10-K: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000062/crcl-20251231.htm
- Circle 2026 Q1 10-Q: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm
- Circle 2025 Q2 10-Q: https://www.sec.gov/Archives/edgar/data/1876042/000162828025039781/crcl-20250630.htm
- Circle Transparency: https://www.circle.com/transparency
- BlackRock Circle Reserve Fund USDXX: https://www.blackrock.com/cash/en-us/products/329365/circle-reserve-fund
- Federal Reserve FOMC statement, 2026-06-17: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
