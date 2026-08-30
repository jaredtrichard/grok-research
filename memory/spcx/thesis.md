# SpaceX working thesis

as_of: 2026-08-30
task: GF-SPCX-1, Gate 4
name_id: spcx
ticker: SPCX

If the model does not say it, it is not here. Numbers live in `models/spcx/`. This file is the claim those numbers make.

## Claim

Last sale $141.50 (Nasdaq lastTradeTimestamp 2026-08-27) already prices nearly twice the enterprise value of the segment SOTP. The 12-month base price target is the line `12-month base price target` in `models/spcx/valuation.md`. Bull in that file only reaches last sale. Bear is a further cut on ARPU, AI conversion, and Connectivity multiple. No rating.

The investment idea is the gap between that target and the tape: the tape is paying for Starship commercial cash and AI infrastructure cash that the three-statement model does not produce through FY2028E.

## What the model says

Point, do not recopy.

- Connectivity is the cash engine. `models/spcx/segments.md` Consumer and Enterprise & Government; `models/spcx/income.md` Connectivity EBIT. `models/spcx/valuation.md` Load-bearing SOTP assigns most of target EV to Connectivity FY2028E EBIT.
- Space remains an R&D hole plus scarce launch capacity. Launch Services revenue is customer Falcon launches only. Starship commercial revenue is zero in every valuation scenario, including bull. `research.md` Starship overlay; `valuation.md` Bear / base / bull assumptions.
- AI is the capex bid. `cashflow.md` AI capex FY2026E–FY2028E; `valuation.md` AI piece is invested-capital conversion with a Customer B haircut, not an FCF multiple.
- Consolidated FCF is negative through FY2027E and approximately zero in FY2028E. `cashflow.md` Free cash flow. The DCF check in `valuation.md` is not load-bearing and still sits well below the SOTP target because the explicit window has no cash.
- Shares are post-Cursor basic. Fully diluted is not obtained. EchoStar is off the base case. Cursor P&L contribution is zero. `balance.md`; `research.md` Model instruction.

## Why this view is right

The statements already show the mix. Q2 Connectivity paid the cash; Q2 AI absorbed it; Q2 Space spent more on R&D than it took in revenue. `register.md` Q2 segment scorecard; `research.md` Node map. The forecast does not reverse that mix by FY2028E: Connectivity still earns, AI still spends, Starship still has no commercial line. `income.md` and `cashflow.md` three-year forecast.

ARPU is a disclosed decline, not a view: $99 FY2023 to $66 Q2 2026. `register.md` Connectivity. The model lets volume still grow and still does not get last sale back except in bull, which needs a 95× Connectivity EBIT exit, 7× AI capital conversion, and a 5% Customer B haircut. `valuation.md` Scenario outputs.

Last sale already prices 40.7× FY2028E revenue and 166.9× FY2028E EBIT against the same model the target uses at 21.0× and 85.9×. `valuation.md` What the last sale already prices. That premium is the variant. It is not a quality story that fails to show up in returns; it is a cash-timing story the workbook dates.

## What others miss or get wrong

- Treating recast FY2023–FY2025 as legacy launch history. Those years include xAI/X common-control combinations. `research.md` What this is.
- Counting total Falcon cadence as launch revenue. Internal Starlink launches have no Space revenue; cost is capitalized into Connectivity satellites. `research.md` Space — Launch Services.
- Booking Starship as a 2026–2028 earnings line. The company stated a H2 2026 payload-to-orbit expectation; the model records that as an expectation, not revenue. Bull still sets Starship revenue to zero.
- Reading AI revenue growth as AI cash. Customer B was 19.5% of consolidated Q2 revenue. Capex on that segment is the residual cash bid. `research.md` AI — Solutions & Infrastructure; `cashflow.md` AI capex.
- Using a Nasdaq-displayed $210 one-year figure as consensus. Constituent estimates were not obtained. `register.md` What is already priced.
- Assuming FCF inflects because IPO cash is large. Cash plus securities at 2026-06-30 funds the bid; `cashflow.md` still burns through FY2027E.

Tracking what is already priced is the whole idea. `memory/spcx/consensus.md`.

## Mechanism and magnitude

Mechanism: last sale capitalizes Connectivity as if ARPU has stabilized, AI as if invested capital already earns a software multiple, and Space as if Starship is a commercial fleet. The SOTP instead capitalizes FY2028E Connectivity EBIT, Space revenue with Starship at zero, and AI capex at a conversion multiple after a Customer B haircut, then discounts that EV to 2027-08-30. `valuation.md` Load-bearing SOTP — base bridge.

Magnitude: the current mixed-date EV premium to base target EV is the line `Current EV premium to base target EV` in `valuation.md`. Bull equity value only recovers last sale. The DCF check, which fades FCF after FY2028E, is lower still and 80.8% terminal. If the tape is right, the miss is in the conversion multiples and Starship-zero, not in a rounding error on FY2028E FCF.

## Killing conditions

Check these on each 10-Q and on the first 10-K (none filed through 2026-08-30).

1. **ARPU and net adds.** If Q3 2026 or FY2026 Starlink ARPU is at or above Q2 $66 and ending lines are on the base path toward 18.0 million then 22.5 million, the consumer cut is not the miss. Kill the ARPU-decline pillar if ARPU rises for two consecutive prints. Source: 10-Q MD&A Key Business Metrics. First check: Q3 2026 10-Q.
2. **Starship commercial line.** If a print discloses Starship payload revenue, or H2 2026 payload-to-orbit arrives with a priced commercial manifest, the zero-revenue overlay is wrong and SOTP Space is too low. First check: Q3/Q4 2026 10-Q MD&A launches and Note 3 disaggregation.
3. **AI cash conversion.** If AI capex / AI revenue falls below 200% and Customer B concentration falls without AI revenue falling, the invested-capital haircut is too harsh. Kill the AI-bid pillar if FY2027E FCF in the live model turns positive on lower AI capex rather than on Connectivity. First check: FY2026 10-K segment Note (or Q4 10-Q if no 10-K yet).
4. **FCF date.** If reported FCF (OCF minus capex, register definition) is positive in FY2026 or the first half of FY2027, the cash-timing claim is dead. First check: FY2026 cash-flow statement.
5. **Multiple paid for Connectivity.** If a primary-source peer EBIT multiple is obtained and sits at or above the base 70× Connectivity exit, the SOTP exit is not aggressive. Kill the “tape is rich vs SOTP” claim only if that peer multiple is obtained and the current EV / FY2028E EBIT no longer stands at a large premium to the target. Check when a 10-K or exchange-derived peer set exists; until then peer multiples remain not obtained.

Do not replace a pillar here. If a kill hits, the next cover revises the same files.
