# NVIDIA model inputs

GF-NVDA-1 · as of 2026-09-29 · USD in millions except per-share data and percentages. Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified forecast; `not obtained` is never replaced with an unlabeled guess.

## Source map

| source | use |
|---|---|
| [Register R2](../../memory/nvda/register.md#r2--historical-pl-and-segment-economics) | company P&L, reportable segments, current market platforms and management outlook |
| [Register R3](../../memory/nvda/register.md#r3--end-markets-units-asp-and-operating-kpis) | prior market taxonomy through FY2026 only; units/ASP gaps |
| [Register R5](../../memory/nvda/register.md#r5--foundry-packaging-memory-and-capacity) | supply commitments as footnote risk only |
| [Register R6](../../memory/nvda/register.md#r6--balance-sheet-cash-flow-and-shares) | 2026-07-26 balance sheet and 1H FY2027 cash-flow/share seeds |
| [Register R9](../../memory/nvda/register.md#r9--explicit-gaps) | disclosure gaps that constrain the model |

## Historical company P&L seeds

All cells below are `[FACT]` copied from register R2.

| $m except EPS/WAS **[FACT]** | FY2024A | FY2025A | FY2026A | Q2 FY2027A | 1H FY2027A |
|---|---:|---:|---:|---:|---:|
| Revenue | 60,922 | 130,497 | 215,938 | 96,221 | 177,837 |
| Cost of revenue | 16,621 | 32,639 | 62,475 | 24,079 | 44,538 |
| Gross profit | 44,301 | 97,858 | 153,463 | 72,142 | 133,299 |
| R&D | 8,675 | 12,914 | 18,497 | 7,054 | 13,375 |
| SG&A | 2,654 | 3,491 | 4,579 | 1,354 | 2,654 |
| Operating income | 32,972 | 81,453 | 130,387 | 63,734 | 117,270 |
| Net income | 29,760 | 72,880 | 120,067 | 59,688 | 118,010 |
| Diluted EPS ($) | 1.19 | 2.94 | 4.90 | 2.46 | 4.85 |
| Diluted WAS (m) | 24,940 | 24,804 | 24,514 | 24,285 | 24,338 |

## Historical reportable-segment seeds

All cells below are `[FACT]` copied from register R2. Segment operating income is the CODM measure and excludes items reconciled in R2.2.

| $m **[FACT]** | FY2024A | FY2025A | FY2026A | Q2 FY2027A | 1H FY2027A |
|---|---:|---:|---:|---:|---:|
| Compute & Networking revenue | 47,405 | 116,193 | 193,479 | 88,299 | 162,850 |
| Compute & Networking operating income | 32,016 | 82,875 | 130,141 | 62,696 | 116,031 |
| Graphics revenue | 13,517 | 14,304 | 22,459 | 7,922 | 14,987 |
| Graphics operating income | 5,846 | 5,085 | 9,156 | 3,899 | 6,840 |

## Current market-platform seeds

All cells below are `[FACT]` copied from register R2. Hyperscale and ACIE sum to Data Center; Data Center and Edge Computing sum to company revenue.

| revenue, $m **[FACT]** | Q2 FY2026 recast | Q2 FY2027A | 1H FY2026 recast | 1H FY2027A |
|---|---:|---:|---:|---:|
| Data Center | 41,096 | 89,023 | 80,208 | 164,269 |
| Hyperscale | 24,168 | 48,710 | 46,428 | 91,761 |
| ACIE | 16,928 | 40,313 | 33,780 | 72,508 |
| Edge Computing | 5,647 | 7,198 | 10,597 | 13,568 |
| Company revenue | 46,743 | 96,221 | 90,805 | 177,837 |

## Prior market taxonomy — history only

All cells below are `[FACT]` copied from register R3. These lines stop at FY2026 and are not forecast drivers.

| revenue, $m **[FACT]** | FY2024A | FY2025A | FY2026A |
|---|---:|---:|---:|
| Data Center | 47,525 | 115,186 | 193,737 |
| Compute | 38,950 | 102,196 | 162,361 |
| Networking | 8,575 | 12,990 | 31,376 |
| Gaming | 10,447 | 11,350 | 16,042 |
| Professional Visualization | 1,553 | 1,878 | 3,191 |
| Automotive | 1,091 | 1,694 | 2,349 |
| OEM and Other | 306 | 389 | 619 |
| Company revenue | 60,922 | 130,497 | 215,938 |

## Balance-sheet and cash-flow seed

All figures are `[FACT]` from register R6 at 2026-07-26 or for 1H FY2027.

| input **[FACT]** | value |
|---|---:|
| Cash and cash equivalents | 22,443 |
| Marketable debt securities | 34,143 |
| Marketable equity securities | 42,783 |
| Accounts receivable | 63,059 |
| Inventory | 31,575 |
| PP&E, net | 14,285 |
| Other assets (residual to filed total assets) **[DEDUCTED]** | calculated by `compute.py` |
| Total assets | 320,272 |
| Accounts payable | 15,059 |
| Short-term debt | 1,000 |
| Long-term debt | 32,366 |
| Other liabilities (residual to filed total liabilities) **[DEDUCTED]** | calculated by `compute.py` |
| Total liabilities | 91,288 |
| Stockholders' equity | 228,984 |
| Operating cash flow | 74,421 |
| PP&E/intangible purchases | 4,434 |
| Principal payments on PP&E/intangibles | 92 |
| Company-defined free cash flow | 69,895 |
| D&A | 2,124 |
| SBC | 3,954 |
| Share repurchases | 39,044 |
| Dividends paid | 6,290 |

## Researcher-specified forecast

Every forecast cell is `[VIEW]`.

### Revenue and mix

| input | FY2027E | FY2028E | FY2029E | rationale |
|---|---:|---:|---:|---|
| Company revenue | [VIEW] 405,000 | [VIEW] 688,500 | [VIEW] 895,000 | FY2027 includes 1H actual, Q3 guide midpoint and Q4 `[VIEW]`; FY2028 follows preliminary management growth; FY2029 growth slows |
| Data Center share | [VIEW] 92.5% | [VIEW] 93.5% | [VIEW] 93.0% | Edge remains minority |
| Hyperscale share of Data Center | [VIEW] 56.0% | [VIEW] 55.0% | [VIEW] 54.0% | ACIE grows slightly faster |
| Edge Computing | [VIEW] residual | [VIEW] residual | [VIEW] residual | only platform residual; no other revenue plug |

FY2027 company revenue comprises `[FACT]` 1H FY2027 revenue from R2, `[FACT]` management Q3 guide midpoint from R2.4, and the researcher-specified `[VIEW]` Q4 residual. `compute.py` performs the bridge.

### Margin, opex, tax and shares

| input | FY2027E | FY2028E | FY2029E | class / rationale |
|---|---:|---:|---:|---|
| GAAP gross margin | [VIEW] 73.0% | [VIEW] 72.5% | [VIEW] 73.0% | R2.5 frames the trough and settle range |
| R&D | [VIEW] 32,000 | [VIEW] 42,000 | [VIEW] 50,000 | FY2027 consistent with management's opex-growth framing |
| SG&A | [VIEW] 7,200 | [VIEW] 9,000 | [VIEW] 10,500 | researcher-specified |
| Tax rate | [VIEW] 17.0% | [VIEW] 17.0% | [VIEW] 17.0% | within R2.5 outlook |
| Diluted WAS (m) | [VIEW] 24,200 | [VIEW] 23,800 | [VIEW] 23,400 | buybacks continue, but slower |

Because market-platform gross margins are `not obtained` (R9.2/R9.6), the model applies the company gross-margin assumption to each platform. This explicit `[VIEW]` makes platform gross profit additive without inventing a hidden gross-profit plug.

### Segment operating-income reconciliation

| input | treatment | class / basis |
|---|---|---|
| Compute & Networking share of total segment OI | 95%; Graphics residual | [VIEW], rounded near recent CODM mix and satisfies the specified ~95% allocation |
| SBC | 30% of R&D + SG&A | [VIEW], researcher-specified |
| Other unallocated/acquisition costs | 10% of R&D + SG&A | [VIEW], near the non-SBC Q2/1H reconciliation intensity |

`compute.py` calculates the `[DEDUCTED]` 1H FY2027 SBC intensity from R6 and leaves the requested 30% forecast assumption unchanged. Forecast total segment OI equals consolidated operating income plus explicitly shown SBC and other unallocated/acquisition costs; no reconciliation plug is hidden.

### Balance sheet and cash flow

| input | FY2027E | FY2028E | FY2029E | class / policy |
|---|---:|---:|---:|---|
| PP&E/intangible purchases | [VIEW] 12,000 | [VIEW] 15,000 | [VIEW] 18,000 | researcher-specified capex |
| D&A | [VIEW] 5,500 | [VIEW] 7,500 | [VIEW] 10,000 | completion assumption; 1H actual is retained in FY2027 |
| Dividends | [VIEW] 13,000 | [VIEW] 14,000 | [VIEW] 15,000 | modest growth from annualized 1H cash dividends |
| Debt repayment | [VIEW] 1,000 | [VIEW] 10,000 | [VIEW] 22,366 | retire short-term debt in FY2027, then long-term debt without refinancing |
| Minimum cash | [VIEW] 20,000 | [VIEW] 20,000 | [VIEW] 20,000 | buybacks receive residual cash after FCF, dividends and debt repayment |

Additional completion assumptions:

- **[DEDUCTED]/[VIEW] Working capital:** `compute.py` calculates AR days on annualized 1H revenue and inventory/AP days on annualized 1H COGS, then holds those days constant.
- **[VIEW] Securities:** marketable debt securities and marketable equity securities are held separately at the 2026-07-26 balances. Equity securities are not used as operating liquidity.
- **[VIEW] Other balance-sheet lines:** other assets and other liabilities are held at their calculated 2026-07-26 residual balances.
- **[VIEW] PP&E:** ending net PP&E equals opening PP&E plus PP&E/intangible purchases less D&A. FY2027 rolls only the forecast second half from the filed 1H balance.
- **[VIEW] Other income:** zero; forecast pre-tax income equals operating income. No investment mark-to-market is forecast.
- **[VIEW] Other operating/noncash cash-flow items:** zero after 1H FY2027; FY2027 retains filed 1H operating cash flow and forecasts only the second-half bridge.
- **[VIEW] Principal payments on PP&E/intangibles:** zero in forecast because the amount is `not obtained`; forecast FCF is operating cash flow less the specified purchases.
- **[VIEW] Equity roll-forward:** opening equity plus net income and SBC, less dividends and buybacks.
- **[VIEW] Buybacks:** residual cash after the minimum-cash floor and the stated debt-repayment/dividend policy. Forecast buyback dollars do not determine the separately specified diluted WAS.
- **[FACT] Supply commitments:** R5.2 remains a footnote/risk only and is not booked as debt.

## Remaining gaps

- Current Gaming, Professional Visualization, Automotive/Robotics and OEM/Other revenue: `not obtained` (R9.1); no forecast split is fabricated.
- GPU/system/networking units, ASP, HBM content/cost and product gross margin: `not obtained` (R9.2).
- Standalone software/support economics: `not obtained` (R9.3).
- Backlog, utilization and architecture-specific orders: `not obtained` (R9.4).
- Segment gross profit, assets, liabilities and capex: `not obtained` (R9.6).
- Forecast other income, marketable-security marks, other working-capital lines and principal payments on PP&E/intangibles: `not obtained`; explicit `[VIEW]` zero/hold assumptions govern.
