# SpaceX segment model

as_of: 2026-08-30
units: USD millions unless stated otherwise
generator: `compute.py`

Forecast drivers are `[VIEW; as_of 2026-08-30; not a filing line]` and implement the captain's 2026-08-30 overlay on `memory/spcx/research.md`. Historical facts point to `memory/spcx/register.md`. Internal Falcon launches do not create Launch Services revenue. Starship commercial revenue is a separate view. Starshield remains a memo inside Enterprise & Government; standalone P&L is **not obtained**.

## Explicit forecast drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Customer / internal Falcon / Starship launches | 22.0 / 58.0 / 2.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Space — Launch Services / Starship overlay |
| H2 2026E | Launch revenue per customer launch | $65.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` recognized revenue per customer launch; list price remains not obtained |
| H2 2026E | Starship commercial flights / assumed revenue per flight | 1.0 / $150.0 [VIEW; as_of 2026-08-30; not a filing line] | Commercial overlay; prospectus H2 2026 payload-to-orbit expectation is the start, but this is not a filing line |
| H2 2026E | Ending subscribers / monthly ARPU | 14.0m / $64.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity — Consumer |
| H2 2026E | Enterprise & Government | $3,300.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity — Enterprise & Government; no Starshield split |
| H2 2026E | Pending EchoStar spectrum/mobile revenue | $100.0 [VIEW; as_of 2026-08-30; not a filing line] | Pending spectrum-enabled mobile overlay; not a filing line |
| H2 2026E | Advertising | $760.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI — Advertising |
| H2 2026E | Solutions & Infrastructure | $5,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside |
| H2 2026E | Cursor revenue | $1,000.0 [VIEW; as_of 2026-08-30; not a filing line] | Cursor memo line rolls into AI; revenue is not obtained from a filing |
| FY2027E | Customer / internal Falcon / Starship launches | 45.0 / 130.0 / 20.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Space — Launch Services / Starship overlay |
| FY2027E | Launch revenue per customer launch | $67.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` recognized revenue per customer launch; list price remains not obtained |
| FY2027E | Starship commercial flights / assumed revenue per flight | 12.0 / $150.0 [VIEW; as_of 2026-08-30; not a filing line] | Commercial overlay; prospectus H2 2026 payload-to-orbit expectation is the start, but this is not a filing line |
| FY2027E | Ending subscribers / monthly ARPU | 18.0m / $61.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity — Consumer |
| FY2027E | Enterprise & Government | 30.0% growth [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity — Enterprise & Government; no Starshield split |
| FY2027E | Pending EchoStar spectrum/mobile revenue | $1,000.0 [VIEW; as_of 2026-08-30; not a filing line] | Pending spectrum-enabled mobile overlay; not a filing line |
| FY2027E | Advertising | 10.0% growth [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI — Advertising |
| FY2027E | Solutions & Infrastructure | 45.0% growth [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside |
| FY2027E | Cursor revenue | $3,000.0 [VIEW; as_of 2026-08-30; not a filing line] | Cursor memo line rolls into AI; revenue is not obtained from a filing |
| FY2028E | Customer / internal Falcon / Starship launches | 50.0 / 140.0 / 60.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Space — Launch Services / Starship overlay |
| FY2028E | Launch revenue per customer launch | $69.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` recognized revenue per customer launch; list price remains not obtained |
| FY2028E | Starship commercial flights / assumed revenue per flight | 50.0 / $140.0 [VIEW; as_of 2026-08-30; not a filing line] | Commercial overlay; prospectus H2 2026 payload-to-orbit expectation is the start, but this is not a filing line |
| FY2028E | Ending subscribers / monthly ARPU | 22.5m / $59.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity — Consumer |
| FY2028E | Enterprise & Government | 25.0% growth [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity — Enterprise & Government; no Starshield split |
| FY2028E | Pending EchoStar spectrum/mobile revenue | $2,500.0 [VIEW; as_of 2026-08-30; not a filing line] | Pending spectrum-enabled mobile overlay; not a filing line |
| FY2028E | Advertising | 8.0% growth [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI — Advertising |
| FY2028E | Solutions & Infrastructure | 30.0% growth [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside |
| FY2028E | Cursor revenue | $5,000.0 [VIEW; as_of 2026-08-30; not a filing line] | Cursor memo line rolls into AI; revenue is not obtained from a filing |

## Forecast cost and capital drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Space cost of revenue | 35.0% Launch Services / 45.0% Launch & Development [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Space segment drivers |
| H2 2026E | Starship commercial cost of revenue | 60.0% of Starship commercial revenue [VIEW; as_of 2026-08-30; not a filing line] | Commercial overlay economics; not a filing line |
| H2 2026E | Space R&D / SG&A | $2,200.0 / $200.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Starship overlay and Corporate |
| H2 2026E | Connectivity cost of revenue | 50.0% Consumer / 32.0% Enterprise & Government [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity segment drivers |
| H2 2026E | Connectivity R&D / SG&A | $350.0 / $350.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity segment drivers |
| H2 2026E | Spectrum/mobile cost of revenue | 50.0% of spectrum/mobile revenue [VIEW; as_of 2026-08-30; not a filing line] | Pending EchoStar overlay; not a filing line |
| H2 2026E | AI cost of revenue | 30.0% Advertising / 45.0% Solutions & Infrastructure [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI segment drivers |
| H2 2026E | AI R&D / SG&A | $4,500.0 / $1,100.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI segment drivers |
| H2 2026E | Cursor cost / R&D / SG&A | 25.0% / 70.0% / 25.0% of Cursor revenue [VIEW; as_of 2026-08-30; not a filing line] | Cursor P&L view; not a filing line |
| H2 2026E | Capex unit drivers | $28.5/launch; $822.0/net add; AI $18,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Capital cycle |
| FY2027E | Space cost of revenue | 34.0% Launch Services / 44.0% Launch & Development [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Space segment drivers |
| FY2027E | Starship commercial cost of revenue | 50.0% of Starship commercial revenue [VIEW; as_of 2026-08-30; not a filing line] | Commercial overlay economics; not a filing line |
| FY2027E | Space R&D / SG&A | $4,200.0 / $220.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Starship overlay and Corporate |
| FY2027E | Connectivity cost of revenue | 47.0% Consumer / 30.0% Enterprise & Government [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity segment drivers |
| FY2027E | Connectivity R&D / SG&A | $1,000.0 / $1,100.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity segment drivers |
| FY2027E | Spectrum/mobile cost of revenue | 40.0% of spectrum/mobile revenue [VIEW; as_of 2026-08-30; not a filing line] | Pending EchoStar overlay; not a filing line |
| FY2027E | AI cost of revenue | 28.0% Advertising / 40.0% Solutions & Infrastructure [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI segment drivers |
| FY2027E | AI R&D / SG&A | $8,000.0 / $2,500.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI segment drivers |
| FY2027E | Cursor cost / R&D / SG&A | 25.0% / 50.0% / 25.0% of Cursor revenue [VIEW; as_of 2026-08-30; not a filing line] | Cursor P&L view; not a filing line |
| FY2027E | Capex unit drivers | $27.0/launch; $800.0/net add; AI $30,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Capital cycle |
| FY2028E | Space cost of revenue | 32.0% Launch Services / 42.0% Launch & Development [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Space segment drivers |
| FY2028E | Starship commercial cost of revenue | 40.0% of Starship commercial revenue [VIEW; as_of 2026-08-30; not a filing line] | Commercial overlay economics; not a filing line |
| FY2028E | Space R&D / SG&A | $3,600.0 / $230.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Starship overlay and Corporate |
| FY2028E | Connectivity cost of revenue | 45.0% Consumer / 29.0% Enterprise & Government [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity segment drivers |
| FY2028E | Connectivity R&D / SG&A | $1,200.0 / $1,300.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Connectivity segment drivers |
| FY2028E | Spectrum/mobile cost of revenue | 35.0% of spectrum/mobile revenue [VIEW; as_of 2026-08-30; not a filing line] | Pending EchoStar overlay; not a filing line |
| FY2028E | AI cost of revenue | 27.0% Advertising / 36.0% Solutions & Infrastructure [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI segment drivers |
| FY2028E | AI R&D / SG&A | $8,500.0 / $2,900.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` AI segment drivers |
| FY2028E | Cursor cost / R&D / SG&A | 25.0% / 40.0% / 20.0% of Cursor revenue [VIEW; as_of 2026-08-30; not a filing line] | Cursor P&L view; not a filing line |
| FY2028E | Capex unit drivers | $25.0/launch; $750.0/net add; AI $25,000.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` Capital cycle |

Kit revenue, churn, launch list price, Falcon 9/Heavy mix, Starshield standalone results, GPU-hours and utilization remain **not obtained**. Consumer revenue therefore models service revenue only; kit contribution is zero `[VIEW; as_of 2026-08-30; not a filing line]`, not a claim that kits have no value. Cursor revenue and costs are explicit `[VIEW; as_of 2026-08-30; not a filing line]` memo lines inside AI from H2 2026 onward; Cursor is not back-cast into Q2.

## Revenue lines

| line | FY2023 | FY2024 | FY2025 | H1 2026A | FY2026E | FY2027E | FY2028E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Launch Services | $1,963.5 [DEDUCTED F001] | $2,588.9 [DEDUCTED F003] | $2,574.2 [DEDUCTED F005] | $978.0 [FACT] | $2,408.0 [DEDUCTED F011] | $3,015.0 [DEDUCTED F020] | $3,450.0 [DEDUCTED F028] |
| Launch & Development | $1,593.5 [DEDUCTED F002] | $1,207.1 [DEDUCTED F004] | $1,511.8 [DEDUCTED F006] | $603.0 [FACT] | $1,303.0 [DEDUCTED F012] | $1,459.4 [DEDUCTED F021] | $1,634.5 [DEDUCTED F029] |
| Starship Commercial | **not obtained** | **not obtained** | **not obtained** | $0.0 [FACT] | $150.0 [DEDUCTED F013] | $1,800.0 [DEDUCTED F027] | $7,000.0 [DEDUCTED F035] |
| Consumer | **not obtained** | **not obtained** | **not obtained** | $4,633.0 [FACT] | $9,625.0 [DEDUCTED F014] | $11,712.0 [DEDUCTED F023] | $14,337.0 [DEDUCTED F031] |
| Enterprise & Government | **not obtained** | **not obtained** | **not obtained** | $2,915.0 [FACT] | $6,215.0 [DEDUCTED F015] | $8,079.5 [DEDUCTED F024] | $10,099.4 [DEDUCTED F032] |
| Spectrum / Mobile Overlay | **not obtained** | **not obtained** | **not obtained** | $0.0 [FACT] | $100.0 [DEDUCTED F016] | $1,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $2,500.0 [VIEW; as_of 2026-08-30; not a filing line] |
| Advertising | **not obtained** | **not obtained** | **not obtained** | $710.0 [FACT] | $1,470.0 [DEDUCTED F017] | $1,617.0 [DEDUCTED F025] | $1,746.4 [DEDUCTED F033] |
| Solutions & Infrastructure | **not obtained** | **not obtained** | **not obtained** | $2,669.0 [FACT] | $7,669.0 [DEDUCTED F018] | $11,120.1 [DEDUCTED F026] | $14,456.1 [DEDUCTED F034] |
| Cursor | **not obtained** | **not obtained** | **not obtained** | $0.0 [FACT] | $1,000.0 [DEDUCTED F019] | $3,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $5,000.0 [VIEW; as_of 2026-08-30; not a filing line] |
| **Space revenue** | $3,557.0 [FACT] | $3,796.0 [FACT] | $4,086.0 [FACT] | $1,581.0 [FACT] | $3,861.0 [DEDUCTED F050] | $6,274.4 [DEDUCTED F074] | $12,084.5 [DEDUCTED F099] |
| **Connectivity revenue** | $3,869.0 [FACT] | $7,599.0 [FACT] | $11,387.0 [FACT] | $7,548.0 [FACT] | $15,940.0 [DEDUCTED F054] | $20,791.5 [DEDUCTED F078] | $26,936.4 [DEDUCTED F103] |
| **AI revenue** | $2,961.0 [FACT] | $2,620.0 [FACT] | $3,201.0 [FACT] | $3,379.0 [FACT] | $10,139.0 [DEDUCTED F058] | $15,737.1 [DEDUCTED F082] | $21,202.4 [DEDUCTED F107] |

Historical Connectivity and AI sub-lines that were not disclosed as absolute annual values remain **not obtained**; reportable-segment totals are shown as `[FACT]`. Historical Launch Services uses the rounded disclosed mix and is therefore `[DEDUCTED]`.

## Reportable-segment operating statements

| period | segment | revenue | cost of revenue | R&D | SG&A | restructuring | impairment | EBIT |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FY2023 | Space | $3,557.0 [FACT] | $1,669.0 [FACT] | $1,538.0 [FACT] | $351.0 [FACT] | $0.0 [FACT] | $0.0 [FACT] | $(1.0) [FACT] |
| FY2023 | Connectivity | $3,869.0 [FACT] | $2,786.0 [FACT] | $381.0 [FACT] | $233.0 [FACT] | $0.0 [FACT] | $0.0 [FACT] | $469.0 [FACT] |
| FY2023 | AI | $2,961.0 [FACT] | $1,655.0 [FACT] | $186.0 [FACT] | $1,081.0 [FACT] | $237.0 [FACT] | $3,775.0 [FACT] | $(3,973.0) [FACT] |
| FY2024 | Space | $3,796.0 [FACT] | $1,541.0 [FACT] | $1,835.0 [FACT] | $375.0 [FACT] | $0.0 [FACT] | $24.0 [FACT] | $21.0 [FACT] |
| FY2024 | Connectivity | $7,599.0 [FACT] | $4,768.0 [FACT] | $453.0 [FACT] | $333.0 [FACT] | $0.0 [FACT] | $39.0 [FACT] | $2,006.0 [FACT] |
| FY2024 | AI | $2,620.0 [FACT] | $1,687.0 [FACT] | $1,176.0 [FACT] | $1,105.0 [FACT] | $213.0 [FACT] | $0.0 [FACT] | $(1,561.0) [FACT] |
| FY2025 | Space | $4,086.0 [FACT] | $1,352.0 [FACT] | $3,004.0 [FACT] | $349.0 [FACT] | $0.0 [FACT] | $38.0 [FACT] | $(657.0) [FACT] |
| FY2025 | Connectivity | $11,387.0 [FACT] | $5,921.0 [FACT] | $575.0 [FACT] | $468.0 [FACT] | $0.0 [FACT] | $0.0 [FACT] | $4,423.0 [FACT] |
| FY2025 | AI | $3,201.0 [FACT] | $2,178.0 [FACT] | $5,064.0 [FACT] | $1,827.0 [FACT] | $487.0 [FACT] | $0.0 [FACT] | $(6,355.0) [FACT] |
| H1 2026A | Space | $1,581.0 [FACT] | $610.0 [FACT] | $2,006.0 [FACT] | $169.0 [FACT] | $0.0 [FACT] | $0.0 [FACT] | $(1,204.0) [FACT] |
| H1 2026A | Connectivity | $7,548.0 [FACT] | $3,711.0 [FACT] | $499.0 [FACT] | $494.0 [FACT] | $0.0 [FACT] | $0.0 [FACT] | $2,844.0 [FACT] |
| H1 2026A | AI | $3,379.0 [FACT] | $1,562.0 [FACT] | $4,557.0 [FACT] | $995.0 [FACT] | $(9.0) [FACT] | $0.0 [FACT] | $(3,726.0) [FACT] |
| FY2026E | Space | $3,861.0 [DEDUCTED F050] | $1,515.5 [DEDUCTED F051] | $4,206.0 [DEDUCTED F052] | $369.0 [DEDUCTED F053] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $(2,229.5) [DEDUCTED F064] |
| FY2026E | Connectivity | $15,940.0 [DEDUCTED F054] | $7,313.0 [DEDUCTED F055] | $849.0 [DEDUCTED F056] | $844.0 [DEDUCTED F057] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $6,934.0 [DEDUCTED F066] |
| FY2026E | AI | $10,139.0 [DEDUCTED F058] | $4,290.0 [DEDUCTED F059] | $9,757.0 [DEDUCTED F060] | $2,345.0 [DEDUCTED F061] | $(9.0) [DEDUCTED F062] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $(6,244.0) [DEDUCTED F068] |
| FY2027E | Space | $6,274.4 [DEDUCTED F074] | $2,567.2 [DEDUCTED F077] | $4,200.0 [VIEW; as_of 2026-08-30; not a filing line] | $220.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $(712.9) [DEDUCTED F089] |
| FY2027E | Connectivity | $20,791.5 [DEDUCTED F078] | $8,328.5 [DEDUCTED F081] | $1,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $1,100.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $10,363.0 [DEDUCTED F091] |
| FY2027E | AI | $15,737.1 [DEDUCTED F082] | $5,650.8 [DEDUCTED F085] | $9,500.0 [DEDUCTED F086] | $3,250.0 [DEDUCTED F087] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $(2,663.7) [DEDUCTED F093] |
| FY2028E | Space | $12,084.5 [DEDUCTED F099] | $4,590.5 [DEDUCTED F102] | $3,600.0 [VIEW; as_of 2026-08-30; not a filing line] | $230.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $3,664.0 [DEDUCTED F114] |
| FY2028E | Connectivity | $26,936.4 [DEDUCTED F103] | $10,255.5 [DEDUCTED F106] | $1,200.0 [VIEW; as_of 2026-08-30; not a filing line] | $1,300.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $14,180.9 [DEDUCTED F116] |
| FY2028E | AI | $21,202.4 [DEDUCTED F107] | $6,925.7 [DEDUCTED F110] | $10,500.0 [DEDUCTED F111] | $3,900.0 [DEDUCTED F112] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $0.0 [VIEW; as_of 2026-08-30; not a filing line] | $(123.3) [DEDUCTED F118] |

Corporate / eliminations operating revenue and expense are zero `[FACT]` because the filed reportable segments reconcile to consolidated EBIT. Financing sits below EBIT in `income.md`.

## Starship overlay

| period | line | value | treatment |
| --- | --- | --- | --- |
| FY2025 | Starship-specific R&D | $3,004 [FACT] | `research.md` Starship overlay |
| H1 2026A | Space R&D, mainly Starship | $2,006 [FACT] | Exact Starship-only amount not obtained |
| FY2026E | Commercial overlay | 1.0 flight × $150.0 = $150.0 [DEDUCTED F013] | View anchored to the prospectus H2 2026 payload-to-orbit expectation; not a filing revenue line |
| FY2027E | Commercial overlay | 12.0 flights × $150.0 = $1,800.0 [DEDUCTED F027] | Assumed cadence and yield; list price not obtained |
| FY2028E | Commercial overlay | 50.0 flights × $140.0 = $7,000.0 [DEDUCTED F035] | Assumed cadence and yield; list price not obtained |
| FY2026E | Space R&D / Starship overlay | $4,206.0 [DEDUCTED F052] | H1 actual plus H2 view |
| FY2027E | Space R&D / Starship overlay | $4,200 [VIEW; as_of 2026-08-30; not a filing line] | Commercial revenue does not remove development spend |
| FY2028E | Space R&D / Starship overlay | $3,600 [VIEW; as_of 2026-08-30; not a filing line] | Commercial revenue does not remove development spend |

Starship filing revenue, standalone capex, list price, payload economics and cost per test remain **not obtained**. The forecast's non-zero commercial revenue is a labeled cadence × assumed revenue-per-flight view.

## Cursor memo P&L — rolls into AI

| period | revenue | cost of revenue | R&D | SG&A | EBIT |
| --- | ---: | ---: | ---: | ---: | ---: |
| FY2026E | $1,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $250.0 [DEDUCTED F046] | $700.0 [DEDUCTED F048] | $250.0 [DEDUCTED F049] | $(200.0) [DEDUCTED F314] |
| FY2027E | $3,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $750.0 [DEDUCTED F071] | $1,500.0 [DEDUCTED F072] | $750.0 [DEDUCTED F073] | $0.0 [DEDUCTED F315] |
| FY2028E | $5,000.0 [VIEW; as_of 2026-08-30; not a filing line] | $1,250.0 [DEDUCTED F096] | $2,000.0 [DEDUCTED F097] | $1,000.0 [DEDUCTED F098] | $750.0 [DEDUCTED F316] |

Cursor filing revenue and margins are **not obtained**. These are explicit forecast views, not filing lines. The 8-K discloses the closing share consideration and implied equity value, not Cursor P&L.

## Segment capex

| period | Space | Connectivity | AI |
| --- | ---: | ---: | ---: |
| H1 2026A | $2,226.0 [FACT] | $2,699.0 [FACT] | $23,551.0 [FACT] |
| H2 2026E | $2,340.3 [DEDUCTED F223] | $1,644.0 [DEDUCTED F225] | $18,000.0 [VIEW; as_of 2026-08-30; not a filing line] |
| FY2026E | $4,566.3 [DEDUCTED F234] | $4,343.0 [DEDUCTED F235] | $41,551.0 [DEDUCTED F236] |
| FY2027E | $5,265.0 [DEDUCTED F227] | $3,200.0 [DEDUCTED F229] | $30,000.0 [VIEW; as_of 2026-08-30; not a filing line] |
| FY2028E | $6,250.0 [DEDUCTED F231] | $3,375.0 [DEDUCTED F233] | $25,000.0 [VIEW; as_of 2026-08-30; not a filing line] |

Space capex = total launches × capex per launch. Connectivity capex = subscriber net adds × capex per net add. AI capex is the residual cash bid `[VIEW; as_of 2026-08-30; not a filing line]` from `research.md` Capital cycle.

## Formula register

Every `[DEDUCTED]` cell above points to one of these formulas.

| id | output | expression | named inputs | result |
| --- | --- | --- | --- | --- |
| F001 | `segment.FY2023.launch_services_revenue` | reported_space_revenue × rounded_launch_services_mix | reported_space_revenue=3557; rounded_launch_services_mix=0.552 | 1,963.5 |
| F002 | `segment.FY2023.launch_development_revenue` | reported_space_revenue - derived_launch_services_revenue | reported_space_revenue=3557; derived_launch_services_revenue=1963.464 | 1,593.5 |
| F003 | `segment.FY2024.launch_services_revenue` | reported_space_revenue × rounded_launch_services_mix | reported_space_revenue=3796; rounded_launch_services_mix=0.682 | 2,588.9 |
| F004 | `segment.FY2024.launch_development_revenue` | reported_space_revenue - derived_launch_services_revenue | reported_space_revenue=3796; derived_launch_services_revenue=2588.872 | 1,207.1 |
| F005 | `segment.FY2025.launch_services_revenue` | reported_space_revenue × rounded_launch_services_mix | reported_space_revenue=4086; rounded_launch_services_mix=0.63 | 2,574.2 |
| F006 | `segment.FY2025.launch_development_revenue` | reported_space_revenue - derived_launch_services_revenue | reported_space_revenue=4086; derived_launch_services_revenue=2574.18 | 1,511.8 |
| F007 | `segment.H2 2026E.launch_services_revenue` | customer_falcon_launches × launch_revenue_per_customer_launch | customer_falcon_launches=22; launch_revenue_per_customer_launch=65 | 1,430.0 |
| F008 | `segment.H2 2026E.starship_commercial_revenue` | commercial_Starship_flights × assumed_revenue_per_flight | commercial_Starship_flights=1; assumed_revenue_per_flight=150 | 150.0 |
| F009 | `segment.H2 2026E.average_subscribers_m` | opening_plus_ending_subscribers ÷ two | opening_plus_ending_subscribers=26; two=2 | 13.0 |
| F010 | `segment.H2 2026E.consumer_revenue` | average_subscribers_m × monthly_ARPU × six_months | average_subscribers_m=13; monthly_ARPU=64; six_months=6 | 4,992.0 |
| F011 | `segment.FY2026E.launch_services` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=978; H2_2026_forecast=1430 | 2,408.0 |
| F012 | `segment.FY2026E.launch_and_development` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=603; H2_2026_forecast=700 | 1,303.0 |
| F013 | `segment.FY2026E.starship_commercial` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=0; H2_2026_forecast=150 | 150.0 |
| F014 | `segment.FY2026E.consumer` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=4633; H2_2026_forecast=4992 | 9,625.0 |
| F015 | `segment.FY2026E.enterprise_and_government` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2915; H2_2026_forecast=3300 | 6,215.0 |
| F016 | `segment.FY2026E.spectrum_/_mobile_overlay` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=0; H2_2026_forecast=100 | 100.0 |
| F017 | `segment.FY2026E.advertising` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=710; H2_2026_forecast=760 | 1,470.0 |
| F018 | `segment.FY2026E.solutions_and_infrastructure` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2669; H2_2026_forecast=5000 | 7,669.0 |
| F019 | `segment.FY2026E.cursor` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=0; H2_2026_forecast=1000 | 1,000.0 |
| F020 | `segment.FY2027E.launch_services_revenue` | customer_falcon_launches × launch_revenue_per_customer_launch | customer_falcon_launches=45; launch_revenue_per_customer_launch=67 | 3,015.0 |
| F021 | `segment.FY2027E.launch_development_revenue` | prior_launch_development_revenue × (one + growth) | prior_launch_development_revenue=1303; one_plus_growth=1.12 | 1,459.4 |
| F022 | `segment.FY2027E.average_subscribers_m` | opening_plus_ending_subscribers ÷ two | opening_plus_ending_subscribers=32; two=2 | 16.0 |
| F023 | `segment.FY2027E.consumer_revenue` | average_subscribers_m × monthly_ARPU × twelve_months | average_subscribers_m=16; monthly_ARPU=61; twelve_months=12 | 11,712.0 |
| F024 | `segment.FY2027E.enterprise_government_revenue` | prior_enterprise_government_revenue × (one + growth) | prior_enterprise_government_revenue=6215; one_plus_growth=1.3 | 8,079.5 |
| F025 | `segment.FY2027E.advertising_revenue` | prior_advertising_revenue × (one + growth) | prior_advertising_revenue=1470; one_plus_growth=1.1 | 1,617.0 |
| F026 | `segment.FY2027E.solutions_infrastructure_revenue` | prior_solutions_infrastructure_revenue × (one + growth) | prior_solutions_infrastructure_revenue=7669; one_plus_growth=1.45 | 11,120.1 |
| F027 | `segment.FY2027E.starship_commercial_revenue` | commercial_Starship_flights × assumed_revenue_per_flight | commercial_Starship_flights=12; assumed_revenue_per_flight=150 | 1,800.0 |
| F028 | `segment.FY2028E.launch_services_revenue` | customer_falcon_launches × launch_revenue_per_customer_launch | customer_falcon_launches=50; launch_revenue_per_customer_launch=69 | 3,450.0 |
| F029 | `segment.FY2028E.launch_development_revenue` | prior_launch_development_revenue × (one + growth) | prior_launch_development_revenue=1459.36; one_plus_growth=1.12 | 1,634.5 |
| F030 | `segment.FY2028E.average_subscribers_m` | opening_plus_ending_subscribers ÷ two | opening_plus_ending_subscribers=40.5; two=2 | 20.3 |
| F031 | `segment.FY2028E.consumer_revenue` | average_subscribers_m × monthly_ARPU × twelve_months | average_subscribers_m=20.25; monthly_ARPU=59; twelve_months=12 | 14,337.0 |
| F032 | `segment.FY2028E.enterprise_government_revenue` | prior_enterprise_government_revenue × (one + growth) | prior_enterprise_government_revenue=8079.5; one_plus_growth=1.25 | 10,099.4 |
| F033 | `segment.FY2028E.advertising_revenue` | prior_advertising_revenue × (one + growth) | prior_advertising_revenue=1617; one_plus_growth=1.08 | 1,746.4 |
| F034 | `segment.FY2028E.solutions_infrastructure_revenue` | prior_solutions_infrastructure_revenue × (one + growth) | prior_solutions_infrastructure_revenue=11120.05; one_plus_growth=1.3 | 14,456.1 |
| F035 | `segment.FY2028E.starship_commercial_revenue` | commercial_Starship_flights × assumed_revenue_per_flight | commercial_Starship_flights=50; assumed_revenue_per_flight=140 | 7,000.0 |
| F036 | `segment.H2 2026E.launch_services_cor` | launch_services_revenue × launch_services_cor_pct | launch_services_revenue=1430; launch_services_cor_pct=0.35 | 500.5 |
| F037 | `segment.H2 2026E.launch_development_cor` | launch_development_revenue × launch_development_cor_pct | launch_development_revenue=700; launch_development_cor_pct=0.45 | 315.0 |
| F038 | `segment.H2 2026E.starship_commercial_cor` | starship_commercial_revenue × starship_commercial_cor_pct | starship_commercial_revenue=150; starship_commercial_cor_pct=0.6 | 90.0 |
| F039 | `segment.H2 2026E.space_cor` | launch_services_cor + launch_development_cor + starship_commercial_cor | launch_services_cor=500.5; launch_development_cor=315; starship_commercial_cor=90 | 905.5 |
| F040 | `segment.H2 2026E.consumer_cor` | consumer_revenue × consumer_cor_pct | consumer_revenue=4992; consumer_cor_pct=0.5 | 2,496.0 |
| F041 | `segment.H2 2026E.enterprise_government_cor` | enterprise_government_revenue × enterprise_government_cor_pct | enterprise_government_revenue=3300; enterprise_government_cor_pct=0.32 | 1,056.0 |
| F042 | `segment.H2 2026E.spectrum_mobile_cor` | spectrum_mobile_revenue × spectrum_mobile_cor_pct | spectrum_mobile_revenue=100; spectrum_mobile_cor_pct=0.5 | 50.0 |
| F043 | `segment.H2 2026E.connectivity_cor` | consumer_cor + enterprise_government_cor + spectrum_mobile_cor | consumer_cor=2496; enterprise_government_cor=1056; spectrum_mobile_cor=50 | 3,602.0 |
| F044 | `segment.H2 2026E.advertising_cor` | advertising_revenue × advertising_cor_pct | advertising_revenue=760; advertising_cor_pct=0.3 | 228.0 |
| F045 | `segment.H2 2026E.solutions_infrastructure_cor` | solutions_infrastructure_revenue × solutions_cor_pct | solutions_infrastructure_revenue=5000; solutions_cor_pct=0.45 | 2,250.0 |
| F046 | `segment.H2 2026E.cursor_cor` | Cursor_revenue × Cursor_cor_pct | Cursor_revenue=1000; Cursor_cor_pct=0.25 | 250.0 |
| F047 | `segment.H2 2026E.ai_cor` | advertising_cor + solutions_infrastructure_cor + cursor_cor | advertising_cor=228; solutions_infrastructure_cor=2250; cursor_cor=250 | 2,728.0 |
| F048 | `segment.H2 2026E.cursor_rd` | Cursor_revenue × Cursor_rd_pct | Cursor_revenue=1000; Cursor_rd_pct=0.7 | 700.0 |
| F049 | `segment.H2 2026E.cursor_sga` | Cursor_revenue × Cursor_sga_pct | Cursor_revenue=1000; Cursor_sga_pct=0.25 | 250.0 |
| F050 | `segment.FY2026E.space_revenue` | launch_services + launch_development + starship_commercial | launch_services=2408; launch_development=1303; starship_commercial=150 | 3,861.0 |
| F051 | `segment.FY2026E.space_cor` | H1_actual + H2_forecast | H1_actual=610; H2_forecast=905.5 | 1,515.5 |
| F052 | `segment.FY2026E.space_rd` | H1_actual + H2_forecast | H1_actual=2006; H2_forecast=2200 | 4,206.0 |
| F053 | `segment.FY2026E.space_sga` | H1_actual + H2_forecast | H1_actual=169; H2_forecast=200 | 369.0 |
| F054 | `segment.FY2026E.connectivity_revenue` | consumer + enterprise_government + spectrum_mobile_overlay | consumer=9625; enterprise_government=6215; spectrum_mobile_overlay=100 | 15,940.0 |
| F055 | `segment.FY2026E.connectivity_cor` | H1_actual + H2_forecast | H1_actual=3711; H2_forecast=3602 | 7,313.0 |
| F056 | `segment.FY2026E.connectivity_rd` | H1_actual + H2_forecast | H1_actual=499; H2_forecast=350 | 849.0 |
| F057 | `segment.FY2026E.connectivity_sga` | H1_actual + H2_forecast | H1_actual=494; H2_forecast=350 | 844.0 |
| F058 | `segment.FY2026E.ai_revenue` | advertising + solutions_infrastructure + Cursor | advertising=1470; solutions_infrastructure=7669; Cursor=1000 | 10,139.0 |
| F059 | `segment.FY2026E.ai_cor` | H1_actual + H2_forecast | H1_actual=1562; H2_forecast=2728 | 4,290.0 |
| F060 | `segment.FY2026E.ai_rd` | H1_actual + H2_xAI_X_forecast + H2_Cursor_forecast | H1_actual=4557; H2_xAI_X_forecast=4500; H2_Cursor_forecast=700 | 9,757.0 |
| F061 | `segment.FY2026E.ai_sga` | H1_actual + H2_xAI_X_forecast + H2_Cursor_forecast | H1_actual=995; H2_xAI_X_forecast=1100; H2_Cursor_forecast=250 | 2,345.0 |
| F062 | `segment.FY2026E.ai_restruct` | H1_actual + H2_forecast | H1_actual=(-9); H2_forecast=0 | (9.0) |
| F063 | `segment.FY2026E.space.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=1515.5; rd=4206; sga=369; restructuring=0; impairment=0 | 6,090.5 |
| F064 | `segment.FY2026E.space.ebit` | revenue - operating_expenses | revenue=3861; operating_expenses=6090.5 | (2,229.5) |
| F065 | `segment.FY2026E.connectivity.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=7313; rd=849; sga=844; restructuring=0; impairment=0 | 9,006.0 |
| F066 | `segment.FY2026E.connectivity.ebit` | revenue - operating_expenses | revenue=15940; operating_expenses=9006 | 6,934.0 |
| F067 | `segment.FY2026E.ai.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=4290; rd=9757; sga=2345; restructuring=(-9); impairment=0 | 16,383.0 |
| F068 | `segment.FY2026E.ai.ebit` | revenue - operating_expenses | revenue=10139; operating_expenses=16383 | (6,244.0) |
| F069 | `segment.FY2027E.starship_commercial_cor` | starship_commercial_revenue × starship_commercial_cor_pct | starship_commercial_revenue=1800; starship_commercial_cor_pct=0.5 | 900.0 |
| F070 | `segment.FY2027E.spectrum_mobile_cor` | spectrum_mobile_revenue × spectrum_mobile_cor_pct | spectrum_mobile_revenue=1000; spectrum_mobile_cor_pct=0.4 | 400.0 |
| F071 | `segment.FY2027E.cursor_cor` | Cursor_revenue × Cursor_cor_pct | Cursor_revenue=3000; Cursor_cor_pct=0.25 | 750.0 |
| F072 | `segment.FY2027E.cursor_rd` | Cursor_revenue × Cursor_rd_pct | Cursor_revenue=3000; Cursor_rd_pct=0.5 | 1,500.0 |
| F073 | `segment.FY2027E.cursor_sga` | Cursor_revenue × Cursor_sga_pct | Cursor_revenue=3000; Cursor_sga_pct=0.25 | 750.0 |
| F074 | `segment.FY2027E.space_revenue` | launch_services + launch_development + starship_commercial | launch_services=3015; launch_development=1459.36; starship_commercial=1800 | 6,274.4 |
| F075 | `segment.FY2027E.launch_services_cor` | launch_services_revenue × launch_services_cor_pct | launch_services_revenue=3015; launch_services_cor_pct=0.34 | 1,025.1 |
| F076 | `segment.FY2027E.launch_development_cor` | launch_development_revenue × launch_development_cor_pct | launch_development_revenue=1459.36; launch_development_cor_pct=0.44 | 642.1 |
| F077 | `segment.FY2027E.space_cor` | launch_services_cor + launch_development_cor + starship_commercial_cor | launch_services_cor=1025.1; launch_development_cor=642.1184; starship_commercial_cor=900 | 2,567.2 |
| F078 | `segment.FY2027E.connectivity_revenue` | consumer + enterprise_government + spectrum_mobile_overlay | consumer=11712; enterprise_government=8079.5; spectrum_mobile_overlay=1000 | 20,791.5 |
| F079 | `segment.FY2027E.consumer_cor` | consumer_revenue × consumer_cor_pct | consumer_revenue=11712; consumer_cor_pct=0.47 | 5,504.6 |
| F080 | `segment.FY2027E.enterprise_government_cor` | enterprise_government_revenue × enterprise_government_cor_pct | enterprise_government_revenue=8079.5; enterprise_government_cor_pct=0.3 | 2,423.9 |
| F081 | `segment.FY2027E.connectivity_cor` | consumer_cor + enterprise_government_cor + spectrum_mobile_cor | consumer_cor=5504.64; enterprise_government_cor=2423.85; spectrum_mobile_cor=400 | 8,328.5 |
| F082 | `segment.FY2027E.ai_revenue` | advertising + solutions_infrastructure + Cursor | advertising=1617; solutions_infrastructure=11120.05; Cursor=3000 | 15,737.1 |
| F083 | `segment.FY2027E.advertising_cor` | advertising_revenue × advertising_cor_pct | advertising_revenue=1617; advertising_cor_pct=0.28 | 452.8 |
| F084 | `segment.FY2027E.solutions_infrastructure_cor` | solutions_infrastructure_revenue × solutions_cor_pct | solutions_infrastructure_revenue=11120.05; solutions_cor_pct=0.4 | 4,448.0 |
| F085 | `segment.FY2027E.ai_cor` | advertising_cor + solutions_infrastructure_cor + Cursor_cor | advertising_cor=452.76; solutions_infrastructure_cor=4448.02; Cursor_cor=750 | 5,650.8 |
| F086 | `segment.FY2027E.ai_rd` | xAI_X_R&D + Cursor_R&D | xAI_X_R&D=8000; Cursor_R&D=1500 | 9,500.0 |
| F087 | `segment.FY2027E.ai_sga` | xAI_X_SG&A + Cursor_SG&A | xAI_X_SG&A=2500; Cursor_SG&A=750 | 3,250.0 |
| F088 | `segment.FY2027E.space.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=2567.2184; rd=4200; sga=220; restructuring=0; impairment=0 | 6,987.2 |
| F089 | `segment.FY2027E.space.ebit` | revenue - operating_expenses | revenue=6274.36; operating_expenses=6987.2184 | (712.9) |
| F090 | `segment.FY2027E.connectivity.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=8328.49; rd=1000; sga=1100; restructuring=0; impairment=0 | 10,428.5 |
| F091 | `segment.FY2027E.connectivity.ebit` | revenue - operating_expenses | revenue=20791.5; operating_expenses=10428.49 | 10,363.0 |
| F092 | `segment.FY2027E.ai.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=5650.78; rd=9500; sga=3250; restructuring=0; impairment=0 | 18,400.8 |
| F093 | `segment.FY2027E.ai.ebit` | revenue - operating_expenses | revenue=15737.05; operating_expenses=18400.78 | (2,663.7) |
| F094 | `segment.FY2028E.starship_commercial_cor` | starship_commercial_revenue × starship_commercial_cor_pct | starship_commercial_revenue=7000; starship_commercial_cor_pct=0.4 | 2,800.0 |
| F095 | `segment.FY2028E.spectrum_mobile_cor` | spectrum_mobile_revenue × spectrum_mobile_cor_pct | spectrum_mobile_revenue=2500; spectrum_mobile_cor_pct=0.35 | 875.0 |
| F096 | `segment.FY2028E.cursor_cor` | Cursor_revenue × Cursor_cor_pct | Cursor_revenue=5000; Cursor_cor_pct=0.25 | 1,250.0 |
| F097 | `segment.FY2028E.cursor_rd` | Cursor_revenue × Cursor_rd_pct | Cursor_revenue=5000; Cursor_rd_pct=0.4 | 2,000.0 |
| F098 | `segment.FY2028E.cursor_sga` | Cursor_revenue × Cursor_sga_pct | Cursor_revenue=5000; Cursor_sga_pct=0.2 | 1,000.0 |
| F099 | `segment.FY2028E.space_revenue` | launch_services + launch_development + starship_commercial | launch_services=3450; launch_development=1634.4832; starship_commercial=7000 | 12,084.5 |
| F100 | `segment.FY2028E.launch_services_cor` | launch_services_revenue × launch_services_cor_pct | launch_services_revenue=3450; launch_services_cor_pct=0.32 | 1,104.0 |
| F101 | `segment.FY2028E.launch_development_cor` | launch_development_revenue × launch_development_cor_pct | launch_development_revenue=1634.4832; launch_development_cor_pct=0.42 | 686.5 |
| F102 | `segment.FY2028E.space_cor` | launch_services_cor + launch_development_cor + starship_commercial_cor | launch_services_cor=1104; launch_development_cor=686.482944; starship_commercial_cor=2800 | 4,590.5 |
| F103 | `segment.FY2028E.connectivity_revenue` | consumer + enterprise_government + spectrum_mobile_overlay | consumer=14337; enterprise_government=10099.375; spectrum_mobile_overlay=2500 | 26,936.4 |
| F104 | `segment.FY2028E.consumer_cor` | consumer_revenue × consumer_cor_pct | consumer_revenue=14337; consumer_cor_pct=0.45 | 6,451.7 |
| F105 | `segment.FY2028E.enterprise_government_cor` | enterprise_government_revenue × enterprise_government_cor_pct | enterprise_government_revenue=10099.375; enterprise_government_cor_pct=0.29 | 2,928.8 |
| F106 | `segment.FY2028E.connectivity_cor` | consumer_cor + enterprise_government_cor + spectrum_mobile_cor | consumer_cor=6451.65; enterprise_government_cor=2928.81875; spectrum_mobile_cor=875 | 10,255.5 |
| F107 | `segment.FY2028E.ai_revenue` | advertising + solutions_infrastructure + Cursor | advertising=1746.36; solutions_infrastructure=14456.065; Cursor=5000 | 21,202.4 |
| F108 | `segment.FY2028E.advertising_cor` | advertising_revenue × advertising_cor_pct | advertising_revenue=1746.36; advertising_cor_pct=0.27 | 471.5 |
| F109 | `segment.FY2028E.solutions_infrastructure_cor` | solutions_infrastructure_revenue × solutions_cor_pct | solutions_infrastructure_revenue=14456.065; solutions_cor_pct=0.36 | 5,204.2 |
| F110 | `segment.FY2028E.ai_cor` | advertising_cor + solutions_infrastructure_cor + Cursor_cor | advertising_cor=471.5172; solutions_infrastructure_cor=5204.1834; Cursor_cor=1250 | 6,925.7 |
| F111 | `segment.FY2028E.ai_rd` | xAI_X_R&D + Cursor_R&D | xAI_X_R&D=8500; Cursor_R&D=2000 | 10,500.0 |
| F112 | `segment.FY2028E.ai_sga` | xAI_X_SG&A + Cursor_SG&A | xAI_X_SG&A=2900; Cursor_SG&A=1000 | 3,900.0 |
| F113 | `segment.FY2028E.space.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=4590.482944; rd=3600; sga=230; restructuring=0; impairment=0 | 8,420.5 |
| F114 | `segment.FY2028E.space.ebit` | revenue - operating_expenses | revenue=12084.4832; operating_expenses=8420.482944 | 3,664.0 |
| F115 | `segment.FY2028E.connectivity.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=10255.46875; rd=1200; sga=1300; restructuring=0; impairment=0 | 12,755.5 |
| F116 | `segment.FY2028E.connectivity.ebit` | revenue - operating_expenses | revenue=26936.375; operating_expenses=12755.46875 | 14,180.9 |
| F117 | `segment.FY2028E.ai.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=6925.7006; rd=10500; sga=3900; restructuring=0; impairment=0 | 21,325.7 |
| F118 | `segment.FY2028E.ai.ebit` | revenue - operating_expenses | revenue=21202.425; operating_expenses=21325.7006 | (123.3) |
| F175 | `segment.H2 2026E.space.revenue` | FY2026_forecast - H1_2026_actual | FY2026_forecast=3861; H1_2026_actual=1581 | 2,280.0 |
| F176 | `segment.H2 2026E.space.cor` | FY2026_forecast - H1_2026_actual | FY2026_forecast=1515.5; H1_2026_actual=610 | 905.5 |
| F177 | `segment.H2 2026E.space.rd` | FY2026_forecast - H1_2026_actual | FY2026_forecast=4206; H1_2026_actual=2006 | 2,200.0 |
| F178 | `segment.H2 2026E.space.sga` | FY2026_forecast - H1_2026_actual | FY2026_forecast=369; H1_2026_actual=169 | 200.0 |
| F179 | `segment.H2 2026E.space.restruct` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F180 | `segment.H2 2026E.space.impairment` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F181 | `segment.H2 2026E.space.ebit` | FY2026_forecast - H1_2026_actual | FY2026_forecast=(-2229.5); H1_2026_actual=(-1204) | (1,025.5) |
| F182 | `segment.H2 2026E.connectivity.revenue` | FY2026_forecast - H1_2026_actual | FY2026_forecast=15940; H1_2026_actual=7548 | 8,392.0 |
| F183 | `segment.H2 2026E.connectivity.cor` | FY2026_forecast - H1_2026_actual | FY2026_forecast=7313; H1_2026_actual=3711 | 3,602.0 |
| F184 | `segment.H2 2026E.connectivity.rd` | FY2026_forecast - H1_2026_actual | FY2026_forecast=849; H1_2026_actual=499 | 350.0 |
| F185 | `segment.H2 2026E.connectivity.sga` | FY2026_forecast - H1_2026_actual | FY2026_forecast=844; H1_2026_actual=494 | 350.0 |
| F186 | `segment.H2 2026E.connectivity.restruct` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F187 | `segment.H2 2026E.connectivity.impairment` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F188 | `segment.H2 2026E.connectivity.ebit` | FY2026_forecast - H1_2026_actual | FY2026_forecast=6934; H1_2026_actual=2844 | 4,090.0 |
| F189 | `segment.H2 2026E.ai.revenue` | FY2026_forecast - H1_2026_actual | FY2026_forecast=10139; H1_2026_actual=3379 | 6,760.0 |
| F190 | `segment.H2 2026E.ai.cor` | FY2026_forecast - H1_2026_actual | FY2026_forecast=4290; H1_2026_actual=1562 | 2,728.0 |
| F191 | `segment.H2 2026E.ai.rd` | FY2026_forecast - H1_2026_actual | FY2026_forecast=9757; H1_2026_actual=4557 | 5,200.0 |
| F192 | `segment.H2 2026E.ai.sga` | FY2026_forecast - H1_2026_actual | FY2026_forecast=2345; H1_2026_actual=995 | 1,350.0 |
| F193 | `segment.H2 2026E.ai.restruct` | FY2026_forecast - H1_2026_actual | FY2026_forecast=(-9); H1_2026_actual=(-9) | 0.0 |
| F194 | `segment.H2 2026E.ai.impairment` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F195 | `segment.H2 2026E.ai.ebit` | FY2026_forecast - H1_2026_actual | FY2026_forecast=(-6244); H1_2026_actual=(-3726) | (2,518.0) |
| F222 | `cashflow.H2 2026E.total_launches` | customer_falcon_launches + internal_falcon_launches + starship_launches | customer_falcon_launches=22; internal_falcon_launches=58; starship_launches=2 | 82.0 |
| F223 | `cashflow.H2 2026E.space_capex` | total_launches × space_capex_per_launch | total_launches=82; space_capex_per_launch=28.54 | 2,340.3 |
| F224 | `cashflow.H2 2026E.subscriber_net_adds_m` | ending_subscribers_m - opening_subscribers_m | ending_subscribers_m=14; opening_subscribers_m=12 | 2.0 |
| F225 | `cashflow.H2 2026E.connectivity_capex` | subscriber_net_adds_m × capex_per_net_add | subscriber_net_adds_m=2; capex_per_net_add=822 | 1,644.0 |
| F226 | `cashflow.FY2027E.total_launches` | customer_falcon_launches + internal_falcon_launches + starship_launches | customer_falcon_launches=45; internal_falcon_launches=130; starship_launches=20 | 195.0 |
| F227 | `cashflow.FY2027E.space_capex` | total_launches × space_capex_per_launch | total_launches=195; space_capex_per_launch=27 | 5,265.0 |
| F228 | `cashflow.FY2027E.subscriber_net_adds_m` | ending_subscribers_m - opening_subscribers_m | ending_subscribers_m=18; opening_subscribers_m=14 | 4.0 |
| F229 | `cashflow.FY2027E.connectivity_capex` | subscriber_net_adds_m × capex_per_net_add | subscriber_net_adds_m=4; capex_per_net_add=800 | 3,200.0 |
| F230 | `cashflow.FY2028E.total_launches` | customer_falcon_launches + internal_falcon_launches + starship_launches | customer_falcon_launches=50; internal_falcon_launches=140; starship_launches=60 | 250.0 |
| F231 | `cashflow.FY2028E.space_capex` | total_launches × space_capex_per_launch | total_launches=250; space_capex_per_launch=25 | 6,250.0 |
| F232 | `cashflow.FY2028E.subscriber_net_adds_m` | ending_subscribers_m - opening_subscribers_m | ending_subscribers_m=22.5; opening_subscribers_m=18 | 4.5 |
| F233 | `cashflow.FY2028E.connectivity_capex` | subscriber_net_adds_m × capex_per_net_add | subscriber_net_adds_m=4.5; capex_per_net_add=750 | 3,375.0 |
| F234 | `cashflow.FY2026E.space_capex` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2226; H2_2026_forecast=2340.28 | 4,566.3 |
| F235 | `cashflow.FY2026E.connectivity_capex` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2699; H2_2026_forecast=1644 | 4,343.0 |
| F236 | `cashflow.FY2026E.ai_capex` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=23551; H2_2026_forecast=18000 | 41,551.0 |
| F314 | `segment.FY2026E.cursor_memo_ebit` | Cursor_revenue - Cursor_cost_of_revenue - Cursor_R&D - Cursor_SG&A | Cursor_revenue=1000; Cursor_cost_of_revenue=250; Cursor_R&D=700; Cursor_SG&A=250 | (200.0) |
| F315 | `segment.FY2027E.cursor_memo_ebit` | Cursor_revenue - Cursor_cost_of_revenue - Cursor_R&D - Cursor_SG&A | Cursor_revenue=3000; Cursor_cost_of_revenue=750; Cursor_R&D=1500; Cursor_SG&A=750 | 0.0 |
| F316 | `segment.FY2028E.cursor_memo_ebit` | Cursor_revenue - Cursor_cost_of_revenue - Cursor_R&D - Cursor_SG&A | Cursor_revenue=5000; Cursor_cost_of_revenue=1250; Cursor_R&D=2000; Cursor_SG&A=1000 | 750.0 |
