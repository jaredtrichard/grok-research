# Tesla working thesis

GF-TSLA-1 · as of 2026-08-29 · name id `tsla`

Numbers live in the workbook. This file owns the claim, the mechanism, and the killing conditions. Official 12-month price target: [`models/tsla/valuation.md`](../../models/tsla/valuation.md). Do not treat a restated figure here as a second target.

## Claim

The official PT is the unadjusted SOTP of four pieces the model actually builds: filed Auto / Energy / Services / credits as core (20× FY2027E core EBIT plus YE2026E net cash plus the SpaceX stake at filing FV) plus three `[VIEW]` platforms in the BASE — incremental FSD, Robotaxi, and Optimus — each DCF’d through FY2032. The platform paths are the operating statements that would have to be true at last-sale scale (fleet, attach, ASP, margin, multiple). They are not a residual plug and they were not solved to equal $348.75. Last close $348.75 (2026-08-28) is a comparison in `valuation.md`; the signed residual there is whatever those paths produce.

If the model does not say it, it is not this thesis. Robotaxi / FSD / Optimus cells are `[VIEW]`, never filings (R8.3).

## Why this view is right

1. Core remains a compressed auto/energy/services business. Auto-ex-services revenue fell FY2023–FY2025 (R2) with deliveries (R3). The core forecast only restores volume to 1.72 / 1.85 / 2.00 million on the FY2025 realized-revenue quotient. Q2 2026 volume was strong; ex-credit auto GM was 16.3%, Energy GM 20.4%, company OI $398m, FCF −$1,092m, FY2026 capex guided above $25bn (R2, R5.8). Core FY2026–FY2027 EBIT stays thin because opex is $17.0 / $18.2 / $19.2bn against core GP $17.6 / $20.1 / $22.8bn. Core is a mid-teens dollar of the SOTP, not the tape.
2. FSD is in the base as incremental revenue above the filing Auto/Services quotient. 1.48 million active subscriptions are a fact at Q2 2026 (R3.1); standalone dollars are not. The `[VIEW]` path is a high-ARPU unsupervised software layer: $3 / $6 / $10bn FY2026–FY2028, $32bn by FY2032, 72% EBIT margin, 20× FY2032 EBIT terminal. That is attach and price on the installed customer fleet, not Robotaxi fares.
3. Robotaxi is in the base as a paid-fleet path: `[VIEW]` average fleet 15 / 80 / 250 thousand in FY2026–FY2028 and 3.5 million by FY2032, at $30–$42k revenue per vehicle and mid-20s to ~50% then fading EBIT margins, 18× FY2032 EBIT terminal. The single disclosed Texas Cybercab line is `>125k`/year installed (R3.2), not current output. This fleet requires additional Cybercab plants and/or Model Y network vehicles; peak implied additions exceed 1 million in a year. The 10-Q does not disclose that plan. That capacity expansion is the `[VIEW]`, not a filing.
4. Optimus is in the base at manufacturing scale: `[VIEW]` 0 / 25 / 200 thousand units in FY2026–FY2028 and 8 million by FY2032, ASP fading to $20k, EBIT margin to 30%, 18× FY2032 EBIT terminal. Fremont Optimus lines installing is the FACT direction; the unit path is `[VIEW]`. It is the second-largest platform EV after Robotaxi.
5. 20× core FY2027E EBIT is a premium to Toyota/BYD EBIT framing. Platform terminals (20× FSD, 18× Robotaxi, 18× Optimus) are software/network multiples, not 16× industrial on a tiny EBIT. Dilution of another 500m shares is ~13% of the filing denominator, not the old $1.1T hole.

## What others miss or get wrong

1. Filing-zero on the platforms is the wrong opposite error. The tape does not price Tesla as 20× core-auto. Leaving an 80% residual was not a SOTP.
2. Fitting the last sale is the other wrong error. The official PT is not $348.75 by construction. The paths were set as operating `[VIEW]`s; the script produced the number.
3. Pre-Q2 company-compiled FY2026 GAAP EPS averaged $1.25 on 1.73 million deliveries (`consensus.md`). Near-term core-plus-platform EPS still differs from that compilation because opex and mix, not because deliveries are the whole debate. Delivery consensus already assumed growth through FY2028.
4. Treating last sale as already-earned autonomy without naming fleet, attach, ASP, margin and multiple is a category error. Those names are in `inputs.md` and `valuation.md`.
5. Post-Q2, as-of-2026-08-29 Street PTs and refreshed EPS: `not obtained`. The July 17 compilation is not the tape.

## Mechanism and magnitude

- Mechanism: company IS is filed segments plus the three `[VIEW]` lines. Official equity is A core + B FSD + C Robotaxi + D Optimus. Robotaxi UFCF is after-tax EBIT minus $22k `[VIEW]` fleet-growth capex, kept off the corporate capex line. FSD UFCF is 90% of after-tax EBIT. Optimus UFCF is 70% of after-tax EBIT. WACC 10%.
- Magnitude: see the official PT, the four-piece SOTP, hole anatomy, and signed last-sale residual in `valuation.md`. Robotaxi is the largest platform EV, then Optimus, then FSD; core is the smallest piece. Checks (not official): 3-year, bear (platforms × 0.5), bull (platforms × 1.5). The signed residual versus $348.75, holding other cells fixed, points at the Robotaxi path as the lever that would close it, because that EV is the largest.

## Killing conditions

Check these on the next official print, not on commentary.

| kill | what would do it | when to check |
|---|---|---|
| Platform P&L replaces a `[VIEW]` | A filing or IR table with Robotaxi/FSD/Optimus revenue, cost, fleet, paid miles or units that overwrites `segments.md` and moves B, C or D | Q3 2026 10-Q / update; any 8-K with numeric Robotaxi or Optimus |
| Cybercab capacity does not expand | Additions stay pinned near one `>125k` line with no second plant or Model Y network disclosure, so the `[VIEW]` 250k / 3.5m fleet path cannot happen | Q3/Q4 2026 update capacity page; next production release |
| FSD dollars far from the path | Subscription count, ARPU or recognized FSD revenue that implies incremental dollars far from `[VIEW]` $3 / $6 / $10bn FY26–28 | next 10-Q contract-liability note; IR KPI page |
| Optimus units far from the path | Disclosed units or revenue that replace `[VIEW]` 0 / 25 / 200k FY26–28 | next 10-K / update product page |
| Core EBIT path breaks | FY2026 or FY2027 core OI (ex-platform) runs materially off `income.md` | Q3 and Q4 2026; FY2026 10-K |
| Capex mix | Corporate capex well below the >$25bn guide, or Robotaxi fleet capex disclosed in a way that double-counts the $22k `[VIEW]` | FY2026 10-K cash flow |

A last-sale move alone does not kill the thesis. A new narrative without a number does not kill it. Do not retune the official PT to the tape.

## What this file is not

Not a rating. Not LONG/SHORT/PASS. The cover PR is the staged thesis. Publication of `names.thesis_ref` is Firstmate’s job after the captain merges.
