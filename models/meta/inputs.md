# Meta Platforms model inputs

GF-META-1 · as of 2026-09-29. USD millions except per-share data, people, percentages, and shares. Arithmetic and derived values live only in [`compute.py`](compute.py). Every forecast input is `[VIEW]`; `not obtained` is never silently filled.

## Source map

| source | use |
|---|---|
| [Register R2](../../memory/meta/register.md#r2--segment-economics) | Advertising, FoA Other, RL revenue; FoA and RL operating contribution |
| [Register R3](../../memory/meta/register.md#r3--advertising-users-and-engagement) | impressions, price, DAP, ARPP |
| [Register R4](../../memory/meta/register.md#r4--functional-expenses-sbc-tax-and-people) | functional expenses, SBC, D&A, tax, headcount, expense/capex outlook |
| [Register R5](../../memory/meta/register.md#r5--cash-flow-liquidity-debt-shares-and-capital-return) | cash flow, balance sheet, debt, shares, capital return |
| [Meta FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) | FY2023–FY2025 history |
| [Meta Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm) | 1H2026 and 2026-06-30 history |

## Segment forecast

| input | FY2026E | FY2027E | FY2028E | class / rationale |
|---|---:|---:|---:|---|
| Advertising revenue | [VIEW] 249,000 | [VIEW] 289,000 | [VIEW] 329,500 | AI recommendation/ad tools support impressions and price; growth decelerates |
| FoA Other revenue | [VIEW] 4,200 | [VIEW] 5,500 | [VIEW] 7,200 | paid messaging and subscriptions; no product split invented |
| FoA operating margin | [VIEW] 41.9% | [VIEW] 44.0% | [VIEW] 46.0% | FY2026 infrastructure/legal/severance pressure, then leverage |
| Reality Labs revenue | [VIEW] 2,500 | [VIEW] 3,400 | [VIEW] 4,800 | glasses, Quest, software/content; units and ASP are not obtained |
| Reality Labs operating loss | [VIEW] (19,100) | [VIEW] (20,000) | [VIEW] (18,500) | FY2026 near company frame; no breakeven assumed |

## Functional income-statement forecast

| input | FY2026E | FY2027E | FY2028E | class / rationale |
|---|---:|---:|---:|---|
| Cost of revenue | [VIEW] 49,000 | [VIEW] 55,000 | [VIEW] 61,000 | infrastructure depreciation, delivery costs, RL hardware |
| R&D | [VIEW] 86,000 | [VIEW] 99,000 | [VIEW] 108,000 | AI infrastructure/model and product investment |
| Marketing and sales | [VIEW] 14,000 | [VIEW] 15,000 | [VIEW] 16,000 | controlled growth |
| G&A | [VIEW] computed residual | [VIEW] computed residual | [VIEW] computed residual | makes functional expenses equal combined-segment OI; no segment allocation |
| Interest and other income / (expense) | [VIEW] (2,000) | [VIEW] (2,500) | [VIEW] (2,000) | debt and investment mix |
| Tax rate | [VIEW] 16% | [VIEW] 16% | [VIEW] 17% | normalized; excludes FY2025 enactment distortion |
| Diluted weighted-average shares | [VIEW] 2,565 | [VIEW] 2,565 | [VIEW] 2,565 | stable share base; period-end forecast is not obtained |

## Cash flow and capital

| input | FY2026E | FY2027E | FY2028E | class / rationale |
|---|---:|---:|---:|---|
| D&A | [VIEW] 26,000 | [VIEW] 38,000 | [VIEW] 52,000 | follows infrastructure build |
| SBC | [VIEW] 28,000 | [VIEW] 32,000 | [VIEW] 35,000 | technical compensation remains elevated |
| Property and equipment purchases | [VIEW] 134,000 | [VIEW] 121,000 | [VIEW] 101,000 | FY2026 plus lease principal sits near outlook midpoint; moderates |
| Finance-lease principal | [VIEW] 4,000 | [VIEW] 4,000 | [VIEW] 4,000 | explicit all-in capex completion |
| Ending marketable securities | [VIEW] 50,000 | [VIEW] 45,000 | [VIEW] 60,000 | liquidity absorbs/rebuilds around capex |
| Ending long-term debt | [VIEW] 83,664 | [VIEW] 83,664 | [VIEW] 83,664 | hold Q2 balance; maturities/issuance schedule not modeled |
| Dividends | [VIEW] 5,500 | [VIEW] 5,800 | [VIEW] 6,100 | gradual growth |
| Share repurchases | [VIEW] — | [VIEW] — | [VIEW] 25,000 | preserve liquidity through capex peak |
| Net-share-settlement taxes | [VIEW] 17,000 | [VIEW] 18,000 | [VIEW] 20,000 | cash use associated with equity awards |

## Valuation

| input | treatment | class |
|---|---|---|
| Official method | 19.0× FY2027E combined-segment operating income plus FY2027E net cash | [VIEW] |
| Share denominator | exact Class A plus Class B shares on the Q2 10-Q cover | [FACT] inputs / [DEDUCTED] sum |
| Bear / bull checks | 15.0× / 23.0× FY2027E operating income plus net cash | [VIEW] |
| DCF check | 9.0% WACC; 3.0% terminal growth; FY2026E–FY2028E unlevered FCF | [VIEW] |
| Official PT rounding | nearest $5 after model-derived per-share value | [VIEW] |

## Completion assumptions and gaps

- **[DEDUCTED]/[VIEW]** Forecast AR and AP use FY2025 AR/FoA-revenue and AP/total-expense ratios, held constant.
- **[VIEW]** PP&E equals prior PP&E plus property purchases less D&A.
- **[VIEW]** Operating-lease assets/liabilities, non-marketable investments, goodwill, long-term income taxes, and accrued/other liabilities hold their latest modeled base unless explicitly changed.
- **[VIEW]** “Other assets / balance completion” is an explicit residual; segment assets and capex are **not obtained** and are not fabricated.
- **[FACT]** Absolute ad impressions/price, WhatsApp economics, RL units/ASP/product margin, and segment cash flow are **not obtained**. The model uses only labeled aggregate `[VIEW]`s.
