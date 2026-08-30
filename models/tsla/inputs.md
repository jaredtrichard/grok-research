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

## Platform `[VIEW]` assumptions

These are researcher-specified assumptions, never filing facts. FSD revenue is incremental above the filing-derived Automotive/Services revenue quotient to limit double counting.

### FSD incremental

| input | FY2026 | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | FY2032 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenue | [VIEW] 3,000 | [VIEW] 6,000 | [VIEW] 10,000 | [VIEW] 15,000 | [VIEW] 21,000 | [VIEW] 27,000 | [VIEW] 32,000 |
| EBIT margin | [VIEW] 72% | [VIEW] 72% | [VIEW] 72% | [VIEW] 72% | [VIEW] 72% | [VIEW] 72% | [VIEW] 72% |

FSD UFCF `[VIEW]` equals EBIT × `(1 − FY2025 effective tax rate)` × 90%.

### Robotaxi

| input | FY2026 | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | FY2032 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Average paid fleet (k) | [VIEW] 15 | [VIEW] 80 | [VIEW] 250 | [VIEW] 650 | [VIEW] 1,400 | [VIEW] 2,500 | [VIEW] 3,500 |
| Revenue / vehicle ($k) | [VIEW] 30 | [VIEW] 34 | [VIEW] 38 | [VIEW] 40 | [VIEW] 41 | [VIEW] 42 | [VIEW] 42 |
| EBIT margin | [VIEW] 25% | [VIEW] 40% | [VIEW] 50% | [VIEW] 50% | [VIEW] 48% | [VIEW] 45% | [VIEW] 43% |

Robotaxi revenue `[VIEW]` equals average fleet (k) × revenue/vehicle ($k). Fleet-growth capex `[VIEW]` is $22k per incremental average-fleet unit versus the prior year. UFCF `[VIEW]` equals after-tax EBIT less fleet-growth capex. The path requires `[VIEW]` multi-plant Cybercab capacity and Model Y network reallocations; the script compares implied additions with the single disclosed Texas `>125k` line. R3.2 is installed capacity, not current output.

### Optimus

| input | FY2026 | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | FY2032 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Units (k) | [VIEW] 0 | [VIEW] 25 | [VIEW] 200 | [VIEW] 800 | [VIEW] 2,500 | [VIEW] 5,000 | [VIEW] 8,000 |
| ASP ($k) | [VIEW] — | [VIEW] 30 | [VIEW] 28 | [VIEW] 24 | [VIEW] 22 | [VIEW] 20 | [VIEW] 20 |
| EBIT margin | [VIEW] — | [VIEW] 8% | [VIEW] 15% | [VIEW] 20% | [VIEW] 25% | [VIEW] 28% | [VIEW] 30% |

Optimus UFCF `[VIEW]` equals EBIT × `(1 − FY2025 effective tax rate)` × 70%.

### SOTP

| input | treatment | class |
|---|---|---|
| Core | 20.0× FY2027E operating income excluding platform wedges + core YE2026E net cash + SpaceX filing FV | [VIEW] |
| Platform discount rate | 10.0%, mid-year convention from 2026-08-29 | [VIEW] |
| Platform terminal | 20.0× FSD, 18.0× Robotaxi and 18.0× Optimus FY2032 EBIT | [VIEW] |
| Bear check | Core + 0.50× total platform EV | [VIEW] |
| Bull check | Core + 1.50× total platform EV | [VIEW] |
| Three-year check | 22.0× FY2028E core operating income + core YE2028E net cash + SpaceX + remaining platform value from YE2028 | [VIEW] |

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
| FY2026 other income | hold reported 1H net other income, which includes the actual SpaceX unrealized gain; zero further mark-to-market and zero other H2 income | [FACT]/[VIEW] |
| NCI income | FY2026 retains reported 1H NCI income and assumes zero in 2H; zero thereafter | [FACT]/[VIEW] |

## Gaps

- Period-end basic shares for FY2026–FY2028: `not obtained`; the model uses the specified diluted WAS only.
- Credit cost: `not obtained`; 100% incremental gross margin is a `[VIEW]`.
- Segment capex, assets, liabilities and cash flow: `not obtained` (R8.5); no allocation is fabricated.
- Filing-based Robotaxi, incremental FSD and Optimus revenue/cost/unit economics: `not obtained` (R8.3); the model uses only the explicitly labeled researcher `[VIEW]` tables above.
- Product-level Energy units, realized pricing and cost/MWh: `not obtained` (R8.2); researcher-specified aggregate deployment and revenue assumptions govern.
- Forecast lease additions, depreciation and residual losses: `not obtained`; lease-fleet assets are held at the 2026-06-30 balance.
