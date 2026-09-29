# AMD working thesis

GF-AMD-1 · as of 2026-09-29 · name id `amd`

Built from [`models/amd/`](../../models/amd/) and [`valuation.md`](../../models/amd/valuation.md). Numeric claims live in the workbook and register; this file states the claim, mechanism, and killing conditions. No rating label.

## Claim

The segment model does not support the last close. Official 12-month price target is in [`valuation.md`](../../models/amd/valuation.md) (blended 65% unlevered FCF DCF + 35% FY2028 segment EBIT SOTP). At that target the investment is: **own the Data Center–led earnings and free-cash-flow path in the workbook, at a cash-and-segment multiple that still leaves Client+Gaming and Embedded as supporting pools—not a platform story priced as if contracted AI gigawatts were already cash.**

Implied change versus the cited last close is also in `valuation.md`. The gap is the thesis: either the model understates cash conversion and duration, or the tape prices a path the filings and this workbook do not yet fund.

## Mechanism and magnitude

1. **Data Center is the bridge.** Research maps revenue to EPYC, Instinct/rack content, networking and adaptive products ([`research.md`](research.md) §3.1). The model embeds that in Data Center revenue and operating income ([`segments.md`](../../models/amd/segments.md)): FY2026–FY2028 Data Center revenue steps with `[VIEW]` growth that is framed against management call language (R7.8: Data Center “more than double” YoY in 2027; server CPU growth commentary) but **not** against contracted GW→dollar schedules (R9.10).
2. **Income statement is segment-summed.** Consolidated operating income equals Data Center OI + Client+Gaming OI + Embedded OI + All Other ([`income.md`](../../models/amd/income.md)). Mix shift and AI ramp must show up as those lines moving; All Other continues to absorb unallocated amortization/SBC-style costs.
3. **Cash is the primary valuation object.** Explicit FY2026–FY2028 model FCF from [`cashflow.md`](../../models/amd/cashflow.md) drives the DCF leg; SOTP on FY2028 segment EBIT is the cross-check. Net cash is the 1H2026 filing figure (R6.1). World Labs is excluded until close (R1.9).
4. **Magnitude.** Workbook forecast revenue / operating income / FCF for FY2026–FY2028 and the official PT bridge live only in the model and `valuation.md`. Do not restate them here.

## Why this view is right (conditional on the model)

- Primary documents (10-K/10-Q, releases, official webcast transcripts S14–S16) support a **Data Center mix shift already underway** (R7.8: Data Center ~58% of revenue in Q2 2026) and multi-year AI/server commentary, without giving product-level units, ASPs, or deal-level revenue (R9.1, R9.10).
- Segment reporting forces honesty: Client and Gaming have revenue but **not** standalone OI; the model refuses fake Client/Gaming EBIT ([`research.md`](research.md) §2).
- Valuation refuses to treat announced OpenAI/Meta/Anthropic gigawatts or deployment milestones as booked FCF. That keeps the PT on cash and filed-segment profit rather than on a narrative multiple.

## What others miss or get wrong (hypothesis, not Street poll)

Company-compiled consensus is **not obtained** ([`consensus.md`](consensus.md)). Relative to the **last close**, the workable hypotheses are:

1. **Tape prices contracted AI scale as near-term cash.** Filings give milestones and power figures, not AMD content × price × recognition schedules (R9.10). A PT built on model FCF will sit below a tape that capitalizes GW headlines.
2. **Duration / terminal multiple.** If investors assume AI FCF compounds longer or exits at a higher multiple than the `[VIEW]` terminal in `valuation.md`, the DCF leg alone cannot meet the last close without rewriting forecast FCF or WACC.
3. **Warrant and deal dilution underweighted.** OpenAI/Meta warrant share overlays matter at scale (sensitivity in `valuation.md`); World Labs (~$8.2B all-stock, R1.9) is not in the base model and will dilute and/or add opex after close.
4. **Gross-margin and NWC conversion.** CFO commentary puts ramping Data Center AI slightly below corporate-average GM while still adding GP dollars (R7.8). Large forecast ΔNWC in FY2027–FY2028 means OCF conversion, not just NI, decides whether the DCF holds.

Without dated Street books, “what others miss” is inferred from price versus this workbook, not from a consensus table.

## Killing conditions (and when to check)

| Kill | Trigger | Check |
|---|---|---|
| Data Center path breaks | FY2027 Data Center revenue or OI well below model (Instinct/Helios/MI450 slip, export, HBM/packaging, hyperscaler delay) | Next 10-Q / earnings + call transcript; refresh segments after each print |
| Cash conversion fails | OCF − capex far below model FCF (ΔNWC, mix GM, opex) | Cash-flow statement each print; re-run `compute.py` |
| Dilution / deal shock | Warrant exercises or World Labs close economics that cut value/share more than sensitivity | 8-K / S-4 / 10-Q share count; add World Labs only after filed accounting |
| Terminal / risk reset | Sustained higher cost of capital or FCF multiple compression vs `[VIEW]`s in valuation | Re-run valuation sensitivity; do not “patch” PT without model move |
| Segment disclosure change | Reporting map change that invalidates DC / C+G / Embedded bridges | New 10-K segment note; rebuild research + model |

If the model and valuation do not move after a print, do not open a new PR for a cosmetic thesis edit.

## Pointers

- Research / drivers: [`research.md`](research.md)
- Facts: [`register.md`](register.md)
- Workbook: [`model.md`](model.md) → `models/amd/`
- Price target and method: [`valuation.md`](../../models/amd/valuation.md)
- Priced expectations: [`consensus.md`](consensus.md)
