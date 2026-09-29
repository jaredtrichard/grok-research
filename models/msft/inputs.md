# Microsoft model inputs

GF-MSFT-1 · as of 2026-09-29 · USD millions except per-share data and percentages.

Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified base forecast; `not obtained` is never replaced with an unlabeled guess.

## Source map

| source | use |
|---|---|
| [Register R2](../../memory/msft/register.md#r2--segment-economics) | FY2024–FY2026 segment revenue, cost, opex, and operating income |
| [Register R3/R4](../../memory/msft/register.md#r3--product-and-service-revenue) | product revenue and current operating drivers |
| [Register R5](../../memory/msft/register.md#r5--consolidated-income-statement) | consolidated income statement and shares |
| [Register R6](../../memory/msft/register.md#r6--balance-sheet-cash-flow-and-capital-intensity) | FY2025–FY2026 balance sheet; FY2024–FY2026 cash flow; capital intensity |
| [Register R7](../../memory/msft/register.md#r7--managements-fy2027-operating-bar) | FY2027 company and segment guidance |
| [FY2026 10-K income statement](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R2.htm) | FY2024–FY2026 consolidated history |
| [FY2026 10-K balance sheet](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R4.htm) | FY2025–FY2026 balance history |
| [FY2026 10-K cash flow](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R6.htm) | FY2024–FY2026 cash-flow history |
| [FY2026 10-K segment table](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R45.htm) | FY2024–FY2026 segment history |
| [FY2026 Q4 official transcript](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) | FY2027 growth, margin, tax, capex, and product direction |

## Historical inputs

| input | periods | class / treatment |
|---|---|---|
| Segment revenue, cost of revenue, opex, operating income | FY2024–FY2026 | [FACT], register R2 |
| Consolidated income statement | FY2024–FY2026 | [FACT], register R5 |
| Balance sheet | FY2025–FY2026 | [FACT], register R6.1 |
| Cash flow | FY2024–FY2026 | [FACT], register R6.2 |
| Segment gross profit | FY2024–FY2026 | [DEDUCTED], revenue less cost of revenue |
| Filing free cash flow | FY2024–FY2026 | [DEDUCTED], OCF less additions to PP&E |
| Azure/Copilot/product KPIs | latest FY2026 | [FACT], register R4; context only, not added as unreported segments |

## Segment forecast assumptions

| input | FY2027E | FY2028E | FY2029E | class / rationale |
|---|---:|---:|---:|---|
| PBP revenue growth | 13.0% | 14.0% | 13.0% | [VIEW]; Q1 guide 11%–12%, later-year acceleration supported by M365 premium/usage and Copilot |
| IC revenue growth | 30.0% | 24.0% | 20.0% | [VIEW]; Q1 guide 33%–34%, Azure ~45% CC, then normalization from capacity-led acceleration |
| MPC revenue growth | (8.0%) | 1.0% | 3.0% | [VIEW]; FY2027 Windows high-teens headwind and XBOX pressure partly offset by Search |
| PBP gross margin | 81.7% | 82.0% | 82.3% | [VIEW]; Copilot usage pressure followed by product/inference efficiency |
| IC gross margin | 56.0% | 55.0% | 56.0% | [VIEW]; Azure/AI mix and infrastructure ahead of demand, then utilization/efficiency |
| MPC gross margin | 55.0% | 55.5% | 56.0% | [VIEW]; mix and lower acquired-content amortization |
| PBP operating margin | 59.5% | 60.0% | 60.5% | [VIEW]; modest leverage beneath premium-SKU growth |
| IC operating margin | 41.0% | 41.0% | 42.0% | [VIEW]; gross-margin pressure offset by opex leverage, then recovery |
| MPC operating margin | 22.0% | 23.0% | 24.0% | [VIEW]; FY2027 revenue pressure, then mix/expense recovery |

The resulting FY2027 company growth and operating-margin change are script outputs checked against management’s R7.1 full-year bar; they are not separately typed assumptions.

## Consolidated forecast assumptions

| input | FY2027E | FY2028E | FY2029E | class / rationale |
|---|---:|---:|---:|---|
| Other income / (expense), net | (400) | (400) | (400) | [VIEW]; approximates Q1 ex-OpenAI guide annualized without forecasting OpenAI marks |
| Effective tax rate | 20.0% | 20.0% | 20.0% | [VIEW]; management FY2027 guide, held |
| Cash additions to PP&E | 140,000 | 155,000 | 150,000 | [VIEW]; FY2027 grows from filed FY2026 cash capex, then remains elevated |
| D&A rate on average net PP&E | 13.0% | 13.0% | 13.0% | [VIEW]; below FY2026 D&A-and-other / average-PP&E relation after useful-life change |
| SBC / revenue | 3.7% | 3.6% | 3.5% | [VIEW]; near filed FY2026 ratio with gradual moderation |
| Cash dividends | 30,000 | 33,000 | 36,000 | [VIEW]; grows from FY2026 cash dividends |
| Common-stock repurchases | 20,000 | 20,000 | 20,000 | [VIEW]; below FY2026 repurchases |
| Debt repayments | 3,000 | 3,000 | 3,000 | [VIEW]; holds FY2026 cash repayment |

## Working-capital and balance-sheet completion assumptions

The script derives FY2026 receivable, inventory, and payable days and ratios for unearned revenue, other operating assets, and other operating liabilities. Each is held flat through FY2029 as a `[DEDUCTED]` seed and `[VIEW]` forecast.

| item | treatment | class |
|---|---|---|
| Accounts receivable | FY2026 days on revenue | [DEDUCTED]/[VIEW] |
| Inventory | FY2026 days on cost of revenue | [DEDUCTED]/[VIEW] |
| Accounts payable | FY2026 days on cost of revenue | [DEDUCTED]/[VIEW] |
| Unearned revenue | FY2026 percentage of revenue | [DEDUCTED]/[VIEW] |
| Other operating assets | FY2026 percentage of revenue | [DEDUCTED]/[VIEW] |
| Other operating liabilities | FY2026 percentage of revenue | [DEDUCTED]/[VIEW] |
| Short-term investments | hold $55,908 | [VIEW] |
| Equity/other investments | hold $36,348 | [VIEW] |
| Goodwill and intangible assets | hold combined $138,260 | [VIEW] |
| Forecast diluted shares | hold FY2026 7,453 million | [VIEW]; buybacks broadly offset equity compensation |
| Forecast period-end shares | hold 7,427 million | [VIEW] |

“Other operating assets” aggregates other current assets, operating-lease right-of-use assets, and other long-term assets. “Other operating liabilities” aggregates accrued compensation, current/long-term taxes, operating-lease liabilities, deferred taxes, and other current/long-term liabilities. The cash-flow statement includes changes in each aggregate so the forecast balance sheet ties without a balancing plug.

## Valuation assumptions

| input | treatment | class |
|---|---|---|
| Valuation date | 2026-09-29 | [FACT] as-of |
| Last close | $509.22 on 2026-09-28 | [FACT], Microsoft IR stock lookup |
| Price-target denominator | 7,427 million FY2026 period-end shares | [FACT] |
| Method | Enterprise DCF of FY2027–FY2029 unlevered FCF plus terminal value, then add FY2026 net cash | [VIEW] |
| WACC | 8.5% | [VIEW] |
| Terminal growth | 4.0% | [VIEW] |
| FCFF | NOPAT + D&A − cash capex − change in operating capital; SBC is not added back | [VIEW], treats SBC as an economic cost |

The official price target is an output of the operating path and DCF, not a residual fitted to the last close. Sensitivities and the market-implied terminal-growth check are diagnostics, not additional official targets.

## Gaps

- Azure, AI, Microsoft 365 Copilot, and GitHub standalone revenue, gross profit, capex, and free cash flow: `not obtained` (register R9).
- Segment balance sheets, capex, D&A, SBC, working capital, and cash flow: `not obtained`; the model does not fabricate segment allocations.
- Commercial RPO duration/conversion schedule and exact OpenAI concentration: `not obtained`.
- FY2027–FY2029 period-end and diluted share counts: `not obtained`; held assumptions are labeled `[VIEW]`.
