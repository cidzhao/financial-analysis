# Project Rules: Financial Data Extraction & Analysis Standard

This document defines the default rules, schemas, and formatting rules for extracting and analyzing quarterly financial data in this workspace. The AI agent will automatically refer to these rules whenever asked to extract or analyze a company's financial results.

---

## 1. Trigger Condition
These rules apply automatically when the user asks to "extract financials", "analyze quarterly results", "update data", or perform financial reviews for any company in the workspace (e.g., google, amazon, meta, nvdia, apple, microsoft, sk_hynix, sea, pdd, etc.).

---

## 2. Source Documents & Location
- Look for source files (PDFs, PPTX slides, HTML earnings releases) under the corresponding company folder in the workspace root (e.g., `sk_hynix/`, `google/`, `microsoft/`).
- If no files are found or the latest quarters are missing, inform the user and request/offer to download them.

---

## 3. Standard Financial Metric Schema
For each company, extract data for the **latest 4 consecutive quarters** (ordered chronologically from left to right, latest quarter first).

The output must cover the following core sections and metrics:

### A. Key Income Statement Data (利润表关键数据)
1. **Revenue** (营业收入)
2. **Cost of Goods Sold** (营业成本) *[if available]*
3. **Gross Profit** (毛利润)
4. **SG&A Expenses** (销售与管理费用) *[note if R&D is included]*
5. **Operating Profit** (营业利润)
6. **Depreciation & Amortization** (折旧与摊销)
7. **EBITDA** (息税折旧摊销前利润) *[calculated as: Operating Profit + Depreciation & Amortization]*
8. **Net Profit** (净利润)

### B. Key Financial Ratios (关键盈利比率)
1. **Gross Margin** (毛利率)
2. **Operating Margin** (营业利润率)
3. **EBITDA Margin** (EBITDA 利润率)
4. **Net Margin** (净利润率)

### C. Balance Sheet & Leverage Ratios (资产负债表与负债比率)
1. **Cash & Cash Equivalents** (现金及现金等价物) *[include short-term financial instruments/investments if marked]*
2. **Interest-bearing Debt** (有息负债总计) *[sum of Short-term borrowings + Current portion of long-term borrowings + Bonds + Long-term borrowings]*
3. **Total Assets** (总资产)
4. **Total Shareholders' Equity** (股东权益总额)
5. **Debt-to-Equity Ratio** (有息负债率) *[Interest-bearing Debt / Shareholders' Equity]*
6. **Net Debt-to-Equity Ratio** (净有息负债率) *[(Interest-bearing Debt - Cash) / Shareholders' Equity]*

### D. Shares & Earnings Per Share (股数与每股收益)
1. **Basic Shares Outstanding** (基本发行股数)
2. **Diluted Shares Outstanding** (稀释发行股数)
3. **Basic EPS** (基本每股收益)
4. **Diluted EPS** (稀释每股收益)

### E. Industry-Specific Key Drivers (行业特定指标) *[Optional / Company Specific]*
- **Semiconductor / Memory (e.g. SK Hynix, Micron):** DRAM & NAND Bit Growth (QoQ), DRAM & NAND ASP (QoQ).
- **Hyperscalers (e.g. Google, Microsoft, Amazon):** Cloud/AWS/Azure revenue segment growth.
- **Ad/Social (e.g. Meta, Alphabet):** Advertising revenue growth, DAU/MAU, Ad impressions.

---

## 4. Currency and Unit Standardization
- **Currency:** By default, convert all values to **USD (美元)**.
- **Unit:** Standardize units to **100 Million USD (亿美元)**, formatted with exactly **two decimal places** (e.g., `359.23`). Basic/Diluted EPS should be in absolute currency terms (e.g., `$39.07`).
- **Foreign Currency Conversion:**
  - For companies reporting in non-USD currencies (e.g. KRW for SK Hynix, RMB for PDD), apply the **average quarterly exchange rate** for income statement items, and the **period-end exchange rate** for balance sheet items.
  - Detail the specific exchange rates used in the footnotes.

---

## 5. Output Format
For any extraction request, the AI must output the following deliverables:

### A. Markdown Table (Default Response)
A structured markdown table with the columns laid out as follows:
```markdown
| Metric (English) | 指标 (中文) | [Latest Q (e.g., 2026 Q1)] | [Q-1 (e.g., 2025 Q4)] | [Q-2] | [Q-3] | 最新 QoQ 增幅/变动 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
```
*Note: For margins and ratios, represent the QoQ/YoY changes in percentage points (e.g., `+10.50 pp` or `-6.69 pp`). For absolute values, use percentage changes (e.g., `+58.52%` or `-14.06%`).*

### B. Footnotes / Notes Section
Always include a footnotes section containing:
1. **Currency rates used** (average and/or ending rates).
2. **Formulas and definitions** (e.g., EBITDA calculation, debt definitions).
3. **Important adjustments or anomalies** (e.g., non-operating items, R&D treatment in SG&A).

### C. CSV File (Save local copy)
Write a copy of the extracted table into the corresponding company's subdirectory as `[company_name]_financial_analysis.csv` matching the schema exactly.
