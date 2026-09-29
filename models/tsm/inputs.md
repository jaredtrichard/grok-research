# TSMC model inputs

As of 2026-09-29. NT$ billions except per-share data, wafer equivalents (thousand 12-inch-equiv.) and percentages. Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified base forecast; `not obtained` is never replaced with a guess.

## Accounting basis

| layer | basis | register / source |
|---|---|---|
| FY2023A–FY2025A annual history | IASB-IFRS (Form 20-F) | R2; S1 F-6–F-11 |
| 1H2026A interim actuals | TIFRS (quarterly filings summed) | R2 latest-quarter table; S3–S5 |
| FY2026E–FY2028E forecast | IASB-IFRS-style company build | `[VIEW]` on top of R2/R6/R7 anchors |

Do not splice TIFRS quarterly earnings into IASB-IFRS annual history without labeling (R2.3A).

## Source map

| source | use |
|---|---|
| [Register R2](../../memory/tsm/register.md#r2--historical-financial-skeleton) | annual and quarterly revenue, margins, NI, shipments |
| [Register R3](../../memory/tsm/register.md#r3--technology-node-and-platform-mix) | node/platform mix; wafer-revenue quotient cross-check |
| [Register R4](../../memory/tsm/register.md#r4--capacity-and-technology-roadmap) | capacity, N2 ramp, packaging capacity signal |
| [Register R6](../../memory/tsm/register.md#r6--margin-and-cost-structure) | margin drivers, R&D/SG&A |
| [Register R7](../../memory/tsm/register.md#r7--capex-cash-conversion-and-balance-sheet) | OCF, capex, balance sheet, 2026 budget |
| [Register R8](../../memory/tsm/register.md#r8--shares-dividends-and-buybacks) | shares, dividends |
| [TSMC 2025 Form 20-F S1](https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf) | FY2023–FY2025 IASB detail lines in `compute.py` |
| [TSMC Q2 2026 materials S3–S5](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/a80d7933be643644081584087731f73b22ea5a2c/2Q26%20EarningsRelease.pdf) | 1H2026 TIFRS roll-up; 2026-06-30 balance sheet |

## Historical and seed inputs

| input | value / treatment | pointer / source | class | as-of |
|---|---|---|---|---|
| Foundry revenue, GP, OI, parent NI, EPS | register / S1 table in script | R2 | [FACT] | FY2023–FY2025 |
| 1H2026 revenue, GP, OI, parent NI, shipments | Q1+Q2 sum | R2 | [FACT] TIFRS | 1H 2026 |
| R&D / G&A / marketing | S1 lines in script | R6.4; S1 F-6 | [FACT] | FY2023–FY2025 |
| OCF / PP&E purchases / D&A | S1 / R7.1 | R2; R7.1 | [FACT] | FY2023–FY2025 |
| Q2 2026 VIS disposal & MTM gain | 63.20; separated in model | R2.4A | [FACT] | Q2 2026 |
| Q2 2026 wafer quotient cross-check | 1,270.38 / 4,336k ≈ 293 NT$k/wafer-equiv. | R3.3 | [DEDUCTED] not ASP | Q2 2026 |
| FY2025 shipments | 15.0m 12-inch-equiv. | R4.1 | [FACT] | FY2025 |
| Q2 2026 node mix (wafer revenue %) | 2/3/5/7nm and advanced totals | R3 | [FACT] | Q2 2026 |
| Q2 2026 platform mix (total revenue %) | HPC 66%, Smartphone 22%, etc. | R3 | [FACT] | Q2 2026 |
| 2026-06-30 balance sheet | cash+securities, debt, WC, PP&E | R7.4 | [FACT] TIFRS | 2026-06-30 |
| Interest-bearing debt FY2023–FY2025 | not fully in register; script uses S1/XBRL where cited | S1 | [FACT]/gap | FY2025 partial |

## Researcher-specified forecast (`[VIEW]`)

| input | FY2026E | FY2027E | FY2028E | class / rationale |
|---|---:|---:|---:|---|
| Revenue (NT$bn) | 5,360 | 6,120 | 6,680 | [VIEW]; FY2026 anchored to management USD growth “slightly above 40%” (R2.6), translated at ~32 NT$/USD on FY2025 mix |
| Wafer shipments (m 12-inch-equiv.) | 20.8 | 22.5 | 23.8 | [VIEW]; capacity-led, below disclosed >17m YE2025 base plus ramps (R4.1) |
| Gross margin | 62.5% | 63.5% | 64.0% | [VIEW]; embeds N2 ramp dilution then maturation (R6.1) and overseas dilution 2–4pp (R6.2) |
| R&D | 283 | 317 | 349 | [VIEW]; ~15%/12%/10% growth |
| G&A + marketing | 108 | 116 | 124 | [VIEW]; scales with footprint |
| Capex (PP&E purchases) | 1,984 | 1,850 | 1,700 | [VIEW]; FY2026 near US$62bn × 32 NT$/USD (R7.3 midpoint); intensity fades |
| VIS / nonrecurring gains | 0 | 0 | 0 | [VIEW]; recurring non-op only |
| Packaging P&L | not modeled | — | — | R10.3; capacity constraint narrative only |
| Diluted WAS (m) | 25,940 | 25,950 | 25,960 | [VIEW]; near R8.5 |
| Cash dividends paid | 520 | 580 | 640 | [VIEW]; payout below FY2025 NT$466.8bn cash dividends (R8.3) at higher earnings |
| Buybacks | 0 | 0 | 0 | [FACT]/[VIEW]; no 2025 repurchases (R8.4) |

### Advanced-node mix (`[VIEW]` — wafer revenue %, not volume)

| node bucket | FY2026E | FY2027E | FY2028E | anchor |
|---|---:|---:|---:|---|
| 2nm | 9% | 14% | 18% | N2 HVM / ramp (R4.3) |
| 3nm | 31% | 30% | 28% | Q2 2026 30% (R3) |
| 5nm | 30% | 28% | 26% | mix shift |
| 7nm | 10% | 9% | 8% | |
| 7nm and below | 80% | 81% | 80% | advanced definition R1.4 |

### Platform mix (`[VIEW]` — % of total revenue)

| platform | FY2026E | FY2027E | FY2028E | anchor |
|---|---:|---:|---:|---|
| HPC | 68% | 69% | 70% | Q2 2026 66% + AI/HPC (R3) |
| Smartphone | 20% | 19% | 18% | Q2 2026 22% (R3) |
| IoT + Auto + DCE + Other | 12% | 12% | 12% | residual |

## Completion assumptions

| input | treatment | class / basis |
|---|---|---|
| Foundry revenue | equals company revenue (one segment) | R1.2 [FACT] |
| Segment gross profit | company GM × revenue; no node P&L | [VIEW] margins |
| Recurring non-operating | interest income 2.5% on beginning cash+securities; other recurring flat | [VIEW] |
| VIS gain | historical Q2 2026 only; zero in forecast | R2.4A / [VIEW] |
| Tax rate | FY2025 effective rate on pre-tax recurring earnings | [DEDUCTED] S1 |
| SBC | 0.5% of revenue | [VIEW]; immaterial vs TSMC scale |
| D&A | 11.5% of average PP&E | [VIEW]; near FY2025 688bn on ~3.7tn PP&E |
| Working-capital days | AR 29, inventory 87 from R7.5; AP from 2026-06-30 annualized COGS | [FACT]/[VIEW] |
| Debt | roll forward; issue if cash below minimum | [VIEW] |
| Minimum cash+securities | 1,500 | [VIEW] liquidity policy |
| Other assets / liabilities | hold residual from latest base | [VIEW] |

## Gaps

- Line-by-line IASB/TIFRS bridge for FY2025 earnings: **not obtained** (R2.3, R10.13).
- Node/platform/packaging operating income and assets: **not obtained** (R10.4).
- Packaging revenue, margin and capacity: **not obtained** (R10.3); modeled only as a demand/capacity constraint.
- Wafer ASP by node: **not obtained** (R10.1); NT$/wafer quotient is not ASP (R3.3).
- Exact utilization by node/site: **not obtained** (R10.2).
- Street consensus: **not obtained** (R10.9).

## Valuation (`[VIEW]` — see [`valuation.md`](valuation.md))

| input | value | note |
|---|---|---|
| As-of / last close | 2026-09-29; TSM ADR $456.94 | Yahoo Finance; `compute.py` constants |
| USD/NTD | 32 | R2.5 guidance anchor |
| Official method | 21.0× FY2027E recurring OI + FY2027E net cash | single foundry segment |
| DCF WACC / terminal g | 9.5% / 3.0% | cross-check on forecast FCF + R7.4 net cash |
| Bear / bull EBIT | 18.0× / 24.0× | sensitivity on same OI |
| Peer EV/EBIT | not obtained | R10.8–R10.9 |
