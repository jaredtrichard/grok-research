# GOLD-RATES — 3y real-rate / Fed path

| Field | Value |
| --- | --- |
| Id | GOLD-RATES |
| Kind | scout (rates only) |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Horizon | 3 years, to 22 Aug 2029 (same as GOLD-METAL) |
| Sector | Gold |
| Official view | `/home/box/agent-data/grok-research/views/GOLD-METAL.md` stays **current** |
| Deck move? | **No.** Does not move **4,900 / 5,900 / 3,900**. TIPS gate stays Bar B. |
| Not this report | 3y S/D rebuild (tabled). No name ratings. `names.stage` stays watch. No ship. |

## Decision for GOLD-METAL

The sourced 3y **policy** path is **hold-to-slightly-higher through 2026, then a slow glide (desks / SEP) or a still-hiked 2027 (CME)**. That is the same regime GOLD-METAL already priced: **10y real at 2.40, no delivered flip**.

| Question | Number | Moves the deck? |
| --- | --- | --- |
| Spot 10y real, 21 Aug | Treasury **2.40%** (FRED DFII10 **2.35%** 20 Aug) | No — already the view input |
| 10y real 4 Aug / SOY | **2.40%** / **1.94%** (2 Jan) | No — already Jefferies / view |
| 10y real 3y-out | **UNSOURCED.** No Treasury / FRED TIPS forward, no 5y5y real series, no desk 2028–29 TIPS card | Do **not** invent. Do not change the 3y gold band off an invented TIPS |
| Funds today | **3.50–3.75%** (July FOMC; UBS 13 Aug) | Consistent with hike-risk, not cuts |
| CME implied YE 2026 | Hold Sept **63.8%** / hike **36.2%**; **≥1 hike by Dec ~67%** (FXBus, CME FedWatch 21 Aug) | Confirms the **cap**, does not raise gold to bull |
| SEP June 2026 median funds | YE26 **3.8** / YE27 **3.6** / YE28 **3.4** / longer-run **3.1** | ~one 25bp hike then **40bp** of ease by YE28. Not a 2024-style cut cycle |
| Desk 2027 | UBS hold 2026, ease 2027; GS two 25bp Jun+Dec 2027 to **3.00–3.25** terminal | Easing, if it comes, is **late and small** |
| TIPS gate | Bar B: *hold* below 21 Aug **2.40**, not a one-day 2.35 | Unchanged |

**Leave GOLD-METAL current.** No view rewrite. No adversarial pass on the view (nothing changed).

Why the numbers do not migrate the gold deck:

- **Bull ($5,900)** needs a *sustained* 10y-real decline from **2.40** *and* Western ETF tonnes in. CME still prices **hike risk into 2027**. SEP/UBS/GS ease, if any, is **2027–28 and 25–50bp**, not a TIPS collapse toward SOY **1.94**. That is not the bull gate.
- **Bear ($3,900)** as *base* needs 10y real **a new high above 2.44 and still rising**. Treasury 17 Aug **2.44** was the local high in the August extract; 21 Aug is back at **2.40**. Curve is **upward-sloping**, not a new real-rate shock from here.
- **Base ($4,900)** already assumed this: structurally bid, cyclically capped until TIPS *hold* lower. The rates path **is** that cap.

## 1. Treasury par real curve (primary)

Source: [Daily Treasury Par Real Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202608&type=daily_treasury_real_yield_curve), August 2026 extract. R-CMT, 5/7/10/20/30.

| Date | 5 YR | 7 YR | 10 YR | 20 YR | 30 YR |
| --- | ---: | ---: | ---: | ---: | ---: |
| 03 Aug 2026 | 2.17 | 2.29 | 2.43 | 2.78 | 2.99 |
| 04 Aug 2026 | 2.14 | 2.26 | **2.40** | 2.75 | 2.96 |
| 17 Aug 2026 | 2.13 | 2.27 | **2.44** | 2.84 | 3.06 |
| 19 Aug 2026 | 2.07 | 2.19 | 2.35 | 2.72 | 2.94 |
| 20 Aug 2026 | 2.05 | 2.18 | 2.35 | 2.73 | 2.95 |
| **21 Aug 2026** | **2.09** | **2.23** | **2.40** | **2.78** | **3.00** |

SOY (already in GOLD-METAL-3Y source pack / Jefferies): **2 Jan 2026 10 YR = 1.94%**.

Read: August 10y real is a **2.35–2.44 box**. Friday **2.40** is **not** a rollover. The real curve is **upward sloping** (5y **2.09** → 30y **3.00**). That is a **term-premium / long-end real** story, not a 5y collapse.

FRED **DFII10 = 2.35%** on **20 Aug 2026** (21 Aug not on FRED in the 3Y pack). Same neighbourhood, 5bp below Treasury par real.

Nominal 10y Treasury **4.74%** on 21 Aug (TE 4.74 / 4.7360). Spot BEI ≈ **2.34 pp**. Not a TIPS forward.

## 2. TIPS forwards — UNSOURCED

Checked for a **published** TIPS forward / 5y5y real / 10y10y real (Treasury, FRED). **None used.**

Do **not** back out `(2 × 10y − 5y)`. That would be **2.71%** on 21 Aug and is **not a published series**. GOLD-METAL already flags: *any other TIPS band / 2028–29 TIPS forecast is not a sourced 3y path — not used.*

**3y 10y-real path for models: stay at the live print (2.40) until a new sourced hold or a new high. No 2029 TIPS number.**

## 3. Fed funds — today and implied

**Today:** target **3.50–3.75%**. UBS (13 Aug / Warsh-era note): July FOMC left rates unchanged at that range; three hawkish dissents; Chair Warsh “watchful thinking.” Fifth consecutive hold.

**SEP, 17 Jun 2026** ([FOMC projections](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm)):

| | 2026 | 2027 | 2028 | Longer run |
| --- | ---: | ---: | ---: | ---: |
| Median funds | **3.8** | **3.6** | **3.4** | **3.1** |
| March median | 3.4 | 3.1 | 3.1 | 3.1 |
| Central tendency | 3.6–4.1 | 3.1–3.9 | 3.1–3.6 | 3.0–3.5 |
| Range | 3.4–4.4 | 2.9–4.4 | 2.9–3.9 | 2.9–3.9 |

June dots **hiked the path** vs March (+40 / +50 / +30bp on the medians). Median PCE **3.6** in 2026, **2.3** in 2027. Chair Warsh **did not submit** a 2026 projection (FRED blog / UBS). Next SEP: **16 Sep 2026**.

**CME FedWatch, 21 Aug 2026** (FXBus 06:12 UTC 21 Aug; Gate recap 20 Aug ET). Primary tool: [CME FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html).

| Meeting | Hold (3.50–3.75) | +25bp | +50bp | Note |
| --- | ---: | ---: | ---: | --- |
| 16 Sep 2026 | **63.8%** | **36.2%** | — | FXBus / Gate |
| 28 Oct 2026 | 51.8% | 41.4% | 6.8% | FXBus |
| Dec 2026 | 32.8% hold | **≥1 hike ~67.2%** | | FXBus YE line |

A third-party CME-method table (kryptomagazin terminal, same 3.50–3.75 starting bin) still has the **modal bin at 3.50–3.75 through mid-2027**, with mass migrating into **3.75–4.00** by Dec 2026–Jan 2027. That is **hike-biased**, not a cut path. **Use FXBus/Gate for the 21 Aug point estimates; do not treat the third-party 2027 grid as CME-primary.**

Implied (desk arithmetic on the FXBus Sept row only): **~36%** of a 25bp hike in September. Not a cut.

## 4. Named desk rates views (not gold cards)

| Desk | Date | Path | Source |
| --- | --- | --- | --- |
| **Jefferies** | 4 Aug 2026 | TIPS **~2.41 vs SOY 1.94**. “Rate markets biased toward tighter policy, **implied rates rising into 2027**, hike probabilities elevated.” Direction of real-rate *expectations* > level. Hormuz resolution could flip it. | [Kitco 4 Aug](https://www.kitco.com/news/article/2026-08-04/gold-can-recover-despite-higher-real-yields-rate-pressures-ease-says) |
| **UBS GWM** | 13 Aug 2026 (Warsh-era note) | Hold **rest of 2026**. “Slower growth and disinflation 2H should support a pivot toward **lower policy rates in 2027**.” Market hike conviction “somewhat too aggressive.” | [UBS](https://www.ubs.com/us/en/wealth-management/insights/market-news/article.3600907.html) |
| **UBS (June vintage)** | ~15 Jun 2026 | Cut path **pushed to Mar + Jun 2027** (was Dec 2026 + Mar 2027). | IDN / Reuters recap — **secondary**; 13 Aug note is the live UBS |
| **Goldman Sachs** (Mericle) | 9 Jun 2026 | **No cuts 2026.** Two 25bp in **Jun + Dec 2027** to terminal **3.00–3.25**. Hike odds **20%**. | [GS](https://www.goldmansachs.com/insights/articles/why-the-fed-is-unlikely-to-cut-rates-this-year) |
| **JPM** (Feroli) | post-July 2026 FOMC | **+25 Dec 2026**, then hold **3.75–4.00**. Pulled forward from 2H 2027. | [JPM](https://www.jpmorgan.com/insights/global-research/economy/fed-rate-cuts) |
| **BofA** (Bhave) | 22 Jun 2026 | Three **+25** Sep/Oct/Dec → **4.25–4.50**. 9 Aug: Sep still on the table; slip risk to Dec+. **June vintage.** | IBKR Campus recap |
| **Citi** | 9 Aug 2026 | Softer inflation would **rule out a Sep hike**. No full 2026–27 Citi ladder after that date. | Gate / Reuters wrap |
| **FOMC SEP** | 17 Jun 2026 | **3.8 / 3.6 / 3.4 / 3.1** | Fed primary |

Cluster: **UBS/GS = hold 2026, 25–50bp of ease in 2027 toward ~3.0–3.4**. **JPM = +25 Dec then hold 3.75–4.00**. **BofA June = three hikes to 4.25–4.50** (stale vs 21 Aug 36% Sept). **Market = hike risk 2026–27**. **Nobody is marking 2024-style 150–200bp of cuts.** **Nobody printed a 2028–29 TIPS.**

## 5. Rival rate paths (steelman, then numbers)

A view is not done if a rival rate path is unexamined. These are **rate** rivals. None of them move **4,900 / 5,900 / 3,900** without a **new TIPS print**.

| Rival | What would have to be true | What the tape says | Winner |
| --- | --- | --- | --- |
| **R1. Deep-cut 2027 (TIPS back toward 1.94, gold bull)** | Funds glide **>100bp** and 10y real *holds* toward SOY **1.94**; Western ETFs flip in | SEP eases **40bp** by YE28. GS **50bp** in 2027. CME still **hike-biased**. TIPS **2.40**, not 1.94 | **Loses.** Would be GOLD-METAL **bull** if it printed. It has not |
| **R2. Hiking cycle / TIPS >2.44 and rising (gold bear as base)** | Another 50–75bp of hikes *and* 10y real holds **above 2.44** | 17 Aug **2.44** failed to hold. 21 Aug **2.40**. Sept hike only **36%** | **Loses as base.** It is the **bear migrate** if it prints (already in GOLD-METAL invalidation) |
| **R3. TIPS no longer prices gold, so this whole report is the wrong gate** | Gold makes a new ATH while 10y real stays ≥2.40 and ETFs stay out | Q2 2026: TIPS up, gold **−8%** q/q, NA ETFs **−$7.7bn**. WGC 30 Jul: NA ETF demand **resumed its negative relationship with US 10y TIPS** | **Loses on 2026 tape.** Same as GOLD-METAL rival 3. Rates path does not reopen it |
| **R4. Market-implied 2027 hike is the 3y mean (mark gold down)** | CME 2027 mass in 3.75–4.25 becomes *realized* and TIPS trends **up** from 2.40 | Possible. Not the **spot**. Desks + SEP still ease 2027–28. 10y real is **flat in a 9bp August box**, not trending up | **Does not win today.** If 10y real **>2.44 and rising**, GOLD-METAL already migrates bear. No pre-emptive deck cut |

## 6. What this does / does not do in the names

GOLD-METAL sleeve rule is unchanged: **royalty-plus-seniors until TIPS *hold* below 2.40 and Western ETFs are in**. Leftover-torque still loses on **$4,500** cost decks vs a **$4,900** 3y midpoint that is **not** a new January ATH.

A GS/UBS 2027 **ease** is a **watch item for Bar B**, not a reason to own leftover torque now. CME **hike risk** is why the 12m check-in stays **$4,500**, not **$5,200**.

## Sources

1. Treasury Daily Par Real Yield Curve, Aug 2026 (21 Aug 5/7/10/20/30 = 2.09 / 2.23 / **2.40** / 2.78 / 3.00).
2. FRED DFII10 **2.35%** 20 Aug 2026 (prior pack).
3. FOMC SEP 17 Jun 2026, `fomcprojtabl20260617.htm`. Median funds **3.8 / 3.6 / 3.4 / 3.1**.
4. CME FedWatch via FXBus 21 Aug 2026 06:12 and Gate 20 Aug recap. Tool: cmegroup.com FedWatch.
5. Jefferies via Kitco 4 Aug 2026 (TIPS 2.41 vs 1.94; implied rates rising into 2027).
6. UBS GWM Warsh-era note, 13 Aug 2026 (hold 2026, ease 2027; funds 3.50–3.75).
7. Goldman Sachs Research / Mericle, Jun 2026 (no 2026 cuts; Jun+Dec 2027 25bp; terminal 3.00–3.25).
8. GOLD-METAL current view (22 Aug 2026) and GOLD-METAL-3Y TIPS/DXY pack.

**Gaps (do not fill):** published TIPS forwards; official 21 Aug LBMA/COMEX (still missing); 2028–29 TIPS or funds *point* from a desk; SOFR 3y strip as a separate table (FedWatch is the funds future).
