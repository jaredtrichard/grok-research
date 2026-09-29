# Amazon model inputs

As of 2026-09-29. USD millions except per-share data and percentages. Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified base forecast; `not obtained` is never replaced with a guess.

## Source map

| source | use |
|---|---|
| [Register R2](../../memory/amzn/register.md#r2--reportable-segment-history) | segment revenue, operating expense and operating income |
| [Register R3](../../memory/amzn/register.md#r3--sales-groups-and-operating-drivers) | sales-group growth, paid units, AWS usage/RPO context |
| [Register R6](../../memory/amzn/register.md#r6--balance-sheet-shares-and-cash-flow) | balance sheet, cash flow, capex outlook, D&A/SBC |
| [Register R7](../../memory/amzn/register.md#r7--investments-commitments-and-contingencies) | strategic investments and non-operating marks |
| [Amazon FY2025 10-K S1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm) | FY2023–FY2025 consolidated statements |
| [Amazon FY2024 10-K S2](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm) | FY2022–FY2024 comparatives |
| [Amazon Q2 2026 10-Q S3](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm) | 1H 2026 segment and consolidated detail |
| [Amazon Q2 2026 earnings release S4](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm) | 1H 2026 income, balance sheet, TTM cash flow |

## Historical and seed inputs

| input | value / treatment | pointer / source | class | as-of |
|---|---|---|---|---|
| North America / International / AWS revenue | register R2 table | R2 | [FACT] | FY2022–FY2025; Q2/1H/TTM 2026 |
| Segment operating income | register R2 table | R2 | [FACT] | same |
| Segment operating expense | register R2 table; TTM opex | R2 | [FACT]/[DEDUCTED] | same |
| Consolidated operating income | equals sum of segment OI; filing consolidated line | R2; S1/S2/S4 | [FACT] | same |
| Sales groups (Online, 3P, Ads, Subs, etc.) | register R3 | R3 | [FACT] | FY2022–FY2025; Q2/TTM 2026 |
| Paid-unit growth / seller mix | Q2 +17% YoY; 61% third-party units | R3.2 | [FACT] | Q2 2026 |
| Product-line / sales-group operating income | not disclosed | R8.2 | **not obtained** | — |
| Prime members / ARPU / ad margin | not disclosed | R3.7, R8.3, R8.4 | **not obtained** | — |
| AWS workload units / utilization / AI revenue dollars | not disclosed | R8.5 | **not obtained** | — |
| Consolidated interest / tax / NI (annual) | S1/S2 statements of operations | S1 pp. 1055–1063; S2 pp. 1100–1119 | [FACT] | FY2022–FY2025 |
| Consolidated interest / tax / NI (1H 2026) | S4 consolidated statements of operations | S4 | [FACT] | 1H 2026 |
| 1H 2026 other income (Anthropic marks, etc.) | 69,062 | R7.1; S4 | [FACT] | 1H 2026 |
| Balance sheet (FY2023–FY2025, 1H 2026) | named filing lines | S1/S2 balance sheets; S4 | [FACT] | respective dates |
| Cash flow (FY2023–FY2025, 1H 2026, TTM) | register R6 table | R6; S1/S3/S4 | [FACT]/[DEDUCTED] | respective periods |
| 2026 capex outlook | about 200,000; definition ambiguous vs cash-flow capex | R6.5 | [FACT] outlook / [VIEW] mapping | 2026-02-05 |
| Diluted WAS | 10,492 / 10,721 / 10,827 / 10,889 (1H 2026) | S1/S4; R6.4 | [FACT] | respective periods |

## Researcher-specified segment forecast

Segment revenue grows from FY2025 base revenue; segment operating income equals revenue times segment operating margin. No sales-group margin splits are modeled (R8.2).

| input | FY2026E | FY2027E | FY2028E | class / research driver |
|---|---:|---:|---:|---|
| North America revenue growth | 13% | 11% | 10% | [VIEW]; Stores mix, ads/subscriptions, paid units R3/R6 retail |
| North America operating margin | 8.0% | 8.3% | 8.5% | [VIEW]; fulfillment density vs shipping/tech R2.3 |
| International revenue growth | 15% | 13% | 11% | [VIEW]; country mix and export rules R5 |
| International operating margin | 3.6% | 3.9% | 4.2% | [VIEW]; margin convergence not automatic R2.3 |
| AWS revenue growth | 26% | 20% | 16% | [VIEW]; usage + AI capacity monetization R3.3–R3.4 |
| AWS operating margin | 37.0% | 37.5% | 38.0% | [VIEW]; depreciation/power vs custom-chip economics R6.5/R7 |

## Completion assumptions

| input | treatment | class / basis |
|---|---|---|
| Consolidated operating income | sum of segment operating income | [DEDUCTED] from R1.5 segment perimeter |
| Tax rate | FY2025 effective rate from named pre-tax and tax lines | [DEDUCTED] S1 |
| Other income (forecast) | FY2026E holds reported 1H other income; zero further investment marks | [FACT]/[VIEW] R7.1 |
| Strategic equity investments (cash) | FY2026E funds remaining OpenAI commitment after 1H | [FACT]/[VIEW] R7.2 |
| Net cash capex | FY2026E maps R6.5 ~200,000 outlook to net purchases less proceeds; decelerates thereafter | [VIEW] R6.5 |
| Capex proceeds rate | FY2025 proceeds ÷ purchases, held flat | [DEDUCTED] R6 |
| D&A | solved from average PP&E using FY2025–1H2026 implied rate | [DEDUCTED]/[VIEW] |
| SBC | 1H 2026 run rate doubled for FY2026E; low single-digit growth thereafter | [VIEW] R6.6 |
| Working-capital days | 2026-06-30 AR, inventory and AP days on annualized 1H revenue/opex; held flat | [DEDUCTED]/[VIEW] |
| Operating lease assets / lease liabilities | roll with PP&E growth proxy; not segment-allocated | [VIEW]; R8.6 gap |
| Minimum cash | 50,000; sell marketable securities before incremental debt | [VIEW] liquidity |
| Other assets / liabilities / AOCI / treasury | hold at latest applicable base (1H 2026 for roll-forward start) | [VIEW] |
| Diluted WAS (forecast) | 10,950 / 11,000 / 11,050 | [VIEW] |
| Dividends / buybacks | zero | [VIEW] |

## Valuation `[VIEW]` assumptions (gate 3)

Official 12-month PT is computed in [`compute.py`](compute.py) and written to [`valuation.md`](valuation.md).

| input | treatment | class |
|---|---|---|
| Valuation as-of | 2026-09-29 | [FACT] task date |
| Last close | $246.67 on 2026-09-29 | [FACT] [Yahoo Finance historical](https://finance.yahoo.com/quote/AMZN/history/) |
| PT share denominator | 10,786,313,572 shares on 2026-07-22 (10-Q cover) | [FACT] R6.4 |
| Segment OI multiple year | FY2027E segment operating income | [VIEW] |
| Net cash for PT | FY2026E cash + STI − debt − lease liabilities | [DEDUCTED] from model balance |
| AWS EV / segment OI | 17.0× | [VIEW] |
| North America EV / segment OI | 12.0× | [VIEW] |
| International EV / segment OI | 10.0× | [VIEW] |
| Strategic stake fair value in official PT | excluded; balance-sheet FV | **not obtained** |
| R6.5 capex outlook mapping | FY2026E net cash capex 200,000 | [VIEW] see valuation.md |
| Bear / bull sensitivity | 0.85× / 1.15× segment multiples on same OI | [VIEW] check only |
| Bull strategic uplift | 50% of R7.2 named cash deployed | [VIEW] check only |
| Consolidated FCF DCF check | 9.0% WACC; 3.0% terminal growth on FY2028 FCF | [VIEW] check only |

## Gaps

- Sales-group operating income and advertising/subscription standalone margins: **not obtained** (R8.2–R8.4); forecast uses segment operating income only.
- Segment balance sheet, segment cash flow and segment cash capex: **not obtained** (R8.6).
- RPO / backlog conversion schedule: **not obtained** (R8.5); AWS growth is a `[VIEW]` path, not backlog math.
- Post-Q2 sell-side consensus and market-implied segment values: **not obtained** (R8.8).
- Official Q2 2026 earnings-call transcript: **not obtained** (R8.9).
