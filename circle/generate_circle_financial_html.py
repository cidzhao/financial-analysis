from __future__ import annotations

from html import escape
from pathlib import Path
import re


OUT = Path(__file__).with_name("circle_financial_analysis.html")


def row(label: str, *values: str) -> list[str]:
    return [label, *values]


def group(label: str) -> list[str]:
    return [label]


def clean_label(label: str) -> str:
    label = label.replace("\n", " ").replace("/", " ")
    label = re.sub(r"\s+", " ", label).strip()
    label = re.sub(r"\(\d+\)", "", label).strip()
    return label


EXACT_CN = {
    "Total Revenue and Reserve Income": "总收入与储备收入合计, 包括储备资产产生的收入以及其他业务收入。",
    "Revenue Less Distribution Costs": "收入减分发成本, 即总收入与储备收入扣除分发、交易及其他成本后的收入能力。",
    "RLDC Margin": "收入减分发成本率, 用 RLDC 除以总收入与储备收入衡量。",
    "Net Income from Continuing Operations": "持续经营净利润, 反映持续业务扣税后的 GAAP 盈利。",
    "Net Income (Loss) from Continuing Operations": "持续经营净利润或净亏损, 反映持续业务扣税后的 GAAP 盈亏。",
    "Net Income (loss) from Continuing Operations": "持续经营净利润或净亏损, 反映持续业务扣税后的 GAAP 盈亏。",
    "Net Income from Continuing Operations Margin": "持续经营净利率, 用持续经营净利润除以总收入与储备收入。",
    "Net Income (loss) from Continuing Operations Margin": "持续经营净利润或净亏损率, 用持续经营净利润或亏损除以总收入与储备收入。",
    "Adjusted EBITDA": "调整后 EBITDA, 公司使用的 Non-GAAP 经营盈利指标。",
    "Adjusted EBITDA (Prior Definition)": "调整后 EBITDA 旧定义, 尚未加入 Q1 2026 起新增的股权激励相关工资税剔除项。",
    "Adjusted EBITDA (New Definition)": "调整后 EBITDA 新定义, 加回股权激励相关工资税后的 Non-GAAP 经营盈利指标。",
    "Adjusted EBITDA Margin": "调整后 EBITDA 率, 用调整后 EBITDA 除以 RLDC。",
    "USDC in Circulation, end of period": "期末流通 USDC 规模, 反映期末外部流通稳定币余额。",
    "USDC in Circulation, average of period": "期间平均流通 USDC 规模, 反映当期平均储备基础。",
    "Average USDC in Circulation": "平均流通 USDC 规模, 反映当期平均储备基础。",
    "Reserve Return Rate": "储备收益率, 反映储备资产组合的收益水平。",
    "USDC on Platform, end of period": "期末平台内 USDC, 反映 Circle 平台上留存的 USDC 余额。",
    "Daily Weighted-Average Percentage of USDC on Platform": "平台内 USDC 日加权平均占比, 反映 USDC 留存在平台内的比例。",
    "USDC on Platform, daily weighted average percentage": "平台内 USDC 日加权平均占比, 反映 USDC 留存在平台内的比例。",
    "USDC on Platform, daily weighted average percentage": "平台内 USDC 日加权平均占比, 反映 USDC 留存在平台内的比例。",
    "USDC Minted": "USDC 铸造量, 反映当期新增发行规模。",
    "USDC Redeemed": "USDC 赎回量, 反映当期赎回规模。",
    "Stablecoin Market Share, end of period": "期末稳定币市场份额, USDC 在符合口径的美元法币支持稳定币中的占比。",
    "Meaningful Wallets, end of period": "期末有效钱包数, 指持有超过 10 美元 USDC 的链上钱包数量。",
    "USDC in Circulation": "流通 USDC 规模, 公司给出的中长期增长指标。",
    "Other Revenue": "其他收入, 包括订阅、服务、交易等非储备收入。",
    "Adjusted Operating Expenses": "调整后运营费用, 剔除部分非现金、一次性或非核心项目后的 Non-GAAP 费用。",
    "Adjusted Operating Expenses (prior definition)": "调整后运营费用旧定义, 不含 Q1 2026 起新增剔除项。",
    "Adjusted Operating Expenses (new definition)": "调整后运营费用新定义, 包含 Q1 2026 起新增的 payroll tax、法律费用、并购费用等剔除口径。",
    "Operating expenses": "运营费用总额, GAAP 口径的各项运营费用合计。",
    "Operating Expenses": "运营费用总额, GAAP 口径的各项运营费用合计。",
    "Reserve Income": "储备收入, 来自支持稳定币储备资产的收益。",
    "Distribution and Transaction Costs": "分发及交易成本, 包括向合作伙伴分成和交易相关成本。",
    "Other Costs": "其他成本, 与收入相关但不属于分发和交易成本的项目。",
    "Other costs": "其他成本, 与收入相关但不属于分发和交易成本的项目。",
    "Total Distribution, Transaction and Other Costs": "分发、交易及其他成本合计。",
    "Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs": "总收入与储备收入减分发、交易及其他成本后的金额, 即 RLDC。",
    "Net Reserve Margin": "净储备利差, 用储备收入减分发及交易成本后除以储备收入。",
    "Cash and cash equivalents": "现金及现金等价物。",
    "Cash and cash equivalents segregated for corporate-held stablecoins": "为公司持有稳定币单独隔离的现金及现金等价物。",
    "Cash and cash equivalents segregated for the benefit of stablecoin holders": "为稳定币持有人利益隔离的现金及现金等价物。",
    "Accounts receivable, net": "应收账款净额。",
    "Stablecoins receivable, net": "应收稳定币净额。",
    "Prepaid expenses and other current assets": "预付款项及其他流动资产。",
    "Total current assets": "流动资产合计。",
    "Restricted cash": "受限现金。",
    "Investments": "投资资产。",
    "Fixed assets, net": "固定资产净额。",
    "Digital assets": "数字资产。",
    "Goodwill": "商誉。",
    "Intangible assets, net": "无形资产净额。",
    "Deferred tax assets, net": "递延所得税资产净额。",
    "Other non-current assets": "其他非流动资产。",
    "Total assets": "资产总额。",
    "Deposits from stablecoin holders": "稳定币持有人存款负债, 与稳定币兑换义务相关。",
    "Accounts payable and accrued expenses": "应付账款及应计费用。",
    "Convertible debt, net of debt discount": "可转换债务, 扣除债务折价后的净额。",
    "Other current liabilities": "其他流动负债。",
    "Total current liabilities": "流动负债合计。",
    "Deferred tax liabilities, net": "递延所得税负债净额。",
    "Warrant liability": "认股权证负债。",
    "Other non-current liabilities": "其他非流动负债。",
    "Total non-current liabilities": "非流动负债合计。",
    "Total liabilities": "负债总额。",
    "Redeemable convertible preferred stock": "可赎回可转换优先股。",
    "Class A common stock": "A 类普通股账面金额及授权、发行、流通股信息。",
    "Class B common stock": "B 类普通股账面金额及授权、发行、流通股信息。",
    "Class C common stock": "C 类普通股账面金额及授权、发行、流通股信息。",
    "Treasury stock at cost": "按成本列示的库存股。",
    "Additional paid-in capital": "资本公积。",
    "Accumulated deficit": "累计亏损。",
    "Accumulated other comprehensive income": "累计其他综合收益。",
    "Total stockholders' equity": "股东权益合计。",
    "Total stockholders' equity attributable to common stockholders": "归属于普通股股东的股东权益合计。",
    "Noncontrolling interests": "非控制性权益。",
    "Noncontrolling Interest": "非控制性权益。",
    "Total liabilities, redeemable convertible preferred stock and stockholders' equity": "负债、可赎回可转换优先股及股东权益合计。",
    "Total liabilities and stockholders' equity": "负债及股东权益合计。",
    "Reserve income": "储备收入, 来自支持稳定币储备资产的收益。",
    "Other revenue": "其他收入, 包括订阅、服务、交易等非储备收入。",
    "Total revenue and reserve income": "总收入与储备收入合计。",
    "Distribution and transaction costs": "分发及交易成本。",
    "Total distribution, transaction and other costs": "分发、交易及其他成本合计。",
    "Compensation expenses": "薪酬费用。",
    "General and administrative expenses": "一般及行政费用。",
    "Depreciation and amortization expenses": "折旧及摊销费用。",
    "IT infrastructure costs": "IT 基础设施成本。",
    "Marketing expenses": "营销费用。",
    "Digital assets losses (gains)": "数字资产损失或收益。",
    "Digital assets (gains) losses": "数字资产收益或损失。",
    "Total operating expenses": "运营费用合计。",
    "Operating income from continuing operations": "持续经营营业利润。",
    "Operating income (loss) from continuing operations": "持续经营营业利润或亏损。",
    "Other income (expense), net": "其他收入或费用净额。",
    "Other (expense) income, net": "其他费用或收入净额。",
    "Net income from continuing operations before income taxes": "持续经营税前净利润。",
    "Net income from continuing operations": "持续经营净利润。",
    "Net income (loss) from continuing operations before income taxes": "持续经营税前净利润或亏损。",
    "Income tax expense (benefit)": "所得税费用或收益。",
    "Income tax (benefit) expense": "所得税收益或费用。",
    "Net income (loss) from continuing operations": "持续经营净利润或净亏损。",
    "Less: Net loss attributable to noncontrolling interests": "减: 归属于非控制性权益的净亏损。",
    "Net income attributable to common stockholders": "归属于普通股股东的净利润。",
    "Net income (loss) attributable to common stockholders": "归属于普通股股东的净利润或亏损。",
    "Loss from operations of discontinued businesses": "终止经营业务亏损。",
    "Net income (loss)": "净利润或净亏损。",
    "Continuing operations": "持续经营业务每股收益或亏损。",
    "Discontinued operations": "终止经营业务每股收益或亏损。",
    "Basic": "基本每股收益或加权平均基本股数, 取决于所在分组。",
    "Diluted": "稀释每股收益或加权平均稀释股数, 取决于所在分组。",
    "Basic earnings (loss) per common share attributable to common stockholders": "归属于普通股股东的基本每股收益或亏损。",
    "Diluted earnings (loss) per common share attributable to common stockholders": "归属于普通股股东的稀释每股收益或亏损。",
    "Weighted-average shares used in computing earnings (loss) per share attributable to common stockholders, basic": "计算基本每股收益或亏损使用的加权平均普通股股数。",
    "Weighted-average shares used in computing earnings (loss) per share attributable to common stockholders, diluted": "计算稀释每股收益或亏损使用的加权平均普通股股数。",
    "Weighted-average shares used in computing earnings (loss) per share: Basic": "计算基本每股收益或亏损使用的加权平均股数。",
    "Weighted-average shares used in computing earnings (loss) per share: Diluted": "计算稀释每股收益或亏损使用的加权平均股数。",
    "Weighted-average shares used to compute earnings per share attributable to common stockholders: Basic": "计算基本每股收益使用的加权平均普通股股数。",
    "Weighted-average shares used to compute earnings per share attributable to common stockholders: Diluted": "计算稀释每股收益使用的加权平均普通股股数。",
    "Net income (loss) from continuing operations attributable to common stockholders": "归属于普通股股东的持续经营净利润或净亏损。",
    "Depreciation and amortization expense": "折旧及摊销费用调节项。",
    "Interest expense, net of amortization of discounts and premiums": "利息费用, 扣除折价及溢价摊销后的净额。",
    "Interest income": "利息收入调节项, 不含储备收入。",
    "Stock-based compensation expense": "股权激励费用。",
    "Stock-based compensation expense and related payroll taxes": "股权激励费用及相关工资税。",
    "Stock-based compensation related payroll expense": "与股权激励相关的工资税费用。",
    "Legal expenses": "特定法律费用或一次性法律相关费用。",
    "Realized and unrealized (gains) losses, net, on digital assets held for investment, other related investments and strategic investments": "投资性数字资产、相关投资和战略投资的已实现及未实现收益或损失净额。",
    "Realized and unrealized losses (gains), net, on digital assets held for investment, other related investments and strategic investments": "投资性数字资产、相关投资和战略投资的已实现及未实现损失或收益净额。",
    "Realized (gains) losses on available-for-sale debt securities": "可供出售债务证券已实现收益或损失。",
    "Realized (gains) on available-for-sale debt securities": "可供出售债务证券已实现收益。",
    "Impairment losses on strategic investments": "战略投资减值损失。",
    "Restructuring expenses": "重组费用。",
    "Acquisition-related costs": "并购相关费用。",
    "Change in fair value of convertible debt, warrant liability, and embedded derivatives": "可转换债务、认股权证负债和嵌入衍生工具公允价值变动。",
    "Change in fair value of convertible debt, warrant liability, embedded derivatives, and U.S. Treasury securities": "可转换债务、认股权证负债、嵌入衍生工具及美国国债公允价值变动。",
    "Charitable contributions to Circle Foundation": "向 Circle Foundation 的慈善捐赠费用。",
    "Losses on sale of long-lived assets": "长期资产出售损失。",
    "Foreign currency exchange (gains) losses": "外汇兑换收益或损失。",
    "Foreign currency exchange (gain) loss": "外汇兑换收益或损失。",
    "Foreign currency exchange loss": "外汇兑换损失。",
    "Stock-based compensation expense": "股权激励费用。",
    "Digital asset (gains) losses": "数字资产收益或损失。",
    "Digital assets losses (gains)": "数字资产损失或收益。",
    "DAF contribution": "捐赠者建议基金捐赠, 与 Circle Foundation 相关。",
    "Payroll tax expense related to stock-based compensation": "与股权激励相关的工资税费用。",
    "Charitable contributions to Circle Foundation": "向 Circle Foundation 的慈善捐赠费用。",
    "Stock-based compensation expense and related payroll taxes": "股权激励费用及相关工资税。",
}


GROUP_CN = {
    "ASSETS": "资产部分。",
    "Current assets:": "流动资产。",
    "Non-current assets:": "非流动资产。",
    "LIABILITIES AND STOCKHOLDERS' EQUITY": "负债及股东权益。",
    "LIABILITIES, REDEEMABLE CONVERTIBLE PREFERRED STOCK AND STOCKHOLDERS' EQUITY": "负债、可赎回可转换优先股及股东权益。",
    "Current liabilities:": "流动负债。",
    "Non-current liabilities:": "非流动负债。",
    "Commitments and contingencies": "承诺及或有事项。",
    "Stockholders' equity": "股东权益。",
    "Revenue and reserve income": "收入与储备收入。",
    "Distribution, transaction and other costs": "分发、交易及其他成本。",
    "Operating expenses": "运营费用。",
    "Earnings (loss) per share:": "每股收益或亏损。",
    "Earnings (loss) per share attributable to common stockholders:": "归属于普通股股东的每股收益或亏损。",
    "Earnings per share attributable to common stockholders:": "归属于普通股股东的每股收益。",
    "Earnings (loss) per share attributable to common stockholders, basic and diluted": "归属于普通股股东的基本和稀释每股收益或亏损。",
    "Basic earnings (loss) per common share attributable to common stockholders:": "归属于普通股股东的基本每股收益或亏损。",
    "Diluted earnings (loss) per common share attributable to common stockholders:": "归属于普通股股东的稀释每股收益或亏损。",
    "Weighted-average common shares used to compute earnings per share:": "用于计算每股收益的加权平均普通股数。",
    "Weighted-average shares used in computing earnings (loss) per share:": "用于计算每股收益或亏损的加权平均股数。",
    "Weighted-average shares used to compute earnings per share attributable to common stockholders:": "用于计算归属于普通股股东每股收益的加权平均股数。",
    "Adjusted for:": "调节项目。",
    "Key Financial Results": "关键财务结果。",
    "Key Operating Indicators": "关键经营指标。",
}


PREFIX_CN = [
    ("Class A common stock", "A 类普通股账面金额及授权、发行、流通股信息。"),
    ("Class B common stock", "B 类普通股账面金额及授权、发行、流通股信息。"),
    ("Class C common stock", "C 类普通股账面金额及授权、发行、流通股信息。"),
    ("Redeemable convertible preferred stock", "可赎回可转换优先股账面金额及股数信息。"),
    ("Treasury stock at cost", "按成本列示的库存股。"),
    ("Weighted-average shares used in computing earnings (loss) per share attributable to common stockholders", "计算归属于普通股股东每股收益或亏损使用的加权平均股数。"),
    ("Basic earnings (loss) per common share", "基本每股收益或亏损。"),
    ("Diluted earnings (loss) per common share", "稀释每股收益或亏损。"),
]


def explain(label: str) -> str:
    normalized = clean_label(label)
    if normalized in GROUP_CN:
        return GROUP_CN[normalized]
    if normalized in EXACT_CN:
        return EXACT_CN[normalized]
    for prefix, cn in PREFIX_CN:
        if normalized.startswith(prefix):
            return cn
    if not normalized:
        return ""
    return "财报原文项目, 中文含义按英文项目名称理解。"


reports = [
    {
        "id": "q2-2025",
        "title": "Q2 2025 Earnings Release",
        "pdf": "Circle-Q2-2025-Earnings-Release.pdf",
        "period": "Second quarter 2025",
        "date": "August 12, 2025",
        "summary": "USDC 流通规模和储备收入快速增长, 但 IPO 相关股权激励和可转换工具公允价值变动导致 GAAP 净亏损。",
        "sections": [
            {
                "title": "Key Financial Results and Operating Indicators",
                "source": "Page 2",
                "unit": "$ in millions unless noted otherwise; USDC figures in $ billions; meaningful wallets in millions",
                "columns": ["Metric", "Q2 2025", "YoY Change"],
                "rows": [
                    group("Key Financial Results"),
                    row("Total Revenue and Reserve Income", "$658", "53%"),
                    row("Revenue Less Distribution Costs(1)", "$251", "38%"),
                    row("RLDC Margin(2)", "38%", "(408bps)"),
                    row("Net Income (Loss) from Continuing Operations", "$(482)", "NM"),
                    row("Adjusted EBITDA(3)", "$126", "52%"),
                    row("Adjusted EBITDA Margin(3)", "50%", "463bps"),
                    group("Key Operating Indicators"),
                    row("USDC in Circulation, end of period", "$61.3", "90%"),
                    row("Average USDC in Circulation", "$61.0", "86%"),
                    row("Reserve Return Rate", "4.1%", "(103bps)"),
                    row("USDC on Platform, end of period", "$6.0", "924%"),
                    row("Daily Weighted-Average Percentage of USDC on Platform", "7.4%", "536bps"),
                    row("USDC Minted", "$42.2", "21%"),
                    row("USDC Redeemed", "$40.8", "17%"),
                    row("Stablecoin Market Share, end of period(4)", "28%", "595bps"),
                    row("Meaningful Wallets, end of period(5)", "5.7", "68%"),
                ],
            },
            {
                "title": "Forward Outlook",
                "source": "Page 4",
                "unit": "Company outlook",
                "columns": ["Key Indicator", "Period", "Outlook"],
                "rows": [
                    row("USDC in Circulation", "Multi-year through cycle", "40% CAGR"),
                    row("Other Revenue", "FY 2025", "$75-$85M"),
                    row("RLDC Margin(1)", "FY 2025", "36-38%"),
                    row("Adjusted Operating Expenses(2)", "FY 2025", "$475-$490M"),
                ],
            },
            {
                "title": "Condensed Consolidated Balance Sheets",
                "source": "Pages 8-9",
                "unit": "in $ thousands, except share information",
                "columns": ["Line Item", "June 30, 2025 (unaudited)", "December 31, 2024"],
                "rows": [
                    group("ASSETS"),
                    group("Current assets:"),
                    row("Cash and cash equivalents", "$1,118,119", "$750,981"),
                    row("Cash and cash equivalents segregated for corporate-held stablecoins", "588,271", "294,493"),
                    row("Cash and cash equivalents segregated for the benefit of stablecoin holders", "61,365,920", "43,918,572"),
                    row("Accounts receivable, net", "13,215", "6,418"),
                    row("Stablecoins receivable, net", "-", "6,957"),
                    row("Prepaid expenses and other current assets", "216,604", "187,528"),
                    row("Total current assets", "63,302,129", "45,164,949"),
                    group("Non-current assets:"),
                    row("Restricted cash", "3,210", "3,558"),
                    row("Investments", "83,794", "84,114"),
                    row("Fixed assets, net", "23,804", "18,682"),
                    row("Digital assets", "35,113", "31,330"),
                    row("Goodwill", "266,384", "169,544"),
                    row("Intangible assets, net", "396,969", "331,394"),
                    row("Deferred tax assets, net", "17,472", "10,223"),
                    row("Other non-current assets", "24,633", "20,615"),
                    row("Total assets", "$64,153,508", "$45,834,409"),
                    group("LIABILITIES, REDEEMABLE CONVERTIBLE PREFERRED STOCK AND STOCKHOLDERS' EQUITY"),
                    group("Current liabilities:"),
                    row("Accounts payable and accrued expenses", "$411,560", "$287,007"),
                    row("Deposits from stablecoin holders", "61,101,523", "43,727,363"),
                    row("Convertible debt, net of debt discount", "206,140", "-"),
                    row("Other current liabilities", "11,211", "16,597"),
                    row("Total current liabilities", "61,730,434", "44,030,967"),
                    group("Non-current liabilities:"),
                    row("Convertible debt, net of debt discount", "-", "40,717"),
                    row("Deferred tax liabilities, net", "31,812", "29,559"),
                    row("Warrant liability", "-", "1,591"),
                    row("Other non-current liabilities", "20,431", "21,281"),
                    row("Total non-current liabilities", "52,243", "93,148"),
                    row("Total liabilities", "$61,782,677", "$44,124,115"),
                    group("Commitments and contingencies"),
                    row("Redeemable convertible preferred stock", "-", "1,139,765"),
                    group("Stockholders' equity"),
                    row("Class A common stock", "23", "6"),
                    row("Class B common stock", "2", "-"),
                    row("Class C common stock", "-", "-"),
                    row("Treasury stock at cost", "(2,877)", "(2,877)"),
                    row("Additional paid-in capital", "3,998,827", "1,792,969"),
                    row("Accumulated deficit", "(1,640,510)", "(1,223,213)"),
                    row("Accumulated other comprehensive income", "15,366", "3,644"),
                    row("Total stockholders' equity", "2,370,831", "570,529"),
                    row("Total liabilities, redeemable convertible preferred stock and stockholders' equity", "$64,153,508", "$45,834,409"),
                ],
            },
            {
                "title": "Condensed Consolidated Statements of Operations",
                "source": "Page 10",
                "unit": "in $ thousands, except per share information",
                "columns": ["Line Item", "Three Months Ended June 30, 2025", "Three Months Ended June 30, 2024", "Six Months Ended June 30, 2025", "Six Months Ended June 30, 2024"],
                "rows": [
                    group("Revenue and reserve income"),
                    row("Reserve income", "$634,274", "$423,263", "$1,192,185", "$782,902"),
                    row("Other revenue", "23,804", "6,767", "44,466", "12,222"),
                    row("Total revenue and reserve income", "658,078", "430,030", "1,236,651", "795,124"),
                    group("Distribution, transaction and other costs"),
                    row("Distribution and transaction costs", "406,472", "246,901", "753,784", "449,643"),
                    row("Other costs", "470", "1,476", "805", "5,471"),
                    row("Total distribution, transaction and other costs", "406,942", "248,377", "754,589", "455,114"),
                    group("Operating expenses"),
                    row("Compensation expenses", "503,392", "67,604", "579,012", "128,753"),
                    row("General and administrative expenses", "43,140", "35,729", "73,824", "66,246"),
                    row("Depreciation and amortization expenses", "14,209", "12,632", "28,089", "24,225"),
                    row("IT infrastructure costs", "8,760", "6,875", "16,432", "13,209"),
                    row("Marketing expenses", "7,910", "5,638", "11,770", "6,456"),
                    row("Digital assets (gains) losses", "(693)", "2,929", "5,577", "(1,444)"),
                    row("Total operating expenses", "576,718", "131,407", "714,704", "237,445"),
                    row("Operating income (loss) from continuing operations", "(325,582)", "50,246", "(232,642)", "102,565"),
                    row("Other (expense) income, net", "(160,421)", "1,921", "(163,524)", "22,478"),
                    row("Net income (loss) from continuing operations before income taxes", "(486,003)", "52,167", "(396,166)", "125,043"),
                    row("Income tax (benefit) expense", "(3,903)", "19,244", "21,143", "43,481"),
                    row("Net income (loss) from continuing operations", "$(482,100)", "$32,923", "$(417,309)", "$81,562"),
                    group("Earnings (loss) per share:"),
                    row("Earnings (loss) per share attributable to common stockholders, basic and diluted", "$(4.48)", "$0.00", "$(5.04)", "$0.00"),
                    group("Weighted-average common shares used to compute earnings per share:"),
                    row("Weighted-average shares used in computing earnings (loss) per share attributable to common stockholders, basic", "107,514", "54,396", "82,877", "54,186"),
                    row("Weighted-average shares used in computing earnings (loss) per share attributable to common stockholders, diluted", "107,514", "70,416", "82,877", "72,976"),
                ],
            },
            {
                "title": "Quarterly Results of Operations",
                "source": "Page 11",
                "unit": "in $ millions, except RLDC Margin and Net Reserve Margin",
                "columns": ["Metric", "June 30, 2025", "March 31, 2025", "December 31, 2024", "September 30, 2024", "June 30, 2024"],
                "rows": [
                    row("Reserve Income", "$634", "$558", "$433", "$445", "$423"),
                    row("Other Revenue", "24", "21", "2", "1", "7"),
                    row("Total Revenue and Reserve Income", "$658", "$579", "$435", "$446", "$430"),
                    row("Distribution and Transaction Costs", "$406", "$347", "$304", "$257", "$247"),
                    row("Other Costs", "0", "0", "1", "0", "1"),
                    row("Total Distribution, Transaction and Other Costs", "$407", "$348", "$305", "$258", "$248"),
                    row("Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs", "$251", "$231", "$131", "$188", "$182"),
                    row("RLDC Margin(1)", "38%", "40%", "30%", "42%", "42%"),
                    row("Net Reserve Margin(2)", "36%", "38%", "30%", "42%", "42%"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted EBITDA to Net Income (Loss) From Continuing Operations",
                "source": "Page 13",
                "unit": "in $ thousands",
                "columns": ["Line Item", "June 30, 2025", "March 31, 2025", "December 31, 2024", "September 30, 2024", "June 30, 2024"],
                "rows": [
                    row("Net income (loss) from continuing operations", "$(482,100)", "$64,791", "$4,433", "$70,996", "$32,923"),
                    group("Adjusted for:"),
                    row("Depreciation and amortization expense", "14,209", "13,880", "13,507", "13,122", "12,632"),
                    row("Interest expense, net of amortization of discounts and premiums", "344", "335", "357", "548", "504"),
                    row("Interest income(1)", "(9,952)", "(7,965)", "(8,646)", "(9,253)", "(8,460)"),
                    row("Income tax (benefit) expense", "(3,903)", "25,046", "5,934", "15,168", "19,244"),
                    row("Stock-based compensation expense", "434,966", "12,716", "11,142", "12,763", "16,749"),
                    row("Legal expenses(2)", "1,706", "1,905", "4,834", "1,813", "956"),
                    row("Realized and unrealized (gains) losses, net, on digital assets held for investment, other related investments and strategic investments", "(5,738)", "8,263", "(4,470)", "(1,955)", "1,324"),
                    row("Realized (gains) losses on available-for-sale debt securities", "-", "-", "(75)", "(9)", "(1)"),
                    row("Impairment losses on strategic investments", "506", "-", "1,580", "623", "155"),
                    row("Restructuring expenses(3)", "-", "-", "-", "646", "1,780"),
                    row("Acquisition-related costs(4)", "-", "535", "1,054", "-", "-"),
                    row("Change in fair value of convertible debt, warrant liability, and embedded derivatives", "167,724", "2,382", "4,225", "(12,369)", "4,586"),
                    row("Losses on sale of long-lived assets", "4", "12", "7", "9", "10"),
                    row("Foreign currency exchange (gains) losses", "8,067", "539", "(1,157)", "1,183", "201"),
                    row("Adjusted EBITDA", "$125,833", "$122,439", "$32,725", "$93,285", "$82,603"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 14",
                "unit": "in $ thousands",
                "columns": ["Line Item", "June 30, 2025", "March 31, 2025", "December 31, 2024", "September 30, 2024", "June 30, 2024"],
                "rows": [
                    row("Operating expenses", "$576,718", "$137,986", "$130,026", "$124,260", "$131,407"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(434,966)", "(12,716)", "(11,142)", "(12,763)", "(16,749)"),
                    row("Depreciation and amortization expense(2)", "(14,209)", "(13,880)", "(13,507)", "(13,122)", "(12,632)"),
                    row("Digital asset (gains) losses(3)", "693", "(6,270)", "4,093", "(1,285)", "(2,929)"),
                    row("Adjusted Operating Expenses", "$128,236", "$105,120", "$109,470", "$97,090", "$99,097"),
                ],
            },
            {
                "title": "Forward Outlook Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 14",
                "unit": "in $ millions",
                "columns": ["Line Item", "FY 2025 Low", "FY 2025 High"],
                "rows": [
                    row("Operating expenses", "$1,150", "$1,190"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(556)", "(571)"),
                    row("Depreciation and amortization expense(2)", "(70)", "(80)"),
                    row("Digital asset (gains) losses(3)", "(6)", "(6)"),
                    row("DAF contribution(4)", "(43)", "(43)"),
                    row("Adjusted Operating Expenses", "$475", "$490"),
                ],
            },
        ],
    },
    {
        "id": "q3-2025",
        "title": "Q3 2025 Earnings Release",
        "pdf": "Circle-Q3-2025-Earnings-Release.pdf",
        "period": "Third quarter 2025",
        "date": "November 12, 2025",
        "summary": "USDC 流通和平台内留存继续加速, 税收收益与公允价值收益推动 GAAP 净利润明显改善。",
        "sections": [
            {
                "title": "Key Financial Results and Operating Indicators",
                "source": "Page 2",
                "unit": "$ in millions unless noted otherwise; USDC figures in $ billions; meaningful wallets in millions",
                "columns": ["Metric", "Q3 2025", "YoY Change"],
                "rows": [
                    group("Key Financial Results"),
                    row("Total Revenue and Reserve Income", "$740", "66%"),
                    row("Revenue Less Distribution Costs(1)", "$292", "55%"),
                    row("RLDC Margin(2)", "39%", "(270bps)"),
                    row("Net Income from Continuing Operations", "$214", "202%"),
                    row("Net Income from Continuing Operations Margin(3)", "29%", "NM"),
                    row("Adjusted EBITDA(4)", "$166", "78%"),
                    row("Adjusted EBITDA Margin(4)", "57%", "737bps"),
                    group("Key Operating Indicators"),
                    row("USDC in Circulation, end of period", "$73.7", "108%"),
                    row("Average USDC in Circulation", "$67.8", "97%"),
                    row("Reserve Return Rate", "4.2%", "(96bps)"),
                    row("USDC on Platform, end of period", "$10.2", "1,277%"),
                    row("Daily Weighted-Average Percentage of USDC on Platform", "13.5%", "1,172bps"),
                    row("USDC Minted", "$79.7", "128%"),
                    row("USDC Redeemed", "$67.3", "112%"),
                    row("Stablecoin Market Share, end of period(5)", "29%", "643bps"),
                    row("Meaningful Wallets, end of period(6)", "6.3", "77%"),
                ],
            },
            {
                "title": "Forward Outlook",
                "source": "Page 4",
                "unit": "Company outlook",
                "columns": ["Key Indicator", "Period", "Prior Outlook", "Updated Outlook"],
                "rows": [
                    row("USDC in Circulation", "Multi-year through cycle", "40% CAGR", "No change"),
                    row("Other Revenue", "FY 2025", "$75-$85M", "$90-$100M"),
                    row("RLDC Margin(1)", "FY 2025", "36-38%", "~38%"),
                    row("Adjusted Operating Expenses(2)", "FY 2025", "$475-$490M", "$495-$510M"),
                ],
            },
            {
                "title": "Condensed Consolidated Balance Sheets",
                "source": "Pages 7-8",
                "unit": "in $ thousands, except share information",
                "columns": ["Line Item", "September 30, 2025 (unaudited)", "December 31, 2024"],
                "rows": [
                    group("ASSETS"),
                    group("Current assets:"),
                    row("Cash and cash equivalents", "$1,348,901", "$750,981"),
                    row("Cash and cash equivalents segregated for corporate-held stablecoins", "837,143", "294,493"),
                    row("Cash and cash equivalents segregated for the benefit of stablecoin holders", "73,372,843", "43,918,572"),
                    row("Accounts receivable, net", "22,154", "6,418"),
                    row("Stablecoins receivable, net", "1,000", "6,957"),
                    row("Prepaid expenses and other current assets", "321,343", "187,528"),
                    row("Total current assets", "75,903,384", "45,164,949"),
                    group("Non-current assets:"),
                    row("Restricted cash", "3,222", "3,558"),
                    row("Investments", "81,781", "84,114"),
                    row("Fixed assets, net", "23,486", "18,682"),
                    row("Digital assets", "51,550", "31,330"),
                    row("Goodwill", "266,384", "169,544"),
                    row("Intangible assets, net", "411,990", "331,394"),
                    row("Deferred tax assets, net", "13,414", "10,223"),
                    row("Other non-current assets", "25,797", "20,615"),
                    row("Total assets", "$76,781,008", "$45,834,409"),
                    group("LIABILITIES, REDEEMABLE CONVERTIBLE PREFERRED STOCK AND STOCKHOLDERS' EQUITY"),
                    group("Current liabilities:"),
                    row("Deposits from stablecoin holders", "$73,267,103", "$43,727,363"),
                    row("Accounts payable and accrued expenses", "268,955", "287,007"),
                    row("Convertible debt, net of debt discount", "149,094", "-"),
                    row("Other current liabilities", "16,604", "16,597"),
                    row("Total current liabilities", "73,701,756", "44,030,967"),
                    group("Non-current liabilities:"),
                    row("Convertible debt, net of debt discount", "-", "40,717"),
                    row("Deferred tax liabilities, net", "31,345", "29,559"),
                    row("Warrant liability", "-", "1,591"),
                    row("Other non-current liabilities", "24,551", "21,281"),
                    row("Total non-current liabilities", "55,896", "93,148"),
                    row("Total liabilities", "$73,757,652", "$44,124,115"),
                    group("Commitments and contingencies"),
                    row("Redeemable convertible preferred stock", "-", "1,139,765"),
                    group("Stockholders' equity"),
                    row("Class A common stock", "23", "6"),
                    row("Class B common stock", "2", "-"),
                    row("Class C common stock", "-", "-"),
                    row("Treasury stock at cost", "(2,877)", "(2,877)"),
                    row("Additional paid-in capital", "4,437,594", "1,792,969"),
                    row("Accumulated deficit", "(1,426,125)", "(1,223,213)"),
                    row("Accumulated other comprehensive income", "14,739", "3,644"),
                    row("Total stockholders' equity", "3,023,356", "570,529"),
                    row("Total liabilities, redeemable convertible preferred stock and stockholders' equity", "$76,781,008", "$45,834,409"),
                ],
            },
            {
                "title": "Condensed Consolidated Statements of Operations",
                "source": "Page 9",
                "unit": "in $ thousands, except per share information",
                "columns": ["Line Item", "Three Months Ended September 30, 2025", "Three Months Ended September 30, 2024", "Nine Months Ended September 30, 2025", "Nine Months Ended September 30, 2024"],
                "rows": [
                    group("Revenue and reserve income"),
                    row("Reserve income", "$711,241", "$445,215", "$1,903,426", "$1,228,117"),
                    row("Other revenue", "28,518", "547", "72,984", "12,769"),
                    row("Total revenue and reserve income", "739,759", "445,762", "1,976,410", "1,240,886"),
                    group("Distribution, transaction and other costs"),
                    row("Distribution and transaction costs", "447,199", "257,422", "1,200,983", "707,065"),
                    row("Other costs", "413", "281", "1,218", "5,752"),
                    row("Total distribution, transaction and other costs", "447,612", "257,703", "1,202,201", "712,817"),
                    group("Operating expenses"),
                    row("Compensation expenses", "129,295", "65,269", "708,307", "194,022"),
                    row("General and administrative expenses", "45,477", "33,337", "119,301", "99,583"),
                    row("Depreciation and amortization expenses", "23,002", "13,122", "51,091", "37,347"),
                    row("IT infrastructure costs", "9,401", "6,865", "25,833", "20,074"),
                    row("Marketing expenses", "5,623", "4,382", "17,393", "10,838"),
                    row("Digital assets (gains) losses", "(1,671)", "1,285", "3,906", "(159)"),
                    row("Total operating expenses", "211,127", "124,260", "925,831", "361,705"),
                    row("Operating income (loss) from continuing operations", "81,020", "63,799", "(151,622)", "166,364"),
                    row("Other (expense) income, net", "72,071", "22,365", "(91,453)", "44,843"),
                    row("Net income (loss) from continuing operations before income taxes", "153,091", "86,164", "(243,075)", "211,207"),
                    row("Income tax expense (benefit)", "(61,294)", "15,168", "(40,151)", "58,649"),
                    row("Net income (loss) from continuing operations", "$214,385", "$70,996", "$(202,924)", "$152,558"),
                    group("Earnings (loss) per share:"),
                    row("Basic", "$0.93", "$0.00", "$(1.53)", "$0.32"),
                    row("Diluted", "$0.64", "$0.00", "$(1.53)", "$0.25"),
                    group("Weighted-average shares used in computing earnings (loss) per share:"),
                    row("Basic", "229,895", "54,553", "132,422", "54,309"),
                    row("Diluted", "266,682", "73,125", "132,422", "73,026"),
                ],
            },
            {
                "title": "Quarterly Results of Operations",
                "source": "Page 10",
                "unit": "in $ millions, except RLDC Margin and Net Reserve Margin",
                "columns": ["Metric", "September 30, 2025", "June 30, 2025", "March 31, 2025", "December 31, 2024", "September 30, 2024"],
                "rows": [
                    row("Reserve Income", "$711", "$634", "$558", "$433", "$445"),
                    row("Other Revenue", "29", "24", "21", "2", "1"),
                    row("Total Revenue and Reserve Income", "$740", "$658", "$579", "$435", "$446"),
                    row("Distribution and Transaction Costs", "$447", "$406", "$347", "$304", "$257"),
                    row("Other Costs", "0", "0", "0", "1", "0"),
                    row("Total Distribution, Transaction and Other Costs", "$448", "$407", "$348", "$305", "$258"),
                    row("Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs", "$292", "$251", "$231", "$131", "$188"),
                    row("RLDC Margin(1)", "39%", "38%", "40%", "30%", "42%"),
                    row("Net Reserve Margin(2)", "37%", "36%", "38%", "30%", "42%"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted EBITDA to Net Income (Loss) From Continuing Operations",
                "source": "Page 12",
                "unit": "in $ thousands",
                "columns": ["Line Item", "September 30, 2025", "June 30, 2025", "March 31, 2025", "December 31, 2024", "September 30, 2024"],
                "rows": [
                    row("Net income (loss) from continuing operations", "$214,385", "$(482,100)", "$64,791", "$4,433", "$70,996"),
                    group("Adjusted for:"),
                    row("Depreciation and amortization expense", "23,002", "14,209", "13,880", "13,507", "13,122"),
                    row("Interest expense, net of amortization of discounts and premiums", "354", "344", "335", "357", "548"),
                    row("Interest income(1)", "(13,453)", "(9,952)", "(7,965)", "(8,646)", "(9,253)"),
                    row("Income tax expense (benefit)", "(61,294)", "(3,903)", "25,046", "5,934", "15,168"),
                    row("Stock-based compensation expense", "59,081", "434,966", "12,716", "11,142", "12,763"),
                    row("Legal expenses(2)", "3,014", "1,706", "1,905", "4,834", "1,813"),
                    row("Realized and unrealized (gains) losses, net, on digital assets held for investment, other related investments and strategic investments", "(2,267)", "(5,738)", "8,263", "(4,470)", "(1,955)"),
                    row("Realized (gains) losses on available-for-sale debt securities", "-", "-", "-", "(75)", "(9)"),
                    row("Impairment losses on strategic investments", "500", "506", "-", "1,580", "623"),
                    row("Restructuring expenses(3)", "-", "-", "-", "-", "646"),
                    row("Acquisition-related costs(4)", "-", "-", "535", "1,054", "-"),
                    row("Change in fair value of convertible debt, warrant liability, and embedded derivatives", "(56,212)", "167,724", "2,382", "4,225", "(12,369)"),
                    row("Losses on sale of long-lived assets", "6", "4", "12", "7", "9"),
                    row("Foreign currency exchange (gain) loss", "(655)", "8,067", "539", "(1,157)", "1,183"),
                    row("Adjusted EBITDA", "$166,461", "$125,833", "$122,439", "$32,725", "$93,285"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 13",
                "unit": "in $ thousands",
                "columns": ["Line Item", "September 30, 2025", "June 30, 2025", "March 31, 2025", "December 31, 2024", "September 30, 2024"],
                "rows": [
                    row("Operating expenses", "$211,127", "$576,718", "$137,986", "$130,026", "$124,260"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(59,081)", "(434,966)", "(12,716)", "(11,142)", "(12,763)"),
                    row("Depreciation and amortization expense(2)", "(23,002)", "(14,209)", "(13,880)", "(13,507)", "(13,122)"),
                    row("Digital asset (gains) losses(3)", "1,671", "693", "(6,270)", "4,093", "(1,285)"),
                    row("Adjusted Operating Expenses", "$130,715", "$128,236", "$105,120", "$109,470", "$97,090"),
                ],
            },
            {
                "title": "Forward Outlook Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 13",
                "unit": "in $ millions",
                "columns": ["Line Item", "FY 2025 Low", "FY 2025 High"],
                "rows": [
                    row("Operating expenses", "$1,153", "$1,193"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(556)", "(571)"),
                    row("Depreciation and amortization expense(2)", "(70)", "(80)"),
                    row("Digital asset (gains) losses(3)", "(4)", "(4)"),
                    row("DAF contribution(4)", "(28)", "(28)"),
                    row("Adjusted Operating Expenses", "$495", "$510"),
                ],
            },
        ],
    },
    {
        "id": "q4-2025",
        "title": "Q4 & FY 2025 Earnings Release",
        "pdf": "Circle-Q4-2025-Earnings-Release.pdf",
        "period": "Fourth quarter and full year 2025",
        "date": "February 25, 2026",
        "summary": "Q4 收入达到四个季度高点, FY2025 Adjusted EBITDA 同比翻倍; FY2026 guidance 改用新的 Adjusted Operating Expenses 口径。",
        "sections": [
            {
                "title": "Key Financial Results",
                "source": "Page 2",
                "unit": "$ in millions unless noted otherwise",
                "columns": ["Metric", "Q4 2025", "Q4 YoY Change", "FY 2025", "FY YoY Change"],
                "rows": [
                    row("Total Revenue and Reserve Income", "$770", "77%", "$2,747", "64%"),
                    row("Revenue Less Distribution Costs(1)", "$309", "136%", "$1,083", "64%"),
                    row("RLDC Margin(2)", "40%", "1,004bps", "39%", "12bps"),
                    row("Net Income (loss) from Continuing Operations", "$133", "NM", "($70)", "NM"),
                    row("Net Income (loss) from Continuing Operations Margin(3)", "17%", "NM", "(3%)", "NM"),
                    row("Adjusted EBITDA(4)", "$167", "412%", "$582", "104%"),
                    row("Adjusted EBITDA Margin(4)", "54%", "NM", "54%", "NM"),
                ],
            },
            {
                "title": "Key Operating Indicators",
                "source": "Pages 3-4",
                "unit": "$ in billions unless noted otherwise; meaningful wallets in millions",
                "columns": ["Metric", "Q4 2025", "Q4 YoY Change", "FY 2025", "FY YoY Change"],
                "rows": [
                    row("USDC in Circulation, end of period", "$75.3", "72%", "$75.3", "72%"),
                    row("USDC in Circulation, average of period", "$76.2", "100%", "$64.9", "95%"),
                    row("Reserve Return Rate", "3.8%", "(68bps)", "4.1%", "(90bps)"),
                    row("USDC on Platform, end of period", "$12.5", "459%", "$12.5", "459%"),
                    row("USDC on Platform, daily weighted average percentage", "17.8%", "1,529bps", "11.1%", "899bps"),
                    row("USDC Minted", "$82.4", "107%", "$257.5", "82%"),
                    row("USDC Redeemed", "$80.9", "157%", "$226.1", "85%"),
                    row("Stablecoin Market Share, end of period(1)", "28%", "426bps", "28%", "426bps"),
                    row("Meaningful Wallets, end of period(2)", "6.8", "59%", "6.8", "59%"),
                ],
            },
            {
                "title": "Guidance",
                "source": "Page 5",
                "unit": "Company guidance",
                "columns": ["Key Indicator", "Period", "Guidance"],
                "rows": [
                    row("USDC in Circulation", "Multi-year through cycle", "40% CAGR"),
                    row("Other Revenue", "FY 2026", "$150-$170M"),
                    row("RLDC Margin(1)", "FY 2026", "38-40%"),
                    row("Adjusted Operating Expenses(2)", "FY 2026", "$570-$585M"),
                ],
            },
            {
                "title": "Consolidated Balance Sheets",
                "source": "Pages 8-9",
                "unit": "in $ thousands, except share information",
                "columns": ["Line Item", "December 31, 2025", "December 31, 2024"],
                "rows": [
                    group("ASSETS"),
                    group("Current assets:"),
                    row("Cash and cash equivalents", "$1,526,046", "$750,981"),
                    row("Cash and cash equivalents segregated for corporate-held stablecoins", "822,963", "294,493"),
                    row("Cash and cash equivalents segregated for the benefit of stablecoin holders", "75,067,932", "43,918,572"),
                    row("Accounts receivable, net", "62,866", "6,418"),
                    row("Stablecoins receivable, net", "-", "6,957"),
                    row("Prepaid expenses and other current assets", "321,660", "187,528"),
                    row("Total current assets", "77,801,467", "45,164,949"),
                    group("Non-current assets:"),
                    row("Restricted cash", "2,792", "3,558"),
                    row("Investments", "84,265", "84,114"),
                    row("Fixed assets, net", "22,791", "18,682"),
                    row("Digital assets", "86,515", "31,330"),
                    row("Goodwill", "265,742", "169,544"),
                    row("Intangible assets, net", "411,146", "331,394"),
                    row("Deferred tax assets, net", "11,110", "10,223"),
                    row("Other non-current assets", "27,379", "20,615"),
                    row("Total assets", "$78,713,207", "$45,834,409"),
                    group("LIABILITIES, REDEEMABLE CONVERTIBLE PREFERRED STOCK AND STOCKHOLDERS' EQUITY"),
                    group("Current liabilities:"),
                    row("Deposits from stablecoin holders", "$74,912,567", "$43,727,363"),
                    row("Accounts payable and accrued expenses", "360,609", "287,007"),
                    row("Convertible debt, net of debt discount", "36,821", "-"),
                    row("Other current liabilities", "18,398", "16,597"),
                    row("Total current liabilities", "75,328,395", "44,030,967"),
                    group("Non-current liabilities:"),
                    row("Convertible debt, net of debt discount", "-", "40,717"),
                    row("Deferred tax liabilities, net", "28,702", "29,559"),
                    row("Warrant liability", "-", "1,591"),
                    row("Other non-current liabilities", "25,337", "21,281"),
                    row("Total non-current liabilities", "54,039", "93,148"),
                    row("Total liabilities", "$75,382,434", "$44,124,115"),
                    group("Commitments and contingencies"),
                    row("Redeemable convertible preferred stock", "-", "1,139,765"),
                    group("Stockholders' equity"),
                    row("Class A common stock", "24", "6"),
                    row("Class B common stock", "2", "-"),
                    row("Class C common stock", "-", "-"),
                    row("Treasury stock at cost", "(2,721)", "(2,877)"),
                    row("Additional paid-in capital", "4,610,216", "1,792,969"),
                    row("Accumulated deficit", "(1,292,709)", "(1,223,213)"),
                    row("Accumulated other comprehensive income", "14,515", "3,644"),
                    row("Total stockholders' equity attributable to common stockholders", "3,329,327", "570,529"),
                    row("Noncontrolling interests", "1,446", "-"),
                    row("Total stockholders' equity", "3,330,773", "570,529"),
                    row("Total liabilities, redeemable convertible preferred stock and stockholders' equity", "$78,713,207", "$45,834,409"),
                ],
            },
            {
                "title": "Consolidated Statements of Operations",
                "source": "Pages 10-11",
                "unit": "in $ thousands, except per share information",
                "columns": ["Line Item", "Three Months Ended December 31, 2025", "Three Months Ended December 31, 2024", "Year Ended December 31, 2025", "Year Ended December 31, 2024"],
                "rows": [
                    group("Revenue and reserve income"),
                    row("Reserve income", "$733,396", "$432,967", "$2,636,822", "$1,661,084"),
                    row("Other revenue", "36,836", "2,400", "109,820", "15,169"),
                    row("Total revenue and reserve income", "770,232", "435,367", "2,746,642", "1,676,253"),
                    group("Distribution, transaction and other costs"),
                    row("Distribution and transaction costs", "460,566", "303,746", "1,661,549", "1,010,811"),
                    row("Other costs", "884", "801", "2,102", "6,553"),
                    row("Total distribution, transaction and other costs", "461,450", "304,547", "1,663,651", "1,017,364"),
                    group("Operating expenses"),
                    row("Compensation expenses", "136,571", "69,388", "844,878", "263,410"),
                    row("General and administrative expenses", "70,971", "37,700", "190,272", "137,283"),
                    row("Depreciation and amortization expenses", "25,536", "13,507", "76,627", "50,854"),
                    row("IT infrastructure costs", "10,805", "7,036", "36,638", "27,109"),
                    row("Marketing expenses", "8,325", "6,488", "25,718", "17,326"),
                    row("Digital assets losses (gains)", "1,387", "(4,093)", "5,293", "(4,251)"),
                    row("Total operating expenses", "253,595", "130,026", "1,179,426", "491,731"),
                    row("Operating income (loss) from continuing operations", "55,187", "794", "(96,435)", "167,158"),
                    row("Other income (expense), net", "84,995", "9,573", "(6,458)", "54,416"),
                    row("Net income (loss) from continuing operations before income taxes", "140,182", "10,367", "(102,893)", "221,574"),
                    row("Income tax expense (benefit)", "6,776", "5,934", "(33,375)", "64,583"),
                    row("Net income (loss) from continuing operations", "133,406", "4,433", "(69,518)", "156,991"),
                    row("Loss from operations of discontinued businesses", "-", "(1,324)", "-", "(1,324)"),
                    row("Net income (loss)", "133,406", "3,109", "(69,518)", "155,667"),
                    row("Less: Net loss attributable to noncontrolling interests", "(10)", "-", "(10)", "-"),
                    row("Net income (loss) attributable to common stockholders", "$133,416", "$3,109", "$(69,508)", "$155,667"),
                    group("Basic earnings (loss) per common share attributable to common stockholders:"),
                    row("Continuing operations", "$0.56", "$0.00", "$(0.44)", "$0.33"),
                    row("Discontinued operations", "-", "$(0.00)", "-", "$(0.00)"),
                    row("Basic earnings (loss) per common share attributable to common stockholders", "$0.56", "$0.00", "$(0.44)", "$0.33"),
                    group("Diluted earnings (loss) per common share attributable to common stockholders:"),
                    row("Continuing operations", "$0.43", "$0.00", "$(0.44)", "$0.30"),
                    row("Discontinued operations", "-", "$(0.00)", "-", "$(0.00)"),
                    row("Diluted earnings (loss) per common share attributable to common stockholders", "$0.43", "$0.00", "$(0.44)", "$0.30"),
                    group("Weighted-average shares used in computing earnings (loss) per share attributable to common stockholders:"),
                    row("Basic", "236,676", "54,722", "158,699", "54,413"),
                    row("Diluted", "267,804", "70,869", "158,699", "73,042"),
                ],
            },
            {
                "title": "Quarterly Results of Operations",
                "source": "Page 12",
                "unit": "in $ millions, except RLDC Margin and Net Reserve Margin",
                "columns": ["Metric", "December 31, 2025", "September 30, 2025", "June 30, 2025", "March 31, 2025", "December 31, 2024"],
                "rows": [
                    row("Reserve Income", "$733", "$711", "$634", "$558", "$433"),
                    row("Other Revenue", "37", "29", "24", "21", "2"),
                    row("Total Revenue and Reserve Income", "$770", "$740", "$658", "$579", "$435"),
                    row("Distribution and Transaction Costs", "$461", "$447", "$406", "$347", "$304"),
                    row("Other Costs", "1", "0", "0", "0", "1"),
                    row("Total Distribution, Transaction and Other Costs", "$461", "$448", "$407", "$348", "$305"),
                    row("Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs", "$309", "$292", "$251", "$231", "$131"),
                    row("RLDC Margin(1)", "40%", "39%", "38%", "40%", "30%"),
                    row("Net Reserve Margin(2)", "37%", "37%", "36%", "38%", "30%"),
                ],
            },
            {
                "title": "Annual Results of Operations",
                "source": "Page 12",
                "unit": "in $ millions, except RLDC Margin and Net Reserve Margin",
                "columns": ["Metric", "Year Ended December 31, 2025", "Year Ended December 31, 2024"],
                "rows": [
                    row("Reserve Income", "$2,637", "$1,661"),
                    row("Other Revenue", "110", "15"),
                    row("Total Revenue and Reserve Income", "$2,747", "$1,676"),
                    row("Distribution and Transaction Costs", "$1,662", "$1,011"),
                    row("Other Costs", "2", "7"),
                    row("Total Distribution, Transaction and Other Costs", "$1,664", "$1,017"),
                    row("Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs", "$1,083", "$659"),
                    row("RLDC Margin(1)", "39%", "39%"),
                    row("Net Reserve Margin(2)", "37%", "39%"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted EBITDA to Net Income (Loss) From Continuing Operations - Quarterly",
                "source": "Page 14",
                "unit": "in $ thousands",
                "columns": ["Line Item", "December 31, 2025", "September 30, 2025", "June 30, 2025", "March 31, 2025", "December 31, 2024"],
                "rows": [
                    row("Net income (loss) from continuing operations", "$133,406", "$214,385", "$(482,100)", "$64,791", "$4,433"),
                    row("Less: Net loss attributable to noncontrolling interests", "(10)", "-", "-", "-", "-"),
                    row("Net income (loss) from continuing operations attributable to common stockholders", "$133,416", "$214,385", "$(482,100)", "$64,791", "$4,433"),
                    group("Adjusted for:"),
                    row("Depreciation and amortization expenses", "25,536", "23,002", "14,209", "13,880", "13,507"),
                    row("Interest expense, net of amortization of discounts and premiums", "193", "354", "344", "335", "357"),
                    row("Interest income(1)", "(16,302)", "(13,453)", "(9,952)", "(7,965)", "(8,646)"),
                    row("Income tax expense (benefit)", "6,776", "(61,294)", "(3,903)", "25,046", "5,934"),
                    row("Stock-based compensation expense", "59,414", "59,081", "434,966", "12,716", "11,142"),
                    row("Legal expenses(2)", "2,875", "3,014", "1,706", "1,905", "4,834"),
                    row("Realized and unrealized (gains) losses, net, on digital assets held for investment, other related investments and strategic investments", "(25,074)", "(2,267)", "(5,738)", "8,263", "(4,470)"),
                    row("Realized (gains) on available-for-sale debt securities", "-", "-", "-", "-", "(75)"),
                    row("Impairment losses on strategic investments", "-", "500", "506", "-", "1,580"),
                    row("Acquisition-related costs(3)", "-", "-", "-", "535", "1,054"),
                    row("Change in fair value of convertible debt, warrant liability, and embedded derivatives", "(42,472)", "(56,212)", "167,724", "2,382", "4,225"),
                    row("Charitable contributions to Circle Foundation(4)", "23,149", "-", "-", "-", "-"),
                    row("Losses on sale of long-lived assets", "-", "6", "4", "12", "7"),
                    row("Foreign currency exchange (gain) loss", "(29)", "(655)", "8,067", "539", "(1,157)"),
                    row("Adjusted EBITDA", "$167,482", "$166,461", "$125,833", "$122,439", "$32,725"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted EBITDA to Net Income (Loss) From Continuing Operations - Annual",
                "source": "Page 15",
                "unit": "in $ thousands",
                "columns": ["Line Item", "Year Ended December 31, 2025", "Year Ended December 31, 2024"],
                "rows": [
                    row("Net income (loss) from continuing operations", "$(69,518)", "$156,991"),
                    row("Less: Net loss attributable to noncontrolling interests", "(10)", "-"),
                    row("Net income (loss) from continuing operations attributable to common stockholders", "$(69,508)", "$156,991"),
                    group("Adjusted for:"),
                    row("Depreciation and amortization expenses", "76,627", "50,854"),
                    row("Interest expense, net of amortization of discounts and premiums", "1,226", "1,906"),
                    row("Interest income(1)", "(47,672)", "(34,712)"),
                    row("Income tax expense (benefit)", "(33,375)", "64,583"),
                    row("Stock-based compensation expense", "566,177", "50,134"),
                    row("Legal expenses(2)", "9,500", "9,281"),
                    row("Realized and unrealized (gains) losses, net, on digital assets held for investment, other related investments and strategic investments", "(24,816)", "(9,464)"),
                    row("Realized (gains) on available-for-sale debt securities", "-", "(88)"),
                    row("Impairment losses on strategic investments", "1,006", "2,358"),
                    row("Restructuring expenses(3)", "-", "3,186"),
                    row("Acquisition-related costs(4)", "535", "1,054"),
                    row("Change in fair value of convertible debt, warrant liability, and embedded derivatives", "71,422", "(11,653)"),
                    row("Charitable contributions to Circle Foundation(5)", "23,149", "-"),
                    row("Losses on sale of long-lived assets", "22", "73"),
                    row("Foreign currency exchange loss", "7,922", "368"),
                    row("Adjusted EBITDA", "$582,215", "$284,871"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted Operating Expenses to Operating Expenses - Quarterly",
                "source": "Page 16",
                "unit": "in $ thousands",
                "columns": ["Line Item", "December 31, 2025", "September 30, 2025", "June 30, 2025", "March 31, 2025", "December 31, 2024"],
                "rows": [
                    row("Operating expenses", "$253,595", "$211,127", "$576,718", "$137,986", "$130,026"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(59,414)", "(59,081)", "(434,966)", "(12,716)", "(11,142)"),
                    row("Depreciation and amortization expenses(2)", "(25,536)", "(23,002)", "(14,209)", "(13,880)", "(13,507)"),
                    row("Digital assets losses (gains)(3)", "(1,387)", "1,671", "693", "(6,270)", "4,093"),
                    row("Charitable contributions to Circle Foundation(4)", "(23,149)", "-", "-", "-", "-"),
                    row("Adjusted Operating Expenses (prior definition)", "$144,109", "$130,715", "$128,236", "$105,120", "$109,470"),
                    group("Adjusted for:"),
                    row("Payroll tax expense related to stock-based compensation(5)", "(8,428)", "(5,015)", "(7,164)", "-", "-"),
                    row("Legal expenses(6)", "(2,875)", "(3,014)", "(1,706)", "(1,905)", "(4,834)"),
                    row("Acquisition-related costs(7)", "-", "-", "-", "(535)", "(1,054)"),
                    row("Adjusted Operating Expenses (new definition)", "$132,806", "$122,686", "$119,366", "$102,680", "$103,582"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted Operating Expenses to Operating Expenses - Annual",
                "source": "Page 17",
                "unit": "in $ thousands",
                "columns": ["Line Item", "Year Ended December 31, 2025", "Year Ended December 31, 2024"],
                "rows": [
                    row("Operating expenses", "$1,179,426", "$491,731"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(566,177)", "(50,134)"),
                    row("Depreciation and amortization expenses(2)", "(76,627)", "(50,854)"),
                    row("Digital assets losses (gains)(3)", "(5,293)", "4,251"),
                    row("Charitable contributions to Circle Foundation(4)", "(23,149)", "-"),
                    row("Adjusted Operating Expenses (prior definition)", "$508,180", "$394,994"),
                    group("Adjusted for:"),
                    row("Payroll tax expense related to stock-based compensation(5)", "(20,607)", "-"),
                    row("Legal expenses(6)", "(9,500)", "(9,281)"),
                    row("Acquisition-related costs(7)", "(535)", "(1,054)"),
                    row("Restructuring expenses(8)", "-", "(3,186)"),
                    row("Adjusted Operating Expenses (new definition)", "$477,538", "$381,473"),
                ],
            },
            {
                "title": "Forward Outlook Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 18",
                "unit": "in $ millions",
                "columns": ["Line Item", "FY26 Low", "FY26 High"],
                "rows": [
                    row("Operating expenses", "$929", "$994"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(219)", "(249)"),
                    row("Depreciation and amortization expenses(2)", "(108)", "(118)"),
                    row("Digital assets losses (gains)(3)", "-", "-"),
                    row("Charitable contributions to Circle Foundation(4)", "(17)", "(17)"),
                    row("Legal expenses(5)", "(7)", "(17)"),
                    row("Acquisition-related costs(6)", "(8)", "(8)"),
                    row("Adjusted Operating Expenses (new definition)", "$570", "$585"),
                ],
            },
        ],
    },
    {
        "id": "q1-2026",
        "title": "Q1 2026 Earnings Release",
        "pdf": "Circle-Q1-2026-Earnings-Release.pdf",
        "period": "First quarter 2026",
        "date": "May 11, 2026",
        "summary": "Q1 收入环比从 Q4 高点回落但同比增长, RLDC margin 提升至 41%; 新定义 Adjusted EBITDA 为 1.514 亿美元。",
        "sections": [
            {
                "title": "Key Financial Results",
                "source": "Page 2",
                "unit": "$ in millions unless noted otherwise",
                "columns": ["Metric", "Q1 2026", "YoY Change"],
                "rows": [
                    row("Total Revenue and Reserve Income", "$694", "20%"),
                    row("Revenue Less Distribution Costs(1)", "$287", "24%"),
                    row("RLDC Margin(2)", "41%", "148bps"),
                    row("Net Income from Continuing Operations", "$55", "(15%)"),
                    row("Net Income from Continuing Operations Margin(3)", "8%", "(324bps)"),
                    row("Adjusted EBITDA(4)", "$151", "24%"),
                    row("Adjusted EBITDA Margin(4)", "53%", "(33bps)"),
                ],
            },
            {
                "title": "Key Operating Indicators and Other Platform Metrics",
                "source": "Pages 2-3",
                "unit": "$ in billions unless noted otherwise; meaningful wallets in millions",
                "columns": ["Metric", "Q1 2026", "YoY Change"],
                "rows": [
                    row("USDC in Circulation, end of period", "$77.0", "28%"),
                    row("USDC in Circulation, average of period", "$75.2", "39%"),
                    row("Reserve Return Rate", "3.5%", "(66bps)"),
                    row("USDC on Platform, end of period", "$13.7", "254%"),
                    row("USDC on Platform, daily weighted average percentage", "17.2%", "1,149bps"),
                    row("USDC Minted", "$73", "38%"),
                    row("USDC Redeemed", "$72", "93%"),
                    row("Stablecoin Market Share, end of period(1)", "28%", "(62bps)"),
                    row("Meaningful Wallets, end of period(2)", "7.2", "47%"),
                ],
            },
            {
                "title": "Guidance",
                "source": "Page 4",
                "unit": "Company outlook",
                "columns": ["Key Indicator", "Period", "Current Outlook"],
                "rows": [
                    row("USDC in Circulation", "Multi-year through cycle", "40% CAGR"),
                    row("Other Revenue", "FY 2026", "$150-$170M"),
                    row("RLDC Margin(1)", "FY 2026", "38-40%"),
                    row("Adjusted Operating Expenses(2)", "FY 2026", "$570-$585M"),
                ],
            },
            {
                "title": "Condensed Consolidated Balance Sheets",
                "source": "Pages 7-8",
                "unit": "in $ thousands, except share information",
                "columns": ["Line Item", "March 31, 2026 (unaudited)", "December 31, 2025"],
                "rows": [
                    group("ASSETS"),
                    group("Current assets:"),
                    row("Cash and cash equivalents", "$1,517,264", "$1,526,046"),
                    row("Cash and cash equivalents segregated for corporate-held stablecoins", "792,662", "822,963"),
                    row("Cash and cash equivalents segregated for the benefit of stablecoin holders", "76,893,681", "75,067,932"),
                    row("Accounts receivable, net", "72,168", "62,866"),
                    row("Prepaid expenses and other current assets", "326,800", "321,660"),
                    row("Total current assets", "79,602,575", "77,801,467"),
                    group("Non-current assets:"),
                    row("Restricted cash", "2,800", "2,792"),
                    row("Investments", "100,073", "84,265"),
                    row("Fixed assets, net", "22,520", "22,791"),
                    row("Digital assets", "84,217", "86,515"),
                    row("Goodwill", "265,742", "265,742"),
                    row("Intangible assets, net", "421,017", "411,146"),
                    row("Deferred tax assets, net", "11,285", "11,110"),
                    row("Other non-current assets", "26,549", "27,379"),
                    row("Total assets", "$80,536,778", "$78,713,207"),
                    group("LIABILITIES AND STOCKHOLDERS' EQUITY"),
                    group("Current liabilities:"),
                    row("Deposits from stablecoin holders", "$76,778,530", "$74,912,567"),
                    row("Accounts payable and accrued expenses", "262,215", "360,609"),
                    row("Convertible debt, net of debt discount", "-", "36,821"),
                    row("Other current liabilities", "14,637", "18,398"),
                    row("Total current liabilities", "77,055,382", "75,328,395"),
                    group("Non-current liabilities:"),
                    row("Deferred tax liabilities, net", "28,071", "28,702"),
                    row("Other non-current liabilities", "24,694", "25,337"),
                    row("Total non-current liabilities", "52,765", "54,039"),
                    row("Total liabilities", "$77,108,147", "$75,382,434"),
                    group("Stockholders' equity"),
                    row("Class A common stock", "25", "24"),
                    row("Class B common stock", "2", "2"),
                    row("Class C common stock", "-", "-"),
                    row("Treasury stock at cost", "(2,683)", "(2,721)"),
                    row("Additional paid-in capital", "4,658,949", "4,610,216"),
                    row("Accumulated deficit", "(1,237,456)", "(1,292,709)"),
                    row("Accumulated other comprehensive income", "8,367", "14,515"),
                    row("Total stockholders' equity attributable to common stockholders", "3,427,204", "3,329,327"),
                    row("Noncontrolling Interest", "1,427", "1,446"),
                    row("Total stockholders' equity", "3,428,631", "3,330,773"),
                    row("Total liabilities and stockholders' equity", "$80,536,778", "$78,713,207"),
                ],
            },
            {
                "title": "Condensed Consolidated Statements of Operations",
                "source": "Page 8",
                "unit": "in $ thousands, except per share information",
                "columns": ["Line Item", "Three Months Ended March 31, 2026", "Three Months Ended March 31, 2025"],
                "rows": [
                    group("Revenue and reserve income"),
                    row("Reserve income", "$652,508", "$557,911"),
                    row("Other revenue", "41,625", "20,662"),
                    row("Total revenue and reserve income", "694,133", "578,573"),
                    group("Distribution, transaction and other costs"),
                    row("Distribution and transaction costs", "405,402", "347,312"),
                    row("Other costs", "1,379", "335"),
                    row("Total distribution, transaction and other costs", "406,781", "347,647"),
                    group("Operating expenses"),
                    row("Compensation expenses", "138,127", "75,620"),
                    row("General and administrative expenses", "57,261", "30,684"),
                    row("Depreciation and amortization expenses", "26,767", "13,880"),
                    row("IT infrastructure costs", "12,722", "7,672"),
                    row("Marketing expenses", "6,617", "3,860"),
                    row("Digital assets losses (gains)", "856", "6,270"),
                    row("Total operating expenses", "242,350", "137,986"),
                    row("Operating income from continuing operations", "45,002", "92,940"),
                    row("Other income (expense), net", "11,683", "(3,103)"),
                    row("Net income from continuing operations before income taxes", "56,685", "89,837"),
                    row("Income tax expense (benefit)", "1,439", "25,046"),
                    row("Net income from continuing operations", "55,246", "64,791"),
                    row("Less: Net loss attributable to noncontrolling interests", "(7)", "-"),
                    row("Net income attributable to common stockholders", "$55,253", "$64,791"),
                    group("Earnings per share attributable to common stockholders:"),
                    row("Basic", "$0.23", "$-"),
                    row("Diluted", "$0.21", "$-"),
                    group("Weighted-average shares used to compute earnings per share attributable to common stockholders:"),
                    row("Basic", "244,038", "57,966"),
                    row("Diluted", "266,687", "75,650"),
                ],
            },
            {
                "title": "Quarterly Results of Operations",
                "source": "Page 9",
                "unit": "in $ millions, except RLDC Margin and Net Reserve Margin",
                "columns": ["Metric", "March 31, 2026", "December 31, 2025", "September 30, 2025", "June 30, 2025", "March 31, 2025"],
                "rows": [
                    row("Reserve Income", "$653", "$733", "$711", "$634", "$558"),
                    row("Other Revenue", "42", "37", "29", "24", "21"),
                    row("Total Revenue and Reserve Income", "$694", "$770", "$740", "$658", "$579"),
                    row("Distribution and Transaction Costs", "$405", "$461", "$447", "$406", "$347"),
                    row("Other Costs", "1", "1", "0", "0", "0"),
                    row("Total Distribution, Transaction and Other Costs", "$407", "$461", "$448", "$407", "$348"),
                    row("Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs", "$287", "$309", "$292", "$251", "$231"),
                    row("RLDC Margin(1)", "41%", "40%", "39%", "38%", "40%"),
                    row("Net Reserve Margin(2)", "38%", "37%", "37%", "36%", "38%"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted EBITDA to Net Income (Loss) From Continuing Operations",
                "source": "Page 11",
                "unit": "in $ thousands",
                "columns": ["Line Item", "March 31, 2026", "December 31, 2025", "September 30, 2025", "June 30, 2025", "March 31, 2025"],
                "rows": [
                    row("Net income (loss) from continuing operations", "$55,246", "$133,406", "$214,385", "$(482,100)", "$64,791"),
                    row("Less: Net loss attributable to noncontrolling interests", "(7)", "(10)", "-", "-", "-"),
                    row("Net income (loss) from continuing operations attributable to common stockholders", "$55,253", "$133,416", "$214,385", "$(482,100)", "$64,791"),
                    group("Adjusted for:"),
                    row("Depreciation and amortization expenses", "26,767", "25,536", "23,002", "14,209", "13,880"),
                    row("Interest expense, net of amortization of discounts and premiums", "38", "193", "354", "344", "335"),
                    row("Interest income(1)", "(13,709)", "(16,302)", "(13,453)", "(9,952)", "(7,965)"),
                    row("Income tax expense (benefit)", "1,439", "6,776", "(61,294)", "(3,903)", "25,046"),
                    row("Stock-based compensation expense", "51,836", "59,414", "59,081", "434,966", "12,716"),
                    row("Legal expenses(2)", "7,019", "2,875", "3,014", "1,706", "1,905"),
                    row("Realized and unrealized losses (gains), net, on digital assets held for investment, other related investments and strategic investments", "3,325", "(25,074)", "(2,267)", "(5,738)", "8,263"),
                    row("Impairment losses on strategic investments", "251", "-", "500", "506", "-"),
                    row("Acquisition-related costs(3)", "1,870", "-", "-", "-", "535"),
                    row("Change in fair value of convertible debt, warrant liability, embedded derivatives, and U.S. Treasury securities", "4,108", "(42,472)", "(56,212)", "167,724", "2,382"),
                    row("Charitable contributions to Circle Foundation(4)", "7,737", "23,149", "-", "-", "-"),
                    row("Losses on sale of long-lived assets", "-", "-", "6", "4", "12"),
                    row("Foreign currency exchange (gains) losses", "(5,121)", "(29)", "(655)", "8,067", "539"),
                    row("Adjusted EBITDA (Prior Definition)", "$140,813", "$167,482", "$166,461", "$125,833", "$122,439"),
                    row("Stock-based compensation related payroll expense(5)", "10,588", "8,428", "5,015", "7,164", "-"),
                    row("Adjusted EBITDA (New Definition)", "$151,401", "$175,910", "$171,476", "$132,997", "$122,439"),
                ],
            },
            {
                "title": "Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 12",
                "unit": "in $ thousands",
                "columns": ["Line Item", "March 31, 2026", "December 31, 2025", "September 30, 2025", "June 30, 2025", "March 31, 2025"],
                "rows": [
                    row("Operating expenses", "$242,350", "$253,595", "$211,127", "$576,718", "$137,986"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense and related payroll taxes(1)", "(62,424)", "(67,842)", "(64,096)", "(442,130)", "(12,716)"),
                    row("Depreciation and amortization expenses(2)", "(26,767)", "(25,536)", "(23,002)", "(14,209)", "(13,880)"),
                    row("Digital assets losses (gains)(3)", "(856)", "(1,387)", "1,671", "693", "(6,270)"),
                    row("Charitable contributions to Circle Foundation(4)", "(7,737)", "(23,149)", "-", "-", "-"),
                    row("Legal expenses(5)", "(7,019)", "(2,875)", "(3,014)", "(1,706)", "(1,905)"),
                    row("Acquisition-related costs(6)", "(1,870)", "-", "-", "-", "(535)"),
                    row("Adjusted Operating Expenses", "$135,677", "$132,806", "$122,686", "$119,366", "$102,680"),
                ],
            },
            {
                "title": "Forward Outlook Reconciliation of Adjusted Operating Expenses to Operating Expenses",
                "source": "Page 12",
                "unit": "in $ millions",
                "columns": ["Line Item", "FY26 Low", "FY26 High"],
                "rows": [
                    row("Operating expenses", "$950", "$1,025"),
                    group("Adjusted for:"),
                    row("Stock-based compensation expense(1)", "(219)", "(249)"),
                    row("Depreciation and amortization expenses(2)", "(108)", "(118)"),
                    row("Digital assets losses (gains)(3)", "-", "-"),
                    row("Charitable contributions to Circle Foundation(4)", "(32)", "(32)"),
                    row("Legal expenses(5)", "(13)", "(33)"),
                    row("Acquisition-related costs(6)", "(8)", "(8)"),
                    row("Adjusted Operating Expenses", "$570", "$585"),
                ],
            },
        ],
    },
]


def money_100m_from_thousands(value: int | None) -> str:
    if value is None:
        return "-"
    amount = value / 100_000
    if amount < 0:
        return f"({abs(amount):.3f})"
    return f"{amount:.3f}"


def money_100m_from_millions(value: float | None) -> str:
    if value is None:
        return "-"
    amount = value / 100
    if amount < 0:
        return f"({abs(amount):.3f})"
    return f"{amount:.3f}"


def money_100m_from_billions(value: float | None) -> str:
    if value is None:
        return "-"
    amount = value * 10
    if amount < 0:
        return f"({abs(amount):.3f})"
    return f"{amount:.3f}"


def per_share(value: float | None) -> str:
    if value is None:
        return "-"
    if value < 0:
        return f"({abs(value):.2f}) USD/share"
    return f"{value:.2f} USD/share"


merged_sections = [
    {
        "title": "Merged Key Financial Results",
        "source": "Q1 2026 page 2; Q4 2025 page 2; Q3 2025 page 2; Q2 2025 page 2",
        "unit": "Monetary amounts are in 亿美元, rounded to three decimals",
        "columns": ["Metric", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            group("Key Financial Results"),
            row("Total Revenue and Reserve Income", money_100m_from_thousands(694_133), money_100m_from_thousands(770_232), money_100m_from_thousands(739_759), money_100m_from_thousands(658_078)),
            row("Revenue Less Distribution Costs(1)", money_100m_from_thousands(287_352), money_100m_from_thousands(308_782), money_100m_from_thousands(292_147), money_100m_from_thousands(251_136)),
            row("RLDC Margin(2)", "41%", "40%", "39%", "38%"),
            row("Net Income (Loss) from Continuing Operations", money_100m_from_thousands(55_246), money_100m_from_thousands(133_406), money_100m_from_thousands(214_385), money_100m_from_thousands(-482_100)),
            row("Net Income (loss) from Continuing Operations Margin(3)", "8%", "17%", "29%", "-"),
            row("Adjusted EBITDA (Prior Definition)", money_100m_from_thousands(140_813), money_100m_from_thousands(167_482), money_100m_from_thousands(166_461), money_100m_from_thousands(125_833)),
            row("Adjusted EBITDA (New Definition)", money_100m_from_thousands(151_401), money_100m_from_thousands(175_910), money_100m_from_thousands(171_476), money_100m_from_thousands(132_997)),
            row("Adjusted EBITDA Margin(4)", "53%", "54%", "57%", "50%"),
        ],
    },
    {
        "title": "Merged Key Operating Indicators",
        "source": "Q1 2026 pages 2-3; Q4 2025 pages 3-4; Q3 2025 page 2; Q2 2025 page 2",
        "unit": "USDC monetary amounts are in 亿美元, rounded to three decimals; meaningful wallets are in millions",
        "columns": ["Metric", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            group("Key Operating Indicators"),
            row("USDC in Circulation, end of period", money_100m_from_billions(77.0), money_100m_from_billions(75.3), money_100m_from_billions(73.7), money_100m_from_billions(61.3)),
            row("USDC in Circulation, average of period", money_100m_from_billions(75.2), money_100m_from_billions(76.2), money_100m_from_billions(67.8), money_100m_from_billions(61.0)),
            row("Reserve Return Rate", "3.5%", "3.8%", "4.2%", "4.1%"),
            row("USDC on Platform, end of period", money_100m_from_billions(13.7), money_100m_from_billions(12.5), money_100m_from_billions(10.2), money_100m_from_billions(6.0)),
            row("USDC on Platform, daily weighted average percentage", "17.2%", "17.8%", "13.5%", "7.4%"),
            row("USDC Minted", money_100m_from_billions(73.0), money_100m_from_billions(82.4), money_100m_from_billions(79.7), money_100m_from_billions(42.2)),
            row("USDC Redeemed", money_100m_from_billions(72.0), money_100m_from_billions(80.9), money_100m_from_billions(67.3), money_100m_from_billions(40.8)),
            row("Stablecoin Market Share, end of period(1)", "28%", "28%", "29%", "28%"),
            row("Meaningful Wallets, end of period(2)", "7.2", "6.8", "6.3", "5.7"),
        ],
    },
    {
        "title": "Merged Condensed Consolidated Balance Sheets",
        "source": "Q1 2026 pages 7-8; Q4 2025 pages 8-9; Q3 2025 pages 7-8; Q2 2025 pages 8-9",
        "unit": "Monetary amounts are in 亿美元, rounded to three decimals",
        "columns": ["Line Item", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            group("ASSETS"),
            group("Current assets:"),
            row("Cash and cash equivalents", money_100m_from_thousands(1_517_264), money_100m_from_thousands(1_526_046), money_100m_from_thousands(1_348_901), money_100m_from_thousands(1_118_119)),
            row("Cash and cash equivalents segregated for corporate-held stablecoins", money_100m_from_thousands(792_662), money_100m_from_thousands(822_963), money_100m_from_thousands(837_143), money_100m_from_thousands(588_271)),
            row("Cash and cash equivalents segregated for the benefit of stablecoin holders", money_100m_from_thousands(76_893_681), money_100m_from_thousands(75_067_932), money_100m_from_thousands(73_372_843), money_100m_from_thousands(61_365_920)),
            row("Accounts receivable, net", money_100m_from_thousands(72_168), money_100m_from_thousands(62_866), money_100m_from_thousands(22_154), money_100m_from_thousands(13_215)),
            row("Stablecoins receivable, net", "-", "-", money_100m_from_thousands(1_000), "-"),
            row("Prepaid expenses and other current assets", money_100m_from_thousands(326_800), money_100m_from_thousands(321_660), money_100m_from_thousands(321_343), money_100m_from_thousands(216_604)),
            row("Total current assets", money_100m_from_thousands(79_602_575), money_100m_from_thousands(77_801_467), money_100m_from_thousands(75_903_384), money_100m_from_thousands(63_302_129)),
            group("Non-current assets:"),
            row("Restricted cash", money_100m_from_thousands(2_800), money_100m_from_thousands(2_792), money_100m_from_thousands(3_222), money_100m_from_thousands(3_210)),
            row("Investments", money_100m_from_thousands(100_073), money_100m_from_thousands(84_265), money_100m_from_thousands(81_781), money_100m_from_thousands(83_794)),
            row("Fixed assets, net", money_100m_from_thousands(22_520), money_100m_from_thousands(22_791), money_100m_from_thousands(23_486), money_100m_from_thousands(23_804)),
            row("Digital assets", money_100m_from_thousands(84_217), money_100m_from_thousands(86_515), money_100m_from_thousands(51_550), money_100m_from_thousands(35_113)),
            row("Goodwill", money_100m_from_thousands(265_742), money_100m_from_thousands(265_742), money_100m_from_thousands(266_384), money_100m_from_thousands(266_384)),
            row("Intangible assets, net", money_100m_from_thousands(421_017), money_100m_from_thousands(411_146), money_100m_from_thousands(411_990), money_100m_from_thousands(396_969)),
            row("Deferred tax assets, net", money_100m_from_thousands(11_285), money_100m_from_thousands(11_110), money_100m_from_thousands(13_414), money_100m_from_thousands(17_472)),
            row("Other non-current assets", money_100m_from_thousands(26_549), money_100m_from_thousands(27_379), money_100m_from_thousands(25_797), money_100m_from_thousands(24_633)),
            row("Total assets", money_100m_from_thousands(80_536_778), money_100m_from_thousands(78_713_207), money_100m_from_thousands(76_781_008), money_100m_from_thousands(64_153_508)),
            group("LIABILITIES AND STOCKHOLDERS' EQUITY"),
            group("Current liabilities:"),
            row("Deposits from stablecoin holders", money_100m_from_thousands(76_778_530), money_100m_from_thousands(74_912_567), money_100m_from_thousands(73_267_103), money_100m_from_thousands(61_101_523)),
            row("Accounts payable and accrued expenses", money_100m_from_thousands(262_215), money_100m_from_thousands(360_609), money_100m_from_thousands(268_955), money_100m_from_thousands(411_560)),
            row("Convertible debt, net of debt discount", "-", money_100m_from_thousands(36_821), money_100m_from_thousands(149_094), money_100m_from_thousands(206_140)),
            row("Other current liabilities", money_100m_from_thousands(14_637), money_100m_from_thousands(18_398), money_100m_from_thousands(16_604), money_100m_from_thousands(11_211)),
            row("Total current liabilities", money_100m_from_thousands(77_055_382), money_100m_from_thousands(75_328_395), money_100m_from_thousands(73_701_756), money_100m_from_thousands(61_730_434)),
            group("Non-current liabilities:"),
            row("Deferred tax liabilities, net", money_100m_from_thousands(28_071), money_100m_from_thousands(28_702), money_100m_from_thousands(31_345), money_100m_from_thousands(31_812)),
            row("Other non-current liabilities", money_100m_from_thousands(24_694), money_100m_from_thousands(25_337), money_100m_from_thousands(24_551), money_100m_from_thousands(20_431)),
            row("Total non-current liabilities", money_100m_from_thousands(52_765), money_100m_from_thousands(54_039), money_100m_from_thousands(55_896), money_100m_from_thousands(52_243)),
            row("Total liabilities", money_100m_from_thousands(77_108_147), money_100m_from_thousands(75_382_434), money_100m_from_thousands(73_757_652), money_100m_from_thousands(61_782_677)),
            group("Stockholders' equity"),
            row("Class A common stock", money_100m_from_thousands(25), money_100m_from_thousands(24), money_100m_from_thousands(23), money_100m_from_thousands(23)),
            row("Class B common stock", money_100m_from_thousands(2), money_100m_from_thousands(2), money_100m_from_thousands(2), money_100m_from_thousands(2)),
            row("Class C common stock", "-", "-", "-", "-"),
            row("Treasury stock at cost", money_100m_from_thousands(-2_683), money_100m_from_thousands(-2_721), money_100m_from_thousands(-2_877), money_100m_from_thousands(-2_877)),
            row("Additional paid-in capital", money_100m_from_thousands(4_658_949), money_100m_from_thousands(4_610_216), money_100m_from_thousands(4_437_594), money_100m_from_thousands(3_998_827)),
            row("Accumulated deficit", money_100m_from_thousands(-1_237_456), money_100m_from_thousands(-1_292_709), money_100m_from_thousands(-1_426_125), money_100m_from_thousands(-1_640_510)),
            row("Accumulated other comprehensive income", money_100m_from_thousands(8_367), money_100m_from_thousands(14_515), money_100m_from_thousands(14_739), money_100m_from_thousands(15_366)),
            row("Total stockholders' equity attributable to common stockholders", money_100m_from_thousands(3_427_204), money_100m_from_thousands(3_329_327), money_100m_from_thousands(3_023_356), money_100m_from_thousands(2_370_831)),
            row("Noncontrolling interests", money_100m_from_thousands(1_427), money_100m_from_thousands(1_446), "-", "-"),
            row("Total stockholders' equity", money_100m_from_thousands(3_428_631), money_100m_from_thousands(3_330_773), money_100m_from_thousands(3_023_356), money_100m_from_thousands(2_370_831)),
            row("Total liabilities and stockholders' equity", money_100m_from_thousands(80_536_778), money_100m_from_thousands(78_713_207), money_100m_from_thousands(76_781_008), money_100m_from_thousands(64_153_508)),
        ],
    },
    {
        "title": "Merged Condensed Consolidated Statements of Operations",
        "source": "Q1 2026 page 8; Q4 2025 pages 10-11; Q3 2025 page 9; Q2 2025 page 10",
        "unit": "Monetary amounts are in 亿美元, rounded to three decimals; per-share amounts remain USD/share",
        "columns": ["Line Item", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            group("Revenue and reserve income"),
            row("Reserve income", money_100m_from_thousands(652_508), money_100m_from_thousands(733_396), money_100m_from_thousands(711_241), money_100m_from_thousands(634_274)),
            row("Other revenue", money_100m_from_thousands(41_625), money_100m_from_thousands(36_836), money_100m_from_thousands(28_518), money_100m_from_thousands(23_804)),
            row("Total revenue and reserve income", money_100m_from_thousands(694_133), money_100m_from_thousands(770_232), money_100m_from_thousands(739_759), money_100m_from_thousands(658_078)),
            group("Distribution, transaction and other costs"),
            row("Distribution and transaction costs", money_100m_from_thousands(405_402), money_100m_from_thousands(460_566), money_100m_from_thousands(447_199), money_100m_from_thousands(406_472)),
            row("Other costs", money_100m_from_thousands(1_379), money_100m_from_thousands(884), money_100m_from_thousands(413), money_100m_from_thousands(470)),
            row("Total distribution, transaction and other costs", money_100m_from_thousands(406_781), money_100m_from_thousands(461_450), money_100m_from_thousands(447_612), money_100m_from_thousands(406_942)),
            group("Operating expenses"),
            row("Compensation expenses", money_100m_from_thousands(138_127), money_100m_from_thousands(136_571), money_100m_from_thousands(129_295), money_100m_from_thousands(503_392)),
            row("General and administrative expenses", money_100m_from_thousands(57_261), money_100m_from_thousands(70_971), money_100m_from_thousands(45_477), money_100m_from_thousands(43_140)),
            row("Depreciation and amortization expenses", money_100m_from_thousands(26_767), money_100m_from_thousands(25_536), money_100m_from_thousands(23_002), money_100m_from_thousands(14_209)),
            row("IT infrastructure costs", money_100m_from_thousands(12_722), money_100m_from_thousands(10_805), money_100m_from_thousands(9_401), money_100m_from_thousands(8_760)),
            row("Marketing expenses", money_100m_from_thousands(6_617), money_100m_from_thousands(8_325), money_100m_from_thousands(5_623), money_100m_from_thousands(7_910)),
            row("Digital assets losses (gains)", money_100m_from_thousands(856), money_100m_from_thousands(1_387), money_100m_from_thousands(-1_671), money_100m_from_thousands(-693)),
            row("Total operating expenses", money_100m_from_thousands(242_350), money_100m_from_thousands(253_595), money_100m_from_thousands(211_127), money_100m_from_thousands(576_718)),
            row("Operating income (loss) from continuing operations", money_100m_from_thousands(45_002), money_100m_from_thousands(55_187), money_100m_from_thousands(81_020), money_100m_from_thousands(-325_582)),
            row("Other income (expense), net", money_100m_from_thousands(11_683), money_100m_from_thousands(84_995), money_100m_from_thousands(72_071), money_100m_from_thousands(-160_421)),
            row("Net income (loss) from continuing operations before income taxes", money_100m_from_thousands(56_685), money_100m_from_thousands(140_182), money_100m_from_thousands(153_091), money_100m_from_thousands(-486_003)),
            row("Income tax expense (benefit)", money_100m_from_thousands(1_439), money_100m_from_thousands(6_776), money_100m_from_thousands(-61_294), money_100m_from_thousands(-3_903)),
            row("Net income (loss) from continuing operations", money_100m_from_thousands(55_246), money_100m_from_thousands(133_406), money_100m_from_thousands(214_385), money_100m_from_thousands(-482_100)),
            row("Less: Net loss attributable to noncontrolling interests", money_100m_from_thousands(-7), money_100m_from_thousands(-10), "-", "-"),
            row("Net income (loss) attributable to common stockholders", money_100m_from_thousands(55_253), money_100m_from_thousands(133_416), money_100m_from_thousands(214_385), money_100m_from_thousands(-482_100)),
            group("Earnings (loss) per share attributable to common stockholders:"),
            row("Basic", per_share(0.23), per_share(0.56), per_share(0.93), per_share(-4.48)),
            row("Diluted", per_share(0.21), per_share(0.43), per_share(0.64), per_share(-4.48)),
            group("Weighted-average shares used in computing earnings (loss) per share:"),
            row("Basic", "244,038", "236,676", "229,895", "107,514"),
            row("Diluted", "266,687", "267,804", "266,682", "107,514"),
        ],
    },
    {
        "title": "Merged Quarterly Results of Operations",
        "source": "Q1 2026 page 9; Q4 2025 page 12; Q3 2025 page 10; Q2 2025 page 11",
        "unit": "Monetary amounts are in 亿美元, rounded to three decimals",
        "columns": ["Metric", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            row("Reserve Income", money_100m_from_millions(653), money_100m_from_millions(733), money_100m_from_millions(711), money_100m_from_millions(634)),
            row("Other Revenue", money_100m_from_millions(42), money_100m_from_millions(37), money_100m_from_millions(29), money_100m_from_millions(24)),
            row("Total Revenue and Reserve Income", money_100m_from_millions(694), money_100m_from_millions(770), money_100m_from_millions(740), money_100m_from_millions(658)),
            row("Distribution and Transaction Costs", money_100m_from_millions(405), money_100m_from_millions(461), money_100m_from_millions(447), money_100m_from_millions(406)),
            row("Other Costs", money_100m_from_millions(1), money_100m_from_millions(1), money_100m_from_millions(0), money_100m_from_millions(0)),
            row("Total Distribution, Transaction and Other Costs", money_100m_from_millions(407), money_100m_from_millions(461), money_100m_from_millions(448), money_100m_from_millions(407)),
            row("Total Revenue and Reserve Income less Total Distribution, Transaction and Other Costs", money_100m_from_millions(287), money_100m_from_millions(309), money_100m_from_millions(292), money_100m_from_millions(251)),
            row("RLDC Margin(1)", "41%", "40%", "39%", "38%"),
            row("Net Reserve Margin(2)", "38%", "37%", "37%", "36%"),
        ],
    },
    {
        "title": "Merged Reconciliation of Adjusted EBITDA to Net Income (Loss) From Continuing Operations",
        "source": "Q1 2026 page 11; Q4 2025 page 14; Q3 2025 page 12; Q2 2025 page 13",
        "unit": "Monetary amounts are in 亿美元, rounded to three decimals",
        "columns": ["Line Item", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            row("Net income (loss) from continuing operations", money_100m_from_thousands(55_246), money_100m_from_thousands(133_406), money_100m_from_thousands(214_385), money_100m_from_thousands(-482_100)),
            row("Less: Net loss attributable to noncontrolling interests", money_100m_from_thousands(-7), money_100m_from_thousands(-10), "-", "-"),
            row("Net income (loss) from continuing operations attributable to common stockholders", money_100m_from_thousands(55_253), money_100m_from_thousands(133_416), money_100m_from_thousands(214_385), money_100m_from_thousands(-482_100)),
            group("Adjusted for:"),
            row("Depreciation and amortization expenses", money_100m_from_thousands(26_767), money_100m_from_thousands(25_536), money_100m_from_thousands(23_002), money_100m_from_thousands(14_209)),
            row("Interest expense, net of amortization of discounts and premiums", money_100m_from_thousands(38), money_100m_from_thousands(193), money_100m_from_thousands(354), money_100m_from_thousands(344)),
            row("Interest income(1)", money_100m_from_thousands(-13_709), money_100m_from_thousands(-16_302), money_100m_from_thousands(-13_453), money_100m_from_thousands(-9_952)),
            row("Income tax expense (benefit)", money_100m_from_thousands(1_439), money_100m_from_thousands(6_776), money_100m_from_thousands(-61_294), money_100m_from_thousands(-3_903)),
            row("Stock-based compensation expense", money_100m_from_thousands(51_836), money_100m_from_thousands(59_414), money_100m_from_thousands(59_081), money_100m_from_thousands(434_966)),
            row("Legal expenses(2)", money_100m_from_thousands(7_019), money_100m_from_thousands(2_875), money_100m_from_thousands(3_014), money_100m_from_thousands(1_706)),
            row("Realized and unrealized losses (gains), net, on digital assets held for investment, other related investments and strategic investments", money_100m_from_thousands(3_325), money_100m_from_thousands(-25_074), money_100m_from_thousands(-2_267), money_100m_from_thousands(-5_738)),
            row("Impairment losses on strategic investments", money_100m_from_thousands(251), "-", money_100m_from_thousands(500), money_100m_from_thousands(506)),
            row("Acquisition-related costs(3)", money_100m_from_thousands(1_870), "-", "-", "-"),
            row("Change in fair value of convertible debt, warrant liability, embedded derivatives, and U.S. Treasury securities", money_100m_from_thousands(4_108), money_100m_from_thousands(-42_472), money_100m_from_thousands(-56_212), money_100m_from_thousands(167_724)),
            row("Charitable contributions to Circle Foundation(4)", money_100m_from_thousands(7_737), money_100m_from_thousands(23_149), "-", "-"),
            row("Losses on sale of long-lived assets", "-", "-", money_100m_from_thousands(6), money_100m_from_thousands(4)),
            row("Foreign currency exchange (gains) losses", money_100m_from_thousands(-5_121), money_100m_from_thousands(-29), money_100m_from_thousands(-655), money_100m_from_thousands(8_067)),
            row("Adjusted EBITDA (Prior Definition)", money_100m_from_thousands(140_813), money_100m_from_thousands(167_482), money_100m_from_thousands(166_461), money_100m_from_thousands(125_833)),
            row("Stock-based compensation related payroll expense(5)", money_100m_from_thousands(10_588), money_100m_from_thousands(8_428), money_100m_from_thousands(5_015), money_100m_from_thousands(7_164)),
            row("Adjusted EBITDA (New Definition)", money_100m_from_thousands(151_401), money_100m_from_thousands(175_910), money_100m_from_thousands(171_476), money_100m_from_thousands(132_997)),
        ],
    },
    {
        "title": "Merged Reconciliation of Adjusted Operating Expenses to Operating Expenses",
        "source": "Q1 2026 page 12; Q4 2025 page 16; Q3 2025 page 13; Q2 2025 page 14",
        "unit": "Monetary amounts are in 亿美元, rounded to three decimals; uses the new definition where available",
        "columns": ["Line Item", "2026 Q1", "2025 Q4", "2025 Q3", "2025 Q2"],
        "rows": [
            row("Operating expenses", money_100m_from_thousands(242_350), money_100m_from_thousands(253_595), money_100m_from_thousands(211_127), money_100m_from_thousands(576_718)),
            group("Adjusted for:"),
            row("Stock-based compensation expense and related payroll taxes(1)", money_100m_from_thousands(-62_424), money_100m_from_thousands(-67_842), money_100m_from_thousands(-64_096), money_100m_from_thousands(-442_130)),
            row("Depreciation and amortization expenses(2)", money_100m_from_thousands(-26_767), money_100m_from_thousands(-25_536), money_100m_from_thousands(-23_002), money_100m_from_thousands(-14_209)),
            row("Digital assets losses (gains)(3)", money_100m_from_thousands(-856), money_100m_from_thousands(-1_387), money_100m_from_thousands(1_671), money_100m_from_thousands(693)),
            row("Charitable contributions to Circle Foundation(4)", money_100m_from_thousands(-7_737), money_100m_from_thousands(-23_149), "-", "-"),
            row("Legal expenses(5)", money_100m_from_thousands(-7_019), money_100m_from_thousands(-2_875), money_100m_from_thousands(-3_014), money_100m_from_thousands(-1_706)),
            row("Acquisition-related costs(6)", money_100m_from_thousands(-1_870), "-", "-", "-"),
            row("Adjusted Operating Expenses", money_100m_from_thousands(135_677), money_100m_from_thousands(132_806), money_100m_from_thousands(122_686), money_100m_from_thousands(119_366)),
        ],
    },
]


def render_table(section: dict) -> str:
    columns = section["columns"]
    total_cols = len(columns) + 1
    html = [
        '<div class="table-card">',
        f'<div class="table-meta"><span>{escape(section["source"])}</span><span>{escape(section["unit"])}</span></div>',
        '<div class="table-scroll">',
        '<table>',
        '<thead><tr>',
    ]
    html.append(f"<th>{escape(columns[0])}</th><th>中文解释</th>")
    for col in columns[1:]:
        html.append(f"<th>{escape(col)}</th>")
    html.append("</tr></thead><tbody>")
    for r in section["rows"]:
        label = r[0]
        if len(r) == 1:
            html.append(f'<tr class="group"><td colspan="{total_cols}">{escape(label)} <span>{escape(explain(label))}</span></td></tr>')
            continue
        vals = r[1:]
        html.append("<tr>")
        html.append(f'<td class="metric">{escape(label)}</td>')
        html.append(f'<td class="cn">{escape(explain(label))}</td>')
        for val in vals:
            html.append(f"<td>{escape(val)}</td>")
        html.append("</tr>")
    html.append("</tbody></table></div></div>")
    return "".join(html)


def count_data_rows() -> int:
    total = 0
    for report in reports:
        for section in report["sections"]:
            total += sum(1 for r in section["rows"] if len(r) > 1)
    return total


def count_merged_rows() -> int:
    return sum(sum(1 for r in section["rows"] if len(r) > 1) for section in merged_sections)


def render_html() -> str:
    nav = '<a href="#merged-quarterly">Merged Quarterly Financials</a><a href="#source-pdfs">Source PDFs</a>'
    cards = "".join(
        f'<article><strong>{escape(r["title"])}</strong><span>{escape(r["date"])}</span><p>{escape(r["summary"])}</p>'
        f'<a class="pdf-link card-link" href="{escape(r["pdf"])}">Open PDF</a></article>'
        for r in reports
    )
    merged_html = []
    for i, section in enumerate(merged_sections, 1):
        open_attr = " open" if i <= 2 else ""
        merged_html.append(f'<details class="section"{open_attr}><summary>{escape(section["title"])}</summary>')
        merged_html.append(render_table(section))
        merged_html.append("</details>")
    missing = sorted(
        {
            clean_label(r[0])
            for section in merged_sections
            for r in section["rows"]
            if len(r) > 1 and explain(r[0]).startswith("财报原文项目")
        }
    )
    missing_html = ""
    if missing:
        items = "".join(f"<li>{escape(x)}</li>" for x in missing)
        missing_html = f'<details class="section"><summary>Rows using generic Chinese explanation</summary><ul>{items}</ul></details>'
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Circle Earnings Financial Data Extraction</title>
  <style>
    :root {{
      --ink: #18212f;
      --muted: #617086;
      --line: #d9e1ec;
      --bg: #f7f9fc;
      --panel: #ffffff;
      --accent: #155eef;
      --accent-soft: #e8f0ff;
      --green: #0f766e;
      --amber: #a15c07;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background: var(--bg);
      font: 14px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", Arial, sans-serif;
    }}
    header {{
      background: #0b1220;
      color: #fff;
      padding: 32px 28px 24px;
    }}
    .wrap {{ max-width: 1280px; margin: 0 auto; }}
    h1 {{ margin: 0 0 10px; font-size: 30px; letter-spacing: 0; }}
    h2 {{ margin: 0; font-size: 24px; letter-spacing: 0; }}
    h3 {{ margin: 0; }}
    p {{ margin: 0; }}
    .sub {{ max-width: 980px; color: #c7d2e5; }}
    .meta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }}
    .pill {{
      border: 1px solid rgba(255,255,255,.24);
      border-radius: 999px;
      padding: 6px 10px;
      color: #edf3ff;
      background: rgba(255,255,255,.08);
    }}
    nav {{
      position: sticky;
      top: 0;
      z-index: 5;
      background: rgba(255,255,255,.96);
      border-bottom: 1px solid var(--line);
      backdrop-filter: blur(10px);
    }}
    nav .wrap {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 10px 28px;
    }}
    nav a {{
      flex: 0 0 auto;
      color: var(--accent);
      text-decoration: none;
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 6px;
      padding: 7px 10px;
      font-weight: 600;
    }}
    main {{ padding: 24px 28px 48px; }}
    .cards {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-bottom: 20px;
    }}
    article {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      min-height: 132px;
    }}
    article strong {{ display: block; margin-bottom: 4px; }}
    article span {{ color: var(--muted); font-size: 12px; }}
    article p {{ margin-top: 10px; color: #334155; }}
    .analysis {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      margin-bottom: 20px;
    }}
    .analysis ul {{ margin: 10px 0 0; padding-left: 20px; }}
    .analysis li {{ margin: 6px 0; }}
    .report {{
      margin-top: 28px;
      border-top: 3px solid #0b1220;
      padding-top: 18px;
    }}
    .report-head {{
      display: flex;
      justify-content: space-between;
      gap: 18px;
      align-items: flex-start;
      margin-bottom: 14px;
    }}
    .report-head p {{ color: var(--green); font-weight: 700; text-transform: uppercase; font-size: 12px; letter-spacing: .04em; }}
    .report-head span {{ color: var(--muted); }}
    .pdf-link {{
      color: #fff;
      background: var(--accent);
      text-decoration: none;
      padding: 8px 12px;
      border-radius: 6px;
      white-space: nowrap;
      font-weight: 700;
    }}
    .card-link {{
      display: inline-block;
      margin-top: 12px;
      padding: 7px 10px;
      font-size: 12px;
    }}
    details.section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      margin: 12px 0;
      overflow: hidden;
    }}
    summary {{
      cursor: pointer;
      padding: 13px 16px;
      font-weight: 800;
      background: #f0f4fa;
      color: #18212f;
    }}
    .table-card {{ padding: 14px 16px 16px; }}
    .table-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
      color: var(--muted);
      font-size: 12px;
    }}
    .table-meta span {{
      background: #f6f8fb;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 4px 7px;
    }}
    .table-scroll {{
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    table {{
      width: 100%;
      min-width: 820px;
      border-collapse: collapse;
      background: #fff;
    }}
    th, td {{
      padding: 9px 10px;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
      text-align: right;
      white-space: nowrap;
    }}
    th:first-child, td:first-child {{ text-align: left; min-width: 280px; white-space: normal; }}
    th:nth-child(2), td:nth-child(2) {{ text-align: left; min-width: 260px; white-space: normal; }}
    thead th {{
      position: sticky;
      top: 45px;
      z-index: 1;
      background: #10213f;
      color: #fff;
      font-size: 12px;
    }}
    tbody tr:nth-child(even):not(.group) {{ background: #fbfdff; }}
    .metric {{ font-weight: 650; }}
    .cn {{ color: #475569; }}
    tr.group td {{
      background: var(--accent-soft);
      color: #0b3b91;
      font-weight: 800;
      text-align: left;
    }}
    tr.group span {{
      margin-left: 8px;
      color: #45618d;
      font-weight: 500;
    }}
    .notes {{
      color: var(--muted);
      font-size: 12px;
      margin-top: 18px;
      border-top: 1px solid var(--line);
      padding-top: 14px;
    }}
    @media (max-width: 900px) {{
      header {{ padding: 26px 18px 20px; }}
      main {{ padding: 18px; }}
      .cards {{ grid-template-columns: 1fr; }}
      .report-head {{ display: block; }}
      .pdf-link {{ display: inline-block; margin-top: 10px; }}
      h1 {{ font-size: 24px; }}
      thead th {{ top: 0; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>Circle 四份财报关键财务数据提取</h1>
      <p class="sub">覆盖 Q2 2025、Q3 2025、Q4 & FY 2025、Q1 2026 四份 earnings release。四个季度已合并为横向对比表, 列顺序从 2026 Q1 到 2025 Q2；聚合金额统一换算为亿美元并保留三位小数。</p>
      <div class="meta-row">
        <span class="pill">Source folder: circle/</span>
        <span class="pill">Reports: 4 PDFs</span>
        <span class="pill">Merged tables: {len(merged_sections)}</span>
        <span class="pill">Merged data rows: {count_merged_rows()}</span>
        <span class="pill">Original extracted rows: {count_data_rows()}</span>
        <span class="pill">Generated HTML: circle_financial_analysis.html</span>
      </div>
    </div>
  </header>
  <nav><div class="wrap">{nav}</div></nav>
  <main class="wrap">
    <section class="analysis">
      <h2>核心分析</h2>
      <ul>
        <li>业务规模继续扩张: 期末 USDC in Circulation 从 2025 Q2 的 613.000 亿美元增至 2026 Q1 的 770.000 亿美元, USDC on Platform 从 60.000 亿美元增至 137.000 亿美元。</li>
        <li>储备收益率走低但规模抵消部分压力: Reserve Return Rate 从 2025 Q3 的 4.2% 降至 2026 Q1 的 3.5%, 但平均流通 USDC 仍保持增长。</li>
        <li>RLDC Margin 持续改善: Q2 2025 为 38%, Q3 为 39%, Q4 为 40%, Q1 2026 达 41%。</li>
        <li>GAAP 净利润波动大: 2025 Q2 因 IPO 后股权激励、公允价值变动等项目出现 4.821 亿美元净亏损, 2025 Q3/Q4 转正, 2026 Q1 为 0.552 亿美元净利润。</li>
        <li>Non-GAAP 口径发生变化: Q4 2025 开始展示 Adjusted Operating Expenses 的 prior/new definition, Q1 2026 Adjusted EBITDA 也披露 prior/new definition, 其中 2026 Q1 新定义 Adjusted EBITDA 为 1.514 亿美元。</li>
      </ul>
    </section>
    <section class="report" id="merged-quarterly">
      <div class="report-head"><div><p>Consolidated quarterly view</p><h2>四季度合并财务数据</h2><span>Column order: 2026 Q1, 2025 Q4, 2025 Q3, 2025 Q2</span></div></div>
      {''.join(merged_html)}
    </section>
    <section class="report" id="source-pdfs">
      <div class="report-head"><div><p>Source files</p><h2>来源 PDF</h2><span>保留原始 PDF 链接用于追溯。</span></div></div>
      <section class="cards">{cards}</section>
    </section>
    {missing_html}
    <section class="notes">
      <p>说明: 本文件基于本地 PDF 文本和表格抽取后人工核对整理。所有企业层面的货币金额均换算为亿美元并保留三位小数；每股收益保留为 USD/share, 因其不是企业总额口径。NM 保留原文含义, 表示 not meaningful。括号表示负数或反向变动, 与原财报披露一致。bps 表示 basis points, 即基点。</p>
    </section>
  </main>
</body>
</html>
"""


if __name__ == "__main__":
    OUT.write_text(render_html(), encoding="utf-8")
    print(OUT)
