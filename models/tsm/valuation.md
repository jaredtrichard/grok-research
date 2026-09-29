# TSMC valuation

At the $456.94 ADR last close, the official **12-month price target** is **$463.15 per ADR** (**NT$2,964.19 per common share**), from a single-segment foundry **EV / recurring EBIT** bridge on the modeled `FY2027E` path plus net cash. TSMC reports one foundry segment (R1.2); this is not a platform SOTP.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | 2026-09-29 |
| Last close (ADR, USD) | $456.94 on 2026-09-29 |
| Last-price source | [Yahoo Finance TSM history](https://finance.yahoo.com/quote/TSM/history/) (cross-check: [Yahoo chart API](https://query1.finance.yahoo.com/v8/finance/chart/TSM?range=5d&interval=1d)) |
| ADR ratio | 1 ADR = 5 common shares (R8.1) |
| FX for ADR bridge | 32 NT$ / USD `[VIEW]` (Q3 2026 guidance anchor R2.5) |
| PT denominator | 25,950m diluted WAS, `FY2027E` model path |
| Primary method | 21.0× `FY2027E` **recurring operating income** + `FY2027E` net cash |
| Recurring earnings | Operating income and parent NI exclude Q2 2026 VIS gain (R2.4A); forecast VIS = 0 `[VIEW]` |

## What the tape must be paying for

The table below compares the **last price** to **model recurring foundry earnings** from [`income.md`](income.md). If the market is rational on this `[VIEW]` forecast path, the implied multiples should bracket the selected 21× EBIT anchor or embed extra growth, packaging scarcity, or geopolitical discount not in the base case.

| item | formula | value |
|---|---|---|
| Last-price market cap (USD bn) | Last close × ADR count | 2,371.5 |
| Last-price market cap (NT$bn) | × 32 USD/NTD [VIEW] | 75,888.6 |
| 2026-06-30 net cash (NT$bn) | R7.4; model 1H2026A | 2,486.3 |
| Current operating EV (NT$bn) | Market cap − net cash | 73,402.3 |
| EV / FY2027E recurring EBIT | Operating EV ÷ OI | 21.3× |
| EV / FY2028E recurring EBIT | Operating EV ÷ OI | 19.3× |
| P/E on FY2027E recurring NI | Market cap ÷ recurring parent NI | 25.8× |
| P/E on FY2028E recurring NI | Market cap ÷ recurring parent NI | 23.3× |
| EV / FY2027E revenue | Operating EV ÷ revenue | 12.0× |
| [DEDUCTED] Tape vs official PT / ADR | $456.94 − $463.15 | $-6.21 (-1.3% vs PT) |

At tape, **EV / FY2027E recurring EBIT** is **21.3×** versus the official **21×** selection. A higher tape multiple implies the market is paying for faster AI/HPC foundry growth, longer advanced-node pricing power, or net-cash optionality beyond the base `FY2027E` `21×` frame; a lower multiple would imply overseas-fab dilution (R6.2), export-control risk (R9.3), or cyclical utilization stress not captured in the `[VIEW]` margin path.

## Official equity bridge (NT$ billions → per share)

| item | basis | NT$bn or multiple |
|---|---|---|
| FY2027E recurring operating income (foundry) | income.md; ex VIS | 3,453.2 |
| [VIEW] Selected EV / EBIT | 21.0×; premium foundry vs diversified semi | 21.0× |
| [VIEW] Operating enterprise value | EBIT × multiple | 72,517.2 |
| FY2027E net cash | Cash + securities − interest-bearing debt; model balance.md | 4,403.5 |
| Official equity value (NT$bn) | Operating EV + net cash | 76,920.7 |
| Diluted WAS (m) | R8.5 / FY2027E [VIEW] path | 25,950 |
| Official 12-month PT / common share | Equity ÷ diluted WAS | 2,964.19 |
| Implied PT / ADR (USD) | Common PT × 5 ÷ 32 USD/NTD [VIEW] | $463.15 |

**[VIEW] Multiple rationale (21×):** TSMC is modeled as a single pure-play leading-edge foundry with net cash and elevated capex converting to revenue on the R7.3 budget path. 21× `FY2027E` recurring operating income sits near the **tape-implied 21.3×** on the same model EBIT, slightly below a bull foundry premium to reflect overseas margin dilution (R6.2) and concentration risk (R5.1, R9.5). It is **not** sourced from peer multiples (R10.8).

## Recurring foundry operating path (valuation inputs)

| line | FY2026E | FY2027E | FY2028E | source |
|---|---:|---:|---:|---|
| Revenue | 5,360.0 | 6,120.0 | 6,680.0 | income.md |
| Gross margin | 62.5% | 63.5% | 64.0% | `[VIEW]` inputs.md |
| Operating income (recurring) | 2,959.0 | 3,453.2 | 3,802.2 | income.md |
| Recurring parent NI | 2,519.9 | 2,944.9 | 3,259.8 | ex VIS |
| Free cash flow | 1,227.1 | 1,790.1 | 2,387.5 | cashflow.md |

## Equity DCF cross-check (recurring FCF)

| [VIEW] item | value | note |
|---|---|---|
| WACC | 9.5% | Foundry leader with net cash; Taiwan/ADR listing; not observed from market data |
| Terminal growth | 3% | Perpetuity on FY2028E FCF [VIEW] |
| Mid-year convention | 0.5 / 1.5 / 2.5 years | FY2026E–FY2028E FCF from cashflow.md |
| PV of forecast FCF | 4,637.7 | Sum of three `[VIEW]` years |
| Terminal FCF (FY2028E × (1+g)) | 2,459.1 | `2,387.5` base FCF |
| PV of terminal | 30,152.5 | Gordon `3%` / WACC `9.5%` |
| DCF equity value | 37,276.5 | PV(FCF) + terminal + 2026-06-30 net cash (R7.4); **not** the official method |
| Implied DCF PT / ADR | $224.45 | vs official $463.15; FCF path is capex-heavy (R7.3) so DCF can sit below EBIT-multiple EV |

Heavy **capex** in the `[VIEW]` forecast (see [`cashflow.md`](cashflow.md)) compresses near-term FCF versus recurring EBIT; the DCF cross-check is therefore expected to land **below** the EV/EBIT official bridge unless terminal growth or WACC is retuned.

| period | recurring FCF (NT$bn) | discount year | WACC |
|---|---|---|---|
| FY2026E | 1,227.1 | 0.5 | 9.5% [VIEW] |
| FY2027E | 1,790.1 | 1.5 | 9.5% [VIEW] |
| FY2028E | 2,387.5 | 2.5 | 9.5% [VIEW] |

## Checks — not additional official targets

| check | method | PT / ADR (USD) |
|---|---|---|
| Bear EV/EBIT | 18× FY2027E OI + net cash | $400.78 |
| Base (official) | 21× FY2027E OI + net cash | $463.15 |
| Bull EV/EBIT | 24× FY2027E OI + net cash | $525.53 |
| 3-year exit check | 19× FY2028E OI + net cash | $472.02 |
| DCF base | WACC 9.5%, terminal g 3% on FY2028E FCF | $224.45 |
| DCF WACC +1.0pp | WACC 10.5% | $196.29 |
| DCF WACC −1.0pp | WACC 8.5% | $262.87 |

Bear and bull rows scale only the **EV/EBIT multiple** on the same `FY2027E` operating income and net cash. DCF rows re-run the same FCF path with **±1.0pp WACC** around the 9.5% base.

## Comparable-company framing

Peer foundry/semi manufacturing multiples were **not obtained** in this gate; do not treat the table as valuation anchors.

| peer / frame | metric sought | status | note |
|---|---|---|---|
| Samsung Electronics (foundry + devices) | EV/EBIT, EV/Sales | not obtained | R10.8; no comparable foundry-only financials in TSMC primary set |
| Intel (Intel Foundry + products) | EV/EBIT | not obtained | R10.8 |
| GlobalFoundries (GFS) | EV/EBIT | not obtained | R10.9; no refreshed peer pull in this gate |
| UMC / SMIC (pure-play foundry peers) | EV/EBIT | not obtained | R10.8; multiples not sourced here |

Samsung and Intel filings mix foundry with large product businesses; GlobalFoundries and UMC would require a separate sourced comp pull (R10.8–R10.9).

## Gaps and what would move the official PT

- Sourced **peer EV/EBIT** for pure-play foundries (R10.8) to test the 21× `[VIEW]` vs the tape-implied 21.3×.
- **Packaging economics** (R10.3) if CoWoS becomes a separately measurable profit pool.
- **IASB/TIFRS bridge** before splicing interim TIFRS into IASB valuation history (R10.13).
- **Street consensus** (R10.9) for external PT distribution — not used here.
- A change in `FY2027E` recurring **operating income** path, **21×** multiple, **net cash** roll-forward, **USD/NTD [VIEW]**, or **diluted share** path.
