# KGC — official view (equity)

| Field | Value |
| --- | --- |
| Id | **KGC** |
| Kind | official view (equity) |
| Status | **current** — KGC-HOUSE. Official 3y **$37 / $58 / $21** on hist k **6.18× / 7.68× / 4.67×**. FCF $44 FLAG. Stage **watch**. |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Ticker | NYSE:**KGC** / TSX:**K** |
| Stage | **watch** — no ship, no live trade, no recommendation, no restage. Watch / no-add is **stage/behavior**, not the midpoint. The midpoint is a **dollar**. |
| Gold path | `/home/box/agent-data/grok-research/views/GOLD-METAL.md` — **current**. Cite only. **This file does not edit it.** Official 3y: **4,900 / 5,900 / 3,900**. 12m **4,500** check-in only. |
| Scout | `/home/box/agent-data/grok-research/reports/KGC-SCOUT.md` |
| Kit | `/home/box/agent-data/grok-research/reports/HOUSE-MODEL.md` |
| Model store | `/home/box/agent-data/grok-research/models/KGC/` — `segment.csv`, `is.csv`, `bs.csv`, `cf.csv`, `valuation.csv`, `tie.csv`, `multiples.csv` |
| Horizon | **3 years to 22 Aug 2029**. Clock = **3y run-rate + path** (company 2026–28 guide is already 2,000 attrib. GEO each year). Not a 2029 volume model. |
| Constraints | No ship. No live trade. `names.view_ref` = this file. GOLD-METAL.md **not** modified. Stage stays **watch**. Official PT = EV/EBITDA on **KGC historical k** (base=mid of FY2022–25 adj range, bull=high, bear=low). **Not** flat 7×. **Not** 8% FCF as the mid. FCF yield is a **check**. |

## Thesis

Kinross is a **watch-stage senior** marked on a **3-year high-plateau gold line**. Official metal is **3y base $4,900**. Official equity mid is **EV/EBITDA**: segment-IS **E $6,750m** (labelled computed) × **6.18×** (mid of FY2022–FY2025 impairment-adjusted EV/EBITDA) plus **$1,917.6m** net cash, over **1,186.2m** shares → **$37** (exact **$36.78**). Bull **$58** (E $8,650m × 7.68×). Bear **$21** (E $4,850m × 4.67×). Friday’s **$32.76** tape sits **~$4 / ~12% under** the $37 mid. Stage stays **watch**.

FCF-yield at 8.0% residual-risk is a **check** only: **$44** (exact $44.42) at $4,900. **FLAG:** $44.42 vs official EV mid $36.78 is **+20.8%** — do **not** average. Tape vs the FCF check is a **~11.0% implied FCF yield**. Tape-implied k on official E is **5.47×** ((32.76×1,186.2 − 1,917.6) / 6,750).

Official mid = **company guide**: **2,000 attrib. GEO**, COS **$1,360**, AISC **$1,730 ±5%**, capex **$1.50bn ($450m / $1.05bn)**, cash tax **$1,125m**, **+$5 COS** and **+$16m tax per +$100 Au**. Country ounces: US **685** / Brazil **600** / Mauritania **505** / Chile **210**. Site COS guides: Tasiast **$1,050**, Paracatu **$1,240**. Manh Choh **70%** already inside US 685. **No Great Bear / Lobo ounces in the mid.**

Do **not** officialize **2× 1H FCF $1,564.3m** ($3,128.6m). 1H attrib. capex was **$685m** vs FY **$1,500m**; 1H cash tax **$775.5m** vs FY **$1,125m**. The hedge for the miss lives in a **labelled node** (US 685 / RM COS **$3,360** / FY AISC outside ±5%), **not** in the mid. 1H AISC **$1,777** is **inside** the $1,644–$1,817 band; Q2 **$1,821** is **outside**.

The **3-year residual** is three clocks:

1. **Tasiast fiscal / political** — 505 koz / **25%**; 1H withholding **$87.5m** “mainly from Mauritania.” This is why the FCF-**check** bucket is **8.0% residual-risk**, not AEM 5% and not quality-neutral 6.5–7.0%.
2. **US AISC / volume** — H2 catch-up after RM/BM Q2 **−49%** YoY GEO; RM COS **$3,360**; US guide **685** vs 1H attrib. **290**.
3. **Great Bear late-2029 clock** — Canada is **2029+**, **not** 2026–28 ounces. First gold **late 2029** is **YE 2025 colour**. Construction capex vs 2024 PEA **$1.429bn** is **UNSOURCED**.

Stage stays **watch / no add**.

## Official gold input (GOLD-METAL current — copy, do not retune)

| Scenario | Band (US$/oz) | Midpoint for models | Horizon |
| --- | --- | --- | --- |
| **3y Base** | **4,400–5,400** | **$4,900** | 3y to 22 Aug 2029 |
| **3y Bull** | **5,400–6,400** | **$5,900** | 3y |
| **3y Bear** | **3,400–4,400** | **$3,900** | 3y |
| *12m check-in* (not official) | *4,400–5,000* | *$4,500* | *12m to 22 Aug 2027* |

**Metal invalid up:** official hold **>$5,400** + 10y real **hold below 2.40** + Western ETF **in**. **Metal invalid down:** official breaks **$4,400** toward **$4,000** with TIPS **≥2.40** and at least one listed companion. A print in **$5,000–$5,400 without** the two bull gates **stays metal base**. Kitco **$4,602.40** / TE **$4,607.35** (21 Aug) is tape, **not** the forward line.

## Official 3y equity deck

**Captain (KGC-HOUSE):** official PT is **EV/EBITDA using Kinross’s historical multiple range**. Base = **mid of that history**, bull = **high**, bear = **low**. Not a flat 7.0×. Not 8% FCF yield as the mid.

| Input | Print | Status |
| --- | --- | --- |
| E = segment IS constructed op. EBITDA | **$6,750m** at $4,900 (**$8,650 / $4,850** bull/bear) | **computed, labelled.** `sales − COS(G) − G&A − AISC-other`. Same cells as the IS table (4,850 / 5,990 / **6,750** / 8,650). Company “adj. EBITDA” string still **UNSOURCED** (Q2 NR count 0). Captain: computed E from segment IS is OK if labelled. |
| k = historical EV/EBITDA | **4.67× / 6.18× / 7.68×** (bear / base / bull) | **sourced.** Window **FY2022–FY2025** continuing ops, as-of **22 Aug 2026**. k = YE EV / E_adj. E_adj = OE + DDA − reversals + charges (impairment years **flagged, not dropped**). Base = **mid of min/max**, not the mean (mean adj **5.79×**; median **5.41×**). |
| Official 3y $/sh | **$37 / $58 / $21** | **current.** PT = (E × k − net debt) / shares. Net cash **$1,917.6m**. Shares **1,186.2m**. Exact **$36.78 / $57.62 / $20.71**. |

**k build** (`models/KGC/history.csv`):

| FY | OE | DDA | Imp. | E_adj | YE EV | k_adj | In range |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2020 | 1,899.4 | 842.3 | −650.9 rev | 2,090.8 | 9,949 | 4.76 | **no** — Russia + reversal |
| 2021 | 463.6 | 840.9 | +144.5 | 1,449.0 | 8,328 | 5.75 | **no** — as-reported includes Russia |
| 2022 | 117.7 | 784.0 | +350.0 | 1,251.7 | 7,172 | **5.73** | yes (RM charge) |
| 2023 | 801.4 | 986.8 | +38.9 | 1,827.1 | 9,309 | **5.09** | yes |
| 2024 | 1,540.3 | 1,147.5 | −74.1 rev | 2,613.7 | 12,218 | **4.67** | yes — **low** |
| 2025 | 3,277.6 | 1,105.0 | −116.1 rev | 4,266.5 | 32,783 | **7.68** | yes — **high** |

YE EV = issued-and-outstanding × NYSE YE close + total debt − cash. Closes: 2020 **$7.34** / 2021 **$5.81** / 2022 **$4.09** / 2023 **$6.05** / 2024 **$9.27** / 2025 **$28.16** ([wallstreetnumbers KGC YE](https://wallstreetnumbers.com/stocks/kgc/price) fetched 22 Aug 2026; Yahoo 31 Dec 2025 close **$28.16**). OE/DDA/cash/debt/shares from company YE FS (q4cdn). Unadj (impairments left in E) 2022–25 range is **4.55×–7.95×**, mid **6.25×** — sensitivity, not the official k. Vendor Alpha Spread 3y/5y avgs **5.6× / 5.7×** are **not** the range.

**Why FY2022–25, not 2020–21:** current franchise is continuing ops post-Russia. 2020–21 are **sourced** in `history.csv` and excluded from the official min/max so a Russia-year or a $651m reversal does not set bear/bull k. n=4 is thin; stated.

**PT arithmetic (official):**

`$/sh = (E(G) × k − (−1,917.6)) / 1,186.2`

| Case | Gold | E $m | k | EV $m | + net cash | $/sh exact | **Card** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bear | 3,900 | 4,850 | 4.67 | 22,650 | 24,567 | 20.71 | **$21** |
| Base | 4,900 | 6,750 | 6.18 | 41,715 | 43,633 | 36.78 | **$37** |
| Bull | 5,900 | 8,650 | 7.68 | 66,432 | 68,350 | 57.62 | **$58** |

`models/KGC/history.csv` is the source table. FCF-yield table below is a **check only**.

### Check only — FLAG table (not official; do not average)

HOUSE-MODEL: a second identity more than **20%** from the official mid is a **FLAG**, not a blend.

| Rival (check) | k or yield | $/sh @ $4,900 | vs official $36.78 |
| --- | --- | ---: | --- |
| Official EV (FY22–25 adj mid) | 6.18× | **$36.78 → $37** | — |
| FCF 8% residual-risk | 8.0% | **$44.42 → $44** | **+20.8% FLAG** |
| Flat 7× on constructed E | 7.0× | $41.46 → $41 | +13% |
| Quality-neutral FCF 6.5% / 7.0% | 6.5–7.0% | $54 / $51 | +48% / +39% |
| Mean / median adj k | 5.79× / 5.41× | $34.56 / $32.40 | −6% / −12% |
| Vendor 3y / 5y avg | 5.6× / 5.7× | $33.48 / $34.05 | −9% / −7% |
| Tape-implied k | 5.47× | $32.76 | tape |
| Unadj range mid | 6.25× | $37.18 | ~same card |
| 2020–25 min k_unadj (out of window) | 3.63× | $22.27 | bear-ish; not official k |

### Stage / behavior (not the midpoint)

| Gold case | Stage / behavior |
| --- | --- |
| 3y base $4,900 | **watch / no add** |
| 3y bull $5,900 | **add torque only if metal invalid-up prints AND US H2 catch-up (RM COS not stuck $3,360)** |
| 3y bear $3,900 | **cut-watch if gold invalid-down OR Tasiast fiscal/political OR AISC stays ≥$1,821 with gold ≤$4,400** |

## FCF at four golds (guide build — not 2× 1H)

**Company FCF definition (YE/Q2 recon):** attrib. FCF = CFO − attrib. capital expenditures − NCI share of OCF.

**NCI FY OCF = UNSOURCED** (1H implied ~$36m from 2,285.4 − 685.1 − 1,564.3; **not 2×’d**). Dropped from the mid.

**Official FCF identity (every gold):**

`FCF(G) = 2,000 koz × (G − AISC(G)) / 1,000 − T(G) − $1,050m`

- `AISC(G) = 1,730 + 5 × (G − 4,500) / 100`  (guide mid + royalty factor on COS, which sits inside AISC)
- `T(G) = 1,125 + 16 × (G − 4,500) / 100`  (cash-tax guide)
- **$1,050m** = guided attrib. **growth** capex (sustaining **$450m** is already inside AISC)
- Algebra check: `CFO(G) = FCF(G) + 1,500` and `CFO = 2,000×(G−AISC)/1000 + 450 − T`

**+$174m FCF / +$100 Au** = 2,000 × ($100 − $5 royalty) − $16m cash tax.

| Gold | COS $/GEO | AISC $/GEO | Cash tax $m | FCF $m | CFO $m | After-sustaining FCF $m (alt.) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **3,900** | 1,330 | 1,700 | 1,029 | **2,321** | 3,821 | 3,371 |
| *4,500* | 1,360 | 1,730 | 1,125 | **3,365** | 4,865 | 4,415 |
| **4,900** | 1,380 | 1,750 | 1,189 | **4,061** | 5,561 | 5,111 |
| **5,900** | 1,430 | 1,800 | 1,349 | **5,801** | 7,301 | 6,851 |

1H printed attrib. FCF **$1,564.3m** is a **historical**. **2× = $3,128.6m is FLAG, not official.** Guide-built FY at the $4,500 deck is **$3,365m** — in the same neighbourhood, but the 1H print is capex-light and tax-heavy vs the FY guides.

## Per-segment map (then sum)

Country 2026 attrib. GEO ±5% and COS from YE 2025 PR (not re-split in Q2). Royalty **+$5/GEO per +$100** applied to each country COS (group factor; labelled allocation). Manh Choh **70%** already in US **685**. GB / Lobo **0 oz**.

**At $4,900** (US$m except oz / COS):

| Segment | Own | GEO koz | COS $/GEO | Rev | COS $ | Capex (S+X) | Cash margin | FCF pre-corp |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Tasiast (Mauritania) | 100% | **505** | 1,070 | 2,474.5 | 540.4 | 80+195=275 | 1,934.2 | 1,659.2 |
| Paracatu (Brazil) | 100% | **600** | 1,260 | 2,940.0 | 756.0 | 190+45=235 | 2,184.0 | 1,949.0 |
| La Coipa (Chile) | 100% | **210** | 1,340 | 1,029.0 | 281.4 | 40+50=90 | 747.6 | 657.6 |
| United States attrib | FK 100% / MC **70%** / RM 100% / BM 100% | **685** | 1,720 | 3,356.5 | 1,178.2 | 140+500=640 | 2,178.3 | 1,538.3 |
| Canada and other (GB / Lobo / corp) | 100% | **0** | n/a | 0 | 0 | 0+260=260 | 0 | −260.0 |
| Group COS recon | — | — | — | — | **+4.05** | — | −4.05 | — |
| **Sum → group** | | **2,000** | **1,380** | **9,800** | **2,760** | **1,500** | **7,040** | — |

Country-weighted COS at the $4,500 deck is **$1,357.975** vs official group **$1,360**. Recon **$4.05m** is **computed** so the segment sum **ties** to the official COS guide. Not a silent plug.

Corporate (not in segment FCF): G&A **$135m** (sourced) + AISC-other ex-G&A ex-sust-capex **$155m** (computed: (AISC−COS)×2.000 − 450 − 135) + cash tax **$1,189m** at $4,900.

AISC−COS stays **$370/GEO** when both move +$5 (royalty), so AISC adders stay **$740m** ($450 S + $135 G&A + $155 other).

`FCF = 7,040 − 740 − 1,189 − 1,050 = 4,061`

Same as `2,000 × (4,900 − 1,750) / 1,000 − 1,189 − 1,050 = 6,300 − 2,239 = 4,061`. Sustaining capex is **inside** the $740 AISC adder, so the only extra deduct after (G−AISC)×Q is cash tax and **growth** capex. Tie.

## Three statements (attrib. 3y run-rate, US$m)

Units US$m. Gold nodes **3,900 / 4,500 / 4,900 / 5,900**. Full cells + status in the CSVs.

### Income statement

| Line | $3,900 | $4,500 | **$4,900** | $5,900 | Status | Source / formula |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| Metal sales | 7,800 | 9,000 | **9,800** | 11,800 | computed | 2,000 × G |
| Production COS | 2,660 | 2,720 | **2,760** | 2,860 | computed | 2,000 × COS(G) |
| G&A | 135 | 135 | **135** | 135 | sourced | YE PR $135m |
| AISC other (ex G&A, ex S) | 155 | 155 | **155** | 155 | computed | $370/GEO × 2,000 − $450 − $135 |
| DD&A | 1,100 | 1,100 | **1,100** | 1,100 | computed | $550/oz × 2,000 (YE PR) |
| Operating earnings | 3,750 | 4,890 | **5,650** | 7,550 | computed | sales − COS − G&A − AISC other − DD&A |
| Interest expense (P&L) | 30 | 30 | **30** | 30 | computed | YE PR $60m incurred, half capitalized |
| EBT | 3,720 | 4,860 | **5,620** | 7,520 | computed | op. earnings − $30 |
| Tax (cash-tax guide) | 1,029 | 1,125 | **1,189** | 1,349 | computed | $1,125 + $16 per +$100 vs $4,500 |
| NI (attrib. model) | 2,691 | 3,735 | **4,431** | 6,171 | computed | EBT − cash-tax guide |
| Company adj. EBITDA | — | — | — | — | **UNSOURCED** | no print; **dropped from mid** |
| Constructed op. EBITDA (official E) | 4,850 | 5,990 | **6,750** | 8,650 | computed | sales − COS − G&A − AISC other. **Labelled computed. Official E** (captain: segment IS OK). Company adj. string still UNSOURCED. |

Other opex guide **$125–150m** and exploration & BD **$220m** are **sourced** as FY guides. Their **sustaining** slice is already in AISC other. Incremental **non-sustaining** expensed vs capitalized split is **UNSOURCED** — **not added again**. Accretion FY **UNSOURCED** (1H $23.7m not 2×’d). NCI FY NI **UNSOURCED**. ETR guide **28–33%** (mid 30.5%) is a **check**, not a second tax.

### Balance sheet (simplified debt)

**Snapshot 30 Jun 2026 (sourced unless noted):**

| Line | US$m | Status | Source |
| --- | ---: | --- | --- |
| Cash | **2,656.4** | sourced | Q2 MD&A / NR |
| Current assets | 4,241.7 | sourced | Q2 MD&A |
| Total assets | 13,596.6 | sourced | Q2 MD&A |
| Non-cash assets | 10,940.2 | computed | 13,596.6 − 2,656.4 |
| Current liabilities | 1,466.6 | sourced | Q2 MD&A |
| LT debt | **738.8** | sourced | senior notes 2033/2041 carrying |
| Total liabilities | 3,822.0 | sourced | Q2 MD&A |
| **Net cash** | **1,917.6** | computed | **2,656.4 − 738.8** |
| Common equity | 9,653.3 | sourced | Q2 MD&A |
| NCI equity | 121.3 | sourced | Q2 MD&A |
| Available credit | 1,708.1 | sourced | Q2 MD&A |
| ST debt | 0 | sourced | carrying debt is entirely LT notes |
| Leases in net debt | — | **UNSOURCED** | company net cash is cash − LT debt; not added |

**Tie check 1 — net cash:** 2,656.4 − 738.8 = **1,917.6**. Holds.

Model-year **ending** cash (computed; **not** the PT denom): `2,656.4 + FCF × (1 − 0.40)` using the 2026 **40% FCF-return policy**. At $4,900: **$5,093.0**. Debt held **$738.8**. PPE roll-forward **UNSOURCED**.

### Cash flow

| Line | $3,900 | $4,500 | **$4,900** | $5,900 | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| CFO | 3,821 | 4,865 | **5,561** | 7,301 | computed = FCF + 1,500 |
| Sustaining capex | 450 | 450 | **450** | 450 | sourced |
| Growth capex | 1,050 | 1,050 | **1,050** | 1,050 | sourced |
| Attrib. capex | 1,500 | 1,500 | **1,500** | 1,500 | sourced |
| **FCF (co. def.)** | **2,321** | **3,365** | **4,061** | **5,801** | computed |
| 1H FCF print | 1,564.3 | 1,564.3 | 1,564.3 | 1,564.3 | sourced historical |
| After-sustaining (alt.) | 3,371 | 4,415 | 5,111 | 6,851 | computed = FCF + 1,050 |
| 40% payout (policy) | 928.4 | 1,346.0 | **1,624.4** | 2,320.4 | computed |
| Debt proceeds | 0 | 0 | **0** | 0 | sourced (none announced) |
| Cash begin (30 Jun) | 2,656.4 | 2,656.4 | **2,656.4** | 2,656.4 | sourced |
| Cash end (model) | 4,049.0 | 4,675.4 | **5,093.0** | 6,137.0 | computed |
| Cash-bridge plug | **0** | **0** | **0** | **0** | computed |

**Tie check 2 — FCF identity:** 5,561 − 1,500 = **4,061**. Holds at every gold.

**Tie check 3 — CF → cash:** 2,656.4 + 5,561 − 1,500 − 1,624.4 = **5,093.0**. Plug **0**.

WC change **UNSOURCED** (dropped). Interest paid ~**$48.4m** (MD&A next-12m notes) is a **note** — **not deducted again** in FCF (may already sit in CFO). FY dividend vs buyback split **UNSOURCED**; 40% is one policy line.

## Guide-miss node (not the mid)

Official mid = printed guide. The miss lives here and in invalidation.

| Miss | What is printed | What we do **not** do |
| --- | --- | --- |
| **US 685** | 1H attrib. US **290** vs FY **685**. RM Q2 GEO **19.8 koz (−49%)**; BM **27.2 (−49%)**. Phase S mill ore “expected in H2” is MD&A colour. | Do not haircut 2,000 GEO. 1H group **984.9** × 2 ≈ **1.97 Moz** already sits inside ±5% if H2 is in line. |
| **RM COS $3,360** | Q2 print. 1H RM **$3,030**. Group 1H COS **$1,358** vs guide **$1,360** — COS **in line**. | Do not lift group COS/AISC to RM’s print. |
| **FY AISC outside ±5%** | Band **$1,644–$1,817**. **1H $1,777 = inside.** **Q2 $1,821 = outside.** Name-level miss = **FY** outside the band, or **stuck ≥$1,821 with gold ≤$4,400**. H2 “in line” is **call colour**. | Do not treat 1H $1,777 as a guide miss. Do not path-weight Q2 into the mid. |

If AISC were stuck at **$1,821** at the $4,500 deck (Q2 print as FY), AISC-other rises **$182m** and official E(4,900) falls to **$6,568m** → EV PT **$35.83 (~$36)** vs **$37**. Same $182m on the FCF check is **$3,879m** → 8% **$42.49 (~$42)**. Sensitivity, not the mid.

## Tape vs $4,900 / $ΔP / $100

| Mark | Level | Note |
| --- | --- | --- |
| NYSE:KGC 21 Aug close | **$32.76** | stockanalysis, 4:00 p.m. EDT; +4.23% vs $31.43. AH $32.82. **Mark, not target.** |
| Official 3y-base PT | **$37** (exact $36.78) | +$4.02 / **+12.3%** vs tape |
| Implied yield at tape | **11.0%** | $4,061 / ($32.76×1.186B − 1,917.6) |
| Kitco / TE 21 Aug | $4,602.40 / $4,607.35 | **not** the forward gold line |
| KGC Q2 / 1H realized | $4,483 / $4,677 | do not restate P&L at Kitco |
| **$ΔP / $100 Au** (official EV) | **$0.99 / sh** | ΔE ≈ $190m × 6.18 / 1,186.2 |
| Tape-implied k @ $4,900 | **5.47×** | (32.76×1,186.2 − 1,917.6) / 6,750 |
| FCF-yield 8% check @ $4,900 | **$44** (exact $44.42) | **FLAG +20.8%** vs $36.78. Check only. |
| FCF $ΔP / $100 (check) | $1.83 / sh | 174 / 0.08 / 1.186B — **not** the official slope |

Spot-tape gold ~$4,600 through the official EV identity: d vs $4,500 = +1; E ≈ 5,990 + 190 = **$6,180m** × 6.18 + 1,917.6 → **$33.81 (~$34)**. FCF-check at the same gold is **~$39**. Neither is official.

## §6.3 — what is NOT in the number

- Great Bear PEA ounces (first-8-year >500 koz, LOM 5.3 Moz) and **late-2029 first gold** as 2026–28 GEO
- Great Bear construction capex vs 2024 PEA **$1.429bn** (UNSOURCED)
- Lobo-Marte **~350 koz/yr**, $4.3bn NPV at $4,100 / 5% from 1 Jan 2028; refresh **initial capex / IRR UNSOURCED**
- US FID package colour (Phase X + Curlew + Redbird 2; **3 Moz**, IRR **59%**, NPV **$4.3bn at $4,500**; first contribution **2028**)
- Invented 2027–29 ounce ramp; invented guide haircut
- Company adj. EBITDA **string** (E is labelled constructed IS). Flat 7× is a check, not official k.
- 2× 1H FCF **$3,128.6m**
- NAV of P&P **20.942 Moz at $2,000** (or at Kitco $4,602 / $4,900)
- NGM / $1.95bn / Barrick NA IPO (NEM–B only)
- Uncommitted ATM / remaining **NCIB** (UNSOURCED)
- RSU **2.8m** + RPSU **2.2m** not in the 1.186B common count (FLAG only)
- Post-28 Jul / August buybacks beyond the 1.7m already in 1,186.2m
- WC change; FY NCI OCF; incremental NS opex/expl above the AISC recon
- Leases in net debt; gold inventory mark
- Invented TIPS/DXY path; 3y gold S/D rebuild
- GDX / gold-equity beta; street multiples / P/NAV
- A fake T. Rowe Share Price tab

## Invalidation (name + metal)

Base **cell** is **$37**. Base **stage** is **watch / no add**. Invalidation migrates the cell and/or stage. Status is **current**; it does **not** restage off watch by itself.

| Direction | Print | Migrate |
| --- | --- | --- |
| **Invalid up** | Metal invalid-up **and** US H2 catch-up (685 path; RM COS not stuck $3,360) | Cell → **3y bull $58**; stage → bull-add (torque only). $5,000–$5,400 without the two metal gates **stays $37 / watch**. |
| **Invalid down** | Metal invalid-down **or** Tasiast shock to the **505 koz** line **or** 2026 AISC **stuck ≥ Q2 $1,821** with gold **≤$4,400** | Cell → **3y bear $21** on a gold break; stage → **cut-watch**. A Tasiast take can cut-watch without $3,900 gold. |
| **Does not break 2026–28 GEO** | GB delay / capex reprint / late-2029 slip | Updates the 2029 clock. **$37 unchanged** until a sourced 2027–29 ounce/E path exists. |
| **Does not change our mind** | Kitco $4,602 restatement; a single $32–$34 tape print; NGM headlines; PEA 518 koz as 2026–28; treating 7× or 8% FCF as official; calling 1H AISC $1,777 a guide miss; officializing 2× 1H FCF | Stay **$37 / watch / no add** |

## Rival views steelmanned (on the **official $37** vs tape **$32.76**)

Steel on **$37 / $58 / $21**. FCF **$44 / $63 / $26** is a **FLAG check** (+20.8% at the base), not a second mid.

### 1) Leftover-torque skip (tape already 11% yield)

**Steelman.** Cost deck is $4,500; official 3y is $4,900. Tape **$32.76** is **36% under $44** and already clears an **11.0%** FCF yield on the $4,900 remake — wider than residual-risk 8% and wider than NEM’s 8%. Own leftover torque in EQX/BTG. Skip the close.

**What would have to be true.** 11% is the *right forever* residual, *and* EQX/BTG leftover IRRs are **rated**, *and* metal holds $4,900-class without a $4,400 break.

**What this view says.** Official cell is **$37**, not “skip.” Tape-implied **5.47×** is inside the 2022–24 k cluster (4.67–5.73) and below the official mid-of-range 6.18×. The 11% FCF yield is a **check**, not the mid. EQX/BTG stay **unrated**. **$32.76 vs $37 is a k gap we do not trade.**

**Who wins.** **This view on the cell and on stage.**

### 2) Clean-FCF upgrade off watch

**Steelman.** Guide-built FCF **$4,061m** at $4,900 after *all* attrib. capex; net cash **$1.92bn**; no gold hedge book; 40% FCF return; S&P **BBB**. Tape prices **11%**; close the gap to 8% / **$44**. Promote.

**What would have to be true.** The $1.05bn growth wall is already a 3y run-rate (we use the guide, but GB/Lobo/US FID can change 2027–29 FCF); Tasiast 25% and US 685 are non-events; 8% is accepted as *the* multiple.

**What this view says.** FCF is **real and labelled**. **$44** is a **FLAG check** (+20.8% vs $37), not a restage and not a second mid. 1H AISC inside the band is **not** a clean bill; US 290 vs 685 is unfinished; Tasiast residual is why the FCF *check* uses 8% not 6.5%.

**Who wins.** **This view on stage.** The rival wins the *cash build* and the *direction of the gap*.

### 3) Tasiast 2010 replay as 3y **base**

**Steelman.** Red Back **$7.1bn**; Financial Post **−21%** one session. Tasiast is still **25%** and the 2025 high-margin site. 1H withholding **$87.5m**. Use bear **$26** (or 10% path **$21**) as the *base*, or skip. Tape **$32.76** already sits between $26 and $35.

**What would have to be true.** A **new** 2026–29 host take that reprints 2010, *and* that this is the mean, *and* that $32.76 is that haircut rather than an 11% yield on $4,900.

**What this view says.** **Own Tasiast 100% already.** No 2026 Red Back cheque. CLA to **2030** is labour, not title. Residual is **clock #1** and the **8% pick**, not a second mid. Cut-watch is **OR**.

**Who wins.** **This view for the $37 base; the rival for the residual (and for the 8% FCF FLAG).**

### 4) Great Bear free call / pay up through $37

**Steelman.** Horizon includes late-2029. AEX **93%**, decline **27 Jul 2026**, PEA >500 koz/yr. $37 is a 2026 run-rate and **understates** 3y. Pay into the bull band.

**What would have to be true.** Construction capital updated and funded at or below 2024$ $1.429bn; first gold **late 2029** in a Q2-class filing; IBA closed; a sourced equity episode.

**What this view says.** Canada is **2029+**. Capex vs PEA **UNSOURCED**. GB is **not a reserve**. GOLD-ROIC: **not a return rule.** **$37 does not include PEA ounces.**

**Who wins.** **This view.**

### 5) Restock because Kitco $4,602 or because $4,900 > $4,500 deck

**Steelman.** Friday metal and official 3y both sit above the cost deck. Treat $32.76 as a gift and mark bull **$58** because $4,900 already exceeds the $4,500 cost deck.

**What would have to be true.** Kitco is the official forward line, *or* $4,900 is allowed to jump the cell to **$63** without metal invalid-up (TIPS **2.40**, last Western ETF extract **outflow**, official not holding **>$5,400**).

**What this view says.** **3y base gold $4,900 → 3y base equity $37.** Stage stays watch because invalid-up has not printed and tape-implied 5.47× is already a 2022–24-like multiple.

**Who wins.** **GOLD-METAL + this view.**

**Bottom line.** Official deck: **$37 / $58 / $21** at **6.18× / 7.68× / 4.67×** on **$4,900 / $5,900 / $3,900**. FCF **$44 / $63 / $26** is a **FLAG check**. None of the five rivals licenses **current** or a restage off **watch**.

## UNSOURCED lines (dropped from the mid — not plugged)

1. **Company-defined adjusted EBITDA** (Q2 NR / MD&A / webcast deck).
2. **Attributable gold ounces produced** (headline is GEO; gold *sold* is printed).
3. **Great Bear 2026 Main Project construction capital vs 2024 PEA $1.429bn.**
4. **Lobo-Marte refresh initial capex / IRR.**
5. **FY NCI share of OCF** (Manh Choh 30%; 1H implied ~$36m not 2×’d).
6. **Working-capital change** (no FY guide).
7. **Incremental non-sustaining opex / exploration** above the AISC recon (guides $125–150m and $220m exist; split vs AISC/capex UNSOURCED).
8. **FY accretion of reclamation** (1H $23.7m not 2×’d).
9. **FY NCI net earnings.**
10. **Remaining NCIB authorization** and exact 40% measurement base.
11. **21 Aug diluted share count** after July 1.7m + any August buybacks (aggregator 1.19B only).
12. **Leases in company net-cash.**
13. **PPE / remaining-assets roll-forward** for the model year.
14. **FY dividend vs buyback split** (policy applied as one 40% cash line).
15. **Official 21 Aug LBMA/COMEX.**
16. **2029 attrib. GEO guide** (none). GB / Lobo ounces.

## Uncertainties (kept)

- 3y equity is a **gold remake of a 2026 guide run-rate**, not a 2029 volume model. GB / Lobo / US FID may change 2027–29 FCF.
- 8.0% is a **desk bucket** on the FCF **check**, not a print. Quality-neutral 6.5–7.0% is **$54 / $51** at $4,900 FCF (FLAG vs $37).
- Royalty factor applied **country-flat**; company prints it as a **group** ±$5/GEO.
- Country COS blend **$1,357.975** vs group **$1,360** — recon **$4.05m** is labelled.
- Interest paid **$48.4m** may already be inside CFO; not deducted twice.
- H2/FY AISC “in line” and Q3/Q4 seasonality are **call colour**.
- No house YE 2028/29 gold point (4,900 is a band midpoint).
- No desk gold-equity beta; no NAV.

## Sources

| Path / URL | Figure used |
| --- | --- |
| `/home/box/agent-data/grok-research/views/GOLD-METAL.md` | Current official 3y metal. **Not edited.** |
| `/home/box/agent-data/grok-research/reports/HOUSE-MODEL.md` | Kit as of 22 Aug 2026: official PT = historical EV/EBITDA k (base = mid of range). FCF yield is a check. Residual-risk 8% still the FCF FLAG. Captain: computed E from segment IS OK if labelled. |
| `/home/box/agent-data/grok-research/reports/KGC-SCOUT.md` | Tape $32.76; GEO; AISC; FCF; capex split; country ounces; Tasiast 25%; Manh Choh 70%; +$5 / +$16 |
| Kinross Q2 2026 NR PDF | https://s204.q4cdn.com/896213035/files/doc_news/2026/07/29/KGC-Q2-2026-results-news-release-final.pdf |
| Q2 2026 MD&A (Ex. 99.1) | https://www.sec.gov/Archives/edgar/data/701818/000110465926088237/tm2621038d1_ex99-1.htm — BS, $48.4m interest, 1,186.2m sh, site tables |
| YE 2025 / 18 Feb 2026 PR | 2026–28 2.0 Moz; country guide; $450/$1,050; cash tax $1,125; G&A $135; DD&A $550/oz |
| `/home/box/agent-data/grok-research/models/KGC/*.csv` | Machine-readable IS/BS/CF/segments/valuation |

---

*End KGC official view. Status = **current**. Stage = **watch**. Official 3y $/sh = **$37 / $58 / $21** (historical EV/EBITDA 6.18× / 7.68× / 4.67× on labelled IS E). FCF-yield **FLAG check** $44 / $63 / $26. `names.view_ref` = this file. GOLD-METAL.md not modified. No ship.*
