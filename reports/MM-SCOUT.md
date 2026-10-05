# MM-SCOUT — Gold open look

| Field | Value |
| --- | --- |
| Date | Friday 21 Aug 2026 (America/New_York); written early Sat 22 Aug 2026 ET |
| Task id | MM-SCOUT |
| Kind | scout |
| Researcher | Gold (sector id `gold`, GICS 15104030) — not Metals & Mining, not Mara |
| Status of constraints | **No official view. No name rows inserted. No trade. No Cursor cloud.** Slate is a recommendation only. Book still empty of gold names. |

## What this is / is not

Desk scout so Firstmate / captain can decide whether Gold is an open look and which liquid names belong on a first follow-list. Written as a coverage map, not a primer.

This is **not** an official view, not a rating, not a NAV or AISC model, and **not** authorization to insert names into `book.db`. It does not cover copper, iron, steel, lithium, or the rest of Metals & Mining (GICS 151040) except the one-line out-of-scope note below.

Numbers below are only what live sources supported on the pull. If a print or corporate fact was not independently sourced, it is flagged.

## The metal (as-of, sources)

**As-of Friday 21 Aug 2026.** Spot is in the high-$4,500s / low-$4,600s. Prints disagree by venue and timestamp; do not treat any single figure as “the” close.

| Print | Level | As-of | Source |
| --- | --- | --- | --- |
| Kitco spot bid | **$4,602.40/oz** (+$84.20 / +1.86%); ask $4,604.40; day range **$4,508.30–$4,632.90** | 21 Aug 2026, 11:35 p.m. ET | Kitco live gold page (fetched) |
| Trading Economics gold CFD | **$4,607.35/oz** (+$91.57 / +2.03% vs prior $4,515.78) | 21 Aug 2026 (page last updated 22 Aug 2026) | Trading Economics; **CFD, not LBMA/COMEX official** |
| WGC / IBA quarterly avg (LBMA PM) | Q2’26 **$4,506.29**; Q1’26 **$4,872.9** (Q1 record avg); Q4’25 $4,135.2; Q2’25 $3,280.4 | Quarter averages to 30 Jun 2026 | World Gold Council *Gold Demand Trends Q2 2026* (30 Jul 2026), citing ICE Benchmark Administration / Metals Focus |

**Not independently retrieved:** official **LBMA Gold Price AM/PM** for 21 Aug 2026 (IBA license wall). Official **COMEX** front-month settlement for 21 Aug 2026 — secondary recaps conflict ($4,571–$4,680 depending on session/article) so **no COMEX settle is used here**. Parent desk also cited a Nation Thailand / Reuters-style afternoon recap (~$4,624 spot / ~$4,681 futures); that page was not fetched cleanly in this pass.

**2026 path (sourced, not modeled):**

- WGC: Q1 average LBMA PM was the **record quarter** at $4,872.9; Q2 average **−8% q/q**, still **+37% y/y**.
- Trading Economics CFD series: **ATH $5,608.35 in January 2026**; 21 Aug print is **+11.54% m/m, +36.59% y/y**, and they describe Friday as highest since **mid-May**.
- Jefferies via Kitco (4 Aug 2026): gold **sold off ~25% from peak** as the 2026 rate path flipped from **1–2 cuts** to **1–2 hikes**; they had 10y TIPS **~2.41%** vs **~1.94%** at the start of the year (Jefferies numbers, not re-marked here).
- Kitco (same 4 Aug note): metal had been “chained” near **$4,000** into early August on inflation / hike pricing after the **US–Iran / Hormuz** oil shock.

**Why this is the open look now — only what sources support:**

1. **Real yields / Fed path.** Jefferies (Kitco, 4 Aug): abrupt hike repricing and higher real rates were the Q2 drawdown. WGC (Jul ETF note): North American ETF selling tracked **higher inflation and rate expectations, stronger USD**. Trading Economics (21 Aug): Friday’s push through $4,600 came with **lower yields and a weaker dollar** after Treasury **increased planned longer-dated buybacks** (fiscal / debasement tape, not a rate cut).
2. **USD.** WGC Q2 GDT: NA ETF outflows tied in part to a **strengthening dollar** in Q2. TE 21 Aug: dollar **lower** on the Treasury buyback headline. Direction of DXY on Friday was **not** independently marked off a primary FX print.
3. **Central banks.** WGC GDT Q2: official-sector demand **289t** in Q2 (after a weak Q1), **+62% y/y**, back to the last-four-year run-rate. WGC still sees **another strong year, below 2025**. Reported H1 buyers (IMF/CB, 4 Aug WGC): Poland 82t, Uzbekistan 41t, China 40t, Kazakhstan 27t; Turkey −83t and Russia −44t ytd on the *reported* series (GDT total includes an unreported estimate).
4. **ETF flows.** WGC: Q2 ETF **−45t**. H1 still **+$8bn** globally; Asia **+$12bn** (strongest H1 on record); North America **−$7.7bn** (weakest H1 since 2013). June alone **−$8.9bn / −74t**. Holdings end-June **4,047t**; H1 AUM **$526bn (−6%)** on a lower price. GLD/IAU are **instruments**, not equity coverage names.
5. **Geopolitics.** Kitco/Jefferies and WGC/TE all treat the **US–Iran conflict and Hormuz / oil** as a live inflation and safe-haven input. That is a **regime** item, not a quantified beta.

**What is not sourced here:** a live 10y TIPS print for 21 Aug, a live DXY print, July/August ETF tonnes after WGC’s 8 Jul / mid-Aug tables, or company-level AISC / reserve / production figures for the slate.

## How we cover gold (buckets + process)

**GICS.** Sector in the book is **Gold**, id `gold`, **15104030**. MSCI/S&P definition: producers of gold and related products, including companies that mine or process gold **and** “South African finance houses which primarily invest in, but do not operate, gold mines.” Royalty / stream names are **economic gold** even when the GICS tag is sloppy. In practice FNV/WPM/RGLD show up in gold / Materials gold industry screens (e.g. Trefis tags FNV Materials / Gold as of 21 Aug 2026). Do **not** assume every royalty is 15104030; check the tag before a GICS-pure screen. Diversified gold-copper seniors (Barrick especially) still sit on this desk because **gold is the coverage reason**; copper is a footnote, not a second sector.

**Buckets we will actually run:**

| Bucket | What it is | What to watch | How a name gets on coverage |
| --- | --- | --- | --- |
| Bullion / ETFs | GLD, IAU, and the metal | Spot vs real yields, DXY, WGC ETF tonnes, COMEX managed-money, CB monthly | Instruments only. Not equity “names.” Use for beta and flow, not a book row. |
| Senior producers | Multi-asset, liquid NYSE/TSX, index-relevant | NGM / spin, reserve replacement, jurisdictional mix, FCF vs sustaining capex, hedge book | Liquid primary listing + gold as primary P&L + captain can follow the print. First slate starts here. |
| Mid-tier | 0.5–1.5 Moz-class producers, still followable | Guidance credibility, single-asset risk, host-government fiscal take | Same liquidity bar; add when the story is distinct (Canada growth, West Africa fiscal, post-merger integration). |
| Juniors / developers | Non-producers / pre-cash | Study, permit, financing, dilution | **Not first slate.** Need a financing path and a listing the desk can trade. |
| Royalty / streamers | FNV, WPM, RGLD, OR | Counterparty, GEO mix, energy/base-metal tail, Panama / Cobre-type contract risk | One name on the first slate is enough; peers are a watchlist. |

**Process (scout → coverage, no shortcuts):**

1. **Scout (this note):** map buckets, confirm tickers after 2025–26 M&A, propose a liquid first slate. No view, no insert.
2. **Watchlist:** captain / Firstmate picks names. Still no official view. Pull 10-K/AIF, last two quarters, reserve/resource rec, cost guidance, jurisdictional map. **Do not invent AISC or ounces.**
3. **Official view (kind=update):** only after a model skeleton (price deck, GEO/oz, AISC or cash cost, sustaining + growth capex, NAV / CFPS, jurisdictional discount). Adversarial review before “current.”
4. **Ship:** only if a name idea is being pursued. Not this task.

Coverage memory for this researcher lives under Gold, not Metals & Mining.

## First slate (recommendation only — 8 names)

Liquid North American listings. Dual listings flagged. **Barrick is NYSE: B / TSX: ABX, not GOLD.** Newmont **delisted TSX: NGT** (close 24 Sep 2025); follow **NYSE: NEM**. No tiny juniors. No developer on v1 (liquidity). Tickers confirmed via company IR / 2026 press, not folklore.

| Ticker | Name | Bucket | Listing | One-line why |
| --- | --- | --- | --- | --- |
| **NEM** | Newmont Corporation | Senior | **Primary NYSE: NEM** (US). Dual **ASX: NEM, PNGX: NEM**. **TSX: NGT gone** (voluntary delist ~24 Sep 2025). | Only S&P 500 gold senior; 10 Aug 2026 NGM reset ($1.95bn to Barrick, Fiberline/Mike in, consent to Barrick NA IPO). |
| **B** | Barrick Mining Corporation | Senior | **Primary follow NYSE: B** (US). Dual **TSX: ABX** (Canada). **Stale: GOLD.** Name/ticker changed 9 May 2025. | Gold core + copper mix; same 10 Aug NGM deal; **NA gold IPO targeted YE 2026** is the live corporate event. |
| **AEM** | Agnico Eagle Mines Limited | Senior | **NYSE: AEM and TSX: AEM** (Canada). | Lowest-drama senior: Canada-heavy, still AEM/AEM on both boards (IR, Jul 2026 Q2). Quality / jurisdictional benchmark vs NEM/B. |
| **KGC** | Kinross Gold Corporation | Senior | **NYSE: KGC** (US). Dual **TSX: K** (Canada). | Liquid senior with US/Brazil/Mauritania/Chile/Canada book (Q2 29 Jul 2026 release). Tsar-era “KGC only” muscle memory still works on NYSE. |
| **AGI** | Alamos Gold Inc. | Mid-tier | **NYSE: AGI and TSX: AGI** (Canada). | Followable Canada/Mexico mid; still independent (Q2 29 Jul 2026). Do not confuse TSX **AFN** (Ag Growth). |
| **EQX** | Equinox Gold Corp. | Mid-tier → self-described new senior | **NYSE American: EQX and TSX: EQX** (Canada). | Live integration tape: Calibre closed 17 Jun 2025; **Orla closed 31 Jul 2026** (OLA/ORLA to be delisted). Americas scale-up, not a clean senior yet. |
| **BTG** | B2Gold Corp. | Mid-tier | **NYSE American: BTG**. Dual **TSX: BTO**, NSX: B2G (Canada / Namibia). | Liquid mid with Mali fiscal + Goose (Canada) in the same name; Menankoto exploitation permit **7 Aug 2026**; still independent. |
| **FNV** | Franco-Nevada Corporation | Royalty / stream | **NYSE: FNV and TSX: FNV** (Canada). | One royalty is enough for v1: gold-focused, liquid, debt-free pitch (Q2 11 Aug 2026). Watch Cobre Panamá stockpile restart / ministerial process. |

**Identity checks that kept names off or corrected:**

- **SAND / SSL (Sandstorm):** **gone.** Royal Gold closed Sandstorm + Horizon **20 Oct 2025** (0.0625 RGLD / SAND). Do not put SAND on any list.
- **Osisko Gold Royalties:** renamed **OR Royalties Inc.** (TSX/NYSE: **OR**) effective **8 May 2025**. Peer, not first slate.
- **WPM, RGLD:** alive (WPM NYSE/TSX; RGLD Nasdaq). Watchlist, not v1 — one royalty.
- **GOLD:** stale Barrick NYSE ticker.
- **NGT:** stale Newmont TSX ticker.
- **Orla (OLA / ORLA) and Calibre (CXB):** absorbed into EQX.
- **AU, GFI, HMY, EDV:** still independent (AU NYSE; GFI NYSE ADS; EDV LSE/TSX). Held off v1 — GFI/AU/HMY are followable but SA/Ghana/Aus mix is a second-wave problem; EDV is LSE/TSX only.

## What we are not covering yet

- **Out of scope for this report (one line):** copper, iron, steel, lithium, aluminum, diversified miners-as-miners, and the rest of Metals & Mining 151040 — those are not Gold’s book.
- Developers / illiquid juniors (no first-slate developer).
- Second royalty (WPM, RGLD, OR).
- SA / Ghana / West Africa seniors as a group (AU, GFI, HMY, EDV) — jurisdiction pack later.
- Silver / PGM primaries (15104045 / 15104040) even if they have a gold tail.
- Bullion as a “name.” GLD/IAU stay instruments.
- Company AISC, reserve, and production tables — **not built**. Do not use street memory.

## Open questions for Firstmate / captain

1. **Confirm Gold is the covering researcher** (sector id `gold` / 15104030) and that Metals & Mining is **not** dual-covering these names.
2. **Authorize watchlist only, or insert?** This scout says **do not insert** until you say so. If insert, which of the eight — all, or seniors + FNV first?
3. **Barrick NA IPO / NGM:** treat B and NEM as a **paired event** through YE 2026. Who owns the spin model — Gold only, or a cross-note if the IPO is a new ticker?
4. **EQX post-Orla:** keep as mid-tier follow or wait for consolidated 2026 guide (company pointed to the 5 Aug 2026 Q2 print) before it is “senior.”
5. **Price deck for any future view:** need a marked LBMA/COMEX series (not TE CFD), a 10y TIPS / real-rate path, and a CB/ETF flow update past June. Official 21 Aug LBMA fix and COMEX settle were **not** captured.
6. **Royalty GICS:** accept FNV/WPM/RGLD on the Gold book even if a vendor tags one of them outside 15104030?
7. **Developer slot:** skip until a liquid TSX/NYSE name has a financed path, or force one (Skeena / similar) on a later scout?
8. **What would be needed before an official view on any name:** last two 10-K/AIF + MD&A, reserve/resource rec, cost and capex guidance, hedge book, jurisdictional / fiscal map, simple NAV and CFPS vs spot and vs $4,000 / $5,000 brackets, and adversarial review. **None of that is done.**

## Sources

- Kitco, *Gold Price Today*, https://www.kitco.com/charts/gold — fetched 21 Aug 2026 ~11:35 p.m. ET.
- Trading Economics, *Gold*, https://tradingeconomics.com/commodity/gold — fetched 22 Aug 2026 UTC; CFD $4,607.35 on 21 Aug; ATH $5,608.35 Jan 2026.
- World Gold Council, *Gold Demand Trends Q2 2026*, 30 Jul 2026, https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q2-2026 — LBMA PM quarterly averages, ETF −45t, CB 289t.
- World Gold Council, *H1 flows remain positive*, 8 Jul 2026, https://www.gold.org/goldhub/research/gold-etfs-holdings-and-flows/2026/07 — H1 +$8bn, Asia +$12bn, NA −$7.7bn.
- World Gold Council, *Central bank gold statistics: June 2026*, 4 Aug 2026, https://www.gold.org/goldhub/gold-focus/2026/08/central-bank-gold-statistics-june-2026.
- Kitco News / Jefferies, *Gold can recover despite higher real yields…*, 4 Aug 2026, https://www.kitco.com/news/article/2026-08-04/gold-can-recover-despite-higher-real-yields-rate-pressures-ease-says.
- MSCI, *GICS Methodology* (Gold 15104030 definition).
- Barrick / Newmont joint release, *Agreement Regarding Nevada Gold Mines Joint Venture*, 10 Aug 2026 — Barrick IR and Newmont 8-K (CIK 1164727). Tickers: **NYSE: B, TSX: ABX**; **NYSE: NEM, ASX: NEM, PNGX: NEM**. $1.95bn; Fourmile / Fiberline / Mike into NGM; Newmont consent to Barrick NA IPO.
- Barrick, name change and **NYSE ticker GOLD → B**, 6–9 May 2025, barrick.com.
- Newmont, *Voluntarily Delist From Toronto Stock Exchange*, Sep 2025 (effective ~24 Sep 2025); Q1 2026 results header shows NYSE/ASX/PNGX only.
- Agnico Eagle IR stock information and 29 Jul 2026 Q2 PR — NYSE/TSX: AEM.
- Kinross Q2 2026 results, 29 Jul 2026 — TSX: K, NYSE: KGC.
- Alamos Gold Q2 2026, 29 Jul 2026 — TSX/NYSE: AGI.
- Equinox Gold, Calibre close 17 Jun 2025; Orla close 31 Jul 2026 — TSX/NYSE American: EQX.
- B2Gold, Menankoto / Fekola Regional permit, 7 Aug 2026 — TSX: BTO, NYSE American: BTG.
- Franco-Nevada Q2 2026, 11 Aug 2026 — TSX/NYSE: FNV; Cobre Panamá stockpile processing note.
- Royal Gold / Sandstorm close, 20 Oct 2025 — SAND/SSL delisted.
- OR Royalties AIF (Mar 2026) — name change from Osisko Gold Royalties, 8 May 2025; TSX/NYSE: OR.

