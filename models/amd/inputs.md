# AMD model inputs

As of 2026-09-29. USD millions except per-share data and percentages. Arithmetic and derived values live only in [`compute.py`](compute.py). `[VIEW]` is the researcher-specified base forecast; `not obtained` is never replaced with a guess.

## Source map

| source | use |
| --- | --- |
| [Register R2](../../memory/amd/register.md#r2--historical-and-latest-reported-economics) | segment and consolidated revenue, gross profit, opex, operating income |
| [Register R5–R6](../../memory/amd/register.md) | capex, inventory, liquidity, OCF/FCF, shares |
| [Register R7.8](../../memory/amd/register.md) | 2027 Data Center segment growth language (not dollar backlog) |
| [Register R1.9](../../memory/amd/register.md) | World Labs — **excluded** from model until close |
| [AMD FY2025 10-K S1](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm) | historical balance sheet / cash flow via XBRL |
| [AMD Q2 2026 10-Q S5](https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm) | 1H 2026 balance sheet and segment actuals |

## Historical inputs

| input | periods | pointer | class |
| --- | --- | --- | --- |
| Data Center / Client / Gaming / Embedded revenue | FY2023–FY2025; 1H 2026 | R2 segment tables | [FACT] |
| Data Center / Client+Gaming / Embedded operating income | same | R2 | [FACT] |
| Client or Gaming standalone operating income | all | R9.5 | **not obtained** |
| All Other operating loss | same | R2 | [FACT] |
| Consolidated revenue, GP, R&D, MG&A, OI, NI, EPS | FY2023–FY2025; 1H 2026 | R2 consolidated | [FACT] |
| Balance sheet major lines | FY2023–FY2025 | XBRL / S1 | [FACT] |
| 1H 2026 cash, STI, AR, inventory, AP, debt | 1H 2026 | R6.1 | [FACT] |
| 1H 2026 OCF, capex, FCF | 1H 2026 | R6.2 | [FACT] |
| World Labs revenue / opex / purchase accounting | — | R1.9 | **not obtained**; excluded |

## Researcher-specified forecast (`[VIEW]`)

Segment revenue growth is applied to the prior fiscal year for FY2026 and to the prior forecast year thereafter. Segment operating income uses segment revenue × segment OI margin. All Other is a dollar `[VIEW]` (unallocated amortization, SBC and acquisition-related costs — not a segment).

| input | FY2026E | FY2027E | FY2028E | class / anchor |
| --- | ---: | ---: | ---: | --- |
| Data Center revenue growth | 78% | 105% | 40% | [VIEW]; FY2027 >100% YoY aligns with R7.8 “more than double” segment revenue language, not contracted dollars |
| Client revenue growth | 18% | 10% | 8% | [VIEW]; 1H unit/mix facts R3.1–R3.2; softer PC 2H R7.8 |
| Gaming revenue growth | −15% | −5% | 0% | [VIEW]; semi-custom cycle R3.3 |
| Embedded revenue growth | 15% | 10% | 8% | [VIEW]; recovery R3.4 |
| Data Center OI margin | 30.0% | 31.0% | 32.0% | [VIEW]; vs 29.6% 1H26 [DEDUCTED] R2 |
| Client + Gaming OI margin | 16.0% | 17.0% | 18.0% | [VIEW]; vs 15.5% 1H26 |
| Embedded OI margin | 39.0% | 39.0% | 38.0% | [VIEW] |
| All Other operating loss ($m) | (5,100) | (5,800) | (6,400) | [VIEW]; scales with SBC/amort trend R2.3 |
| Consolidated gross margin | 54% | 55% | 55% | [VIEW]; vs 53% 1H26 R2; AI mix R7.8 |
| R&D | 9,600 | 10,800 | 11,600 | [VIEW]; AI headcount R5.1–R5.2 |
| MG&A | 4,900 | 5,400 | 5,800 | [VIEW] |
| Tax rate (pre-tax) | 13% | 13% | 13% | [VIEW]; Q3 guide R7.4 |
| Interest expense | 150 | 160 | 170 | [VIEW] |
| Other income | 80 | 60 | 50 | [VIEW] |
| D&A (cash-flow add-back) | 1,200 | 1,400 | 1,600 | [VIEW]; filing D&A split **not obtained** |
| SBC (cash-flow add-back) | 2,100 | 2,400 | 2,600 | [VIEW]; vs 1H ~990 R2.3 |
| Capex | 2,800 | 3,500 | 4,000 | [VIEW]; vs 1H 1,197 R5.3 |
| Buybacks | 400 | 600 | 800 | [VIEW]; vs 1H 221 R6.4 |
| Diluted WAS (m) | 1,660 | 1,670 | 1,680 | [VIEW]; Q3 guide ~1,660 R7.4; warrants R6.5 **not modeled** |

Working capital: AR, inventory and AP days `[DEDUCTED]` from 1H 2026 balance sheet and annualized 1H revenue/COGS (see `cashflow.md`). Minimum cash balance `[VIEW]` $4,000m.

## Valuation `[VIEW]` (see `compute.py` constants)

| input | value | rationale |
| --- | --- | --- |
| WACC | 9.5% | Fabless high-growth semi risk blend |
| Terminal g | 2.5% | Long-run fade after AI capex cycle |
| Terminal FCF multiple | 24× FY2028 FCF | Exit cross-check vs Gordon |
| SOTP EBIT multiples | DC 26× / C+G 14× / Emb 17× | Segment comp anchors |
| Official blend | 65% DCF / 35% SOTP | Cash path primary, segments check |
| PT shares | FY2028E diluted WAS (1,680m) | Forward NI denominator; basic 1,632.475m for market-cap vs last close (R6.5) |
| Last close | $607.57 on 2026-09-29 | Yahoo Finance (cited in `valuation.md`) |

## Gaps that block a higher-confidence target

- Segment gross profit and product-level units/ASP: R9.1–R9.5.
- Contracted AI deployment dollars and warrant dilution: R9.10, R6.5 (sensitivity only).
- World Labs close effects: R1.9.
- Street consensus: R9.9.
- Lease guarantees and strategic investment funding (R6.6–R6.7) not in FCF.
