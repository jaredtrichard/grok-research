# SpaceX segment model

as_of: 2026-08-30
units: USD millions unless stated otherwise
generator: `compute.py`

Forecast drivers are `[VIEW]` and implement `memory/spcx/research.md`. Historical facts point to `memory/spcx/register.md`. Internal Falcon launches and Starship launches do not create Launch Services revenue. Starshield remains a memo inside Enterprise & Government; standalone P&L is **not obtained**.

## Explicit forecast drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Customer / internal Falcon / Starship launches | 22.0 / 58.0 / 2.0 [VIEW] | `research.md` Space — Launch Services / Starship overlay |
| H2 2026E | Launch revenue per customer launch | $65.0 [VIEW] | `research.md` recognized revenue per customer launch; list price remains not obtained |
| H2 2026E | Ending subscribers / monthly ARPU | 14.0m / $64.0 [VIEW] | `research.md` Connectivity — Consumer |
| H2 2026E | Enterprise & Government | $3,300.0 [VIEW] | `research.md` Connectivity — Enterprise & Government; no Starshield split |
| H2 2026E | Advertising | $760.0 [VIEW] | `research.md` AI — Advertising |
| H2 2026E | Solutions & Infrastructure | $5,000.0 [VIEW] | `research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside |
| FY2027E | Customer / internal Falcon / Starship launches | 45.0 / 130.0 / 5.0 [VIEW] | `research.md` Space — Launch Services / Starship overlay |
| FY2027E | Launch revenue per customer launch | $67.0 [VIEW] | `research.md` recognized revenue per customer launch; list price remains not obtained |
| FY2027E | Ending subscribers / monthly ARPU | 18.0m / $61.0 [VIEW] | `research.md` Connectivity — Consumer |
| FY2027E | Enterprise & Government | 30.0% growth [VIEW] | `research.md` Connectivity — Enterprise & Government; no Starshield split |
| FY2027E | Advertising | 10.0% growth [VIEW] | `research.md` AI — Advertising |
| FY2027E | Solutions & Infrastructure | 45.0% growth [VIEW] | `research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside |
| FY2028E | Customer / internal Falcon / Starship launches | 50.0 / 140.0 / 10.0 [VIEW] | `research.md` Space — Launch Services / Starship overlay |
| FY2028E | Launch revenue per customer launch | $69.0 [VIEW] | `research.md` recognized revenue per customer launch; list price remains not obtained |
| FY2028E | Ending subscribers / monthly ARPU | 22.5m / $59.0 [VIEW] | `research.md` Connectivity — Consumer |
| FY2028E | Enterprise & Government | 25.0% growth [VIEW] | `research.md` Connectivity — Enterprise & Government; no Starshield split |
| FY2028E | Advertising | 8.0% growth [VIEW] | `research.md` AI — Advertising |
| FY2028E | Solutions & Infrastructure | 30.0% growth [VIEW] | `research.md` AI — Solutions & Infrastructure; Customer B concentration is the named downside |

## Forecast cost and capital drivers

| period | driver | assumption | research instruction |
| --- | --- | --- | --- |
| H2 2026E | Space cost of revenue | 35.0% Launch Services / 45.0% Launch & Development [VIEW] | `research.md` Space segment drivers |
| H2 2026E | Space R&D / SG&A | $2,200.0 / $200.0 [VIEW] | `research.md` Starship overlay and Corporate |
| H2 2026E | Connectivity cost of revenue | 50.0% Consumer / 32.0% Enterprise & Government [VIEW] | `research.md` Connectivity segment drivers |
| H2 2026E | Connectivity R&D / SG&A | $350.0 / $350.0 [VIEW] | `research.md` Connectivity segment drivers |
| H2 2026E | AI cost of revenue | 30.0% Advertising / 45.0% Solutions & Infrastructure [VIEW] | `research.md` AI segment drivers |
| H2 2026E | AI R&D / SG&A | $4,500.0 / $1,100.0 [VIEW] | `research.md` AI segment drivers |
| H2 2026E | Capex unit drivers | $28.5/launch; $822.0/net add; AI $18,000.0 [VIEW] | `research.md` Capital cycle |
| FY2027E | Space cost of revenue | 34.0% Launch Services / 44.0% Launch & Development [VIEW] | `research.md` Space segment drivers |
| FY2027E | Space R&D / SG&A | $4,200.0 / $220.0 [VIEW] | `research.md` Starship overlay and Corporate |
| FY2027E | Connectivity cost of revenue | 47.0% Consumer / 30.0% Enterprise & Government [VIEW] | `research.md` Connectivity segment drivers |
| FY2027E | Connectivity R&D / SG&A | $1,000.0 / $1,100.0 [VIEW] | `research.md` Connectivity segment drivers |
| FY2027E | AI cost of revenue | 28.0% Advertising / 40.0% Solutions & Infrastructure [VIEW] | `research.md` AI segment drivers |
| FY2027E | AI R&D / SG&A | $8,000.0 / $2,500.0 [VIEW] | `research.md` AI segment drivers |
| FY2027E | Capex unit drivers | $27.0/launch; $800.0/net add; AI $30,000.0 [VIEW] | `research.md` Capital cycle |
| FY2028E | Space cost of revenue | 32.0% Launch Services / 42.0% Launch & Development [VIEW] | `research.md` Space segment drivers |
| FY2028E | Space R&D / SG&A | $3,600.0 / $230.0 [VIEW] | `research.md` Starship overlay and Corporate |
| FY2028E | Connectivity cost of revenue | 45.0% Consumer / 29.0% Enterprise & Government [VIEW] | `research.md` Connectivity segment drivers |
| FY2028E | Connectivity R&D / SG&A | $1,200.0 / $1,300.0 [VIEW] | `research.md` Connectivity segment drivers |
| FY2028E | AI cost of revenue | 27.0% Advertising / 36.0% Solutions & Infrastructure [VIEW] | `research.md` AI segment drivers |
| FY2028E | AI R&D / SG&A | $8,500.0 / $2,900.0 [VIEW] | `research.md` AI segment drivers |
| FY2028E | Capex unit drivers | $25.0/launch; $750.0/net add; AI $25,000.0 [VIEW] | `research.md` Capital cycle |

Kit revenue, churn, launch list price, Falcon 9/Heavy mix, Starshield standalone results, GPU-hours and utilization remain **not obtained**. Consumer revenue therefore models service revenue only; kit contribution is zero `[VIEW]`, not a claim that kits have no value. Cursor P&L contribution is zero `[VIEW]` in H2 2026 because contribution is **not obtained**; Cursor is not back-cast.

## Revenue lines

| line | FY2023 | FY2024 | FY2025 | H1 2026A | FY2026E | FY2027E | FY2028E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Launch Services | $1,963.5 [DEDUCTED F001] | $2,588.9 [DEDUCTED F003] | $2,574.2 [DEDUCTED F005] | $978.0 [FACT] | $2,408.0 [DEDUCTED F010] | $3,015.0 [DEDUCTED F016] | $3,450.0 [DEDUCTED F023] |
| Launch & Development | $1,593.5 [DEDUCTED F002] | $1,207.1 [DEDUCTED F004] | $1,511.8 [DEDUCTED F006] | $603.0 [FACT] | $1,303.0 [DEDUCTED F011] | $1,459.4 [DEDUCTED F017] | $1,634.5 [DEDUCTED F024] |
| Consumer | **not obtained** | **not obtained** | **not obtained** | $4,633.0 [FACT] | $9,625.0 [DEDUCTED F012] | $11,712.0 [DEDUCTED F019] | $14,337.0 [DEDUCTED F026] |
| Enterprise & Government | **not obtained** | **not obtained** | **not obtained** | $2,915.0 [FACT] | $6,215.0 [DEDUCTED F013] | $8,079.5 [DEDUCTED F020] | $10,099.4 [DEDUCTED F027] |
| Advertising | **not obtained** | **not obtained** | **not obtained** | $710.0 [FACT] | $1,470.0 [DEDUCTED F014] | $1,617.0 [DEDUCTED F021] | $1,746.4 [DEDUCTED F028] |
| Solutions & Infrastructure | **not obtained** | **not obtained** | **not obtained** | $2,669.0 [FACT] | $7,669.0 [DEDUCTED F015] | $11,120.1 [DEDUCTED F022] | $14,456.1 [DEDUCTED F029] |
| **Space revenue** | $3,557.0 [FACT] | $3,796.0 [FACT] | $4,086.0 [FACT] | $1,581.0 [FACT] | $3,711.0 [DEDUCTED F039] | $4,474.4 [DEDUCTED F058] | $5,084.5 [DEDUCTED F076] |
| **Connectivity revenue** | $3,869.0 [FACT] | $7,599.0 [FACT] | $11,387.0 [FACT] | $7,548.0 [FACT] | $15,840.0 [DEDUCTED F043] | $19,791.5 [DEDUCTED F062] | $24,436.4 [DEDUCTED F080] |
| **AI revenue** | $2,961.0 [FACT] | $2,620.0 [FACT] | $3,201.0 [FACT] | $3,379.0 [FACT] | $9,139.0 [DEDUCTED F047] | $12,737.1 [DEDUCTED F066] | $16,202.4 [DEDUCTED F084] |

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
| FY2026E | Space | $3,711.0 [DEDUCTED F039] | $1,425.5 [DEDUCTED F040] | $4,206.0 [DEDUCTED F041] | $369.0 [DEDUCTED F042] | $0.0 [VIEW] | $0.0 [VIEW] | $(2,289.5) [DEDUCTED F053] |
| FY2026E | Connectivity | $15,840.0 [DEDUCTED F043] | $7,263.0 [DEDUCTED F044] | $849.0 [DEDUCTED F045] | $844.0 [DEDUCTED F046] | $0.0 [VIEW] | $0.0 [VIEW] | $6,884.0 [DEDUCTED F055] |
| FY2026E | AI | $9,139.0 [DEDUCTED F047] | $4,040.0 [DEDUCTED F048] | $9,057.0 [DEDUCTED F049] | $2,095.0 [DEDUCTED F050] | $(9.0) [DEDUCTED F051] | $0.0 [VIEW] | $(6,044.0) [DEDUCTED F057] |
| FY2027E | Space | $4,474.4 [DEDUCTED F058] | $1,667.2 [DEDUCTED F061] | $4,200.0 [VIEW] | $220.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] | $(1,612.9) [DEDUCTED F071] |
| FY2027E | Connectivity | $19,791.5 [DEDUCTED F062] | $7,928.5 [DEDUCTED F065] | $1,000.0 [VIEW] | $1,100.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] | $9,763.0 [DEDUCTED F073] |
| FY2027E | AI | $12,737.1 [DEDUCTED F066] | $4,900.8 [DEDUCTED F069] | $8,000.0 [VIEW] | $2,500.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] | $(2,663.7) [DEDUCTED F075] |
| FY2028E | Space | $5,084.5 [DEDUCTED F076] | $1,790.5 [DEDUCTED F079] | $3,600.0 [VIEW] | $230.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] | $(536.0) [DEDUCTED F089] |
| FY2028E | Connectivity | $24,436.4 [DEDUCTED F080] | $9,380.5 [DEDUCTED F083] | $1,200.0 [VIEW] | $1,300.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] | $12,555.9 [DEDUCTED F091] |
| FY2028E | AI | $16,202.4 [DEDUCTED F084] | $5,675.7 [DEDUCTED F087] | $8,500.0 [VIEW] | $2,900.0 [VIEW] | $0.0 [VIEW] | $0.0 [VIEW] | $(873.3) [DEDUCTED F093] |

Corporate / eliminations operating revenue and expense are zero `[FACT]` because the filed reportable segments reconcile to consolidated EBIT. Financing sits below EBIT in `income.md`.

## Starship overlay

| period | line | value | treatment |
| --- | --- | --- | --- |
| FY2025 | Starship-specific R&D | $3,004 [FACT] | `research.md` Starship overlay |
| H1 2026A | Space R&D, mainly Starship | $2,006 [FACT] | Exact Starship-only amount not obtained |
| H2 2026E | Space R&D / Starship overlay | $2,200 [VIEW] | `research.md` Starship remains R&D/capex, not revenue |
| FY2027E | Space R&D / Starship overlay | $4,200 [VIEW] | No Starship revenue line; commercial pricing not obtained |
| FY2028E | Space R&D / Starship overlay | $3,600 [VIEW] | No Starship revenue line; commercial pricing not obtained |

Starship customer revenue, standalone capex, commercial price, payload economics and cost per test remain **not obtained**. Forecast launches affect Space capex and cadence only.

## Segment capex

| period | Space | Connectivity | AI |
| --- | ---: | ---: | ---: |
| H1 2026A | $2,226.0 [FACT] | $2,699.0 [FACT] | $23,551.0 [FACT] |
| H2 2026E | $2,340.3 [DEDUCTED F198] | $1,644.0 [DEDUCTED F200] | $18,000.0 [VIEW] |
| FY2026E | $4,566.3 [DEDUCTED F209] | $4,343.0 [DEDUCTED F210] | $41,551.0 [DEDUCTED F211] |
| FY2027E | $4,860.0 [DEDUCTED F202] | $3,200.0 [DEDUCTED F204] | $30,000.0 [VIEW] |
| FY2028E | $5,000.0 [DEDUCTED F206] | $3,375.0 [DEDUCTED F208] | $25,000.0 [VIEW] |

Space capex = total launches × capex per launch. Connectivity capex = subscriber net adds × capex per net add. AI capex is the residual cash bid `[VIEW]` from `research.md` Capital cycle.

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
| F008 | `segment.H2 2026E.average_subscribers_m` | opening_plus_ending_subscribers ÷ two | opening_plus_ending_subscribers=26; two=2 | 13.0 |
| F009 | `segment.H2 2026E.consumer_revenue` | average_subscribers_m × monthly_ARPU × six_months | average_subscribers_m=13; monthly_ARPU=64; six_months=6 | 4,992.0 |
| F010 | `segment.FY2026E.launch_services` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=978; H2_2026_forecast=1430 | 2,408.0 |
| F011 | `segment.FY2026E.launch_and_development` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=603; H2_2026_forecast=700 | 1,303.0 |
| F012 | `segment.FY2026E.consumer` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=4633; H2_2026_forecast=4992 | 9,625.0 |
| F013 | `segment.FY2026E.enterprise_and_government` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2915; H2_2026_forecast=3300 | 6,215.0 |
| F014 | `segment.FY2026E.advertising` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=710; H2_2026_forecast=760 | 1,470.0 |
| F015 | `segment.FY2026E.solutions_and_infrastructure` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2669; H2_2026_forecast=5000 | 7,669.0 |
| F016 | `segment.FY2027E.launch_services_revenue` | customer_falcon_launches × launch_revenue_per_customer_launch | customer_falcon_launches=45; launch_revenue_per_customer_launch=67 | 3,015.0 |
| F017 | `segment.FY2027E.launch_development_revenue` | prior_launch_development_revenue × (one + growth) | prior_launch_development_revenue=1303; one_plus_growth=1.12 | 1,459.4 |
| F018 | `segment.FY2027E.average_subscribers_m` | opening_plus_ending_subscribers ÷ two | opening_plus_ending_subscribers=32; two=2 | 16.0 |
| F019 | `segment.FY2027E.consumer_revenue` | average_subscribers_m × monthly_ARPU × twelve_months | average_subscribers_m=16; monthly_ARPU=61; twelve_months=12 | 11,712.0 |
| F020 | `segment.FY2027E.enterprise_government_revenue` | prior_enterprise_government_revenue × (one + growth) | prior_enterprise_government_revenue=6215; one_plus_growth=1.3 | 8,079.5 |
| F021 | `segment.FY2027E.advertising_revenue` | prior_advertising_revenue × (one + growth) | prior_advertising_revenue=1470; one_plus_growth=1.1 | 1,617.0 |
| F022 | `segment.FY2027E.solutions_infrastructure_revenue` | prior_solutions_infrastructure_revenue × (one + growth) | prior_solutions_infrastructure_revenue=7669; one_plus_growth=1.45 | 11,120.1 |
| F023 | `segment.FY2028E.launch_services_revenue` | customer_falcon_launches × launch_revenue_per_customer_launch | customer_falcon_launches=50; launch_revenue_per_customer_launch=69 | 3,450.0 |
| F024 | `segment.FY2028E.launch_development_revenue` | prior_launch_development_revenue × (one + growth) | prior_launch_development_revenue=1459.36; one_plus_growth=1.12 | 1,634.5 |
| F025 | `segment.FY2028E.average_subscribers_m` | opening_plus_ending_subscribers ÷ two | opening_plus_ending_subscribers=40.5; two=2 | 20.3 |
| F026 | `segment.FY2028E.consumer_revenue` | average_subscribers_m × monthly_ARPU × twelve_months | average_subscribers_m=20.25; monthly_ARPU=59; twelve_months=12 | 14,337.0 |
| F027 | `segment.FY2028E.enterprise_government_revenue` | prior_enterprise_government_revenue × (one + growth) | prior_enterprise_government_revenue=8079.5; one_plus_growth=1.25 | 10,099.4 |
| F028 | `segment.FY2028E.advertising_revenue` | prior_advertising_revenue × (one + growth) | prior_advertising_revenue=1617; one_plus_growth=1.08 | 1,746.4 |
| F029 | `segment.FY2028E.solutions_infrastructure_revenue` | prior_solutions_infrastructure_revenue × (one + growth) | prior_solutions_infrastructure_revenue=11120.05; one_plus_growth=1.3 | 14,456.1 |
| F030 | `segment.H2 2026E.launch_services_cor` | launch_services_revenue × launch_services_cor_pct | launch_services_revenue=1430; launch_services_cor_pct=0.35 | 500.5 |
| F031 | `segment.H2 2026E.launch_development_cor` | launch_development_revenue × launch_development_cor_pct | launch_development_revenue=700; launch_development_cor_pct=0.45 | 315.0 |
| F032 | `segment.H2 2026E.space_cor` | launch_services_cor + launch_development_cor | launch_services_cor=500.5; launch_development_cor=315 | 815.5 |
| F033 | `segment.H2 2026E.consumer_cor` | consumer_revenue × consumer_cor_pct | consumer_revenue=4992; consumer_cor_pct=0.5 | 2,496.0 |
| F034 | `segment.H2 2026E.enterprise_government_cor` | enterprise_government_revenue × enterprise_government_cor_pct | enterprise_government_revenue=3300; enterprise_government_cor_pct=0.32 | 1,056.0 |
| F035 | `segment.H2 2026E.connectivity_cor` | consumer_cor + enterprise_government_cor | consumer_cor=2496; enterprise_government_cor=1056 | 3,552.0 |
| F036 | `segment.H2 2026E.advertising_cor` | advertising_revenue × advertising_cor_pct | advertising_revenue=760; advertising_cor_pct=0.3 | 228.0 |
| F037 | `segment.H2 2026E.solutions_infrastructure_cor` | solutions_infrastructure_revenue × solutions_cor_pct | solutions_infrastructure_revenue=5000; solutions_cor_pct=0.45 | 2,250.0 |
| F038 | `segment.H2 2026E.ai_cor` | advertising_cor + solutions_infrastructure_cor | advertising_cor=228; solutions_infrastructure_cor=2250 | 2,478.0 |
| F039 | `segment.FY2026E.space_revenue` | launch_services + launch_development | launch_services=2408; launch_development=1303 | 3,711.0 |
| F040 | `segment.FY2026E.space_cor` | H1_actual + H2_forecast | H1_actual=610; H2_forecast=815.5 | 1,425.5 |
| F041 | `segment.FY2026E.space_rd` | H1_actual + H2_forecast | H1_actual=2006; H2_forecast=2200 | 4,206.0 |
| F042 | `segment.FY2026E.space_sga` | H1_actual + H2_forecast | H1_actual=169; H2_forecast=200 | 369.0 |
| F043 | `segment.FY2026E.connectivity_revenue` | consumer + enterprise_government | consumer=9625; enterprise_government=6215 | 15,840.0 |
| F044 | `segment.FY2026E.connectivity_cor` | H1_actual + H2_forecast | H1_actual=3711; H2_forecast=3552 | 7,263.0 |
| F045 | `segment.FY2026E.connectivity_rd` | H1_actual + H2_forecast | H1_actual=499; H2_forecast=350 | 849.0 |
| F046 | `segment.FY2026E.connectivity_sga` | H1_actual + H2_forecast | H1_actual=494; H2_forecast=350 | 844.0 |
| F047 | `segment.FY2026E.ai_revenue` | advertising + solutions_infrastructure | advertising=1470; solutions_infrastructure=7669 | 9,139.0 |
| F048 | `segment.FY2026E.ai_cor` | H1_actual + H2_forecast | H1_actual=1562; H2_forecast=2478 | 4,040.0 |
| F049 | `segment.FY2026E.ai_rd` | H1_actual + H2_forecast | H1_actual=4557; H2_forecast=4500 | 9,057.0 |
| F050 | `segment.FY2026E.ai_sga` | H1_actual + H2_forecast | H1_actual=995; H2_forecast=1100 | 2,095.0 |
| F051 | `segment.FY2026E.ai_restruct` | H1_actual + H2_forecast | H1_actual=(-9); H2_forecast=0 | (9.0) |
| F052 | `segment.FY2026E.space.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=1425.5; rd=4206; sga=369; restructuring=0; impairment=0 | 6,000.5 |
| F053 | `segment.FY2026E.space.ebit` | revenue - operating_expenses | revenue=3711; operating_expenses=6000.5 | (2,289.5) |
| F054 | `segment.FY2026E.connectivity.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=7263; rd=849; sga=844; restructuring=0; impairment=0 | 8,956.0 |
| F055 | `segment.FY2026E.connectivity.ebit` | revenue - operating_expenses | revenue=15840; operating_expenses=8956 | 6,884.0 |
| F056 | `segment.FY2026E.ai.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=4040; rd=9057; sga=2095; restructuring=(-9); impairment=0 | 15,183.0 |
| F057 | `segment.FY2026E.ai.ebit` | revenue - operating_expenses | revenue=9139; operating_expenses=15183 | (6,044.0) |
| F058 | `segment.FY2027E.space_revenue` | launch_services + launch_development | launch_services=3015; launch_development=1459.36 | 4,474.4 |
| F059 | `segment.FY2027E.launch_services_cor` | launch_services_revenue × launch_services_cor_pct | launch_services_revenue=3015; launch_services_cor_pct=0.34 | 1,025.1 |
| F060 | `segment.FY2027E.launch_development_cor` | launch_development_revenue × launch_development_cor_pct | launch_development_revenue=1459.36; launch_development_cor_pct=0.44 | 642.1 |
| F061 | `segment.FY2027E.space_cor` | launch_services_cor + launch_development_cor | launch_services_cor=1025.1; launch_development_cor=642.1184 | 1,667.2 |
| F062 | `segment.FY2027E.connectivity_revenue` | consumer + enterprise_government | consumer=11712; enterprise_government=8079.5 | 19,791.5 |
| F063 | `segment.FY2027E.consumer_cor` | consumer_revenue × consumer_cor_pct | consumer_revenue=11712; consumer_cor_pct=0.47 | 5,504.6 |
| F064 | `segment.FY2027E.enterprise_government_cor` | enterprise_government_revenue × enterprise_government_cor_pct | enterprise_government_revenue=8079.5; enterprise_government_cor_pct=0.3 | 2,423.9 |
| F065 | `segment.FY2027E.connectivity_cor` | consumer_cor + enterprise_government_cor | consumer_cor=5504.64; enterprise_government_cor=2423.85 | 7,928.5 |
| F066 | `segment.FY2027E.ai_revenue` | advertising + solutions_infrastructure | advertising=1617; solutions_infrastructure=11120.05 | 12,737.1 |
| F067 | `segment.FY2027E.advertising_cor` | advertising_revenue × advertising_cor_pct | advertising_revenue=1617; advertising_cor_pct=0.28 | 452.8 |
| F068 | `segment.FY2027E.solutions_infrastructure_cor` | solutions_infrastructure_revenue × solutions_cor_pct | solutions_infrastructure_revenue=11120.05; solutions_cor_pct=0.4 | 4,448.0 |
| F069 | `segment.FY2027E.ai_cor` | advertising_cor + solutions_infrastructure_cor | advertising_cor=452.76; solutions_infrastructure_cor=4448.02 | 4,900.8 |
| F070 | `segment.FY2027E.space.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=1667.2184; rd=4200; sga=220; restructuring=0; impairment=0 | 6,087.2 |
| F071 | `segment.FY2027E.space.ebit` | revenue - operating_expenses | revenue=4474.36; operating_expenses=6087.2184 | (1,612.9) |
| F072 | `segment.FY2027E.connectivity.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=7928.49; rd=1000; sga=1100; restructuring=0; impairment=0 | 10,028.5 |
| F073 | `segment.FY2027E.connectivity.ebit` | revenue - operating_expenses | revenue=19791.5; operating_expenses=10028.49 | 9,763.0 |
| F074 | `segment.FY2027E.ai.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=4900.78; rd=8000; sga=2500; restructuring=0; impairment=0 | 15,400.8 |
| F075 | `segment.FY2027E.ai.ebit` | revenue - operating_expenses | revenue=12737.05; operating_expenses=15400.78 | (2,663.7) |
| F076 | `segment.FY2028E.space_revenue` | launch_services + launch_development | launch_services=3450; launch_development=1634.4832 | 5,084.5 |
| F077 | `segment.FY2028E.launch_services_cor` | launch_services_revenue × launch_services_cor_pct | launch_services_revenue=3450; launch_services_cor_pct=0.32 | 1,104.0 |
| F078 | `segment.FY2028E.launch_development_cor` | launch_development_revenue × launch_development_cor_pct | launch_development_revenue=1634.4832; launch_development_cor_pct=0.42 | 686.5 |
| F079 | `segment.FY2028E.space_cor` | launch_services_cor + launch_development_cor | launch_services_cor=1104; launch_development_cor=686.482944 | 1,790.5 |
| F080 | `segment.FY2028E.connectivity_revenue` | consumer + enterprise_government | consumer=14337; enterprise_government=10099.375 | 24,436.4 |
| F081 | `segment.FY2028E.consumer_cor` | consumer_revenue × consumer_cor_pct | consumer_revenue=14337; consumer_cor_pct=0.45 | 6,451.7 |
| F082 | `segment.FY2028E.enterprise_government_cor` | enterprise_government_revenue × enterprise_government_cor_pct | enterprise_government_revenue=10099.375; enterprise_government_cor_pct=0.29 | 2,928.8 |
| F083 | `segment.FY2028E.connectivity_cor` | consumer_cor + enterprise_government_cor | consumer_cor=6451.65; enterprise_government_cor=2928.81875 | 9,380.5 |
| F084 | `segment.FY2028E.ai_revenue` | advertising + solutions_infrastructure | advertising=1746.36; solutions_infrastructure=14456.065 | 16,202.4 |
| F085 | `segment.FY2028E.advertising_cor` | advertising_revenue × advertising_cor_pct | advertising_revenue=1746.36; advertising_cor_pct=0.27 | 471.5 |
| F086 | `segment.FY2028E.solutions_infrastructure_cor` | solutions_infrastructure_revenue × solutions_cor_pct | solutions_infrastructure_revenue=14456.065; solutions_cor_pct=0.36 | 5,204.2 |
| F087 | `segment.FY2028E.ai_cor` | advertising_cor + solutions_infrastructure_cor | advertising_cor=471.5172; solutions_infrastructure_cor=5204.1834 | 5,675.7 |
| F088 | `segment.FY2028E.space.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=1790.482944; rd=3600; sga=230; restructuring=0; impairment=0 | 5,620.5 |
| F089 | `segment.FY2028E.space.ebit` | revenue - operating_expenses | revenue=5084.4832; operating_expenses=5620.482944 | (536.0) |
| F090 | `segment.FY2028E.connectivity.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=9380.46875; rd=1200; sga=1300; restructuring=0; impairment=0 | 11,880.5 |
| F091 | `segment.FY2028E.connectivity.ebit` | revenue - operating_expenses | revenue=24436.375; operating_expenses=11880.46875 | 12,555.9 |
| F092 | `segment.FY2028E.ai.operating_expenses` | cost_of_revenue + rd + sga + restructuring + impairment | cost_of_revenue=5675.7006; rd=8500; sga=2900; restructuring=0; impairment=0 | 17,075.7 |
| F093 | `segment.FY2028E.ai.ebit` | revenue - operating_expenses | revenue=16202.425; operating_expenses=17075.7006 | (873.3) |
| F150 | `segment.H2 2026E.space.revenue` | FY2026_forecast - H1_2026_actual | FY2026_forecast=3711; H1_2026_actual=1581 | 2,130.0 |
| F151 | `segment.H2 2026E.space.cor` | FY2026_forecast - H1_2026_actual | FY2026_forecast=1425.5; H1_2026_actual=610 | 815.5 |
| F152 | `segment.H2 2026E.space.rd` | FY2026_forecast - H1_2026_actual | FY2026_forecast=4206; H1_2026_actual=2006 | 2,200.0 |
| F153 | `segment.H2 2026E.space.sga` | FY2026_forecast - H1_2026_actual | FY2026_forecast=369; H1_2026_actual=169 | 200.0 |
| F154 | `segment.H2 2026E.space.restruct` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F155 | `segment.H2 2026E.space.impairment` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F156 | `segment.H2 2026E.space.ebit` | FY2026_forecast - H1_2026_actual | FY2026_forecast=(-2289.5); H1_2026_actual=(-1204) | (1,085.5) |
| F157 | `segment.H2 2026E.connectivity.revenue` | FY2026_forecast - H1_2026_actual | FY2026_forecast=15840; H1_2026_actual=7548 | 8,292.0 |
| F158 | `segment.H2 2026E.connectivity.cor` | FY2026_forecast - H1_2026_actual | FY2026_forecast=7263; H1_2026_actual=3711 | 3,552.0 |
| F159 | `segment.H2 2026E.connectivity.rd` | FY2026_forecast - H1_2026_actual | FY2026_forecast=849; H1_2026_actual=499 | 350.0 |
| F160 | `segment.H2 2026E.connectivity.sga` | FY2026_forecast - H1_2026_actual | FY2026_forecast=844; H1_2026_actual=494 | 350.0 |
| F161 | `segment.H2 2026E.connectivity.restruct` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F162 | `segment.H2 2026E.connectivity.impairment` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F163 | `segment.H2 2026E.connectivity.ebit` | FY2026_forecast - H1_2026_actual | FY2026_forecast=6884; H1_2026_actual=2844 | 4,040.0 |
| F164 | `segment.H2 2026E.ai.revenue` | FY2026_forecast - H1_2026_actual | FY2026_forecast=9139; H1_2026_actual=3379 | 5,760.0 |
| F165 | `segment.H2 2026E.ai.cor` | FY2026_forecast - H1_2026_actual | FY2026_forecast=4040; H1_2026_actual=1562 | 2,478.0 |
| F166 | `segment.H2 2026E.ai.rd` | FY2026_forecast - H1_2026_actual | FY2026_forecast=9057; H1_2026_actual=4557 | 4,500.0 |
| F167 | `segment.H2 2026E.ai.sga` | FY2026_forecast - H1_2026_actual | FY2026_forecast=2095; H1_2026_actual=995 | 1,100.0 |
| F168 | `segment.H2 2026E.ai.restruct` | FY2026_forecast - H1_2026_actual | FY2026_forecast=(-9); H1_2026_actual=(-9) | 0.0 |
| F169 | `segment.H2 2026E.ai.impairment` | FY2026_forecast - H1_2026_actual | FY2026_forecast=0; H1_2026_actual=0 | 0.0 |
| F170 | `segment.H2 2026E.ai.ebit` | FY2026_forecast - H1_2026_actual | FY2026_forecast=(-6044); H1_2026_actual=(-3726) | (2,318.0) |
| F197 | `cashflow.H2 2026E.total_launches` | customer_falcon_launches + internal_falcon_launches + starship_launches | customer_falcon_launches=22; internal_falcon_launches=58; starship_launches=2 | 82.0 |
| F198 | `cashflow.H2 2026E.space_capex` | total_launches × space_capex_per_launch | total_launches=82; space_capex_per_launch=28.54 | 2,340.3 |
| F199 | `cashflow.H2 2026E.subscriber_net_adds_m` | ending_subscribers_m - opening_subscribers_m | ending_subscribers_m=14; opening_subscribers_m=12 | 2.0 |
| F200 | `cashflow.H2 2026E.connectivity_capex` | subscriber_net_adds_m × capex_per_net_add | subscriber_net_adds_m=2; capex_per_net_add=822 | 1,644.0 |
| F201 | `cashflow.FY2027E.total_launches` | customer_falcon_launches + internal_falcon_launches + starship_launches | customer_falcon_launches=45; internal_falcon_launches=130; starship_launches=5 | 180.0 |
| F202 | `cashflow.FY2027E.space_capex` | total_launches × space_capex_per_launch | total_launches=180; space_capex_per_launch=27 | 4,860.0 |
| F203 | `cashflow.FY2027E.subscriber_net_adds_m` | ending_subscribers_m - opening_subscribers_m | ending_subscribers_m=18; opening_subscribers_m=14 | 4.0 |
| F204 | `cashflow.FY2027E.connectivity_capex` | subscriber_net_adds_m × capex_per_net_add | subscriber_net_adds_m=4; capex_per_net_add=800 | 3,200.0 |
| F205 | `cashflow.FY2028E.total_launches` | customer_falcon_launches + internal_falcon_launches + starship_launches | customer_falcon_launches=50; internal_falcon_launches=140; starship_launches=10 | 200.0 |
| F206 | `cashflow.FY2028E.space_capex` | total_launches × space_capex_per_launch | total_launches=200; space_capex_per_launch=25 | 5,000.0 |
| F207 | `cashflow.FY2028E.subscriber_net_adds_m` | ending_subscribers_m - opening_subscribers_m | ending_subscribers_m=22.5; opening_subscribers_m=18 | 4.5 |
| F208 | `cashflow.FY2028E.connectivity_capex` | subscriber_net_adds_m × capex_per_net_add | subscriber_net_adds_m=4.5; capex_per_net_add=750 | 3,375.0 |
| F209 | `cashflow.FY2026E.space_capex` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2226; H2_2026_forecast=2340.28 | 4,566.3 |
| F210 | `cashflow.FY2026E.connectivity_capex` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=2699; H2_2026_forecast=1644 | 4,343.0 |
| F211 | `cashflow.FY2026E.ai_capex` | H1_2026_actual + H2_2026_forecast | H1_2026_actual=23551; H2_2026_forecast=18000 | 41,551.0 |
