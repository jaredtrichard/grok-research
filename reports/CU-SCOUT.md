# CU-SCOUT — Open copper

| Field | Value |
| --- | --- |
| Date | Saturday 22 Aug 2026 (America/New_York); last official LME/COMEX/SHFE session Fri 21 Aug 2026 |
| Task id | CU-SCOUT |
| Kind | scout |
| Researcher | Copper (sector id `copper`, GICS 15104025) — not Gold, not Metals & Mining |
| Status of constraints | **No official metal view. No name rows. No ship. No gold rewrite. No trade. No Cursor cloud.** First-name slate is a recommendation only. Firstmate signs names. |

## What this is / is not

Desk scout so Firstmate can decide how copper is covered and which liquid names belong on a first follow-list. Coverage map plus sourced tape/physicals. Not a rating and **not** authorization to write `views/COPPER-METAL.md` current.

Gold stays with Gold. Lithium, iron, steel, and diversified majors (BHP/RIO/VALE) are out of scope.

Numbers below are only what live sources supported on this pull. Official LME.com and CME.com pages were Cloudflare/timeout blocked; reprints are labelled. If a print or corporate fact was not independently sourced, it is flagged. Do not blend ICSG / USGS / IEA / Cochilco / SMM balances.

## The tape (as-of Fri 21 Aug 2026)

Conversion used: **1 t = 2,204.62 lb**.

| Print | Level | As-of | Source / flag |
| --- | --- | --- | --- |
| LME cash official settlement | **14,291.00 USD/t** (6.4823 USD/lb) | Fri 21 Aug 2026 | Westmetall reprint (not LME.com) |
| LME 3-month | **14,235.00 USD/t** (6.4569 USD/lb) | Fri 21 Aug 2026 | Westmetall reprint |
| Cash − 3m | **+56 USD/t backwardation** | Fri 21 Aug 2026 | derived (14,291 − 14,235) |
| LME warehouse stocks | **238,575 t** | Fri 21 Aug 2026 | Westmetall reprint |
| COMEX front HGU26 (Sep-26) | **6.5870s USD/lb** = 14,521.83 USD/t | Fri 21 Aug 2026 | Barchart settlement-style (`s`); CME.com timed out |
| COMEX − LME 3m | **+286.83 USD/t** (+0.1301 USD/lb) | Fri 21 Aug 2026 | derived; not freight/VAT/tariff-adjusted |
| COMEX − LME cash | **+230.83 USD/t** | Fri 21 Aug 2026 | derived |
| SHFE most-traded last | **107,750 CNY/t** (+0.53%) | Fri 21 Aug 2026 Beijing | Sina / Reuters; **last, not stated 结算价** |
| SHFE CU2609 prior settle | 107,180 CNY/t | Thu 20 Aug 2026 | Lange reprint |
| Yangshan warrant avg | **87 USD/t** (79–95) | Thu 20 Aug 2026 | SMM (not exchange) |
| Yangshan (Reuters week) | ~**93 USD/t** | week to Fri 21 Aug | Zawya/Reuters; not the same as SMM 20 Aug 87 |
| China bonded (SMM) | 36,800 t (+1,600 WoW) | Thu 20 Aug 2026 | SMM survey |

**Week path (LME cash official reprint, Westmetall):** Mon 17 Aug **14,850** (ATH reprint; back **+535**) → 14,335 → 14,180 → 14,170 → Fri **14,291**. Backwardation collapsed as stocks rose 207,825 t (17 Aug) → 238,575 t (21 Aug). Reuters (Zawya) 3m **14,187** at 10:21 GMT Fri is **intraday**, not official close. Kitco Sat 01:13 NY 6.4491 USD/lb is **live indicative**.

**Path (Westmetall LME cash official reprints, not CFDs):**

| Window | High | Low |
| --- | --- | --- |
| 2024 | 10,857 (20 May) | 8,085.50 (12 Feb) |
| 2025 | 12,512 (30 Dec) | 8,539 (9 Apr) |
| 2026 YTD through 21 Aug | **14,850 ATH (17 Aug)** | 11,826 (19 Mar) |
| Last 12m cash | 14,850 (17 Aug 2026) | 9,643 (22 Aug 2025) |
| COMEX HGU26 52w (Barchart) | 6.8665 (6 Aug 2026) | 4.6265 (27 Aug 2025) |

Do not mix Investing’s derived 52w low 4.4345 with Barchart 4.6265. Trading Economics CFD ATH ~6.83 is **COMEX/CFD, not LME cash**. Discard stale SMM “21 Aug” comments still quoting LME ~9,721 / SHFE 78,730.

**Dollar/rates:** Reuters cites a weaker dollar as Friday support. **No official DXY or 10y print was retrieved** — no invented rates.

**Failed tape fetches:** LME.com (Cloudflare), CME.com (timeout), FastMarkets official table, Trading Economics (500), SHFE daily form, Lange Fri official table not yet up.

## Physicals

### Official S/D (vintages labelled — do not average)

ICSG 21 Aug 2026 monthly PDF exists but **text was not extracted**. Latest parsed official table is **21 Jul 2026** (data through May 2026).

| Metric | Value | Vintage / period | Source |
| --- | --- | --- | --- |
| World mine (ICSG) | **23,216 kt** | CY 2025 prelim. | ICSG 21 Jul 2026 PR |
| World refined (ICSG) | **28,665 kt** (primary 23,320 + secondary 5,345) | CY 2025 | same |
| World usage (ICSG) | **28,195 kt** | CY 2025 | same |
| 2025 refined balance | **+469 kt** (bonded-adj. +478) | CY 2025, pub. 21 Jul 2026 | same |
| 5M26 mine / refined / usage | mine **−1.9%** (conc. −3.4%, SX-EW +3.5%); refined **+3%**; usage **+2.2%** | Jan–May 2026 | same |
| 5M26 refined balance | **+221 kt** (bonded-adj. **+189 kt**) | Jan–May 2026 | same |
| Mine / refinery util. | mine 80.6% (2025) / 76.6% (5M26); refinery 80.4% / 79.7% | 2025 / 5M26 | same |
| USGS 2025 e | mine **23.0 Mt**; refined **29.0 Mt** | MCS 2026 | USGS (rounded; do not blend with ICSG) |
| ICSG FY2026 forecast | mine **+1.6%**; refined **+0.4%**; usage **+1.6%** (China +1.9%, RoW +1.3%); surplus **+96 kt** | **23 Apr 2026** Lisbon | SMM / ScrapMonster of ICSG PR (official PDF not extracted) |
| ICSG FY2027 forecast | surplus **+377 kt**; mine +2.3%; refined +3%; usage +2% | Apr 2026 | same |
| ICSG FY2026 (prior vintage) | **−150 kt** deficit | **8 Oct 2025** | ICSG Oct 2025 PR |
| WoodMac 2026 | “slight surplus” | 2026 | WoodMac PR; **no kt extracted** |
| Cochilco Chile mine | **5.27 Mt 2026 (−2.6%)**; 5.55 Mt 2027 | released 11 Aug 2026 | LSE/Reuters recap |
| Cochilco world surplus | 225 kt 2026 | Aug 2026 | Industrial Info — **FLAG** primary PDF not fetched |

**IEA vs ICSG conflict:** IEA GCMO 2026 (via Mining.com) says 2025 disruptions **1.5 Mt** (~6% of mined supply) “tipped the refined market into deficit.” That **conflicts** with ICSG July 2025 surplus **+469 kt**. Treat as competing definitions/vintages. IEA 2025 refined *consumption* “almost 28 Mt” is close to ICSG usage 28,195 kt.

**Do not use** E&MJ absolute 24.2 / 30.4 / 28.9 Mt for 2026: they are internally inconsistent with ICSG July 2025 actuals plus ICSG’s own Apr growth rates (that math is ~23.6 / ~28.8 / ~28.6 Mt). Use **growth rates + surplus kt**.

### Disruptions that still bind 2026 tonnes

| Node | Sourced fact |
| --- | --- |
| **Chile** | ICSG 5M26 mine **−8.8%** (conc. −10.7%). Codelco 2025 **1.31 Mt** (lowest in ~3 decades). El Teniente ~−27% in 5M26 after 31 Jul 2025 rockburst; Andes Norte expansion suspended (union: up to 2 years). |
| **Grasberg / Indonesia** | Sep 2025 mud-rush. ICSG Indonesia concentrate **−38%** 5M26. USGS Indonesia mine 2025 e **710 kt** (vs 1,010 in 2024). PTFI (20 May 2026): ~50% then **65% later in 2026**; cathode ~**800 Mlb (~363 kt**, arithmetic); near-full H2 2027. FCX cut 2026 sales **3.4 → 3.1 Blb Cu**. |
| **Kamoa (DRC)** | ICSG DRC concentrate **−31%** 5M26 (SX-EW +7.2%). Ivanhoe 2026 guide tightened to **290–310 kt** anode/blister (was 380–420 early-2026). 2025 388,838 t (100%). IVN owns **39.6%**. |
| **Cobre Panama (FM)** | Full mine **not** restarted (halt Nov 2023). Stockpile only: end-Jun **2.1 Mt ore / ~3.2 kt Cu**; ~**70 kt** recoverable left (~12 months). 2026 guide includes **30–40 kt** from stockpile. Not a restart. |
| **Peru / Zambia / Mongolia** | Peru MINEM CY2025 **2.770 Mt**; 5M26 +3.3% (Reuters). FQM Zambia H1 2026 **184,929 t**. ICSG Mongolia concentrate ~**+23%** (Oyu Tolgoi UG). |
| **Acid / SX-EW** | IEA: Hormuz sulphur + China H2SO4 export ban from May 2026. >15% primary Cu via SX-EW; DRC ~1.5 Mt leached; Chile ~1.2 Mt. |

### Scrap / China

| Metric | Value | Period | Flag |
| --- | --- | --- | --- |
| ICSG secondary refined | **5,345 kt = 18.6%** of world refined | CY 2025 | calculated from ICSG table |
| ICSG secondary 5M26 | 2,140 kt = **17.8%**; **+5.5% YoY** | Jan–May 2026 | ICSG |
| China scrap imports | 7M26 **1.461 Mt (+9.4%)**; Jul 219.1 kt | GACC via SMM | SMM reprint of GACC |
| China share of refined usage | “about **59%**” | 5M26 | ICSG Jul PR |
| China apparent demand | **+3%** (ex bonded); net refined imports **−17%** | 5M26 | ICSG |
| China conc. imports | H1 **14.611 Mt (−0.8%)**; Jul **2.379 Mt (−7.0% YoY)** | GACC via SMM | |
| China cathode imports | Jul **280 kt (−16% YoY)** | GACC via SMM | 7M cumulative 1.674 Mt is **FLAG** (snippet) |
| NBS-type H1 refined | **7.608 Mt +5.2%** | H1 2026 | SunSirs/Mysteel — **FLAG** NBS English not fetched |

### Visible stocks

ICSG end-Jun 2026: LME+COMEX+SHFE **1,066 kt**, **+321 kt / +43% vs end-Dec 2025** (COMEX +151, LME +180, SHFE −10). H1 build is the **tariff / Section 232 metal-into-COMEX** story.

Then LME *drew* from an ~**403 kt** April-area peak toward the low-200s into mid-Aug (cancelled-warrant tightness, cash back). **18–21 Aug unwind:** deliveries + re-warranting; cancelled warrants **77 kt** on 18 Aug (−18.7 kt d/d); cash back **+535 → +56**. COMEX 19 Aug (Vault Report, not CME PDF): registered **447.3k short tons (~406 kt)**; eligible ~267 kt; total ~**673 kt**. SHFE receipts still small vs LME/COMEX (Jin10 19 Aug receipts 56,698 t — not shfe.com.cn).

ICSG world refined stocks EOP May 2026 table: **2,132 kt** (broader than exchanges).

### TC/RCs and the tightness split

| Print | Level | As-of | Source |
| --- | --- | --- | --- |
| 2026 annual TC/RC | **$0 / 0¢** (lowest ever) | CY 2026 annual | Mysteel; IEA |
| Mysteel spot clean conc. TC | **−$176.22/dmt** | 14 Aug 2026 | Mysteel |
| Antaike imported conc. TC | ~**−$176/t**; negative **19 consecutive months** | 7 Aug 2026 | SMM/Antaike |
| Mid-year term | Antofagasta + some China smelters: **spot-index + undisclosed floor** | ~1 Jul 2026 | Reuters / Mysteel |
| Fastmarkets | **not fetched** (paywall) | — | — |

**Mechanics:** high TCs = concentrate abundant vs smelters; **negative TCs = concentrate scarce vs smelter capacity** (smelters pay for feed). 2026 $0 annual + mid-Aug −$176 spot is concentrate tightness vs **China smelter overcapacity**. Acid by-product can keep furnaces running anyway.

**Split tightness (descriptive, not a view):** the tight node is **concentrate** (mine −1.9%, Indonesia conc. −38%, DRC conc. −31%, Chile conc. −10.7%, TCs deeply negative). **Cathode is less tight globally** (ICSG surplus + H1 exchange build) but **regionally tight** (LME cash squeeze; metal parked on COMEX). CSPT >10% 2026 cut pledge is **not** showing in national output (NBS-type H1 refined +5.2%). IEA: China smelter util. ~**85%** vs RoW **<70%**. Mysteel small-smelter util. **−13 ppt**. SMM’s own 2026 conc. “hard deficit” ~606 kt is **FLAG** (consultant model, not ICSG).

## Demand (what grows vs what is the stack)

**IWCC 2024 end-use of Cu/alloy semis** (ICSG Factbook 2025 p.48) — this is the *installed* stack, not the growth increment:

| End-use | Share |
| --- | --- |
| Building construction | 26% |
| Consumer / electronics / cooling | 23% |
| Infrastructure (power & telecom) | 17% |
| Transport | 13% |
| Industrial equipment | 12% |
| Other | 9% |

First-use form: wire **63%**. Construction + infrastructure + industrial = **55%** “build / grid / factory.”

**Growth is not that stack.** IEA (GCMO 2025): China **grid investment was the single largest contributor** to copper demand growth over the prior two years. China is **~58–59%** of world refined usage (ICSG). Property/construction China kt for 2025–26: **not sourced** — do not invent one. Directionally IEA names **grid, not housing starts**.

IEA STEPS (GCMO 2025 copper chapter): 2024 demand **26,717 kt** (cleantech 7,737; other 18,980) → 2030 **31,348** → 2040 **34,137**. Cleantech (grids + EVs + renewables + storage) **7,737 → 10,910 kt by 2030** (+3.2 Mt). IEA does **not** publish a standalone 2026 data-centre kt on the public copper page — **do not invent one**. ICSG Apr 2026 lists data centres qualitatively. ICA EV intensities (Factbook): ICE ~23 kg; BEV **83 kg**.

India: ICA **1,878 kt FY25** (+9.3%). Growth pocket (ICA ~9–9.5% toward ~3 Mt by 2030), **mid-single-digit** of world ~28–29 Mt. Not a China substitute. EU/Japan “subdued” (ICSG Apr 2026).

**CRU 2025–26 end-use table: not sourced.** WoodMac tonne-by-end-use tables: not retrieved. Watch ICSG (apparent refined usage) vs IEA (STEPS total demand) — **do not add the two series.**

## What actually moves copper equities

Miners are **not** a clean LME tracker. Residual vs metal is operating leverage, **Au/Mo/Ag credits**, **volume/guidance**, jurisdiction, and risk-off.

1. **Tape still marks NAV.** FCX can beat and still slip with the metal (MINING.COM, mid-2026: Q2 adj. NI $1.1bn, realized **$6.17/lb**, shares **−2.2%** with copper). COMEX–LME / US tariff metal lock is a **price** event (ICRA: COMEX stocks ~98 kt Jan 2025 → ~**498 kt** Dec 2025) that still marks miner NAV even if “true” demand is unchanged.
2. **Guidance revisions > the spot print** when they change 12–24m volume. FCX Grasberg: 2026 sales **3.4 → 3.1 Blb**, stock **−13%**. IVN Kamoa: 2026 **290–310 kt** (was 380–420). FM 2026 **405–475 kt** only because of **30–40 kt Panama stockpile**, not a restart.
3. **Credits are first-order.** FCX Q2’26 filed mix: Cu **75.7%** of $7,029m; Mo $728m; Au $640m — and Grasberg gold collapsed (123 koz vs 522 koz Q2’25), so 2026 FCX residual is a **Grasberg-gold** story as much as copper volume. SCCO 3-year mix **~75.9% Cu / 10.9% Mo**; FY25 cash cost **$0.58/lb** is credit-heavy. ANTO net **$1.15–1.35/lb** vs **$2.30–2.50** before credits. HBM gold was **38% of Q2’26 revenue** — Cu-Au, not a pure-play. IEA: smelter P&L has flipped from TC/RCs to **Au/Ag/acid + cathode premiums**. Same logic at the mine.
4. **Jurisdiction is a sleeve, not a daily beta.** Cobre Panama = FM 36-month residual. Chile Law 21.591 (1% ad valorem + 8–26% operating-margin royalty; 46.5% total-tax cap) is a **NAV/tax** factor for ANTO/TECK/LUN/CS/FCX-El Abra, not a daily LME driver. ANTO: Los Pelambres already on the new royalty; Centinela/Antucoya stability into **2030/31**.
5. **$0 TC/RC** is **bullish integrated miners / concentrate sellers**, **bearish custom smelters**. Do not use smelters as a copper-equity substitute.
6. **China PMI / State Grid weeks** still dominate incremental demand *perception*. USD and risk-off hit TSX mid-caps (HBM, CS, ERO, FM) harder than SCCO/ANTO. **No sourced 2026 equity-to-LME beta** in this file — do not use blog 1.8–2.2x COPX numbers.

Sourced unit costs (not a WoodMac curve; industry percentile curve **not sourced**): FCX 2026 unit net cash **~$1.90/lb** (Q2 $1.97 ex idle; ~$1.2bn FY26 idle/restoration). SCCO FY25 **$0.58/lb**. ANTO 2026 net **$1.15–1.35**. CS 2026 C1 **$2.45–2.75**. ERO **$2.15–2.35**. LUN Q2 **$2.11**. FM 2026 C1 **$2.15–2.40** (Q2 $2.48 ex-CP / $2.54 incl.). IVN/Kamoa 2026 C1 **$2.60–3.00** (100%). TECK Cu segment GP margin before D&A **65%** in Q2’26.

IEA (Mar 2026): average mine grade **−40% since 1991**; brownfield capex intensity **+65% since 2020**; ~**17 years** discovery-to-production.

## How to cover

| Sleeve | Role | Residual vs LME |
| --- | --- | --- |
| **Producers (core)** | Realized price × payable t − C1; credits; tax; sustaining vs growth capex | Guidance, jurisdiction, credits |
| **Developers / growers** | NAV + FID option | Dilution, timeline, permit |
| **Royalty / streamers** | Only if **copper is the main driver** | **Almost none qualify.** FNV is gold (Panama stream is a kicker). No liquid Cu-majority royalty sourced. **Do not book FNV here.** |
| **Diversified majors** | Exclude as copper-only | BHP / RIO / VALE / AAL / GLEN |
| **Gold names with Cu** | Exclude | NEM / B / AEM stay with Gold |
| **Metal control** | CPER = COMEX futures (K-1). AUM cited **$732m** as of 14 Aug 2026 (third-party). **Not an equity.** COPX is a miners basket overlay. | Roll / curve / tariffs |

Cadence: weekly LME/COMEX/SHFE + bonded + spot TC + China grid/PMI + USD. Quarterly: production, C1, guidance bridge, by-product deck. Event: Panama, Grasberg ramp, Kamoa recovery, Chile tax/permits, US tariff, concentrate tightness.

## First-name slate (recommendation only — do not insert rows)

Liquid names where copper is the **main P&L driver**. Caps are Yahoo/aggregator **~21–22 Aug 2026**. Cu% unsourced for FM, CS, ERO, ANTO, IVN (flagged). Firstmate signs names.

**Core liquid Cu**

| Name | Listing | Why | Sourced intensity / cost | Cap | One risk |
| --- | --- | --- | --- | --- | --- |
| **FCX** | NYSE | Institutional copper proxy; Americas + Grasberg; 2026 sales ~**3.06–3.1 Blb** | Q2’26 filed: Cu **75.7%** of $7,029m; 2026 unit net cash **~$1.90/lb** | Yahoo **$96.1bn** | Grasberg Block Cave / ~$1.2bn idle + gold-volume hole |
| **SCCO** | NYSE / BVL | Lowest-cost large producer; Peru + Mexico; Grupo México 88.9% | 10-K: **~75.9% Cu** over 3 years; FY25 cash cost **$0.58/lb** | Yahoo **$158.6bn** | Thin free float / parent; Peru-Mexico; Mo/Ag credit reversal |
| **ANTO** | LSE | Chile copper (Pelambres, Centinela, Antucoya, Zaldívar) | FY25 **653.7 kt**; 2026 **650–700 kt**; net CC **$1.15–1.35/lb**. Cu% **not broken out** in FY25 PR | Yahoo **£38.1bn** | Chile royalty (Pelambres in) + water/grade + family control |
| **TECK** | NYSE / TSX | Post-coal, copper is the story (QB + HVC/Antamina) | FY25 Cu segment **62% rev / 67% GP**; Q2’26 Cu **75%** of revenue; 2026 **455–530 kt** | Yahoo NYSE **$32.3bn** | QB/TMF capex; zinc residual |
| **LUN** | TSX | Chile/Brazil + Vicuña growth | Q2’26 Cu **~88% of revenue**; cash cost **$2.11/lb**; FY **310–335 kt** | Yahoo **~C$29.6–29.8bn** | Caserones weather/power; Vicuña capex |

**Higher-beta / event**

| Name | Listing | Why | Sourced | Cap | One risk |
| --- | --- | --- | --- | --- | --- |
| **FM** | TSX | Kansanshi/Sentinel + **Cobre Panama option** | 2025 **396 kt**; 2026 **405–475 kt** (incl. 30–40 kt stockpile). Cu% **not sourced** | Yahoo **C$31.0bn** | Panama politics + Zambia power; high beta |
| **IVN** | TSX | Kamoa growth + Western Forelands | **39.6%** of Kamoa; 2026 **290–310 kt** (100%). Kipushi is zinc. Cu% consol. **not sourced** (JV equity) | stockanalysis **C$15.1bn** | DRC recovery + NCI/partner + zinc/Platreef dilution |
| **HBM** | NYSE / TSX | Americas Cu-Au; copper still majority | Gold **38% of Q2’26 revenue** | Yahoo NYSE **$13.4bn** | Will decouple from LME when Au moves |
| **CS** | TSX / ASX | Mid-cap Chile + Arizona | 2025 **225 kt** at C1 $2.44; 2026 **200–230 kt** at **$2.45–2.75**. Cu% **not sourced** | companiesmarketcap **$8.10bn** | Chile labour; MV Optimized capex |
| **ERO** | TSX / NYSE | Brazil (Caraíba, Tucumã) | 2026 **67.5–77.5 kt** at C1 **$2.15–2.35**. Cu% **not sourced** | Yahoo NYSE **$4.11bn** | BRL; Tucumã ramp; Xavantina gold mix |

**Off-slate:** BHP, RIO, VALE, AAL, GLEN. All gold names. **FNV**. CPER is metal control, not a name. No liquid copper-majority royalty sourced — **do not force a royalty line**.

## Working hypotheses (scout, not a view)

These are **not** official and must not be written current.

1. **Tape is already at a cash-official ATH reprint (14,850 on 17 Aug) and still in backwardation**, even after the 18–21 Aug LME stock rebuild. That is a *price* fact, not a house target.
2. **Concentrate is tighter than cathode.** Negative TCs + mine −1.9% vs refined +3% + ICSG surplus is the same sentence: smelters are overbuilt relative to mines; metal can still squeeze locally (LME cash, COMEX park).
3. **ICSG’s own vintage swing is the risk to a “deficit” narrative:** Oct 2025 had 2026 **−150 kt**; Apr 2026 has **+96 kt** (and +377 kt in 2027) on slower usage and more secondary. IEA still talks deficit/gap. A metal view later has to **steelman both**, not average them.
4. **Equity residual that pays:** Grasberg ramp (FCX), Panama binary (FM), Kamoa recovery (IVN), credit mix (SCCO/ANTO/HBM), QB execution (TECK). Not “beta to LME.”
5. **Do not start a copper-metal official view off this scout** until Firstmate/captain promote the task. Missing: LME.com/CME.com official pages, ICSG Aug monthly and Apr PDF primary, Fastmarkets TC, WoodMac surplus kt, data-centre 2026 kt, industry C1 curve.

## Failed / incomplete (do not fill with vibes)

- LME.com official ring and warehouse; CME.com settlement and stocks PDF; SHFE official daily.
- ICSG 23 Apr 2026 forecast PDF; ICSG 21 Aug 2026 monthly PDF text.
- Fastmarkets TC/RC; WoodMac surplus tonnes; CRU end-use; NBS/GACC/Cochilco primaries (used flagged reprints).
- Official DXY / 10y; copper % of revenue for FM, CS, ERO, ANTO, IVN; industry-wide C1 percentiles; 2026 data-centre kt.

## What this does **not** do

No `views/COPPER-METAL.md`. No name rows. No gold rewrite. No ship. No live trade.

Working notes (not the official report): `/workspace/cu-scout-tape.md`, `/workspace/cu-scout-physicals.md`, `/workspace/cu-scout-equities.md`.
