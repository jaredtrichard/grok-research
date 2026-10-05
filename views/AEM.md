# AEM — Agnico Eagle Mines (current)

| Field | Value |
| --- | --- |
| Status | **current**. No ship. Stage **watch**. Review empty / risk low. |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Clock | **3y run-rate + path** (2026 guide mid held on the 2026–28 3.3–3.5 Moz box). Not a 2029 volume model. |
| Official k | Sourced YE 2016–25 hist EV/EBITDA **8.10 / 12.00 / 15.89** on remade E. |
| Official 3y $/sh | **$150 / $297 / $494** at gold **$3,900 / $4,900 / $5,900**. Checks: 7.0× $176/$221/$130; FCF 5% ~$263; vendor spot k **10.39**; tape-implied **8.66×**. Do **not** swap official k for tape or vendor spot. |
| k (official identity) | Sourced vendor YE 2016–2025 [wallstreetnumbers AEM EV/EBITDA](https://wallstreetnumbers.com/stocks/aem/ev-ebitda): 11.76, 12.23, 14.34, **15.89**, 12.63, **8.10**, 9.58, 8.99, 8.43, 10.26. Mid = (8.10+15.89)/2 = **12.00**. Spot 21 Aug **10.39**. 7.0× is T. Rowe check only. |
| EBITDA source | Q2 2026 SEC Exhibit 99.1 Financial Results Summary: adj. EBITDA **Q2 $2,738m / H1 $5,748m**. YE 2025 adj. EBITDA **$8,090m**. |
| EBITDA URL | https://www.sec.gov/Archives/edgar/data/2809/000110465926088794/tm2619289d4_ex99-1.htm |
| Net cash | **$3,267m** (30 Jun 2026). Equity = EV + net cash. |
| Shares | **506.36m labelled** (stockanalysis Shares Out 21 Aug). YE issued **500.7684m**. 30 Jun filing count **UNSOURCED**. CVRs **out**. |
| GOLD-METAL | Locked **4900 / 5900 / 3900**. 12m check **4500**. This file does **not** retune metal. **GOLD-METAL.md not touched.** |

Pack: `/home/box/agent-data/grok-research/models/AEM/{segment,is,bs,cf,valuation,tie}.csv`. This view is **current**.

---

## Thesis

Agnico is a Canada-heavy, net-cash senior with a printed 2026–28 volume box of **3.30–3.50 Moz** (mid **3.40**; Q2 2026 SEC 99.1 Guidance Summary **Mid-Point 3,400**), TCC **$1,070** and AISC **$1,475** at a **$4,500** cost deck, and total capex **$3.025bn** after the Hope Bay sanction lift. Q2 2026 printed **record FCF $1,335m** and **adj. EBITDA $2,738m** at realized **$4,483/oz**, with H1 adj. EBITDA **$5,748m** at **$4,672/oz**.

Official equity mid is hist-k **$297** at $4,900 (8.10 / 12.00 / 15.89 on remade E). 7.0× remade adj. EBITDA + $3,267m / 506.36m is a **check**. 5% FCF-yield is a **check**. The company did **not** print an EBITDA / $oz lever — the remake is **FLAG**ed: annualize H1 adj. EBITDA and slope gold with the only printed royalty lever (**$3/oz TCC per $100 gold**) on **3.40 Moz**.

Barnat (lower-end colour, **−60 to −80 koz H2 2026**, **up to −150 koz/yr 2027–28**) sits in the **miss hedge**, not the mid. Hope Bay **2030** ounces, Ikkari, San Nicolás, Upper Beaver first gold, and Rupert CVRs are **out of the number**.

Tape 21 Aug **$216.06** is **above** the 7.0x $4,900 PT (**$176**). Implied multiple on remade E($4,900) **$12,248m** is **~8.66x**. That is a **desk-multiple gap**, not proof the tape has discounted $4,900.

---

## Segment roll-up

Site TCC other than **CM $1,260** (Q2 update) and the **consol $1,020–$1,120** print: pack labels those Feb site costs **computed / not a 2026 guide print** unless a Feb site-TCC table is attached.
 (official **volume** mid = Feb 2026 range mids → 3.40 Moz; not an equity mid)

Units: koz payable gold; TCC US$/oz by-product; revenue / segment cash US$m. Site TCC **held** across gold. Consol royalty lever only.

| Segment | Mid koz | TCC $ (deck) | Q2 koz / TCC (check) | Rev @ $4,900 | Seg cash @ $4,900 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Canadian Malartic | 590 | 1,260 (Q2 update; Feb 1,187) | 135.2 / 1,185 | 2,891 | 2,148 |
| Detour Lake | 715 | 921 | 207.3 / 825 | 3,504 | 2,845 |
| Macassa | 315 | 1,079 | 80.1 / 1,041 | 1,544 | 1,204 |
| Meliadine | 390 | 1,047 | 97.5 / 1,033 | 1,911 | 1,503 |
| Meadowbank | 485 | 930 | 100.2 / 1,206 | 2,377 | 1,925 |
| Fosterville | 150 | 1,374 | 42.0 / 1,114 | 735 | 529 |
| Kittila | 220 | 1,267 | 62.0 / 1,133 | 1,078 | 799 |
| Pinos Altos | 75 | 2,092 | 21.0 / 1,873 | 368 | 211 |
| LaRonde | 340 | 919 | 81.3 / 953 | 1,666 | 1,354 |
| Goldex | 120 | 1,054 | 29.3 / 1,081 | 588 | 462 |
| **Sum mines** | **3,400** | wtd **$1,083** | **855.8 / 1,054** | **16,660** | site then recon |
| recon siteTCC→consol | 0 | −$12.9/oz at $4,500 deck | — | 0 | **~$+3** at $4,900 (site wtd $1,083 vs consol $1,082). −$43.9 is the **$4,500** cost bridge, not this cash column. |
| **Consol** | **3,400** | **1,070 @ $4,500 → 1,082 @ $4,900** | 855.8 / 1,054 | **16,660** | **12,981** |

LaRonde + Goldex are **sourced Feb mids**, not a silent residual plug. They complete **3.40**. Site-weighted TCC **$1,082.9** vs reiterated consol **$1,070** after the CM **$1,260** print — **FLAG** in `tie.csv`; consol **$1,070** wins.

Q1 key-project tighter CM **575–590** / Detour **700–715** is a **check**, not a second mid.

---

## Three statements (numbers)

### Income statement (US$m unless noted)

| Line | Q2 2026 | H1 2026 | FY 2025 | RR $3,900 | RR $4,500 | RR $4,900 | RR $5,900 | source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gold US$/oz | 4,483 | 4,672 | 3,454 | 3,900 | 4,500 | 4,900 | 5,900 | sourced / locked |
| Produced koz | 855.8 | 1,680.9 | 3,447.4 | 3,400 | 3,400 | 3,400 | 3,400 | sourced / guide mid |
| Revenue (gold) | 3,746 | 7,780 | 11,747 | 13,260 | 15,300 | 16,660 | 20,060 | computed |
| TCC US$/oz | 1,054 | 1,073 | 953 | 1,052 | 1,070 | 1,082 | 1,112 | sourced / computed |
| TCC $m | 902 | 1,804 | 3,285 | 3,577 | 3,638 | 3,679 | 3,781 | computed |
| NTI | — | — | 56 | 190 | 190 | 190 | 190 | sourced; gold lever UNSOURCED |
| G&A | — | — | 236 | 245 | 245 | 245 | 245 | sourced mid |
| Other | — | — | 163 | 85 | 85 | 85 | 85 | sourced mid |
| Expl & corp dev | — | — | 207 | 290 | 290 | 290 | 290 | sourced mid |
| **Adj. EBITDA (company)** | **2,738** | **5,748** | **8,090** | — | — | — | — | **sourced** |
| **Adj. EBITDA remade** | — | — | — | **8,950** | **10,929** | **12,248** | **15,546** | computed FLAG λ |
| Guide-build EBITDA | — | — | — | 8,873 | 10,852 | 12,171 | 15,469 | computed |
| D&A | UNSOURCED | UNSOURCED | 1,645 | 1,650 | 1,650 | 1,650 | 1,650 | sourced mid / Q2 UNSOURCED |
| Interest | UNSOURCED | UNSOURCED | UNSOURCED | 0 | 0 | 0 | 0 | UNSOURCED (set 0) |
| ETR | — | — | 33% | 35% | 35% | 35% | 35% | sourced mid |
| NI (company) | 1,600 | 3,296 | 4,461 | — | — | — | — | sourced |
| NI (RR from remake) | — | — | — | 4,745 | 6,031 | 6,889 | 9,032 | computed |

### Balance sheet (US$m)

| Line | 30 Jun 2026 | 31 Dec 2025 | source |
| --- | ---: | ---: | --- |
| Cash | **3,464** | 2,866 | sourced |
| Total debt | **197** | 196 | sourced |
| **Net cash** | **3,267** | 2,670 | sourced; **ties** 3,464 − 197 |
| PPE / AR / other assets / book equity / NCI / leases | **UNSOURCED** | **UNSOURCED** | do not invent |

### Cash flow (US$m)

| Line | Q2 2026 | H1 2026 | FY 2025 | RR $3,900 | RR $4,500 | RR $4,900 | RR $5,900 | source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CFO | 2,144 | 3,490 | 6,817 | — | — | — | — | sourced |
| Capex (total) | 801 | 1,375 | 2,391 | 3,025 | 3,025 | 3,025 | 3,025 | sourced / guide mid |
| **FCF company** | **1,335** | **2,067** | **4,399** | **4,341** | **5,627** | **6,484** | **8,628** | hist sourced; RR computed |
| Cash tax | 623 | 2,400 | 1,178 | 1,507 | 2,200 | 2,662 | 3,816 | hist sourced; RR FLAG |
| Ending cash | 3,464 | 3,464 | 2,866 | 3,464 | 3,464 | 3,464 | 3,464 | held; ties to BS |

Q2 printed FCF **$1,335m** vs CFO − capex **$1,343m** (**+$8m**) — **FLAG**, not plugged. H1 **+48m**, FY25 **+27m**. See `tie.csv`. NI cannot flow to RE (book equity **UNSOURCED**).

---

## Working 7.0× PT table (check only — not official)

**Identity:** `E(G) = 11,496 + 3.298 × (G − 4,672)` → `EV = 7.0 × E(G)` → `Equity = EV + 3,267` → `$/sh = Equity / 506.36`.

**EBITDA source URL:** https://www.sec.gov/Archives/edgar/data/2809/000110465926088794/tm2619289d4_ex99-1.htm

IR mirror: https://www.agnicoeagle.com/English/news-and-media/news-releases/news-details/2026/AGNICO-EAGLE-REPORTS-SECOND-QUARTER-2026-RESULTS---RECORD-QUARTERLY-FREE-CASH-FLOW-REFLECTS-SOLID-OPERATIONAL-PERFORMANCE-RECORD-QUARTERLY-SHAREHOLDER-RETURNS/default.aspx

YE 2025 IR (adj. EBITDA **$8,090m** at realized **$3,454**): https://www.agnicoeagle.com/English/news-and-media/news-releases/news-details/2026/AGNICO-EAGLE-REPORTS-FOURTH-QUARTER-AND-FULL-YEAR-2025-RESULTS---RECORD-QUARTERLY-AND-ANNUAL-FREE-CASH-FLOW-2025-PRODUCTION-GUIDANCE-ACHIEVED-TOTAL-2025-SHAREHOLDER-RETURNS-OF-1-4-BILLION-DIVIDEND-INCREASED-BY-12-5-UPDATED-THREE-YEAR-GUIDANCE/default.aspx

**Remake FLAG:** AEM did **not** print an EBITDA / $1 gold lever. λ uses the **only** company gold print: **$100/oz gold ≈ $3/oz TCC** (Feb YE). Do **not** take (gold − AISC) × oz as the PT.

| Node | Gold | E remade US$m | EV (7.0x) | Equity | $/sh exact | Working $/sh (not official) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 3y bear | 3,900 | 8,950 | 62,650 | 65,917 | 130.18 | **$130** |
| 12m check | 4,500 | 10,929 | 76,501 | 79,768 | 157.53 | **$158 (not official)** |
| **3y base** | **4,900** | **12,248** | **85,736** | **89,003** | **175.77** | **$176** |
| 3y bull | 5,900 | 15,546 | 108,822 | 112,089 | 221.36 | **$221** |

**$ΔP / $100 Au (7x):** **$4.56/sh**. Tape **$216.06** is **above** the 7.0× working tape **$176** by **+23%** (7.0× vs tape is −18.6%; the stock is rich on 7×, cheap on 12× $297). Implied k at tape on E($4,900) ≈ **8.66x**.

---

## FCF-yield check (not official)

Company FCF after **total** capex (Hope Bay cash is real; after-sustaining rejected as the engine).

`FCF(G) = 3.40×(G − TCC(G)) − 190 − 245 − 85 − 290 − cash_tax_rr(G) − 3,025`  
`cash_tax_rr = 2,200 + 35% × Δ guide-EBITDA vs $4,500` (**FLAG**: $2,200 = $3,500 guide − $1,300 2025 residual).

| Node | Gold | FCF US$m | 5.0% yield + net cash / 506.36m |
| --- | ---: | ---: | ---: |
| bear | 3,900 | 4,341 | $177 |
| 12m | 4,500 | 5,627 | $229 |
| base | 4,900 | 6,484 | **$263** |
| bull | 5,900 | 8,628 | $347 |

**3y-base FCF-yield ~$263 vs 7x $176 vs hist-k $297.** Parked: identities disagree; do not average. Official k stays hist. Prior draft $265 / $345 / $180 was the 5% card — **superseded as the official engine**, kept as check. Bear 5.5% check ≈ **$162**.

---

## Miss hedge (not the mid)

| Item | Treatment |
| --- | --- |
| FY2026 “near **lower end**” 3.30 Moz | **Sensitivity only.** Official **volume** mid stays **3.40** until a restated guide. |
| Slope-only 3.30 remake @ $4,900 | ≈ **$175/sh** — FLAG: H1-anchored E_RR barely moves. |
| Volume-scaled hedge: E_RR × 3.30/3.40 + 3.30×0.97×(4900−4672) | E ≈ **$11,895m** → 7x **≈ $171/sh**. Prefer this hedge. |
| Barnat **−60 to −80 koz H2 2026** | In H2 path / hedge. Not a second mid. |
| Barnat **up to −150 koz/yr 2027–28** | Hedge + invalidation only. 2026–28 company box still **3.3–3.5**. |
| CM TCC **$1,260** vs consol **$1,070** | Site line updated; consol reiterated — recon FLAG. |
| Detour Q1 **700–715** vs Feb **700–730** | Check. Mid stays **715**. |

---


## Parked FLAGs (not blockers for a later official; not invented)

| FLAG | Park | Why not closed |
| --- | --- | --- |
| Projected 3y BS | **N/A / snapshot.** EV identity uses 30 Jun **net cash $3,267m** only. PPE / AR / book equity stay **UNSOURCED**. | Do **not** invent a 3y BS. |
| NI → CFO / FCF identity vs printed stmt | **Sensitivity.** Identity FCF vs stmt FCF (~$400m recon class). Q2 CFO−capex $1,343 vs printed FCF $1,335 (**+$8m**). | Residual = cash tax vs book + WC + definition. Not a silent plug. |
| 7.0× / FCF vs hist-k | **Sensitivity.** 7.0× $176 and FCF ~$263 vs official-identity $297. | Do not average. Official k stays hist. 10.39 and 8.66× are checks. |
| EBITDA gold lever | **Sensitivity.** Company did not print λ. Slope uses $3/oz TCC per $100 gold on 3.40 Moz. | Remake FLAG stays labelled. |
| CM TCC $1,260 vs consol $1,070 | **Sensitivity / recon.** | Consol reiterated. |
| 2016–19 high × sloped $4,900-E (metal double-count) | **Sensitivity / invalidation #6.** YE 2021–25 cluster mean **~9.07** → **~$226** on remade E $12,248m. Vendor 10.39 × remade E → **~$258**. Tape-implied 8.66× is the tape. 1Y vendor range 6.36–15.48. TTM E $10.23bn vs remade $12.25bn. | Official k stays 8.10 / 12.00 / 15.89. Do not swap to 10.39 or 8.66. |


## Spot ~$4,600 node (HOUSE §6.1)

Kitco/TE 21 Aug ~**$4,600–$4,607** (not the forward line). Same remake identities:

| Object | k or yield | E or FCF | Working $/sh |
| --- | ---: | ---: | ---: |
| 7.0× check | 7.0 | E ≈ $11,259m | **$162** |
| Vendor spot k 21 Aug | 10.39 on vendor TTM E $10.23bn | vendor object, not remade $4,900 E | tape-consistent by construction |
| Tape-implied on remade E($4,900) | **8.66** | $12,248m | $216 |
| Hist-k mid on remade E($4,600) | 12.00 | E ≈ $11,259m | **$273** |
| Hist-k mid on remade E($4,900) | 12.00 | $12,248m | **$297** |
| FCF 5% check | 5% | FCF ≈ $6,251m | **$253** |

## Invalidation

Official-identity hist-k **$297** (and the 7.0× $176 check) is **invalid** if:

1. AEM **formally cuts** payable-gold guidance **through 3.30 Moz** (PR / MD&A restatement), or Barnat **−150 koz** is printed as a **new** 2027–28 consolidated box below 3.3 Moz.
2. Consol TCC **stuck ≥ $1,220** (high-end $1,120 + $100) at the $4,500 deck, or cash tax run-rate **fails to drop** the $1.3bn 2025 residual after 2026.
3. A printed FY adj. EBITDA lands **well below ~$9bn** at ~$4,500–$4,700 gold (sourced print, not a desk haircut) — i.e. the H1 run-rate is not a 3y object.
4. GOLD-METAL **breaks $4,400** toward $4,000 with the metal invalidation gates — **names re-run; they do not retune gold here**.
5. Net cash **disappears** (Hope Bay + Finland + NCIB + tax) without a matching EBITDA print; or a **diluted filing count ≥ 530m** lands (Rupert paper not offset).
6. **Metal double-count (sensitivity, not a k swap).** YE 2016–19 highs (14–16× at low gold), or even the **12.00** mid, applied to 2026 remade E already sloped to official **$4,900 / $5,900**. Same YE tape already compressed once E rose: 2021–25 **8.10 / 9.58 / 8.99 / 8.43 / 10.26** (mean **~9.07 → ~$226** on E $12,248m). Vendor 21 Aug **10.39 × remade E($4,900) → ~$258**. Tape-implied **8.66×**. If the live object is that compressed cluster, hist-mid **$297** overstates. Official k does **not** move.

---

## Official k tape

`E(G) = 2×H1 adj. EBITDA $11,496m + 3.40×0.97×(G−4,672)` (λ FLAG: company did not print EBITDA/$oz; uses $3/oz TCC per $100 gold).  
`Equity = k × E + $3,267m`; shares **506.36m**. k from YE 2016–25 vendor window.

| Node | Gold | E US$m | k | EV | Equity | Official $/sh |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 3y bear | 3,900 | 8,950 | 8.10 | 72,495 | 75,762 | **150** |
| 12m check | 4,500 | 10,929 | 12.00 | 131,148 | 134,415 | 266 (not a 3y mid) |
| 3y base | 4,900 | 12,248 | 12.00 | 146,976 | 150,243 | **297** |
| 3y bull | 5,900 | 15,546 | 15.89 | 247,026 | 250,293 | **494** |

Tape **$216.06** is **below** official-identity 12.0× **$297** and **above** 7.0× $176. Implied k on E($4,900) ≈ **8.66×**. 10.39 and 8.66× stay **checks**. Do not swap official k.

## Rivals

0. **House-winning objection (steelman).** Official PT *when current is allowed* is this historical-k remake, not 5% FCF and not flat 7×. Kit §4.0: base = mid of sourced history, bull = high, bear = low; 7.0× is the T. Rowe check. That card is **$297 / $494 / $150** — now the **current** official identity. A 7×-only rivals list is how $176 gets smuggled in as official — that is the error this pass closed.

**Parked rival — 2016–19 high × $4,900-E double-counts metal (do not swap k).** Live vendor k 21 Aug is **10.39** on vendor TTM EBITDA **$10.23bn**. Tape-implied on remade E($4,900) is **8.66×** (between 7.0 and hist-bear 8.10). YE 2016–19 highs (14–16×) were printed when gold/E were much lower; applying that high (or even the 12.00 mid) to 2026 E already sloped to official gold **$4,900 / $5,900** can pay for the metal twice. That is a real objection to **$297 / $494**. It lives in **Parked FLAGs (double-count row)** and **invalidation #6**. Official k does **not** move to 10.39 or 8.66. Those stay checks, same as 7.0× and FCF 5%.

1. **Tape already at ~8.7x** on remade E($4,900). 7.0x is a **desk / T. Rowe identity**, not “the market is wrong.” AEM-quality can sit **7.5–8.0x on the cross-check**; working 7.0× is a check, not an official hold.
2. **FCF-yield $263-class** (prior draft $265) is the HOUSE AEM-quality **5%** card. Identities disagree **>20%** because **$3.025bn total capex** (Hope Bay) crushes company FCF vs EBITDA. HOUSE: both printed as checks. Official k stays hist 12.00; do not average with 7× or FCF.
3. **Annualize Q2 $2,738 × 4 = $10,952** instead of H1 × 2. That is **not** the official base (H1 includes Q1 at $4,872-class realized). Using Q2×4 at $4,483 would print a lower E($4,900) and a lower PT — FLAG as an alternate, not used.
4. **Barrick 7.0x** used a **printed** $2.7m EBITDA / $1 oz lever. AEM has **no** such print. Copying Barrick λ would be invention.
5. **NEM** leads FCF yield 8% (residual-risk senior). AEM is not NEM; the 5% check is the AEM-quality bucket, not the official engine on this run.
6. **KGC** correctly refused to copy 7x without sourced EBITDA. Sourced E lets a **7.0× working check** exist; it does **not** license an official 7.0× mid. HOUSE §4.0 official engine (when current is allowed) is sourced historical k.
7. **Shares 500.77m YE** instead of 506.36m tape: official hist-k base **$297** would be **~$300** (~+1%). The old ~$178 figure was the 7.0× check, not the official identity. Filing 30 Jun count still **UNSOURCED**. CVRs are cash-contingent, not shares.

---

## Not in the number

- Hope Bay **2030** 400–435 koz, $2.4bn initial capex beyond the 2026 $3.025bn envelope
- Odyssey shaft #2 / Marban / Wasamac **2033** fill-the-mill ounces
- Detour UG first ore **2028** colour (20–30 koz) — not in the Feb box
- Upper Beaver **2030**, San Nicolás (50% Teck; construction not sanctioned)
- Ikkari / Rupert resources on an AEM basis; **207.7m CVRs** (up to $3.00 cash)
- Barsele 55% close confirmation (UNSOURCED after 30 Jun)
- Invented guide haircut (lower-end 3.30 path-weighted into the mid)
- (gold − AISC) × oz as EBITDA or as the PT
- After-sustaining FCF as the official cash line
- PPE / AR / book equity / leases below the net-cash headline
- Uncommitted NCIB path; period-end 30 Jun share integer
- NGM / Barrick NA IPO facts (not an AEM asset)
- Reserve-price NAV at $1,500–$2,000 or at Kitco $4,602
- Invented TIPS / DXY path; 3y gold S/D rebuild
- Street multiples / street PTs / P/NAV
- GDX / gold-equity beta

---

## Sources

1. Q2 2026 SEC Exhibit 99.1 (adj. EBITDA, FCF, cash/debt, production, guide): https://www.sec.gov/Archives/edgar/data/2809/000110465926088794/tm2619289d4_ex99-1.htm
2. Same release, Agnico IR: https://www.agnicoeagle.com/English/news-and-media/news-releases/news-details/2026/AGNICO-EAGLE-REPORTS-SECOND-QUARTER-2026-RESULTS---RECORD-QUARTERLY-FREE-CASH-FLOW-REFLECTS-SOLID-OPERATIONAL-PERFORMANCE-RECORD-QUARTERLY-SHAREHOLDER-RETURNS/default.aspx
3. YE 2025 / Feb 2026 three-year guide + mine mids + $3/oz TCC lever + FY25 adj. EBITDA $8,090m: https://www.agnicoeagle.com/English/news-and-media/news-releases/news-details/2026/AGNICO-EAGLE-REPORTS-FOURTH-QUARTER-AND-FULL-YEAR-2025-RESULTS---RECORD-QUARTERLY-AND-ANNUAL-FREE-CASH-FLOW-2025-PRODUCTION-GUIDANCE-ACHIEVED-TOTAL-2025-SHAREHOLDER-RETURNS-OF-1-4-BILLION-DIVIDEND-INCREASED-BY-12-5-UPDATED-THREE-YEAR-GUIDANCE/default.aspx
4. 40-F YE 2025 issued shares 500,768,400: https://www.sec.gov/Archives/edgar/data/2809/000110465926032153/R24.htm
5. AEM-SCOUT (21–22 Aug 2026) — Q2 koz/TCC check, source list
6. Vendor YE 2016–2025 EV/EBITDA series (as-of 22 Aug 2026; E as labelled on vendor page): https://wallstreetnumbers.com/stocks/aem/ev-ebitda — working k 8.10 / 12.00 / 15.89 only; not a company print.
7. HOUSE-MODEL — official k = sourced historical EV/EBITDA (7.0× check only); guide-is-mid; GOLD-METAL lock
8. GOLD-METAL (current; **not edited**) — 4900 / 5900 / 3900; 12m 4500
9. Tape: stockanalysis.com NYSE AEM 21 Aug 2026 close $216.06; Shares Out 506.36m (aggregator)

*End AEM official view. Current. No recommendation. No ship.*
