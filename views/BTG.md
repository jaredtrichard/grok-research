# BTG — official view (name)

| Field | Value |
| --- | --- |
| Id | BTG |
| Kind | official view (name) — task **BTG-HOUSE**, kind=**update** |
| Status | **current** |
| As-of | Saturday 22 Aug 2026 (America/New_York) |
| Name | B2Gold |
| Ticker | NYSE American:**BTG** / TSX:**BTO** / NSX:**B2G** |
| Stage | **watch** — no ship, no live trade |
| Official horizon | **3 years — to 22 Aug 2029** |
| 12-month path | check-in only (to 22 Aug 2027) |
| Kit | `/home/box/agent-data/grok-research/reports/HOUSE-MODEL.md` |
| Model | `/home/box/agent-data/grok-research/models/BTG/` |
| Gold | `/home/box/agent-data/grok-research/views/GOLD-METAL.md` **current**. **Not retuned.** |
| Scout | `/home/box/agent-data/grok-research/reports/BTG-SCOUT.md` |
| Official PT | k = YE EV/EBITDA **3.34 / 5.06 / 6.79** (2019–2025 ex 2021). **$8.94 / $15.59 / $4.10**. |

## Thesis

House remake of the **2026 printed guide** into a full segment → IS/BS/CF pack. Volume mid **870 koz** (820–920). AISC mid **$2,460**. 3y gold **$4,900 / $5,900 / $3,900**. Statements **tie** (`models/BTG/tie.json`).

**Official k is sourced.** Window **YE 2019–2025**, drop 2021 (community/nrit parse). E = IS-built audited annual IS. Close = NYSE American BTG last December session (Yahoo chart 22 Aug 2026). EV = N × close + YE net debt. **k low 3.34 / mid-of-range 5.06 / high 6.79.** Official 3y $/sh uses those ks on model E at GOLD-METAL: **$8.94 / $15.59 / $4.10**. 7.0× and FCF yield stay checks. Prior colour $8/$13/$3.50 is not the engine. Vendor EV/EBITDA averages unused.

Ask-user (4,000 tpd / first Regional ore = de-risking, not a 2028 run-rate) **closed**. Stage **watch**.

## k — historical EV/EBITDA

| Piece | Sourced | Role |
| --- | --- | --- |
| E | IS-built from audited annual IS 2019–2025 (`k_history.csv`) | Same definition as the 3y model E |
| YE close | Yahoo chart **BTG** NYSE American last December session (2019-12-31 … 2025-12-31; 2022-12-30 / 2023-12-29 when 31 was a weekend) | Not a vendor multiple |
| YE net debt / N | Audited BS + issued or WASO (labelled) | Stream out of debt |
| Official k | **3.34 / 5.06 / 6.79** (min / mid-of-range / max), window YE 2019–2025 **ex 2021** | 2021 dropped (community/nrit parse) |
| Not used | Alpha 3.2 / 3.4 avgs; AIF monthly high/low; 7.0× | Checks / vendor only |

Range lives in `models/BTG/k_history.md`. 2021 dropped. 2019 (6.79×) is the high; 2022–2025 cluster ~3.3–3.5×. Mid-of-range is **(min+max)/2 = 5.06**, not the median (~3.5). Vendor 3.4× avg unused.

## Official equity deck (3y)

Identity: `$/sh = (E_scenario × k_scenario − net_debt_open − NCI) / 1.489867bn`. Open net debt **$169.510m**. NCI **$32.717m**. E = IS-built 3y run-rate.

| Scenario | Gold | E $m | k | Midpoint | Horizon |
| --- | ---: | ---: | ---: | ---: | --- |
| **3y Base** | 4,900 | 2,670 | **5.06** | **8.94** | 22 Aug 2029 |
| **3y Bull** | 5,900 | 3,452 | **6.79** | **15.59** | 22 Aug 2029 |
| **3y Bear** | 3,900 | 1,888 | **3.34** | **4.10** | 22 Aug 2029 |
| *12m check-in* | *4,500* | *2,357* | *5.06* | *7.88* | *22 Aug 2027* |
| *Spot tape* | *~4,600* | *2,435* | *5.06* | *8.14* | *print only* |

Tape **$5.52** vs 3y-base **$8.94** = 38% cheap. 7× check at $4,900 is **$12.40**. FCF-yield check **$11.10**. Neither is official.

## Tape / gold

- Yahoo BTG **$5.52** close 21 Aug 2026 4:00 p.m. EDT. Mkt cap **$7.292bn**. TSX:BTO close **UNSOURCED** (Alpha printed CA$7.61; not used as the tape).
- Diluted WASO **1,489.867m** (Q2). Convert @ ~$3.17 **ITM** → dilution, not a second debt.
- Kitco **$4,602.40** / TE **$4,607.35** 21 Aug — **not** the forward line.
- GOLD-METAL: 3y **4,900 / 5,900 / 3,900**; 12m check-in **4,500**. TIPS 2.40% 21 Aug.

## Checks (not official)

Identity: `$/sh = (E × k − net_debt_open − NCI) / 1.489867bn`. Open net debt **$169.510m**. NCI **$32.717m**. Stream **$257.3m** not in net debt. E = **IS-built** EBITDA (company adj. EBITDA **UNSOURCED**).

| Node | Gold | Official $/sh | FCF-yield check | 7.0× check | FLAG vs official |
| --- | ---: | ---: | --- | ---: | --- |
| 3y bear | 3,900 | **4.10** | $5.40 @ 11% | 8.75 | **yes** FCF +32%; 7× +113% |
| 12m check | 4,500 | 7.88 | $9.30 @ 9% | 10.95 | FCF +18% |
| Spot tape | ~4,600 | 8.14 | $9.75 @ 9% | 11.30 | FCF +20% |
| 3y base | 4,900 | **8.94** | $11.10 @ 9% | 12.40 | **yes** FCF +24%; 7× +39% |
| 3y bull | 5,900 | **15.59** | $17.60 @ 8% | 16.10 | FCF +13% |

Tape **$5.52** vs official **$8.94** = **38% cheap**. Implied k on model E $2,670m: EV ≈ 5.52×1.4899 + 0.170 + 0.033 = **$8.43bn** → **3.16×** (next to Alpha current 3.2×, unused). That is tape vs model E, not a second mid.

Official gold lever at k_mid 5.06: ~**$0.27/sh per $100** Au (ΔE ≈ $78m / $100 from the $4,900 node). 7× lever ~$0.37 is a check only. Collar leftover notional **UNSOURCED**; 12m check is **pre-collar**.

## Per-segment (2026 guide mid, $4,900)

100% ounces = arithmetic mid of 6 Aug 2026 ranges. See `models/BTG/segments.csv`.

| Segment | 100% koz | % | Attrib koz | Cash op | AISC | Rev $m | Cash op $m | Roy $m | Mine EBITDA $m | Capex $m |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Fekola Complex | 405 | 80 | 324 | 1,110 | 2,745 | 1,984.5 | 449.55 | 346.3 | 1,188.6 | 173.3 |
| Masbate | 190 | 100 | 190 | 950 | 1,505 | 931.0 | 180.5 | 45.4 | 705.1 | 61.6 |
| Otjikoto | 90 | 90 | 81 | 1,250 | 1,905 | 441.0 | 112.5 | 17.6 | 311.0 | 29.8 |
| Goose | 185 | 100 | 185 | 1,710 | 2,820 | 906.5 | 316.4 | 20.3 | 569.9 | 276.6 |
| Fekola Regional | 0 | 65 | 0 | — | — | 0 | 0 | 0 | 0 | 88.6 |
| Gramalote / other expl. | 0 | — | 0 | — | — | 0 | 0 | 0 | 0 | 83.1 |
| **Consol. / corp** | **870** | | **780** | **1,218** | **2,460** | **4,263** | **1,059** | **430** | **2,670** after G&A | **713** |

Royalties = Q2 mine roy / (sold × site px), scaled to scenario gold. Regional 2026 oz **UNSOURCED** (not in 2026 guide). 65/35 is 2028 colour.

## Three statements (3y base @ $4,900)

Full cases in `models/BTG/{is,bs,cf}.csv`. **tie_gap = 0** on every case.

### IS (US$m, 100%, run-rate)

| Line | $m | Kind |
| --- | ---: | --- |
| Gold revenue | 4,263 | computed: 870 koz × $4,900 |
| Production costs | 1,059 | computed: seg oz × guide cash-op mid |
| Royalties & production taxes | 430 | computed: Q2 roy% × gold × oz |
| G&A / SBC / community | 71 / 29 / 5 | computed: H1 × 2 |
| **EBITDA (IS-built)** | **2,670** | computed. Company adj. EBITDA **UNSOURCED** |
| D&A | 506 | computed: H1 DA / H1 sold × 870 koz |
| Interest | 68 | computed: H1 × 2 |
| Current tax | 478 | computed: Q2 tax / Q2 gold rev × EBT (22.79%) |
| Deferred tax | — | **UNSOURCED** (dropped) |
| NI / attrib. NI | 1,619 / 1,462 | computed; NCI = NI × mine-EBITDA weight × (1−own) |

### BS (US$m)

| Stamp | Cash | Debt | Net debt | Equity | Tie |
| --- | ---: | ---: | ---: | ---: | ---: |
| 30 Jun 2026 sourced | 286.6 | 456.1 | 169.5 | 4,004.6 | 0 |
| Working open +$95m RCF | 381.6 | 551.1 | 169.5 | 4,004.6 | 0 |
| Run-rate end @ $4,900 | 1,730.5 | 598.0 | −1,132.5 | (see csv) | 0 |

Stream **$257.3m** not in net debt. Other assets held from the sourced BS (one line). Convert accretion in end debt.

### CF (US$m, 3y base)

| Line | $m | Kind |
| --- | ---: | --- |
| OCF | 2,221 | computed: NI + DA + SBC + **all** IS interest (BTG prints cash interest in financing) |
| Sustaining capex | 474 | computed: H1 sustaining × 2 |
| Growth capex | 239 | computed: H1 (total − sust) × 2 |
| Total mining capex | 713 | 474 + 239 |
| **Company FCF** | **1,508** | OCF − all mining-interest capex |
| Interest paid / div / NCI dist | 21 / 105 / 34 | H1 × 2 |
| Δcash | +1,349 | ties to BS end cash |

WC = **0** labelled (Q2 WC $(118)m not in mid). Buyback path **0** (YTD $172m already in the share count).

## What is not in the $8.94 / $15.59 / $4.10

Regional 2028 oz; Goose 300 koz colour; Gramalote FID; Antelope; invented collar leftover; NCIB path; 2023 Code extra take; invented ETR; street / vendor multiples (Alpha 3.4 unused); NAV at reserve gold or Kitco $4,602; TIPS/DXY path; GDX beta; 2021 k (dropped); 7.0× as official k.

## Invalidation

- **$8.94 invalid up** if GOLD-METAL 3y bull prints **and** the 2026 guide is intact → migrate toward **$15.59**.
- **$8.94 invalid down** if official gold breaks $4,400 with TIPS ≥2.40 **or** the company restates 2026 guide below 820 koz / AISC above $2,550 **or** YE k range reprints with high ≤4 (2019 6.79× falls out) → mid-of-range collapses toward the 2022–25 cluster.
- **$15.59 invalid** if 3y bull gold invalid or the guide is cut.
- **$4.10 invalid** if gold holds $4,400+ and the 2019–25 window still includes a high ≥6.5.
- **Guide restated** below 820 koz or AISC above $2,550 → rebuild segments (k unchanged until the YE window changes).
- **GOLD-METAL migrates** → rerun E × same k; do not retune gold here.
- **Company prints adj. EBITDA** → replace IS-built E (k series should be rebuilt on the same E).

## Rivals

1. **Use 7.0× anyway ($12.40).** Steelman: kit still prints 7× as the T. Rowe check; base FCF check is within 20%. **Loses:** captain forbade a flat 7× as official k. History is the mid.
2. **Use Alpha 3.4× / 2022–25 cluster as k_mid (~$5.90).** Steelman: vendor avg and the recent k cluster sit near 3.3–3.5×, closer to tape 3.16× than 5.06. **Loses on the kit:** official mid is mid-of-range (min+max)/2, not the median. 2019 6.79× stays in the window.
3. **Keep colour $8 on 900 koz 2028.** **Loses** on §3.0: no 2028 guide. $8.94 is a different engine.
4. **Tape $5.52 is right.** Steelman: implied 3.16× on model E, Mali, growth wall, collars, and 2022–25 k. **Loses as the official mid** (38% cheap vs $8.94) unless the YE window drops 2019. Lives as a rival, not the number.
5. **Official mid should haircut to 820 / Goose fire.** **Loses** on §3.0 until the guide is restated.
6. **Convert is a $3.17 floor.** Dilution, not a put.

## Uncertainties

- Mid-of-range **5.06** sits above the 2022–25 cluster (~3.3–3.5×); only 2019 is 6.79×.
- Company adj. EBITDA **UNSOURCED**.
- No FY capex / G&A / ETR guides (H1 × 2).
- Deferred tax, WC, collar leftover notional.
- TSX:BTO close; period-end diluted shares.

## Sources

HOUSE-MODEL; GOLD-METAL current; BTG-SCOUT; `models/BTG/*` including `k_history.csv`; Yahoo chart BTG Dec closes 22 Aug 2026; Alpha Spread averages unused.
