# NEM — official equity view (HOUSE-MODEL remake)

| Field | Value |
| --- | --- |
| Id | NEM |
| Kind | official view (equity) |
| Status | **current**. No ship. Stage **watch**. Review empty / risk low. |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Ticker | NYSE: **NEM** (ASX/PNGX: NEM; TSX: NGT delisted 24 Sep 2025) |
| Stage | **watch** (do not promote; kit does not restage) |
| Task | **NEM-HOUSE** |
| Kit | **HOUSE-MODEL** (`/workspace/HOUSE-MODEL.md`) §4.0 |
| Horizon | **3 years — to 22 Aug 2029**. Clock: **3y run-rate + path**. Run-rate = **2026 guide**. Y2/Y3 path is **uncertainty / not in the number**. 12m to 22 Aug 2027 is a **check-in only**. |
| Gold input | Official **GOLD-METAL** (do not change): 3y base **$4,900** (4,400–5,400), bull **$5,900** (5,400–6,400), bear **$3,900** (3,400–4,400). 12m check-in **$4,500** (4,400–5,000). Path: `/home/box/agent-data/grok-research/views/GOLD-METAL.md` |
| Scout | `/workspace/NEM-SCOUT.md` |
| Model | `/home/box/agent-data/grok-research/models/NEM/` (workspace twin `/workspace/nem-models/`) |
| Compare | GOLD-COMPARE |
| Not this view | **No ship. No live trade. No Cursor cloud.** Do not edit GOLD-METAL. Stage stays **watch**. |

This is a **priced official view**, not a recommendation. Words BUY / SELL / HOLD are not used.

**Gate:** **current** after empty review (risk low). `names.view_ref` = this path. Stage stays **watch**. No ship.

**Official PT:** `PT = (EBITDA × k_scenario − net_debt) / diluted_shares`. **Official E = company-guide cost IS EBITDA** (`is.csv` `EBITDA_IS_computed` = EBIT + D&A on guide CAS **$1,055**, guide G&A / expl / recl / D&A). **Official k = hist mid-of-range 9.04** (WSN YE 2016–2025 cleaned; low 5.45 / high 12.63). **Not** TTM-fat 1H AISC. **Not** flat 7×. **Not** FCF yield. **Not** series median 8.36.

## Thesis

Newmont is a residual-risk senior modelled **as guided** (5,260 koz / CAS $1,055 / AISC $1,680 / sustain $1,950m / develop $1,400m). Official E at $4,900 is **$17,363m** (guide-cost IS), not the TTM remake **$20,049m**. Official k **9.04** prints **3y-base $151**. 7× check on the same E is **$118**. Tape **$131.58** sits between 7× and official (tape-implied **7.82×** on guide E). The 1H AISC beat (**$1,321** vs guide **$1,680**) is a **hedge / sensitivity / invalidation**, not in official E. Stacked rival **TTM-fat E × 9.04** reprints the old unpublished card **$175 / $304 / $80** — steelmanned below, **not the mid**. $1.95bn NGM cheque **out** ($1.85/sh footnote). NGM **38.5** lock.

## Tape we are marking (sourced)

- Equity: NYSE NEM **$131.58** close 21 Aug 2026, 4:00 p.m. ET (stockanalysis.com / Yahoo). Shares **1,053,692,271** (16 Jul 2026 10-Q outstanding). Scout diluted WASO **1,067m** printed as FLAG only — official count is the 10-Q outstanding. Desk mkt cap **$138.6bn**. Working EV = 138,645 − 2,805 = **$135.8bn**.
- Gold: Kitco bid **$4,602.40** 21 Aug 11:35 p.m. ET; TE CFD **$4,607.35**. Official 21 Aug LBMA/COMEX **missing**. NEM Q2 realized **$4,414/oz**. 1H realized **$4,661**. Company 2026 cost deck **$4,500**. **3y models use $4,900.**
- 30 Jun 2026: cash **$9,009m**, debt **$5,083m**, leases **$515m**, net cash **$3,411m** incl. leases. July buybacks **$606m** → working net cash **$2,805m**. **net_debt = −2,805.** Do not subtract $1.95bn.

## Official k (sourced)

**Primary series:** WallStreetNumbers YE EV/EBITDA **2016–2025**, live fetch 22 Aug 2026. https://wallstreetnumbers.com/stocks/nem/ev-ebitda  
What E: vendor YE EV / TTM EBITDA. Cleaned: drop k>20 and negative E. **Nothing dropped** in this window.

| YE | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| WSN k | 8.44 | 7.69 | 7.54 | 10.50 | 8.81 | 8.27 | 8.45 | 12.63 | 5.45 | 8.09 |

| | k | Method |
| --- | ---: | --- |
| **Bear** | **5.45** | low (2024 YE) |
| **Base** | **9.04** | **(5.45+12.63)/2** — not series median **8.36** |
| **Bull** | **12.63** | high (2023 YE). Not 144×. Not ~25×. |
| 12m | **9.04** | same base k |

WSN spot 21 Aug **8.23**. Yahoo current **8.17**. GF 10y extract 17 Jun: min 5.61 / med 9.86 / max **144.01 DROP**. Full series: `models/NEM/k_history.csv`.

## Official E (guide-cost IS)

`is.csv` `EBITDA_IS_computed` = EBIT + D&A. Sales = 4,850 koz × G + by-product deck. CAS = **4,850 × $1,055**. Guide D&A $2,815 / G&A $375 / expl+AP $525 / recl $385.

| Gold | Official E $m | TTM-fat rival E $m |
| ---: | ---: | ---: |
| 3,900 | **12,513** | 14,999 |
| 4,500 | **15,423** | 18,029 |
| 4,900 | **17,363** | 20,049 |
| 5,900 | **22,213** | 25,099 |

TTM remade = 16,765 + $505m/$100 × (G − 4,250). That embeds the 1H cost beat. **Rival only.**

**Miss (not in official E):** 1H 2026 AISC **$1,321** vs FY26 guide **$1,680**. If 2H merely repeats 1H, E is fatter. House rule: keep guide in the mid; put the beat in hedge / invalidation.

## Targets (US$/share)

`PT = (E × k + 2,805) / 1,053.692271`

| Scenario | Gold | Official E $m | k | **Official PT** | 7× on guide E | FCF FLAG | TTM-fat rival (same k) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **3y Base** | **4,900** | **17,363** | **9.04** | **$151** | $118 | $108 same-basis / $137 mixed | **$175** |
| **3y Bull** | **5,900** | **22,213** | **12.63** | **$269** | $150 | $180 same-basis / $218 mixed | **$304** |
| **3y Bear** | **3,900** | **12,513** | **5.45** | **$67** | $86 | $56 same-basis / $78 mixed | **$80** |
| *12m check-in* | *4,500* | *15,423* | *9.04* | *$135* | $105 | $99 same-basis / $129 mixed | *$157* |

Algebra (base): (17,363.2 × 9.04 + 2,805) / 1,053.692271 = **151.63 → $151**. Bull 268.92 → **$269**. Bear 67.38 → **$67**. 12m 134.98 → **$135**.

**3y-base vs FCF (same-basis first):** named guide-cost cash is **IS NI + D&A − PPE** at $4,900 = 9,630.1 + 2,815 − 3,525 = **$8,920m** (`is.csv`/`cf.csv` PPE). At 8% + $2,805 → **$108**, gap vs $151 **40% — FLAG**. Drop unlabelled $8.5bn / $9,852m. cf.csv **FCF_company $11,353m @ 8% → $137** is the 1H-beat remake — **mixed vs guide-cost E**, not an all-clear. Do not average. Do not lead $175.

**Read:** tape **$131.58** is **−13% vs official $151**, **+12% vs 7× $118**. Tape-implied k on guide E **7.82×** @ $4,900 (8.54× @ ~$4,600 E $15,908). Patience on size. Bull $269 is if-flip + high-k. Bear $67 is plateau-fail + cycle-low k.

## Clock

**3y run-rate + path.** Run-rate = 2026 guide (19 Feb, reaffirmed 23 Jul, **pre-NGM expansion**). Y2/Y3 (Tanami E2 2H 2027; Cadia PC2-3 / PC1-2; Lihir barrier 2028; Red Chris FID 2H 2026; ~6 Moz / 150 kt Cu colour) **not in the number**.

## Operating model

Ops mid **5,260 / $1,055 / $1,680 / $1,950 / $1,400**. NGM **935** (19 Feb PR). P&L sold **4,850** ex PV 255 / FDN 155 (equity-method). NGM **38.5** proportionate. By-product deck held at **$4,500**. FY equity income and FY NCI **UNSOURCED** (dropped from FY NI). `tie.json` NI→RE and cash bridge **false**.

Site PR: https://www.newmont.com/investors/news-release/news-details/2026/Newmont-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Provides-2026-Guidance-and-Announces-Enhanced-Capital-Allocation-Framework/default.aspx

Q2 exhibit: https://www.sec.gov/Archives/edgar/data/1164727/000116472726000034/newmontq22026earningsrelea.htm

## Kit §8

| Cell | 3y run-rate |
| --- | --- |
| Volume (guide, no haircut) | **5,260** attrib (sold 4,850 + PV 255 + FDN 155) |
| Official E | **17,363 / 22,213 / 12,513** |
| Official k | **9.04 / 12.63 / 5.45** |
| Official PT | **151 / 269 / 67** |
| 7× check | **118 / 150 / 86** |
| TTM-fat rival | **175 / 304 / 80** |
| FCF FLAG | **$108 same-basis** (IS NI+DA−PPE @ 8%) / **$137 mixed** (cf.csv FCF_company) |
| Net debt | **−2,805** |
| Shares | **1,053.692271m** |
| Tape vs $151 | **−13%**; implied k **7.82×** |
| $ΔP / $100 Au | **+$4.16** at base k (IS lever ~$485m / $100 × 9.04 / 1,053.69). Company pretax print $505m/$100 is the hedge check. |
| Guide-miss | 5,260×0.95 = 4,997; AISC $1,764; **or** 1H AISC $1,321 repeats (fattens E toward TTM rival) |

## §6.1 Tape vs implied

| Mark | vs official $151 | vs 7× $118 | vs TTM-fat $175 |
| --- | --- | --- | --- |
| Tape $131.58 @ $4,900 | **−13%** | **+12%** | **−25%** |
| ~$4,600 (not forward) | guide E ~15,908 × 9.04 → **$139**; tape-implied **8.54×** | 7× → **$108** | TTM-fat ~18,533 × 9.04 → **$162** (this $162 is **spot gold × official k on fat E**, not the dead median-8.36 3y-base) |

## §6.2 Gold sensitivity (official k held at 9.04 except official bull/bear)

| Node | Gold | Official (k scenario) | 7× guide E | FCF FLAG |
| --- | ---: | ---: | ---: | ---: |
| 12m | 4,500 | **135** | 105 | 99 / 129 |
| Spot tape | ~4,600 | **139** (k 9.04) | 108 | mixed ~132 |
| 3y base | 4,900 | **151** | **118** | 108 / 137 |
| 3y bear / bull | 3,900 / 5,900 | **67 / 269** | 86 / 150 | 56 / 180 vs mixed 78 / 218 |

Official bull/bear also move k (12.63 / 5.45). Constant-9.04 at $5,900 / $3,900 would be ~$193 / ~$110.

## Guide-miss / 1H beat (sensitivity, **not** the mid)

- Low-end ounces 5,260 × 0.95 = **4,997**; high-end AISC **$1,764**; Cadia Q3 fails pre-event (10-Q Note 7).
- **1H AISC $1,321 vs guide $1,680:** if the beat holds, official E fattens toward TTM-fat and the stacked rival **$175** becomes the working tape. That is a **hedge**, not a mid rewrite.
- Does **not** move official **$151**. Invalidation is a **formal guide restatement** or Q3 fail bar.

## NGM / Barrick (NEM side — lock)

- Direct **38.5%** NGM LLC member. 8-K does not restate.
- **$1.95bn** 30 days after Fourmile. **Out.** Footnote **$1.85/sh**.
- YE 2026 IPO = Barrick colour. **Unused.**
- NGM FY26 **935 koz** attrib. from 19 Feb PR.

## Invalidation

- **$151 invalid up** if GOLD-METAL migrates to 3y bull (gold holds $5,400 a quarter and 10y real sustained below 2.40 and Western ETF tonnes in) **and** NEM still prints ~5.3 Moz-class **guide** EBITDA without a new Ghana AISC restatement. Then migrate toward **$269**. A sustained 1H-style cost beat **without** a guide restatement is **not** automatic migration to $175 — that is the TTM-fat rival.
- **Invalid down** if GOLD-METAL migrates to 3y bear (breaks $4,400 toward ~$4,000 with 10y real still ≥2.40 and a GOLD-METAL companion). **Or any of:** company **restates** 5,260 / $1,680; Cadia **fails pre-event in Q3**; Ghana **restates** unit-cost guidance; 8-K / Exhibit 10.1 **restates NEM below 38.5%**. Then toward **$67**.
- **k history invalid** if a later sourced 10y cleaned series replaces WSN 5.45–12.63 — re-run PTs. Do not silently swap to 7.0×.
- **12m $135** fails if YE 2026 / Aug 2027 official gold is outside 4,400–5,000.

## Rival views tested (steelman)

### 1) Tape / 7× is already fair — $151 is a museum multiple

**Steelman.** Tape-implied **7.82×** on guide E; vendor spot ~8.2×. Cycle-high gold should not get 2016–25 mid 9.04.

**What would have to be true.** Official k = spot or 7.0×. Kit §4.0 says historical range.

**Who wins.** **This view for the official mid.** 7× $118 and tape 7.82× stay printed checks. Evidence sits closer to 7–8× than 9.04 — that is a **k-history vs tape** gap, labelled.

### 2) Lead FCF-yield $108–$137

**Steelman.** Residual-risk 8% on company FCF. Same-basis IS NI+DA−PPE **$108**; cf.csv 1H-beat **$137**.

**What would have to be true.** Official engine = FCF yield. Retired by §4.0.

**Who wins.** **This view.** FCF is FLAG. vs $151 the same-basis **$108 FLAGs 40%**. Mixed $137 is not an all-clear.

### 3) Value-trap — mid-$90s

**Steelman.** $1.95bn out, Ghana ISA expired (tax 35%), Cadia, YE 2025 reserves **118.2 vs 134.1 Moz**, Yanacocha WTP ~$1.8bn, Cadia resource −8.5 Moz. $132 is the bounce.

**What would have to be true.** Bear E + bear k as the **base**, or a guide restatement.

**Who wins.** **This view for the base.** Official bear **$67** is the plateau-fail card. Those scout facts sit in invalidation / not-in-the-number, not a silent haircut.

### 4) Import AEM 5% or 8–10× quality k

**Steelman.** NEM should never see 9×.

**Who wins.** **This view.** Official k is **NEM history**.

### 5) Stacked TTM-fat E × hist k — the old $175 card

**Steelman.** Printed company KPI is TTM Adj. EBITDA **$16,765**. Remade at $4,900 = **$20,049**. 1H AISC **$1,321** already beat guide **$1,680**. Using that E × official 9.04 reprints **$175 / $304 / $80**. Eight of ten WSN YE prints sit below 9.04, but the **stack** (fat E + mid-range k) is what the first remake published.

**What would have to be true.** Official E = TTM remake / 1H run-rate, not the guided machine. Firstmate 22 Aug: **not closed intent.** House rule is model as guided; put the miss in hedge.

**Who wins.** **This view for the official mid ($151).** TTM-fat **$175** stays the printed rival. If the company **restates** unit-cost guidance down toward 1H, migrate; do not do it from the 1H print alone.

## §6.3 What is NOT in the number

- Exploration / Fourmile / Fiberline / Mike ounces (not in the 8-K)
- Uncommitted projects; **~6 Moz** colour
- Barrick NA IPO %; NEM 38.5% into a listco
- **$1.95bn until received**
- Uncommitted buyback path; invented guide haircut
- GDX beta; invented TIPS / DXY; 3y gold S/D
- Street multiples / P/NAV; reserve NAV at $2,000 or Kitco $4,602
- Invented (gold−AISC)×oz EBITDA
- **Flat 7.0× as official k**; **FCF as official mid**; **$860 residual cash**
- **TTM-fat E as official E** (rival 5)
- GF 144× / 169× / ~25× on bull
- YE 2026 IPO colour

## Uncertainties / blockers

- Official 21 Aug LBMA/COMEX missing.
- GF live HTML blocked 22 Aug; 10y 5.61 / 9.86 / 144.01 is a 17 Jun extract.
- TickerLeague / Macrotrends EV/EBITDA **UNSOURCED**.
- Vendor E defs differ. Official E is **guide-cost IS**, not vendor TTM.
- FY NI→CFO / equity / NCI **UNSOURCED**. `tie.json` bridges false.
- Fourmile close / $1.95bn / Exhibit 10.1.
- Guide is pre-NGM expansion. Ghana L.I. 2517 rider not in 2026 guidance. Cadia Q3 pre-event bar.

## Sources

- HOUSE-MODEL §4.0 / §5.2 (22 Aug 2026). GOLD-METAL current (not edited). NEM-SCOUT.
- `models/NEM/{segment,is,bs,cf,valuation,k_history}.csv` + `tie.json`.
- 19 Feb 2026 FY/guidance PR (NGM **935**). Q2 2026 Exhibit 99.1 (TTM Adj. **$16,765**; net cash **$3,411**; 1H AISC **$1,321**).
- 10-Q 16 Jul 2026 shares **1,053,692,271**.
- WSN https://wallstreetnumbers.com/stocks/nem/ev-ebitda (22 Aug). Yahoo key-statistics. GF extract 17 Jun 2026.
- Tape $131.58 21 Aug 2026.

---

*End NEM-HOUSE. Status **current**. Stage **watch**. Official mid **guide-E hist-k $151**. TTM-fat $175 is rival 5. No ship. No trade. No GOLD-METAL edit. NGM 38.5 lock. $1.95bn out.*
