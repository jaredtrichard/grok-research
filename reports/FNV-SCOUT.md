# FNV-SCOUT — Franco-Nevada first look

| Field | Value |
| --- | --- |
| Date | Friday 21 Aug 2026 (America/New_York); written Sat 22 Aug 2026 UTC |
| Task id | FNV-SCOUT |
| Kind | scout |
| Name id | FNV |
| Researcher | Franco-Nevada (name id `FNV`, agent 15010d9e-9fd7-4259-bb9f-c714245e3b3b) |
| Coverage stage | `watch` (not idea, not investment). Do not promote. |
| Status of constraints | **No official view. No ship. No live trade. No Cursor cloud.** No model. No target price. No recommendation. WPM / RGLD / OR are watchlist colour only. SAND does not trade (merged into RGLD 20 Oct 2025). Do not cover BTG. NGM / Barrick NA IPO is NEM–B, not this note. |

Gold tape used as given (MM-SCOUT / Gold 21 Aug). Official LBMA/COMEX 21 Aug not captured. Desk conventions for **this royalty**: GEOs **as FNV reports them**; fixed conversion ratios **beginning 2026** — 2025 GEOs are **not** like-for-like. Do **not** mix FNV GEOs with miner gold koz. **No miner AISC line.** Cash cost / Net GEOs as FNV defines them. Energy / base-metal tail is a **mix footnote**, not a second sector. FCF after corporate; streams have a delivery cost, royalties do not. Realized / implied gold vs this tape — **do not restate at $4,602** unless labelled sensitivity. No street memory.

**Print status (the whole note turns on this):** latest issuer print is **Q2 2026 results + MD&A dated 11 Aug 2026** (call 12 Aug). No later FNV operating print found before 22 Aug 2026 UTC. First Quantum’s Cobre Panamá ops print is **28 Jul 2026** (earlier than FNV’s 11 Aug note).

**Metal tape (use as given; do not invent LBMA/COMEX 21 Aug):**
- Kitco spot bid **$4,602.40/oz** Fri 21 Aug 2026 **11:35pm ET** (range $4,508.30–$4,632.90).
- TE CFD **$4,607.35**; TE ATH **$5,608.35** Jan 2026. **Not LBMA/COMEX.**
- Official 21 Aug LBMA/COMEX not captured.
- WGC Q2 LBMA PM avg **$4,506.29**; Q1 **$4,872.9**.
- Q2 = real-rate/hike-repricing drawdown; 21 Aug bounce = weaker USD / fade in hike odds, not a cut.
- CB Q2 289t; ETF Q2 −45t. GLD/IAU are instruments.
- **FNV’s own Q2 2026 LBMA PM Fix average: $4,517/oz** (Q2 2025 $3,279). Silver LBMA Fix $73.44 (vs $33.64). Source: Q2 2026 MD&A commodity table, 11 Aug 2026. **Not a $4,602 restatement.**

---

## 1. What this note is / is not

A first sourced look at Franco-Nevada as a **gold-focused royalty/stream** (NYSE:FNV / TSX:FNV): model, portfolio, GEOs, cash cost (not AISC), capital, Cobre Panamá / First Quantum counterparty, risks, open questions.

Not a view. Not a ship. Not a rank vs WPM / RGLD / OR. Not a Gold sector view. Not a miner note.

---

## 2. Sources pulled / what could not be got

**Fetched and used (primary), 21–22 Aug 2026:**
- Q2 2026 results PR, 11 Aug 2026 (PR Newswire reprint of issuer release): https://www.prnewswire.com/news-releases/franco-nevada-reports-q2-2026-results-302848909.html
- Q2 2026 MD&A (information as at 11 Aug 2026), SEC EX-99.2 on 6-K acc-no **0001104659-26-094181**, filed 12 Aug 2026: https://www.sec.gov/Archives/edgar/data/1456346/000110465926094181/fnv-20260630xex99d2.htm — local extract `/workspace/fnv-src/q2-mda.txt`. CIK **0001456346**, file 001-35286, Canadian FPI.
- Q2 2026 condensed FS figures as printed in the same PR (income, BS, CF). Full FS exhibit not separately extracted.
- Q1 2026 results PR (Cascabel buy-backs): https://www.prnewswire.com/news-releases/franco-nevada-reports-record-q1-2026-results-302770055.html
- YE 2025 / 2026 guidance: SEC EX-99.1 YE package https://www.sec.gov/Archives/edgar/data/1456346/000110465926025955/fnv-20251231xex99d1.htm and YE MD&A exhibit https://www.sec.gov/Archives/edgar/data/1456346/000110465926032133/fnv-20251231xex99d2.htm (used for FY 2025 GEOs + Cascabel terms; not the live print).
- First Quantum Q2 2026 results, **28 Jul 2026** (operator, Cobre Panamá): https://www.first-quantum.com/news/first-quantum-minerals-reports-second-quarter-2026-results/
- Equity tape 21 Aug 2026: https://stockanalysis.com/stocks/fnv/history/ (NYSE) and https://stockanalysis.com/quote/tsx/FNV/history/ (TSX). Yahoo live tape **not** used.
- FNV IR hub (page located; PDFs not downloaded from Q4): https://www.franco-nevada.com/investors/financials/quarterly-results/default.aspx
- EDGAR company index: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001456346&type=6-K

**Could not get / incomplete:**
- Official 21 Aug LBMA/COMEX (none captured; FNV Q2 average is a **quarter** print, not 21 Aug).
- Native SEDAR+ packages (SEC EX-99.2 + PR used).
- Q2 2026 earnings **presentation / asset handbook PDF** (IR presentation page exists; file not pulled). Seeking Alpha deck page found, not extracted.
- Company IR PDF of the Q2 quarterly report from franco-nevada.com / q4cdn (Q4 listing empty / login wall). Relied on SEC HTML + PR.
- Standalone **cash operating margin** line — FNV does **not** print that phrase in Q2 2026 selected financials. They print Cash Costs, Cash Costs per GEO, Net GEOs, Adjusted EBITDA margin. Any “margin per GEO” below is **computed** and labelled.
- Integer **drawn** revolver balance (BS shows no interest-bearing debt; debt-to-equity “—”; PR says debt-free). Undrawn status is the company pitch, not a bank confirmation.
- Full stream purchase-price schedule (Purchase Commitments table in MD&A not extracted line-by-line).
- FY 2025 cash / revenue complete P&L (FY GEOs sourced; full YE income statement not extracted in this pass).
- Panama ministerial **recommendation date** as an FNV or FM number. Spanish press (La Prensa / Crítica, minister Moltó) says a proposal to President Mulino before year-end 2026 — **not** in the FNV 11 Aug MD&A. Treat as press, not issuer.
- NGM Fourmile / Barrick NA IPO royalty — **not found** in FNV Q2 print. Do not assume. South Arturo is NGM-operated (Carlin plan); that is not Fourmile.
- Consensus / street multiples — not pulled; **no invented multiple**.

---

## 3. Company / listing / tape

- **Issuer:** Franco-Nevada Corporation. Toronto HQ (199 Bay Street, Suite 2000). Canadian FPI. SEC CIK 0001456346. SIC 1040.
- **Listings:** TSX:FNV and NYSE:FNV (same symbol). ISIN CA3518581051 (centralcharts / listings pages).
- **What they are:** gold-focused royalty and streaming company. Do not operate mines. Revenue from NSRs, GMRs, streams, profit-based royalties (NPI/NRI), working interests, other (Q2 MD&A Strategy).
- **CEO:** Paul Brink, President & CEO (Q2 PR). CFO Sandip Rana (quoted in reprints of the call; not needed for this scout).
- **Shares (MD&A as of 11 Aug 2026):** common outstanding **192,873,810**. Options 542,212; RSUs 88,258. Q2 basic WASO **192.9 million**; H1 **192.8 million**. Jun 30 table: 192.9 million vs 192.8 million at 31 Dec 2025.
- **Equity tape Friday 21 Aug 2026** (stockanalysis.com; session stamps as printed):
  - **NYSE:FNV** close **$265.74**, +2.94%, open 266.32 / high 267.59 / low 262.85, volume 1,072,341. “At close: Aug 21, 2026, 4:00 PM EDT.” After-hours 267.25. https://stockanalysis.com/stocks/fnv/history/
  - **TSX:FNV** close **C$365.83**, +2.55%, open 362.76 / high 367.48 / low 361.76, volume 383,101. “Aug 21, 2026, 4:00 PM EST.” https://stockanalysis.com/quote/tsx/FNV/history/
- **Computed market cap (labelled, not a company figure):** 192,873,810 × $265.74 ≈ **$51.25 bn**. EV not computed (cash + undrawn facilities + equity book vs no drawn debt — do not invent net cash construct beyond the cash line).
- **Peers (watchlist colour only):** Wheaton Precious Metals (WPM), Royal Gold (RGLD), OR Royalties (OR). **SAND does not trade** (merged into RGLD 20 Oct 2025). Do not deep-dive peers here.

---

## 4. Royalty / streaming model

How FNV makes money (Q2 MD&A Strategy + GEO section + Costs of Sales):

| Instrument | Mechanic | Cost to FNV after close |
| --- | --- | --- |
| **NSR / GR / similar revenue royalties** | % of proceeds / production, gross of operator AISC | Generally **no** ongoing delivery payment. GEOs estimated **gross**. |
| **Streams** | % of metal produced/sold; FNV buys metal at a contracted ongoing price (often a % of spot or a fixed + inflation) then sells | **Delivery / purchase cost.** Q2 2026 “Costs of stream sales” **$40.6 m** of $45.9 m cash costs. |
| **GMR / NPI / NRI / profit-based** | % of margin or profit | Exposed to **operator costs** (the exception to “no operating-cost leverage”). H1 2026: WI/NPI/NRI/GMR were **12%** of revenue; royalty+stream production-based **88%**. |
| **Working interests** | Participating interest; limited cash calls | The MD&A’s only “additional capital” exception besides initial commitment. |

**GEO definition (company, beginning 2026):** attributable production after recovery/payability. NSR on a gross basis; streams **before** the per-ounce contractual price; NPI after NPI economics; in-kind bullion at receipt. Silver, PGM, iron ore, oil, gas, other converted to GEOs.

**Fixed conversion beginning 2026:** ratios locked to 2026 guidance prices — **$4,500/oz Au, $75.00/oz Ag, $2,000/oz Pt, $1,650/oz Pd, $100/t Fe 62% CFR China, $70/bbl WTI, $3.00/mcf HH**. Replaces 2025 **variable** conversion off prevailing prices. **Q2 2025 / FY 2025 GEOs are not restated.** MD&A: Q2 2026 silver GEOs look larger in part because of a more favourable Ag:Au **assumed** ratio; Diversified GEOs can **fall** even when Diversified **revenue** rises, because the gold denominator is $4,500 not the old spot. Compare like-for-like or say so.

**Net GEOs:** GEOs minus (Cash Costs ÷ gold price used in GEO math). Q2 2026 uses **$4,500** (the fixed assumption), not tape $4,602 and not Q2 LBMA $4,517. Q2: 132,405 − 10,200 = **122,205** Net GEOs.

**No miner AISC.** Inflation leverage is limited except on profit-based interests and on streams whose ongoing price is a % of spot.

---

## 5. Assets / portfolio

**Book at 11 Aug 2026 (MD&A Overview table):** 447 interests — Precious 257 / Other mining 107 / Energy 83. Producing 121 (PM 53, other mining 13, energy 55); Advanced 47; Exploration 279.

Energy is still on the book via U.S. royalties (incl. Continental Royalty Acquisition Venture) and Canadian energy (Weyburn NRI called out). Remaining Continental commitment **$30.1 m** at 30 Jun 2026. Not a second sector — mix footnote.

**Q2 2026 top precious contributors (company GEOs, MD&A narrative + metal-sales table).** Gold-oz column is **gold ounces sold**, not total GEOs, except where MD&A states GEOs:

| Asset | Interest (as printed) | Q2 2026 | Q2 2025 | H1 2026 | Note |
| --- | --- | --- | --- | --- | --- |
| Candelaria | Stream 68% Au / 68% Ag | **13,233 GEOs** (Au oz 10,492; Ag oz 164,457) | 16,648 GEOs | Au oz 22,461 | Phase 11 → 12; H2 weighted (Lundin). |
| Guadalupe-Palmarejo | Stream 50% | 10,084 GEOs | 12,986 | Au oz 21,776 | Lower grade mix YoY. |
| Antapaccay | Stream (indexed) Au+Ag | **10,870 GEOs** (Au oz 8,620; Ag oz 135,000) | 5,630 GEOs | Au oz 15,920 | Higher grade; 2025 delivery shortfall. |
| Antamina | Stream 22.5% Ag | 825,000 Ag oz (~**13,750 Ag-GEOs** at 75/4500) | 700,000 Ag oz | 1,865,000 Ag oz | Q3 deliveries guided lower. Ag-GEO is **fixed-ratio computed**. |
| Musselwhite | NPI 5% | 5,198 GEOs | 2,820 | 6,375 Au oz | **3,951 GEOs are 2025-period** catch-up. |
| Côté Gold | GMR 7.5% | 4,871 GEOs (table Au 4,867) | 418 | 8,797 | Acquired late Jun 2025. IAMGOLD 96,200 oz (100%). |
| Tocantinzinho | Stream 12.5% | 4,766 Au oz | 4,500 | 10,001 | H2 weighted (G Mining). |
| Detour Lake | NSR 2% | 4,043 Au oz | 3,151 | 7,775 | Agnico; UG ramp 180 m at 30 Jun. |
| South Arturo | GR 4–9% | 3,123 GEOs | 1,207 | 7,430 Au oz | **NGM / Carlin plan**, Phase 1 through end-2026. **Not Fourmile.** |
| Western Limb | Stream gold (indexed) | 3,601 Au oz | 2,752 | 8,014 | Sibanye K4 ramp 77% at Jun 2026. |
| Tasiast | NSR 2% | 2,893 Au oz | 2,089 | 5,700 | Kinross. |
| Yanacocha | NSR 1.8% | 2,337 Au oz | 2,412 | 4,875 | Newmont 2026 ~460 koz (100%); H1 272 koz. |
| Cobre Panamá | Stream (indexed) Au+Ag | **— GEOs / $0** | — / 783 H1 2025 Au oz | H1 2026 silver 8,976 oz / **$4.7 m** | Stockpile path; deliveries Q3 (see §9). |
| Cascabel / Alpala | Stream + NSR, **50% bought back Mar 2026** | residual, not a Q2 GEO driver | — | buy-back gain in Q1 | Remaining: stream **7.0% Au** (step-down 4.2% after 262,500 oz delivered); NSR **0.5%**. |

**Material 2025–2026 deals (filings/PRs only):**
- Cascabel 50% stream + 50% NSR buy-back **March 2026** after JCC/SolGold close 4 Mar 2026: **$40.7 m** in gold (net of 20% spot ongoing) + **$97.5 m** cash. Gain **$63.8 m** in Q1 NI and Adjusted NI; **excluded** from Adjusted EBITDA. Residual Cascabel pre-construction payment guided **$11.7 m** in 2026.
- i-80 Gold 1.5% NSR (steps to 3.0% from 1 Jan 2031) closed **16 Mar 2026**, $225 m up front, $25 m contingent.
- Bullabulling (Minerals 260) **26 Feb / 26 Mar 2026**: A$170 m royalty + A$50 m equity (~4.9%).
- Victoria Gold six-royalty book **16 Apr 2026**, $40.0 m (C$55.0 m) — AurMac 6% NSR (5% buy-back), Hyland, Cove milestones.
- Youanmi 1.0% NSR **29 May 2026**, $32.9 m (A$47.0 m).
- Greenstone incremental 5% NPI + 2% NSR (part of EQX property) **22 Jun 2026**, $2.0 m.
- Comet Vale 2.0% GR **15 Jul 2026** (subsequent), $8.4 m + $2.1 m contingent.
- Casa Berardi stream effective **1 Jan 2026** (5% fixed through 2030 then variable; 20% of spot ongoing). Q2 Au oz 1,625.
- Continental RAV still live; H1 contributions $6.4 m; remaining **$30.1 m**.

**Q2 2026 revenue mix (PR + MD&A):** Precious Metals **86%** of revenue (gold 70%, silver 14%, PGM 2%). Americas **88%** (S. America 40%, Canada 25%, U.S. 16%, Central America & Mexico 7%). Diversified **$82.2 m** (Energy $70.4 m: U.S. $46.2 m, Canada $24.2 m; iron/other mining $11.8 m). H1: 89% of revenue from mining assets, of which 87% precious (Strategy).

**Type of interest, Q2 2026 (MD&A):**

| Type | GEOs | Revenue |
| --- | --- | --- |
| Revenue-based royalties | 47,079 | $211.5 m |
| Streams | 66,166 | $287.1 m |
| Profit-based royalties | 16,537 | $70.5 m |
| Interest / other (incl. 9.9% LIORC) | 2,623 | $11.8 m |
| **Total** | **132,405** | **$580.9 m** |

---

## 6. GEOs and production

**Conversion flag:** 2026 = fixed ratios at guidance prices. 2025 comparatives = old variable-price method. Do not stack them as a clean volume CAGR.

| Period | Total GEOs | Net GEOs | Gold oz | Silver oz | PGM oz | Diversified GEOs / rev | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q2 2026 | **132,405** | **122,205** | 91,224 | 1,181,458 (19,695 GEOs) | 7,865 oz / 3,192 GEOs | 18,294 GEOs / $82.2 m | Q2 PR / MD&A |
| Q2 2025 | 112,093 | 101,876 | 78,738 | 1,140,041 (11,520 GEOs) | 7,109 / 2,191 GEOs | 19,644 / $62.7 m | same; **old conversion** |
| H1 2026 | **268,758** | **248,225** | 182,382 | 2,598,799 (43,313 GEOs) | 15,699 / 6,396 GEOs | 36,667 / $164.8 m | same |
| H1 2025 | 238,678 | 215,014 | 164,261 | 2,285,705 (24,011 GEOs) | 14,308 / 4,800 GEOs | 45,606 / $137.5 m | old conversion |
| FY 2025 | **519,106** | — | precious **440,140 GEOs**; diversified **78,966 GEOs** | — | — | see left | YE transcript / YE MD&A exhibit |
| **2026 guidance** | **510,000–570,000** | — | 360–400 koz | 4.7–5.5 Moz | 32–37 koz | Diversified **rev $245–285 m** | Q2 PR; YE guide. ~90% PM / ~10% diversified **at assumed prices** |

Company (11 Aug): tracking **upper half** of 2026 GEO range because of H2 weighting (Candelaria, Tocantinzinho, Côté, Greenstone, Valentine) **plus** anticipated Cobre Panamá stockpile deliveries. Q1 print had said guidance **did not** include incremental Cobre Panamá; Q2 print **includes** anticipated stockpile deliveries in the “upper half” comment.

Energy sensitivity (company, not $4,602 gold): +$10/bbl vs $70 WTI ≈ **+12% oil revenue**. H1 oil revenue **$78.8 m**, +20% vs H1 2025.

**Implied gold vs tape (computed from PR gold line, not a company “realized” label):** Q2 gold revenue $403.0 m / 91,224 oz ≈ **$4,418/oz**. MD&A: average realized **below** Q2 LBMA PM $4,517 because sales were weighted to the back of the quarter as prices were falling. **Do not restate at $4,602.**

---

## 7. Costs / margins

**Not AISC.** FNV Cash Costs = costs of sales **minus** depletion & depreciation (Q2 MD&A non-GAAP). Cash Costs per GEO = Cash Costs / GEOs sold (ex prepaid GEOs).

| | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | Source |
| --- | --- | --- | --- | --- | --- |
| Cash Costs | **$45.9 m** | $33.5 m | **$92.4 m** | $72.0 m | MD&A / PR |
| Cash Costs / GEO | **$347** | $299 | **$344** | $302 | MD&A |
| of which Costs of stream sales | **$40.6 m** | $30.3 m | — | — | MD&A Costs of Sales |
| Mineral production taxes | $1.9 m | $0.8 m | — | — | same |
| Energy costs of sales | $3.4 m | $2.4 m | — | — | same |
| Depletion & depreciation | $84.0 m | $64.0 m | $161.9 m | $132.4 m | PR FS |
| Gross profit | $451.0 m | $271.9 m | $977.3 m | $533.4 m | PR FS |
| Adjusted EBITDA | $529.7 m | $365.7 m | $1,121.6 m | $687.6 m | PR |
| Adj. EBITDA margin | **91.2%** | 99.0% | **91.1%** | 93.2% | PR recon |
| Adj. NI margin | 60.1% | 64.6% | 65.6% | 60.2% | PR recon |
| G&A | $7.8 m | $9.6 m | $17.0 m | $19.0 m | PR FS |

Stream cost rose on (i) more stream ounces and (ii) higher ongoing price on **spot-linked** streams. Royalties do not carry that line. **Do not blend** royalty GEOs and stream GEOs into one “margin” without the label.

**Computed (not a company line) cash operating margin / GEO:** ($580.9 m / 132,405) − $347 ≈ **$4,040/GEO**. Uses blended revenue (royalty + stream + energy + iron). **UNSOURCED as a company KPI.** Net GEOs are the company way to show the stream haircut.

2026 depletion guide **$310–340 m**; H1 actual $161.9 m (in line run-rate). Tax rate guide **20–23%**. Q2 tax $104.9 m.

---

## 8. Capital / balance sheet

**30 Jun 2026 vs 31 Dec 2025 (PR FS + MD&A):**

| | 30 Jun 2026 | 31 Dec 2025 |
| --- | --- | --- |
| Cash & equivalents | **$1,014.2 m** | $670.9 m |
| Royalty/stream/WI, net | $6,262.3 m | $6,043.1 m |
| Investments | $1,215.1 m | $1,141.3 m |
| Total assets | $8,922.2 m | $8,241.4 m |
| Total liabilities | $681.5 m | $606.1 m |
| Equity | $8,240.7 m | $7,635.3 m |
| Interest-bearing debt | **none on the printed BS** | none |
| Debt-to-equity | **—** | **—** |
| Available capital (company) | **$4,305.4 m** | $2,840.1 m |

Available capital (MD&A note 4 / PR endnote 3) = cash $1,014.2 m + equity investments ex-LIORC $1,041.2 m + **$1.5 bn** undrawn revolvers + **$750 m** accordions. Corporate Revolver $1.0 bn, maturity **10 Mar 2031**, accordion $500 m (extended 10 Mar 2026). FNIC Revolver $500 m, maturity **8 May 2029**, accordion $250 m (new 8 May 2026). Company pitch: **debt-free**; facilities exist and are described as available. Drawn balance **not** printed as a positive number.

**Cash flow (not a labelled FCF line):**

| | Q2 2026 | H1 2026 |
| --- | --- | --- |
| Operating cash flow | **$482.5 m** | **$1,002.9 m** (H1 record) |
| Investing | $(101.4) m | $(499.3) m |
| of which acquisition of R/S/WI | $(80.3) m | $(529.7) m |
| Cascabel NSR buy-back proceeds | — | +$97.5 m |
| Financing | $(81.2) m | $(162.0) m |
| Dividends paid (cash) | $80.6 m | $161.1 m |
| Dividends declared | $0.44/sh; $84.0 m incl. DRIP | $0.88/sh; $168.4 m |
| Net change in cash | +$299.5 m | +$343.3 m |

Q2 dividend **US$0.44**, pay **24 Sep 2026**, record **10 Sep 2026**. DRIP treasury at **1%** discount. H1 declared $168.4 m of which $7.3 m in shares.

Other capital: LOMI margin facility C$25 m drawn 17 Jun 2026 ($17.8 m). CRA security released Q1: LC $47.3 m released; cash $44.1 m + ~$5.4 m interest (settlement 11 Sep 2025). Barbados QDMTT $32.8 m still payable; BRA: no penalty/interest if paid by **30 Sep 2026**.

FNV describes itself as a “free cash flow generating business” with no capex beyond initial commitments and limited WI cash calls. They **do not** print a single FCF subtotal in the Q2 selected table. Use OCF and the CF statement; do not invent FCF after corporate.

---

## 9. Cobre Panamá / First Quantum counterparty

**Label the speaker.** Mine on P&SM since **Nov 2023**. Stream is indexed gold (and silver). Q2 2026 FNV GEOs from the mine: **nil** on the gold line; H1 silver 8,976 oz / $4.7 m (MD&A revenue table). While shut / before offtake sales, FNV does **not** earn the historical run-rate. Deliveries are triggered by **First Quantum concentrate sales under offtake**, not by mill start alone.

**Government / process (FNV MD&A 11 Aug + FM PR 28 Jul, consistent on the facts below):**
- GOP approved P&SM plan **30 May 2025**.
- President Mulino (1 Jan 2026 State of the Nation) said GOP would authorize stockpile remove/process/export.
- **7 Apr 2026** MICI **Resolution No. 27** authorized the Processing Program. Resolution states stockpile was mined during the concession’s validity (FNV).
- SGS integral audit; MiAmbiente published final report **19 Jun 2026**: **361/370** commitments, **87.7%**. FM: 7 partial, 3 non-compliant (reforestation suspended since 2023); none “fundamentally absent.”
- High-level **ministerial commission** (Commerce & Industries, Economy & Finance, Environment) to evaluate the mine’s future. **No restart decision** in either issuer print.

**Stockpile execution:**
- First of three milling circuits commissioned **May 2026**; first concentrate. **~2.1 Mt** processed, 0.23% head, 67% recovery, **3,216 t Cu** (FNV and FM).
- FM: total stockpile **~38 Mt**, **~70 kt** recoverable Cu, ~12 months at current rates. Site employment ~2,350 early Apr → **~3,000** end-Jun.
- FM 2026 Cu from stockpile **30–40 kt** (unchanged); remainder 2027 for ~70 kt total. **No Cobre Panamá copper sales in Q2 2026** (FM ops table: sales “—”). That is why FNV stream deliveries are guided to **start Q3 2026**.
- FNV (11 Aug, based on FM estimates): stream deliveries **~23,100 Au oz + 265,000 Ag oz** over the program; **~one-third in H2 2026**.

**What this is not:** a full mine restart. P&SM + stockpile only. Ministerial path is open. Panama press (not FNV/FM) has ministers talking a recommendation to Mulino before end-2026 and no contract-law route — **gap / press only**.

**Counterparty:** First Quantum (TSX:FM). Contract risk + jurisdiction risk sit on this scout. FM Q2: Cobre Panamá negative EBITDA **$51 m** pre-production P&SM; commissioning costs noted. FM net debt $5,407 m at 30 Jun 2026 — operator leverage is a **counterparty** fact, not an FNV debt fact.

---

## 10. Risks

- **Cobre Panamá contract / concession / restart.** Stream value is binary-ish on a durable legal path. Stockpile is a **bridge**, not the mine. Deliveries start only when concentrate is **sold**.
- **First Quantum counterparty.** Operator balance sheet, offtake timing, P&SM funding (~$250 m working-capital-heavy, FM).
- **Jurisdiction.** Panama, plus Peru (Antapaccay, Antamina, Yanacocha), Chile (Candelaria, Caserones), Ecuador residual (Cascabel), Mexico (Palmarejo), Argentina (PSJ/San Jorge RIGI), West Africa (Tasiast, Sabodala, Séguéla), South Africa (Western Limb).
- **GEO mix / conversion.** Fixed 2026 ratios at $4,500 Au **understate** GEOs from non-gold if actual gold >> $4,500 (Diversified GEOs already down YoY on higher gold denominator). Energy/copper/iron are a tail, not a second book — but oil was +20% H1 revenue vs 2025.
- **Profit-based slice.** 12% H1 revenue (NPI/GMR/WI) **does** see operator costs (Musselwhite, Hemlo, Côté GMR, Weyburn NRI).
- **Stream delivery inflation.** Spot-linked ongoing payments rose with the metal tape; cash cost/GEO $347 vs $299.
- **Depletion on new books.** Casa Berardi, i-80, Côté, Yanacocha-era capital — higher D&A per GEO until reserves grow (company comment).
- **Buy-backs.** Cascabel already halved. Guidance excludes other operator-elected buy-backs.
- **Tax.** Transfer-pricing law change enacted 26 Mar 2026 effective 2026 (impact under evaluation). Barbados QDMTT $32.8 m due. CRA 2013–19 settled Sep 2025.
- **Valuation.** No sourced multiple in this pass — **skip**. Do not invent EV/EBITDA or P/NAV.

---

## 11. Open questions

1. When does First Quantum actually **sell** stockpile concentrate, and do Q3 FNV deliveries match the “one-third of ~23.1 koz Au” sketch?
2. What does the ministerial commission recommend, and on what legal vehicle (FNV/FM have not specified; press is not a source for a desk fact)?
3. Does a full Cobre Panamá restart — if any — restore the historical stream, or is the contract rewritten?
4. 2026 GEO conversion vs 2025: will FNV ever publish a **restated** 2025 GEO tape on 2026 ratios?
5. How much of H2 “upper half” is Cobre stockpile vs Candelaria/Côté/Valentine/Greenstone/TZ volume?
6. Continental RAV: deploy the last $30.1 m or let it lapse? Energy still material at $70.4 m Q2 revenue.
7. Residual Cascabel (7% / 0.5%) — first production timing still **UNSOURCED** in this Q2 print (YE call colour had ~2030 / 15–20 koz; that is **call memory**, not reused as a fact here).
8. Drawn vs undrawn confirmation on the two revolvers at a date later than 30 Jun.
9. Q2 presentation / asset handbook asset-level GEO waterfall (not pulled).
10. Any **Fourmile / NGM HoldCo** royalty? Not in the Q2 book as named. South Arturo ≠ Fourmile.

---

## 12. What this does NOT decide

No official view. No ship. No live trade. No Cursor cloud. No model. No target. No recommendation. No rank vs WPM, RGLD, or OR. No Gold sector stance. No BTG. No promotion from watch to idea.

Franco-Nevada is a **royalty/stream** with a still-live energy tail, a **fixed-2026 GEO ruler**, and a **Cobre Panamá stockpile-not-restart** tape. That is the watchlist file. It is not a decision.

---

## Source key (short)

- FNV Q2 2026 PR, 11 Aug 2026: https://www.prnewswire.com/news-releases/franco-nevada-reports-q2-2026-results-302848909.html
- FNV Q2 2026 MD&A EX-99.2, 11 Aug 2026 / 6-K 12 Aug 2026: https://www.sec.gov/Archives/edgar/data/1456346/000110465926094181/fnv-20260630xex99d2.htm
- FNV Q1 2026 PR (Cascabel): https://www.prnewswire.com/news-releases/franco-nevada-reports-record-q1-2026-results-302770055.html
- FNV YE 2025 EX-99.1 / EX-99.2 (FY GEOs, Cascabel terms, 2026 guide): https://www.sec.gov/Archives/edgar/data/1456346/000110465926025955/fnv-20251231xex99d1.htm
- FM Q2 2026 PR, 28 Jul 2026: https://www.first-quantum.com/news/first-quantum-minerals-reports-second-quarter-2026-results/
- NYSE tape 21 Aug: https://stockanalysis.com/stocks/fnv/history/
- TSX tape 21 Aug: https://stockanalysis.com/quote/tsx/FNV/history/
- Gold frame: MM-SCOUT / Gold, 21 Aug 2026 (as given).
