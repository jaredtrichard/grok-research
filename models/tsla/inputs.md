# Tesla model inputs

As of 2026-08-29. USD millions except per-share data, vehicles, GWh and percentages. Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified base forecast; `not obtained` is never replaced with a guess.

## Source map

| source | use |
|---|---|
| [Register R2/R3](../../memory/tsla/register.md#r2--historical-economics) | segment revenue/gross profit; production, deliveries, storage |
| [Register R5](../../memory/tsla/register.md#r5--balance-sheet-cash-flow-and-obligations) | Q2/1H balance sheet, cash flow, shares, capex outlook |
| [Tesla FY2025 10-K S1](https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm) | FY2023–FY2025 income/cash flow; FY2024–FY2025 balance sheets |
| [Tesla Q2 2026 10-Q S3](https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm) | 1H 2026 income/cash flow; 2026-06-30 balance sheet |
| [Tesla FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm) | FY2023 balance sheet |

## Historical and seed inputs

| input | value / treatment | pointer / source | class | as-of |
|---|---|---|---|---|
| Automotive ex-Services revenue and GP | register table | R2 | [FACT] | FY2023–FY2025; 1H 2026 |
| Services and other revenue and GP | register table; GP deduced from named revenue/cost lines | R2 | [FACT]/[DEDUCTED] | FY2023–FY2025; 1H 2026 |
| Energy revenue and GP | register table | R2 | [FACT] | FY2023–FY2025; 1H 2026 |
| Regulatory-credit revenue | FY2023 1,790; FY2024 2,763; FY2025 1,993; 1H 2026 526; Q2 2026 146 | S1 statements of operations; R2.1/S3 | [FACT] | respective periods |
| Credit cost | not obtained; model treats revenue as GP | S1/S3 | [VIEW] | 2026-08-29 |
| Production / deliveries / storage | register R3; compute script also carries FY2023/FY2024 official-update history | R3; S1/S3 official updates | [FACT] | respective periods |
| FY2025 auto-ex-Services revenue quotient seed | 69,526 revenue; 1,636,129 deliveries | R2/R3 | [DEDUCTED] working quotient, not ASP | FY2025 |
| Q2 2026 quotient cross-check | 20,516 revenue; 480,126 deliveries | R2.1/R3 | [DEDUCTED] working quotient, not ASP | Q2 2026 |
| R&D / SG&A / restructuring / OI / other / tax / NI | named S1/S3 lines | S1 statements pp. 50, 53; S3 pp. 5, 8 | [FACT] | FY2023–FY2025; 1H 2026 |
| Balance-sheet history | named filing lines | FY2023 10-K p. 49; S1 p. 49; S3 p. 4 | [FACT] | FY2023–2026-06-30 |
| Cash-flow history | named filing lines | S1 p. 53; S3 p. 8 | [FACT] | FY2023–FY2025; 1H 2026 |
| Q2 diluted WAS / latest shares outstanding | 3,540 / 3,949,547,394 | R5.3 | [FACT] | Q2 2026 / 2026-07-16 |
| SpaceX investment | hold 3,007; no further mark-to-market | R6.2 | [FACT] balance / [VIEW] hold | 2026-06-30 onward |
| Related-party Energy | disclosure footnote only; no demand uplift | R6 | [FACT] | 2026-06-30 |
| Lease fleet | hold balance-sheet asset at 4,253; operating unit count remains 141,876 | R3.1/R5.7 | [VIEW] hold | 2026-06-30 onward |

## Researcher-specified forecast

| input | FY2026 | FY2027 | FY2028 | class / rationale |
|---|---:|---:|---:|---|
| Deliveries (k) | 1,720 | 1,850 | 2,000 | [VIEW]; pack constraint R3.4 |
| Energy deployments (GWh) | 55 | 70 | 85 | [VIEW] |
| Energy realized revenue ($/kWh) | 240 | 230 | 220 | [VIEW]; ASP pressure R2.5 |
| Services revenue | 16,800 | 19,000 | 21,500 | [VIEW]; aggregate only |
| Regulatory-credit revenue | 500 | 350 | 200 | [VIEW]; standalone declining |
| Automotive ex-credit GM | 16.5% | 17.2% | 17.8% | [VIEW] |
| Energy GM | 22.0% | 23.0% | 24.0% | [VIEW] |
| Services GM | 13.0% | 13.5% | 14.0% | [VIEW] |
| R&D | 9,200 | 10,000 | 10,600 | [VIEW] |
| SG&A | 7,800 | 8,200 | 8,600 | [VIEW] |
| Capex | 26,000 | 22,000 | 18,000 | [VIEW]; FY2026 above R5.8 guide |
| Diluted WAS (m) | 3,620 | 3,700 | 3,780 | [VIEW] |
| Dividend | 0 | 0 | 0 | [VIEW] |
| Buyback | 0 | 0 | 0 | [VIEW] |
| Robotaxi / incremental FSD / Optimus revenue | 0 | 0 | 0 | [VIEW]; R8.3 not obtained |

## Completion assumptions

| input | treatment | class / basis |
|---|---|---|
| Auto revenue per delivery | hold FY2025 total auto-ex-Services working quotient; subtract separately modeled credits to derive vehicles+leasing revenue | [VIEW] / [DEDUCTED] seed |
| SBC | 25% of R&D plus SG&A | [VIEW], near 1H 2026 run-rate |
| D&A | 12% of average PP&E; script solves the PP&E/D&A relation explicitly | [VIEW] |
| Tax rate | FY2025 effective tax rate from named tax/pre-tax lines | [DEDUCTED] from S1 |
| Interest income | 3% of beginning cash plus short-term investments | [VIEW] |
| Interest expense | 4% of beginning debt and finance leases | [VIEW] |
| Core working-capital days | 2026-06-30 AR, inventory and AP days, using annualized 1H revenue/COGS; held flat | [DEDUCTED]/[VIEW] |
| Minimum cash | 5,000; sell short-term investments before issuing incremental debt | [VIEW] liquidity policy |
| Other assets / liabilities / AOCI / NCI | hold at the latest applicable base value | [VIEW] |
| FY2026 other income | include actual 1H SpaceX unrealized gain; zero further mark-to-market and zero other H2 income | [FACT]/[VIEW] |

## Gaps

- Period-end basic shares for FY2026–FY2028: `not obtained`; the model uses the specified diluted WAS only.
- Credit cost: `not obtained`; 100% incremental gross margin is a `[VIEW]`.
- Segment capex, assets, liabilities and cash flow: `not obtained` (R8.5); no allocation is fabricated.
- Robotaxi, incremental FSD and Optimus revenue/cost/unit economics: `not obtained` (R8.3); base revenue is zero.
- Product-level Energy units, realized pricing and cost/MWh: `not obtained` (R8.2); researcher-specified aggregate deployment and revenue assumptions govern.
- Forecast lease additions, depreciation and residual losses: `not obtained`; lease-fleet assets are held at the 2026-06-30 balance.
