# SpaceX working thesis

as_of: 2026-08-30
task: GF-SPCX-1, send-back
name_id: spcx
ticker: SPCX

If the model does not say it, it is not here. Numbers live in `models/spcx/`. This file is the claim those numbers make.

## Claim

The base case now carries Starship commercial revenue, Cursor P&L, and the pending EchoStar deal as labeled `[VIEW]`s, not as zeros. The 12-month base price target is the line `12-month base price target` in `models/spcx/valuation.md`. Last sale $141.50 (Nasdaq lastTradeTimestamp 2026-08-27) still sits above that target. Bull in the same file is above last sale; bear is a cut on cadence, Cursor, ARPU, and multiples. No rating.

The investment idea is the remaining gap: even after putting the omitted lines into base the way the tape treats them as real, the SOTP of this workbook still does not reach last sale. The tape is paying for more Starship cadence, more AI/Cursor conversion, and less dilution than the base views.

## What the model says

Point, do not recopy.

- Starship commercial is a base overlay, not a filing line. `models/spcx/segments.md` Starship commercial flights and assumed revenue per flight. FY2026E–FY2028E revenue path is in that file; FY2028E base is 50 flights at $140 million per flight. Bear keeps a non-zero 10-flight path. `valuation.md` Load-bearing SOTP values Space as launch plus Starship revenue.
- Cursor P&L is a base `[VIEW]` from H2 2026, not back-cast into Q2. Revenue/EBIT path is in `segments.md`; FY2028E base EBIT is the Cursor piece of `valuation.md` SOTP at a 40× EBIT exit. No synergy premium.
- EchoStar is pending and in base: 261.8 million Class A shares, equity plus cash consideration, spectrum on the balance sheet, and a spectrum/mobile revenue overlay in Connectivity. `balance.md` share bridge; `segments.md` Pending EchoStar spectrum/mobile revenue. Closing remains pending.
- Connectivity remains the cash engine. ARPU is still a disclosed decline. `register.md` Connectivity; `segments.md` ending subscribers and ARPU.
- AI core capex is still the residual cash bid. Customer B concentration remains a named haircut on the AI invested-capital piece. `cashflow.md` AI capex; `valuation.md` AI core.
- Consolidated FCF is still negative through FY2027E and turns positive in FY2028E. `cashflow.md` Free cash flow. The DCF check is not load-bearing.
- Share count in the target is post-Cursor plus pending EchoStar basic shares. Fully diluted is not obtained.

## Why this view is right

Filings omit Starship commercial revenue, Cursor contribution, and EchoStar close. The captain send-back is that the stock is not valued at those zeros. The workbook now prices them as `[VIEW]`s with named cadence, price, Cursor scale, and pending share/cash/spectrum. `segments.md` Explicit forecast drivers; `valuation.md` Bear / base / bull assumptions.

After that inclusion, last sale still prices a premium to base target EV on the same FY2028E denominators. `valuation.md` What the last sale already prices. Bull only clears last sale if Starship goes to 100 flights at $160 million, Cursor to $8,000 million revenue at 25% EBIT, Connectivity to 95× EBIT, and AI conversion to 7× with a 5% Customer B haircut. That is the tape's implied stack, not the base.

ARPU $99 FY2023 to $66 Q2 2026 is still a fact. Volume can grow in base and the target still does not match last sale. The miss, if the tape is right, is Starship cadence, Cursor conversion, and exit multiples, not a forgotten zero.

## What others miss or get wrong

- Treating omitted filing lines as zero enterprise value. This cover does not. Starship, Cursor, and EchoStar sit in base as views.
- Treating recast FY2023–FY2025 as legacy launch history. Those years include xAI/X common-control combinations. `research.md` What this is.
- Counting total Falcon cadence as launch revenue. Internal Starlink launches still have no Space revenue.
- Reading AI revenue growth as AI cash. Capex on that segment is still the residual bid; Customer B was 19.5% of consolidated Q2 revenue.
- Dropping EchoStar dilution because close is pending. Base share count includes the 261.8 million contemplated Class A shares. `valuation.md` Price target share line.
- Using a Nasdaq-displayed $210 one-year figure as consensus. Constituent estimates were not obtained. `register.md` What is already priced.

Tracking what is already priced is still the idea. `memory/spcx/consensus.md`.

## Mechanism and magnitude

Mechanism: SOTP capitalizes FY2028E Connectivity EBIT (including the pending spectrum/mobile overlay), Space revenue including Starship commercial, AI invested capital after a Customer B haircut, and Cursor EBIT, then discounts to 2027-08-30. `valuation.md` Load-bearing SOTP — base bridge.

Magnitude: the current mixed-date EV premium to base target EV is the line `Current EV premium to base target EV` in `valuation.md`. Compared with the pre-send-back cover, the gap narrowed because zeros were replaced with views; it did not close. If the tape is right, raise Starship flights and Cursor conversion before raising Connectivity's already-high EBIT exit.

## Killing conditions

Check these on each 10-Q and on the first 10-K (none filed through 2026-08-30).

1. **ARPU and net adds.** Kill the ARPU-decline pillar if ARPU rises for two consecutive prints. Source: 10-Q MD&A Key Business Metrics. First check: Q3 2026 10-Q.
2. **Starship commercial cadence.** Base FY2028E is 50 commercial flights at $140 million assumed revenue per flight. If a print discloses commercial Starship revenue or a priced manifest that implies a run-rate above that view, Space SOTP is too low. If H2 2026 payload-to-orbit slips with no commercial flights in FY2027, the view is too high. First check: Q3/Q4 2026 10-Q MD&A launches and Note 3.
3. **Cursor P&L.** Base FY2028E is $5,000 million revenue and $750 million EBIT. If post-close disclosure shows a run-rate far above or below that view, reset the Cursor SOTP piece. First check: first 10-Q that disaggregates or MD&A-discusses Cursor.
4. **EchoStar close or break.** If the pending deal closes on the contemplated share and cash split, the base treatment stands. If it breaks, drop the 261.8 million shares, the cash, the spectrum asset, and the mobile overlay. First check: 8-K on close or termination.
5. **FCF date.** If reported FCF (OCF minus capex) is positive in FY2026, the cash-timing claim is dead. First check: FY2026 cash-flow statement.
6. **Tape vs SOTP.** Kill “last sale still rich to this SOTP” only if a primary-source peer multiple is obtained and current EV / FY2028E EBIT no longer stands at a premium to the target. Until then peer multiples remain not obtained.

Do not replace a pillar here. If a kill hits, the next cover revises the same files.
