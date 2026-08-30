# Tesla working thesis

GF-TSLA-1 · as of 2026-08-29 · name id `tsla`

Numbers live in the workbook. This file owns the claim, the mechanism, and the killing conditions. Official 12-month price target: [`models/tsla/valuation.md`](../../models/tsla/valuation.md). Do not treat a restated figure here as a second target.

## Claim

The official PT is a SOTP the model actually builds: filed Auto / Energy / Services / credits (core, 20× FY2027E core EBIT plus YE2026E net cash plus the SpaceX stake at filing FV) plus three researcher `[VIEW]` platforms that sit in the base — incremental FSD, Robotaxi, and Optimus — each DCF’d through FY2032 with a 16× FY2032 EBIT terminal at 10% WACC. Last close $348.75 (2026-08-28) still sits above that SOTP; the residual in `valuation.md` is the gap after those `[VIEW]`s, not a substitute for leaving the platforms at filing-zero.

If the model does not say it, it is not this thesis. Robotaxi / FSD / Optimus cells are `[VIEW]`, never filings (R8.3).

## Why this view is right

1. Core Auto-ex-services revenue fell FY2023–FY2025 (R2) with deliveries (R3). The core forecast only restores volume to 1.72 / 1.85 / 2.00 million on the FY2025 realized-revenue quotient. Q2 2026 volume was strong; ex-credit auto GM was 16.3%, Energy GM 20.4%, company OI $398m, FCF −$1,092m, FY2026 capex guided above $25bn (R2, R5.8). Core FY2026–FY2027 EBIT stays thin because opex is $17.0 / $18.2 / $19.2bn against core GP $17.6 / $20.1 / $22.8bn.
2. FSD is in the base as incremental revenue above the filing Auto/Services quotient (1.48 million active subscriptions are a fact at Q2 2026 — R3.1 — standalone dollars are not). The `[VIEW]` path reaches $13.0bn incremental revenue and $9.1bn EBIT by FY2032 at 70% margin.
3. Robotaxi is in the base, not a residual. Average paid fleet `[VIEW]` 5 / 30 / 100 / 220 / 400 / 600 / 800 thousand through FY2032, at rising revenue per vehicle and mid-30s to 55% then fading EBIT margins. Cybercab installed capacity `>125k`/year (R3.2) is the conservative addition ceiling; additions above that are explicit `[VIEW]` Model Y reallocations. That is a capacity-consistent fleet, not a 5-million-vehicle terminal.
4. Optimus is in the base from the Fremont line-install fact, not from a unit filing: `[VIEW]` 0 / 5 / 40 thousand units in FY2026–FY2028, 200 thousand by FY2032. It is the smallest of the three platform EVs.
5. 20× core FY2027E EBIT is already a premium to the Toyota/BYD EBIT framing in the comps table. Platform terminals use 16× FY2032 EBIT, not a software multiple on FY2027.

## What others miss or get wrong

1. Filing-zero on Robotaxi / FSD / Optimus is the wrong opposite error. The tape does not price Tesla as a 20× core-auto residual. This book puts the platforms in the base as `[VIEW]`s so the PT is an argument about the ramp, not a shrug.
2. Pre-Q2 company-compiled FY2026 GAAP EPS averaged $1.25 on 1.73 million deliveries (`consensus.md`). Core-plus-platform FY2026 diluted EPS in `income.md` is $0.64 on 1.72 million core deliveries. The near-term gap is still margin and opex, not volume. Delivery consensus already assumed growth through FY2028.
3. Treating $348.75 as already-earned autonomy is a category error. The residual after this SOTP is the extra platform the last price still needs — more fleet, more FSD dollars, more Optimus, or a higher terminal multiple — not proof that any one of those exists.
4. Post-Q2, as-of-2026-08-29 Street PTs and refreshed EPS: `not obtained`. The July 17 compilation is not the tape.

## Mechanism and magnitude

- Mechanism: company IS is filed segments plus the three `[VIEW]` lines. Official equity is A core + B FSD + C Robotaxi + D Optimus in `valuation.md`. Robotaxi UFCF is after-tax EBIT minus $25k `[VIEW]` fleet-growth capex, kept off the corporate capex line. FSD UFCF is 90% of after-tax EBIT. Optimus UFCF is 70% of after-tax EBIT.
- Magnitude: see the official PT, the four-piece SOTP, and the last-price residual in `valuation.md`. Robotaxi is the largest platform EV; FSD next; Optimus a small third. Checks (not official): 3-year, bear (platforms × 0.5), bull (platforms × 1.75) live in that file.

## Killing conditions

Check these on the next official print, not on commentary.

| kill | what would do it | when to check |
|---|---|---|
| Platform P&L replaces a `[VIEW]` | A filing or IR table with Robotaxi/FSD/Optimus revenue, cost, fleet, paid miles or units that can overwrite `segments.md` and move B, C or D | Q3 2026 10-Q / update; any 8-K with numeric Robotaxi or Optimus |
| Cybercab capacity/output breaks the fleet path | Run-rate additions clearly above or stuck far below the `>125k` ceiling, or paid fleet disclosed far from the `[VIEW]` 5k / 30k / 100k FY26–28 averages | Q3/Q4 2026 update capacity page; next production release |
| FSD dollars appear | Subscription count, ARPU or recognized FSD revenue that implies incremental dollars far from the `[VIEW]` $2.0 / $3.5 / $5.5bn FY26–28 path | next 10-Q contract-liability note; IR KPI page |
| Optimus units appear | Disclosed units or revenue that replace the `[VIEW]` 0 / 5 / 40k FY26–28 path | next 10-K / update product page |
| Core EBIT path breaks | FY2026 or FY2027 core OI (ex-platform) runs materially off `income.md` because GP or opex moves | Q3 and Q4 2026; FY2026 10-K |
| Capex mix | Corporate capex well below the >$25bn guide, or Robotaxi fleet capex disclosed in a way that double-counts the $25k `[VIEW]` | FY2026 10-K cash flow |

A higher last price alone does not kill the thesis. A new narrative without a number does not kill it.

## What this file is not

Not a rating. Not LONG/SHORT/PASS. The cover PR is the staged thesis. Publication of `names.thesis_ref` is Firstmate’s job after the captain merges.
