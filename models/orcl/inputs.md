# Oracle model inputs

As of 2026-09-29. USD millions except MW, GPUs, percentages and shares. Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified base forecast; `not obtained` is never replaced with a guess.

## Source map

| source | use |
|---|---|
| [Register R2](../../memory/orcl/register.md#r2--historical-economics) | consolidated and product revenue; segment revenue and margin |
| [Register R3](../../memory/orcl/register.md#r3--cloud-applications-rpo-and-capacity) | Cloud Applications / OCI; RPO; capacity KPIs |
| [Register R5](../../memory/orcl/register.md#r5--capital-intensity-liquidity-and-capital-structure) | balance sheet, capex, prepayments, shares |
| [Register R8](../../memory/orcl/register.md#r8--explicit-gaps) | explicit modeling gaps |
| [Oracle FY2026 Form 10-K S1](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm) | corporate opex bridge (XBRL) |
| [Oracle Q1 FY2027 Form 10-Q S2](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm) | latest quarter cross-check |

## Historical and seed inputs

| input | value / treatment | pointer / source | class | as-of |
|---|---|---|---|---|
| Product revenue pools | register tables | R2 | [FACT] | FY2024–FY2026 |
| Cloud Applications / OCI split | FY2025–FY2026 only | R3 | [FACT] | FY2025–FY2026 |
| FY2024 cloud apps / OCI | not obtained | R3 / R8 | **not obtained** | FY2024 |
| Reported segment revenue and margin | three segments | R2; exclusions R1.4 | [FACT] | FY2024–FY2026 |
| Consolidated revenue, OI, NI, OCF, capex | register | R2 | [FACT] | FY2024–FY2026 |
| R&D, G&A, amortization, restructuring, SBC | SEC XBRL 10-K | S1 | [FACT] | FY2024–FY2026 |
| Interest, tax, other non-operating | SEC XBRL 10-K | S1 | [FACT] | FY2024–FY2026 |
| Segment→OI residual | computed in script to tie filed OI | R1.4 bridge | [DEDUCTED] | FY2024–FY2026 |
| Balance sheet history | SEC XBRL 10-K | S1 | [FACT] | FY2024–FY2026 |
| Q1 FY2027 cloud apps / OCI / margins | earnings tables | R2/R3 | [FACT] | Q1 FY2027 |
| Q1 FY2027 license vs support split | not obtained | R2 (software line only) | **not obtained** | Q1 FY2027 |

## Researcher-specified revenue growth `[VIEW]`

Applied to prior-year product revenue (OCI and Cloud Applications separately; cloud total is their sum).

| driver | FY2027E | FY2028E | FY2029E | class / rationale |
|---|---:|---:|---:|---|
| OCI revenue growth | 75% | 45% | 30% | [VIEW]; capacity/RPO-led but decelerating from Q1 run-rate (R3) |
| Cloud Applications growth | 11% | 10% | 9% | [VIEW]; near Q1 FY2027 YoY (R3.2) |
| Software license growth | −4% | −4% | −3% | [VIEW]; continued erosion (R2 history) |
| Software support growth | 1% | 1% | 1% | [VIEW]; stable installed base (R1.5) |
| Hardware growth | 6% | 5% | 4% | [VIEW]; Exadata-led (R7.4) |
| Services growth | 4% | 4% | 3% | [VIEW]; aggregate only |

## Researcher-specified segment margin `[VIEW]`

Margin % applied to respective **segment revenue** (cloud+license+support, hardware, services).

| margin | FY2027E | FY2028E | FY2029E | class / rationale |
|---|---:|---:|---:|---|
| Cloud and software | 54.5% | 53.5% | 52.5% | [VIEW]; infra expense pressure (R3.3); starts at Q1 FY2027 disclosed rate |
| Hardware | 65.0% | 65.0% | 64.5% | [VIEW]; near FY2026 actual |
| Services | 30.0% | 30.5% | 31.0% | [VIEW]; modest improvement from FY2026 |

## Corporate bridge and cash `[VIEW]`

| input | FY2027E | FY2028E | FY2029E | class |
|---|---:|---:|---:|---|
| R&D | 11,200 | 11,800 | 12,300 | [VIEW] |
| G&A | 1,700 | 1,750 | 1,800 | [VIEW] |
| Amortization of intangibles | 1,500 | 1,350 | 1,200 | [VIEW] |
| Restructuring | 800 | 500 | 400 | [VIEW] |
| Stock-based compensation | 5,100 | 5,300 | 5,500 | [VIEW] |
| Segment→OI residual | 0 | 0 | 0 | [VIEW]; historical residual not projected |
| Capex | 72,000 | 68,000 | 62,000 | [VIEW]; above FY2026; no written FY2027 range (R5.3, R8.7) |
| Customer prepay in OCF | 25,000 | 18,000 | 12,000 | [VIEW]; financing component separated (R5.2) |
| Net debt issuance | 15,000 | 8,000 | 0 | [VIEW] funding plug |
| Diluted WAS (m) | 3,050 | 3,100 | 3,120 | [VIEW]; ATM completed; preferred conversion not modeled (R5.7) |
| Buybacks / dividends | 0 | 0 | 0 | [VIEW] |

## Completion assumptions

| input | treatment | class |
|---|---|---|
| Interest income | 2.5% of beginning cash + marketable securities | [VIEW] |
| Interest expense | 3.8% of beginning total debt | [VIEW] |
| Tax rate | FY2026 effective rate from filed pre-tax and tax | [DEDUCTED] |
| D&A proxy | scales with revenue from FY2026 depreciation + amortization | [VIEW] |
| AR days | 56 held flat | [VIEW] |
| AP days | 59 on ~35% of revenue proxy for cost base | [VIEW] |
| Deferred revenue | prior year × 1.15 | [VIEW] |
| Off-BS lease / purchase commitments | not modeled | **not obtained** / R5.4 |

## Gaps blocking valuation (not modeled here)

- Product-level OCI / application gross profit and margin (R8.3).
- Segment assets, capex, D&A, debt and cash flow (R8.5).
- RPO quality, customer concentration, cancellation and margin (R8.2).
- Numerical FY2027 capex guidance (R8.7).
- Mandatory convertible preferred future share count (R5.7).
- Multicloud marketplace net economics (R6.3).
- Standalone valuation module: **pending** (see [`memory/orcl/model.md`](../../memory/orcl/model.md)).
