# EQX — official view (house remake)

| Field | Value |
| --- | --- |
| Id | EQX |
| Kind | official view (name) |
| Status | **current** |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Name | Equinox Gold (NYSE American / TSX: **EQX**) |
| Stage | **watch**. This remake does **not** promote. |
| Task | EQX-HOUSE |
| Kit | `/home/box/agent-data/grok-research/reports/HOUSE-MODEL.md` |
| Pack | `/home/box/agent-data/grok-research/models/EQX/` (`segment.csv`, `is.csv`, `bs.csv`, `cf.csv`, `valuation.csv`, `tie.csv`, `hist_k.csv`) |
| Scout | `/home/box/agent-data/grok-research/reports/EQX-SCOUT.md` |
| Metal | `/home/box/agent-data/grok-research/views/GOLD-METAL.md` — **do not change** |
| Clock | **3y run-rate = 2026 printed guide** (12 months EQX + Aug–Dec Musselwhite / Camino Rojo). Not a 2029 volume model. |
| Engine | **Official PT = EV / guide-built EBITDA × this name’s sourced historical k.** Base = **mid of range**, bull = **high**, bear = **low**. **7.0× T. Rowe is a check only.** FCF yield is a check. |

## Thesis

EQX is **integration tape with a printed 2026 guide**, valued on GOLD-METAL **$4,900** with **this name’s own 2019–2025 EV/EBITDA history**. Official mid **= company guide** (no ounce haircut). **Hedge the miss** in the node and invalidation.

House 3y base **$20** (k **9.16×** mid of sourced 2019–2025 range on $2,808.75m built EBITDA, FD 1,247,524,702, net debt **$96.22m**). Tape **$13.53**. 12m check-in at gold **$4,500** is **$18**. Spot ~$4,600 at the same k is **$19**. 7.0× check on the same E is **$16** — that is **not** the official mid.

Do **not** put 1.1 Moz or P2 +70–80 koz in the mid. Prior official 3y **$18 / $28 / $9** ounce×metal is **retired**. **7.0× is retired as official k.**

**Watch. Patience on size.** Torque only on GOLD-METAL 3y bull flip.

## Historical k (sourced; vendor averages unused)

Window: **year-end EV / company adj. EBITDA, 2019–2025**. `k_year = (N_basic × NYSE-A year close + company net debt) / that year’s printed adj. EBITDA`. Full grid: `models/EQX/hist_k.csv`.

| Year | Adj. EBITDA $m | Perimeter | YE basic shares | YE close $ | Mkt $m | Co. net debt $m | YE EV $m | **k** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2019 | 98.2 | printed | 113,452,363 | 7.70 (2019-12-31) | 874 | 196.3 | 1,070 | **10.90** |
| 2020 | 274.6 | printed | 242,354,406 | 10.34 (2020-12-31) | 2,506 | 200.3 | 2,706 | **9.86** |
| 2021 | 303.1 | printed | 301,324,604 | 6.76 (2021-12-31) | 2,037 | 235.2 | 2,272 | **7.50** |
| 2022 | 168.7 | printed | 307,365,588 | 3.28 (2022-12-30) | 1,008 | 627.3 | 1,636 | **9.69** |
| 2023 | 304.4 | printed | 318,013,861 | 4.89 (2023-12-29) | 1,555 | 733.0 | 2,288 | **7.52** |
| 2024 | 458.2 | printed | 455,232,521 | 5.02 (2024-12-31) | 2,285 | 1,108.5 | 3,394 | **7.41** |
| 2025 | 1,339.6 | **All Ops** | 785,632,450 | 14.04 (2025-12-31) | 11,030 | 1,147.3 | 12,178 | **9.09** |

**Range: low 7.41 (2024) / high 10.90 (2019). Mid of range (low+high)/2 = 9.16.** Mean of yearly k = 8.85; median = 9.09. Official uses **range mid / high / low** (not the mean).

Sources: contemporaneous year-end MD&A for E and company net debt (2019 net debt = FS loans − cash; 2020 MDA comparative $196.3m agrees); YE shares from that year’s FS equity roll; NYSE-A **last session close** from Yahoo EQX ASE (not a vendor EV/EBITDA average). 2025 uses **All Operations** E because YE EV still owned Brazil (sold 23 Jan 2026). Continuing 2025 E $889.3m is **not** the YE k denominator.

Company historical net debt **includes converts some years**. Today’s EV plug is **30 Jun debt ex-convert $96.22m** (ITM converts in N). Labelled date-mix, not a silent plug.

If this window is rejected, there is **no official mid**.

## Tape / shares / simplified debt

- NYSE-A **$13.53** (21 Aug 2026). TSX **C$18.62**.
- **N = 1,247,524,702** FD (MD&A 5 Aug, post-Orla). Converts ITM → **dilution, not debt**. Basic 1,167.5m.
- **Cash $317.783m** (30 Jun FS). Loans **$583.000m**. Convert host **~$169m**. **Debt ex-convert $414.000m. Net debt EV plug $96.217m**. 31 Jul pf net cash **$214m** is mixed-date colour.
- Interest / D&A / ETR / C&M / E&E: same computed plugs as the tied pack (`is.csv`). Run-rate ETR is **Q2 continuing 28.47%** ($86.993/$305.591). **H1 continuing 34.5%** ($213.834/$619.602) is the contrary print — hits FCF-yield, not official EV/EBITDA.

## Locked gold (do not retune)

| Scenario | Band | Mid | Horizon |
| --- | --- | --- | --- |
| **3y Base** | 4,400–5,400 | **4,900** | to 22 Aug 2029 |
| **3y Bull** | 5,400–6,400 | **5,900** | same |
| **3y Bear** | 3,400–4,400 | **3,900** | same |
| *12m check-in* | *4,400–5,000* | *4,500* | *to 22 Aug 2027* |
| *Spot tape* | | *~4,600* | *21 Aug — not the forward line* |

## Official mid = 2026 guide (no haircut)

| Item | Range | **Mid (official)** |
| --- | --- | --- |
| Gold koz (12+5 mo) | 870–920 | **895** |
| Cash cost $/oz | 1,600–1,700 | **1,650** |
| AISC $/oz (excl. G&A) | 1,900–2,000 | **1,950** |
| Growth capex $m | 600–650 | **625** |
| Growth exploration $m | 110–120 | **115** |
| G&A $m | 95–105 | **100** |
| Sustaining | AISC − cash = **$300/oz** | **$268.5m** |

Segment mids: Greenstone **262.5 / 1,600 / 1,950 / 150**; Musselwhite **105 / 1,250 / 1,750 / 12.5**; Valentine **145 / 2,000 / 2,100 / 190**; Nicaragua **237.5 / 1,850 / 2,050 / 120**; Camino Rojo **60 / 750 / 1,000 / 32.5**; Mesquite **75 / 1,850 / 2,550 / 10**. Seg oz **885** vs consol **895** — printed **10 koz residual**, not rounding; **consol 895 binds**. Pipeline residual growth **$110m**.

Q2 actuals (pre-Orla, **check not haircut**): 176.8 koz, cash $1,816, AISC $2,175, realized $4,256.

Hedges: prepays **17.8 koz** + swap 6,657 oz @ $2,204 roll off by Sep 2026 (**12m**). **74 koz** purchase @ 20% of spot is a remaining book — mid still prices **100% of 895 koz** at $4,900; miss node only (schedule **UNSOURCED**).

## Per-segment → EBITDA (3y base, $4,900)

`Seg. EBITDA = oz × ($4,900 − cash)`. Official consol. EBITDA = **895 × ($4,900 − $1,650) − $100 = $2,808.75m**. Grid in `segment.csv`. **Not company adj. EBITDA** (Q2 $358m is the wrong perimeter).

## Three statements — 3y run-rate ($m)

Tied pack unchanged. WC **$0**. Capex **$1,008.5m**. C&M **$86.27** and E&E **$32.26** below EBITDA. Other income **UNSOURCED** (dropped). See `is.csv` / `bs.csv` / `cf.csv` / `tie.csv`.

| IS | $4,900 | $5,900 | $3,900 | $4,500 | ~$4,600 |
| --- | --- | --- | --- | --- | --- |
| **EBITDA (PT E)** | **2,808.75** | **3,703.75** | **1,913.75** | **2,450.75** | **2,540.25** |
| **NI** | **1,475.60** | **2,115.82** | **835.38** | **1,219.51** | **1,283.53** |
| **CFO** | **2,065.16** | **2,705.38** | **1,424.94** | **1,809.07** | **1,873.09** |
| **FCF (all capex)** | **1,056.66** | **1,696.88** | **416.44** | **800.57** | **864.59** |
| After-sustaining alt | 1,796.66 | 2,436.88 | 1,156.44 | 1,540.57 | 1,604.59 |
| Ending cash | 1,269.37 | 1,909.59 | 629.15 | 1,013.28 | 1,077.30 |

**Tie:** BS.cash = CF.ending; RE = open + NI − div; assets = L+E. EV **still uses 30 Jun $96.22m**, not ending cash.

## 3y $/sh (official)

`EV = k_scenario × built EBITDA`; `Equity = EV − $96.22m`; `$/sh = Equity / 1,247,524,702`.

| Scenario | Gold | E $m | **k** | **Official $/sh** | 7.0× check | FCF y=9% |
| --- | --- | --- | --- | --- | --- | --- |
| **3y Base** | 4,900 | 2,808.75 | **9.16 mid** | **$20** (20.55) | $15.68 | $9.33 |
| **3y Bull** | 5,900 | 3,703.75 | **10.90 high** | **$32** (32.28) | $20.71 | $15.04 |
| **3y Bear** | 3,900 | 1,913.75 | **7.41 low** | **$11** (11.29) | $10.66 | $3.63 |
| *12m check-in* | *4,500* | *2,450.75* | *9.16* | *$18* (17.92) | *$13.67* | *$7.05* |
| *Spot ~$4,600* | *4,600* | *2,540.25* | *9.16* | *$19* (18.57) | *$14.18* | *$7.62* |

**FLAG:** official $20 vs FCF-yield $9.33 = **120%**. vs 7.0× $15.68 = **31%**. Print both checks. Do **not** average.

| Scenario | Band | Mid | vs $13.53 |
| --- | --- | --- | --- |
| **3y Base** | **$17–24** | **$20** | +48% |
| **3y Bull** | **$27–36** | **$32** | +136% |
| **3y Bear** | **$8–14** | **$11** | −19% |
| *12m* | *$15–21* | *$18* | *+32%* |

**$100/oz** at k 9.16: E ±$89.5m → **±$0.66/sh**.

## Guide-miss node (not the mid)

| Miss | What changes | Approx $/sh (k 9.16) |
| --- | --- | --- |
| Low-end ounces **870** | E −$81m | **$19.9 vs unrounded $20.55** |
| High-end cash **$1,700** | E −$44.75m | **$20.22 vs unrounded $20.55 (−$0.3)** |
| Q2 cash $1,816 as run-rate | E −$149m | **$19.4 vs unrounded $20.55** |
| Remaining 74 koz @ 20% of spot (Q2 pace ~6 koz/yr) | E −$23.5m if 6 koz; 74 koz schedule **UNSOURCED** | **$20.4 vs $20.53** (do not haircut $20) |
| Formal cut through **<870** or AISC restated **≥$2,175** | Mid reprints | invalidate $20 |
| **Announced raise** | migrate bear | **$11** / tape |

P2 / 1.1 Moz / 1.9 Moz stack: **not the mid**.

## What is NOT in the $20

1.1 Moz full-year Orla; P2 ounces; Kitco as G; 31 Jul $214m pf net cash as EV; 7.0× as official k; vendor EV/EBITDA averages; 2025 continuing E $889.3 as the hist-k denominator; path-weighted Q2 haircut; year-by-year 2027–29 koz (**UNSOURCED**).

## Sanity

- Tape $13.53 vs official $20 = **−32%**. Implied k on $2,808.75m E and $96m net debt ≈ **6.04×**, **below** the 2019–2025 low (7.41). That is a **multiple gap vs this name’s history**, not proof the tape has rejected $4,900.
- 7.0× $15.68 is a **below-range check** (hist low **7.41**). Tape implied **6.04×** is also below the low. Official k is the range mid **9.16**, not 7.0.
- Q2 AISC $2,175 vs guide $1,950 is the **hedge**, not a second mid.
- IS/BS/CF tie in `tie.csv`.

## Invalidation

- **$20 invalid up → $32** if GOLD-METAL 3y bull (hold **>$5,400** + TIPS **hold below 2.40** + Western ETF-in).
- **$20 mark toward $17 (still base)** if gold holds $4,400+ and FY prints high-end cost or Q2-like — guide-miss, **not** a new mid until they **restate**.
- **$20 invalid down → $11** if GOLD-METAL 3y bear **or** an **announced raise**. Sticky costs **alone** do not migrate $11.
- **12m $18** fails as check-in if Aug 2027 tape is outside $15–21 while gold is in 4,400–5,000.

## Rivals (on these numbers)

### 1) Keep 7.0× as the mid
**Steelman.** Kit used to lead T. Rowe H=7. 7× → **$16**. Hist mid 9.16 overstates a growth-wall mid-tier. Tape 6.0× agrees more with 7 than 9.
**Must be true.** Official k is 7, not this name’s history.
**Wins:** **Captain 22 Aug: 7.0× is a check.** Official k is the sourced range.

### 2) FCF-yield $9.33 *is* the mid
**Steelman.** 8–10% mid-tier on $1.06bn FCF → **$9**. Hist k was earned on smaller E and a different perimeter.
**Wins:** **EV/EBITDA is official.** $9.33 is the check. Do not average.

### 3) Drop 2019 (tiny E) — range 7.40–9.84, mid 8.62 → **$19**
**Steelman.** 2019 $98m E is pre-scale; high 10.88 is one year.
**Must be true.** Desk drops a sourced year.
**Wins:** **Keep 2019.** Sourced. Mid of full range is the rule. $19 is inside the $17–24 band.

### 4) Old $18 ounce×metal
**Steelman.** $13.53 × (4,900/4,500) × (1.1/0.895) ≈ $18.
**Wins:** **895 koz binds.** $18 is the **12m check-in**, not the 3y mid.

### 5) Path to 1.9 Moz / P2 in the mid
**Wins:** **Out of the mid.**

## Open

Guide gold-price assumption; 2027–29 koz; post-Orla R&R; FY company adj. EBITDA on the Orla perimeter; 21 Aug ROD; official 21 Aug LBMA.

*EQX-HOUSE current 22 Aug 2026. Hist k sourced from filings + YE closes. Pack ties. Stage watch. Not a trade.*
