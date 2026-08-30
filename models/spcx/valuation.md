# SpaceX valuation

as_of: 2026-08-30
target_date: 2027-08-30
units: USD millions except per-share data, shares and operating drivers
generator: `compute.py`

## Price target

| item | value | basis |
| --- | ---: | --- |
| **12-month base price target** | **$73.40 [DEDUCTED F317]** | Segment SOTP discounted to 2027-08-30 |
| Last sale | $141.50 [FACT] | Nasdaq `lastTradeTimestamp` 2026-08-27 |
| Implied change | -48.1% [DEDUCTED F318] | Price target ÷ last sale − one |
| Basic shares | 13,572.8 million [DEDUCTED F288] | Post-Cursor; fully diluted shares not obtained |
| Load-bearing method | SOTP | Connectivity EBIT, Space revenue with zero Starship commercial revenue, AI invested-capital conversion with Customer B haircut |

The target is generated from the segment model and named valuation inputs below. It is not fitted to the last sale.

## Load-bearing SOTP — base bridge

| piece | metric | metric value | valuation input | FY2028 value | 12-month value |
| --- | --- | ---: | --- | ---: | ---: |
| Connectivity | FY2028E scenario EBIT | $12,555.9 [DEDUCTED F307] | 70× EBIT [VIEW] | $878,913.4 [DEDUCTED F308] | $769,360.2 [DEDUCTED F319] |
| Space | FY2028E modeled revenue; Starship revenue zero | $5,084.5 [DEDUCTED F309] | 12× revenue [VIEW] | $61,013.8 [DEDUCTED F310] | $53,408.7 [DEDUCTED F320] |
| AI | Cumulative FY2026E–FY2028E AI capex | $96,551.0 [DEDUCTED F301] | 2× capital, then 20% Customer B haircut [VIEW] | $154,481.6 [DEDUCTED F312] | $135,226.1 [DEDUCTED F321] |
| **Enterprise value** | Sum of pieces |  |  | $1,094,408.8 [DEDUCTED F313] | $957,995.0 [DEDUCTED F315] |
| Net cash | Target-date base cash bridge |  |  |  | $38,237.1 [DEDUCTED F300] |
| **Equity value** | Target EV + net cash |  |  |  | $996,232.0 [DEDUCTED F316] |
| **Price target** | Equity value ÷ basic shares | 13,572.8 [DEDUCTED F288] |  |  | $73.4 [DEDUCTED F317] |

Target net cash uses FY2026E ending liquidity less debt and eight months of FY2027E FCF, with no new financing. EchoStar is excluded. Cursor P&L contribution and synergy premium are zero.

## Bear / base / bull assumptions

| scenario | driver | assumption | treatment |
| --- | --- | --- | --- |
| Bear | Connectivity subscribers / ARPU | 17.0m → 20.0m / $54.0 [VIEW] | `research.md` explicit subscriber and ARPU paths |
| Bear | Enterprise & Government factor | 85.0% of base [VIEW] | Starshield remains embedded; standalone P&L not obtained |
| Bear | Connectivity exit EBIT multiple | 40.0× [VIEW] | Selected SOTP input; primary-source peer multiple not obtained |
| Bear | Space exit revenue multiple / Starship revenue | 8.0× / $0.0 [VIEW] | Starship commercial revenue stays zero |
| Bear | AI capital conversion / Customer B haircut | 0.8× / 40.0% [VIEW] | AI capex conversion with explicit concentration haircut |
| Bear | WACC / years to FY2028 | 13.5% / 1.3 [VIEW] | Discount FY2028 segment values to the 12-month target date |
| Base | Connectivity subscribers / ARPU | 18.0m → 22.5m / $59.0 [VIEW] | `research.md` explicit subscriber and ARPU paths |
| Base | Enterprise & Government factor | 100.0% of base [VIEW] | Starshield remains embedded; standalone P&L not obtained |
| Base | Connectivity exit EBIT multiple | 70.0× [VIEW] | Selected SOTP input; primary-source peer multiple not obtained |
| Base | Space exit revenue multiple / Starship revenue | 12.0× / $0.0 [VIEW] | Starship commercial revenue stays zero |
| Base | AI capital conversion / Customer B haircut | 2.0× / 20.0% [VIEW] | AI capex conversion with explicit concentration haircut |
| Base | WACC / years to FY2028 | 10.5% / 1.3 [VIEW] | Discount FY2028 segment values to the 12-month target date |
| Bull | Connectivity subscribers / ARPU | 19.0m → 25.0m / $65.0 [VIEW] | `research.md` explicit subscriber and ARPU paths |
| Bull | Enterprise & Government factor | 115.0% of base [VIEW] | Starshield remains embedded; standalone P&L not obtained |
| Bull | Connectivity exit EBIT multiple | 95.0× [VIEW] | Selected SOTP input; primary-source peer multiple not obtained |
| Bull | Space exit revenue multiple / Starship revenue | 20.0× / $0.0 [VIEW] | Starship commercial revenue stays zero |
| Bull | AI capital conversion / Customer B haircut | 7.0× / 5.0% [VIEW] | AI capex conversion with explicit concentration haircut |
| Bull | WACC / years to FY2028 | 9.0% / 1.3 [VIEW] | Discount FY2028 segment values to the 12-month target date |

Starship commercial revenue is zero in every scenario. Bull and bear change Connectivity ARPU/net adds, Enterprise & Government realization, AI capex conversion, Customer B concentration haircut, exit multiples and WACC.

## Scenario outputs

| scenario | FY2028 Consumer revenue | FY2028 Connectivity EBIT | target EV | target equity | price / share | vs last sale |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Bear | $11,988.0 [DEDUCTED F343] | $10,355.0 [DEDUCTED F347] | $420,905.2 [DEDUCTED F355] | $459,142.3 [DEDUCTED F356] | $33.8 [DEDUCTED F357] | -76.1% [DEDUCTED F358] |
| Base | $14,337.0 [DEDUCTED F303] | $12,555.9 [DEDUCTED F307] | $957,995.0 [DEDUCTED F315] | $996,232.0 [DEDUCTED F316] | $73.4 [DEDUCTED F317] | -48.1% [DEDUCTED F318] |
| Bull | $17,160.0 [DEDUCTED F323] | $15,017.5 [DEDUCTED F327] | $1,934,822.1 [DEDUCTED F335] | $1,973,059.2 [DEDUCTED F336] | $145.4 [DEDUCTED F337] | 2.7% [DEDUCTED F338] |

## Dilution sensitivity — not known fully diluted shares

| item | value | treatment |
| --- | ---: | --- |
| Basic shares | 13,572.8 million [DEDUCTED F288] | Base price-target denominator |
| Potentially dilutive awards | 564.0 million [FACT] | Sensitivity only; treasury-stock-method dilution not obtained |
| Sensitivity shares | 14,136.8 [DEDUCTED F362] million | Basic plus all potentially dilutive awards |
| Sensitivity price / share | $70.5 [DEDUCTED F363] | Same base equity value |
| Price haircut | 4.0% [DEDUCTED F364] | Sensitivity price versus base |

The sensitivity does not assert that the awards are fully dilutive.

## What the last sale already prices

| measure | value | basis |
| --- | ---: | --- |
| Last sale | $141.50 [FACT] | Nasdaq `lastTradeTimestamp` 2026-08-27 |
| Current market capitalization | $1,920,554.3 [FACT] | `register.md` What is already priced |
| Current mixed-date enterprise value | $1,859,909.3 [DEDUCTED F299] | Market cap plus debt less cash and securities |
| Base target implied enterprise value | $957,995.0 [DEDUCTED F315] | Discounted SOTP pieces |
| Current EV / FY2028E revenue | 40.7× [DEDUCTED F367] | Current EV ÷ model revenue |
| Base target EV / FY2028E revenue | 21.0× [DEDUCTED F365] | Target EV ÷ model revenue |
| Current EV / FY2028E EBIT | 166.9× [DEDUCTED F368] | Current EV ÷ model EBIT |
| Base target EV / FY2028E EBIT | 85.9× [DEDUCTED F366] | Target EV ÷ model EBIT |
| Current EV premium to base target EV | 94.1% [DEDUCTED F369] | Same FY2028 model denominator |

## Consolidated DCF check — not load-bearing

Explicit model FCF is negative through FY2027E and approximately zero in FY2028E. The extension makes the terminal auditable by fading consolidated revenue growth and FCF margins explicitly.

| period | revenue | fade assumption | FCF | PV FCF |
| --- | ---: | --- | ---: | ---: |
| FY2028E | $45,723.3 [DEDUCTED F142] | model | $31.1 [DEDUCTED F263] | $27.2 [DEDUCTED F371] |
| FY2029E | $54,867.9 [DEDUCTED F372] | 20.0% revenue growth / 8.0% FCF margin [VIEW] | $4,389.4 [DEDUCTED F373] | $3,477.2 [DEDUCTED F375] |
| FY2030E | $63,646.8 [DEDUCTED F376] | 16.0% revenue growth / 16.0% FCF margin [VIEW] | $10,183.5 [DEDUCTED F377] | $7,300.6 [DEDUCTED F379] |
| FY2031E | $71,284.4 [DEDUCTED F380] | 12.0% revenue growth / 23.0% FCF margin [VIEW] | $16,395.4 [DEDUCTED F381] | $10,637.0 [DEDUCTED F383] |
| FY2032E | $77,700.0 [DEDUCTED F384] | 9.0% revenue growth / 28.0% FCF margin [VIEW] | $21,756.0 [DEDUCTED F385] | $12,773.6 [DEDUCTED F387] |
| FY2033E | $82,362.0 [DEDUCTED F388] | 6.0% revenue growth / 31.0% FCF margin [VIEW] | $25,532.2 [DEDUCTED F389] | $13,566.3 [DEDUCTED F391] |

| item | value | basis |
| --- | ---: | --- |
| WACC | 10.5% [VIEW] | Named discount-rate input |
| Terminal growth | 3.5% [VIEW] | Perpetuity-growth input |
| Exit FCF multiple | 25.0× [VIEW] | Alternative terminal-value check |
| Perpetuity DCF enterprise value | $248,369.1 [DEDUCTED F395] | Extended explicit fade plus terminal value |
| Perpetuity DCF value / share | $21.1 [DEDUCTED F397] | Basic shares |
| PV terminal value / DCF EV | 80.8% [DEDUCTED F398] | Shows terminal dependence |
| Exit-multiple DCF enterprise value | $386,939.0 [DEDUCTED F401] | 25× FY2033E FCF terminal |
| Exit-multiple DCF value / share | $31.3 [DEDUCTED F403] | Basic shares |

## Comps check

| peer set | primary-source trading multiple | treatment |
| --- | --- | --- |
| Listed launch providers | **not obtained** | No filing/exchange-derived comparable EV multiple obtained |
| Satellite connectivity providers | **not obtained** | No filing/exchange-derived comparable EV multiple obtained |
| AI infrastructure / platform providers | **not obtained** | No filing/exchange-derived comparable EV multiple obtained |

No peer EV/EBITDA multiple is invented. Current and target implied multiples are shown in “What the last sale already prices.”

## Exclusions and gaps

- EchoStar consideration and shares remain a scenario, not base.
- Cursor P&L contribution and synergy premium are zero; standalone contribution is **not obtained**.
- Starshield standalone P&L, launch list price, GPU-hours and utilization remain **not obtained**.
- Fully diluted shares remain **not obtained**; the award count is only a sensitivity.

## Valuation formula register

Every `[DEDUCTED]` cell above points to one of these formulas.

| id | output | expression | named inputs | result |
| --- | --- | --- | --- | --- |
| F299 | `valuation.current_enterprise_value` | current_market_cap + debt_and_finance_leases - cash - marketable_securities | current_market_cap=1920554.3; debt_and_finance_leases=39364; cash=93522; marketable_securities=6487 | 1,859,909.3 |
| F300 | `valuation.target_net_cash` | FY2026_ending_liquidity - debt + FY2027_FCF × months_to_target ÷ twelve_months | FY2026_ending_liquidity=86220.72; debt=39364; FY2027_FCF=(-12929.439372); months_to_target=8; twelve_months=12 | 38,237.1 |
| F301 | `valuation.ai_invested_capital` | FY2026E_AI_capex + FY2027E_AI_capex + FY2028E_AI_capex | FY2026E_AI_capex=41551; FY2027E_AI_capex=30000; FY2028E_AI_capex=25000 | 96,551.0 |
| F302 | `valuation.base.average_subscribers` | (opening_subscribers + ending_subscribers) ÷ two | opening_subscribers_m=18; ending_subscribers_m=22.5; two=2 | 20.3 |
| F303 | `valuation.base.consumer_revenue` | average_subscribers × ARPU × twelve_months | average_subscribers_m=20.25; ARPU=59; twelve_months=12 | 14,337.0 |
| F304 | `valuation.base.enterprise_revenue` | base_enterprise_revenue × scenario_factor | base_enterprise_revenue=10099.375; scenario_factor=1 | 10,099.4 |
| F305 | `valuation.base.consumer_ebit_change` | (scenario_consumer_revenue - base_consumer_revenue) × incremental_margin | scenario_consumer_revenue=14337; base_consumer_revenue=14337; incremental_margin=0.55 | 0.0 |
| F306 | `valuation.base.enterprise_ebit_change` | (scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin | scenario_enterprise_revenue=10099.375; base_enterprise_revenue=10099.375; incremental_margin=0.6 | 0.0 |
| F307 | `valuation.base.connectivity_ebit` | base_connectivity_EBIT + consumer_EBIT_change + enterprise_EBIT_change | base_connectivity_EBIT=12555.90625; consumer_EBIT_change=0; enterprise_EBIT_change=0 | 12,555.9 |
| F308 | `valuation.base.connectivity_value_FY2028` | scenario_connectivity_EBIT × connectivity_exit_EBIT_multiple | scenario_connectivity_EBIT=12555.90625; connectivity_exit_EBIT_multiple=70 | 878,913.4 |
| F309 | `valuation.base.space_revenue` | modeled_launch_revenue + Starship_commercial_revenue | modeled_launch_revenue=5084.4832; Starship_commercial_revenue=0 | 5,084.5 |
| F310 | `valuation.base.space_value_FY2028` | space_revenue × space_exit_revenue_multiple | space_revenue=5084.4832; space_exit_revenue_multiple=12 | 61,013.8 |
| F311 | `valuation.base.ai_gross_value_FY2028` | AI_invested_capital × AI_capital_conversion_multiple | AI_invested_capital=96551; AI_capital_conversion_multiple=2 | 193,102.0 |
| F312 | `valuation.base.ai_value_FY2028` | AI_gross_value × (one - Customer_B_haircut) | AI_gross_value=193102; Customer_B_haircut=0.2 | 154,481.6 |
| F313 | `valuation.base.end_FY2028_enterprise_value` | Connectivity + Space + AI | Connectivity=878913.4375; Space=61013.7984; AI=154481.6 | 1,094,408.8 |
| F314 | `valuation.base.discount_factor` | one_plus_WACC ^ years_from_target_to_FY2028 | one_plus_WACC=1.105; years_from_target_to_FY2028=1.3333333333 | 1.1 |
| F315 | `valuation.base.target_enterprise_value` | end_FY2028_enterprise_value ÷ discount_factor | end_FY2028_enterprise_value=1094408.8359; discount_factor=1.142395202714266041915937358 | 957,995.0 |
| F316 | `valuation.base.target_equity_value` | target_enterprise_value + target_net_cash | target_enterprise_value=957994.9506963499470218053017; target_net_cash=38237.093752 | 996,232.0 |
| F317 | `valuation.base.price_target` | target_equity_value ÷ basic_shares_m | target_equity_value=996232.0444483499470218053017; basic_shares_m=13572.821625 | 73.4 |
| F318 | `valuation.base.implied_change` | price_target ÷ last_sale - one | price_target=73.39903757472020465175790606; last_sale=141.5; one=1 | (0.5) |
| F319 | `valuation.base.pv_connectivity` | FY2028_connectivity_value ÷ discount_factor | FY2028_connectivity_value=878913.4375; discount_factor=1.142395202714266041915937358 | 769,360.2 |
| F320 | `valuation.base.pv_space` | FY2028_space_value ÷ discount_factor | FY2028_space_value=61013.7984; discount_factor=1.142395202714266041915937358 | 53,408.7 |
| F321 | `valuation.base.pv_ai` | FY2028_AI_value ÷ discount_factor | FY2028_AI_value=154481.6; discount_factor=1.142395202714266041915937358 | 135,226.1 |
| F322 | `valuation.bull.average_subscribers` | (opening_subscribers + ending_subscribers) ÷ two | opening_subscribers_m=19; ending_subscribers_m=25; two=2 | 22.0 |
| F323 | `valuation.bull.consumer_revenue` | average_subscribers × ARPU × twelve_months | average_subscribers_m=22; ARPU=65; twelve_months=12 | 17,160.0 |
| F324 | `valuation.bull.enterprise_revenue` | base_enterprise_revenue × scenario_factor | base_enterprise_revenue=10099.375; scenario_factor=1.15 | 11,614.3 |
| F325 | `valuation.bull.consumer_ebit_change` | (scenario_consumer_revenue - base_consumer_revenue) × incremental_margin | scenario_consumer_revenue=17160; base_consumer_revenue=14337; incremental_margin=0.55 | 1,552.7 |
| F326 | `valuation.bull.enterprise_ebit_change` | (scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin | scenario_enterprise_revenue=11614.28125; base_enterprise_revenue=10099.375; incremental_margin=0.6 | 908.9 |
| F327 | `valuation.bull.connectivity_ebit` | base_connectivity_EBIT + consumer_EBIT_change + enterprise_EBIT_change | base_connectivity_EBIT=12555.90625; consumer_EBIT_change=1552.65; enterprise_EBIT_change=908.94375 | 15,017.5 |
| F328 | `valuation.bull.connectivity_value_FY2028` | scenario_connectivity_EBIT × connectivity_exit_EBIT_multiple | scenario_connectivity_EBIT=15017.5; connectivity_exit_EBIT_multiple=95 | 1,426,662.5 |
| F329 | `valuation.bull.space_revenue` | modeled_launch_revenue + Starship_commercial_revenue | modeled_launch_revenue=5084.4832; Starship_commercial_revenue=0 | 5,084.5 |
| F330 | `valuation.bull.space_value_FY2028` | space_revenue × space_exit_revenue_multiple | space_revenue=5084.4832; space_exit_revenue_multiple=20 | 101,689.7 |
| F331 | `valuation.bull.ai_gross_value_FY2028` | AI_invested_capital × AI_capital_conversion_multiple | AI_invested_capital=96551; AI_capital_conversion_multiple=7 | 675,857.0 |
| F332 | `valuation.bull.ai_value_FY2028` | AI_gross_value × (one - Customer_B_haircut) | AI_gross_value=675857; Customer_B_haircut=0.05 | 642,064.2 |
| F333 | `valuation.bull.end_FY2028_enterprise_value` | Connectivity + Space + AI | Connectivity=1426662.5; Space=101689.664; AI=642064.15 | 2,170,416.3 |
| F334 | `valuation.bull.discount_factor` | one_plus_WACC ^ years_from_target_to_FY2028 | one_plus_WACC=1.09; years_from_target_to_FY2028=1.3333333333 | 1.1 |
| F335 | `valuation.bull.target_enterprise_value` | end_FY2028_enterprise_value ÷ discount_factor | end_FY2028_enterprise_value=2170416.314; discount_factor=1.121765288559719670594006561 | 1,934,822.1 |
| F336 | `valuation.bull.target_equity_value` | target_enterprise_value + target_net_cash | target_enterprise_value=1934822.138048759082509029356; target_net_cash=38237.093752 | 1,973,059.2 |
| F337 | `valuation.bull.price_target` | target_equity_value ÷ basic_shares_m | target_equity_value=1973059.231800759082509029356; basic_shares_m=13572.821625 | 145.4 |
| F338 | `valuation.bull.implied_change` | price_target ÷ last_sale - one | price_target=145.3683903254537232238200401; last_sale=141.5; one=1 | 0.0 |
| F339 | `valuation.bull.pv_connectivity` | FY2028_connectivity_value ÷ discount_factor | FY2028_connectivity_value=1426662.5; discount_factor=1.121765288559719670594006561 | 1,271,801.3 |
| F340 | `valuation.bull.pv_space` | FY2028_space_value ÷ discount_factor | FY2028_space_value=101689.664; discount_factor=1.121765288559719670594006561 | 90,651.5 |
| F341 | `valuation.bull.pv_ai` | FY2028_AI_value ÷ discount_factor | FY2028_AI_value=642064.15; discount_factor=1.121765288559719670594006561 | 572,369.4 |
| F342 | `valuation.bear.average_subscribers` | (opening_subscribers + ending_subscribers) ÷ two | opening_subscribers_m=17; ending_subscribers_m=20; two=2 | 18.5 |
| F343 | `valuation.bear.consumer_revenue` | average_subscribers × ARPU × twelve_months | average_subscribers_m=18.5; ARPU=54; twelve_months=12 | 11,988.0 |
| F344 | `valuation.bear.enterprise_revenue` | base_enterprise_revenue × scenario_factor | base_enterprise_revenue=10099.375; scenario_factor=0.85 | 8,584.5 |
| F345 | `valuation.bear.consumer_ebit_change` | (scenario_consumer_revenue - base_consumer_revenue) × incremental_margin | scenario_consumer_revenue=11988; base_consumer_revenue=14337; incremental_margin=0.55 | (1,292.0) |
| F346 | `valuation.bear.enterprise_ebit_change` | (scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin | scenario_enterprise_revenue=8584.46875; base_enterprise_revenue=10099.375; incremental_margin=0.6 | (908.9) |
| F347 | `valuation.bear.connectivity_ebit` | base_connectivity_EBIT + consumer_EBIT_change + enterprise_EBIT_change | base_connectivity_EBIT=12555.90625; consumer_EBIT_change=(-1291.95); enterprise_EBIT_change=(-908.94375) | 10,355.0 |
| F348 | `valuation.bear.connectivity_value_FY2028` | scenario_connectivity_EBIT × connectivity_exit_EBIT_multiple | scenario_connectivity_EBIT=10355.0125; connectivity_exit_EBIT_multiple=40 | 414,200.5 |
| F349 | `valuation.bear.space_revenue` | modeled_launch_revenue + Starship_commercial_revenue | modeled_launch_revenue=5084.4832; Starship_commercial_revenue=0 | 5,084.5 |
| F350 | `valuation.bear.space_value_FY2028` | space_revenue × space_exit_revenue_multiple | space_revenue=5084.4832; space_exit_revenue_multiple=8 | 40,675.9 |
| F351 | `valuation.bear.ai_gross_value_FY2028` | AI_invested_capital × AI_capital_conversion_multiple | AI_invested_capital=96551; AI_capital_conversion_multiple=0.75 | 72,413.3 |
| F352 | `valuation.bear.ai_value_FY2028` | AI_gross_value × (one - Customer_B_haircut) | AI_gross_value=72413.25; Customer_B_haircut=0.4 | 43,448.0 |
| F353 | `valuation.bear.end_FY2028_enterprise_value` | Connectivity + Space + AI | Connectivity=414200.5; Space=40675.8656; AI=43447.95 | 498,324.3 |
| F354 | `valuation.bear.discount_factor` | one_plus_WACC ^ years_from_target_to_FY2028 | one_plus_WACC=1.135; years_from_target_to_FY2028=1.3333333333 | 1.2 |
| F355 | `valuation.bear.target_enterprise_value` | end_FY2028_enterprise_value ÷ discount_factor | end_FY2028_enterprise_value=498324.3156; discount_factor=1.183934879555245110264851961 | 420,905.2 |
| F356 | `valuation.bear.target_equity_value` | target_enterprise_value + target_net_cash | target_enterprise_value=420905.1732534475493443443835; target_net_cash=38237.093752 | 459,142.3 |
| F357 | `valuation.bear.price_target` | target_equity_value ÷ basic_shares_m | target_equity_value=459142.2670054475493443443835; basic_shares_m=13572.821625 | 33.8 |
| F358 | `valuation.bear.implied_change` | price_target ÷ last_sale - one | price_target=33.82806314640914242062356607; last_sale=141.5; one=1 | (0.8) |
| F359 | `valuation.bear.pv_connectivity` | FY2028_connectivity_value ÷ discount_factor | FY2028_connectivity_value=414200.5; discount_factor=1.183934879555245110264851961 | 349,850.7 |
| F360 | `valuation.bear.pv_space` | FY2028_space_value ÷ discount_factor | FY2028_space_value=40675.8656; discount_factor=1.183934879555245110264851961 | 34,356.5 |
| F361 | `valuation.bear.pv_ai` | FY2028_AI_value ÷ discount_factor | FY2028_AI_value=43447.95; discount_factor=1.183934879555245110264851961 | 36,697.9 |
| F362 | `valuation.dilution_sensitivity_shares` | basic_shares_m + potentially_dilutive_awards_m | basic_shares_m=13572.821625; potentially_dilutive_awards_m=564 | 14,136.8 |
| F363 | `valuation.dilution_sensitivity_price` | base_target_equity_value ÷ basic_plus_potential_awards_m | base_target_equity_value=996232.0444483499470218053017; basic_plus_potential_awards_m=14136.821625 | 70.5 |
| F364 | `valuation.dilution_sensitivity_haircut` | one - sensitivity_price ÷ base_price_target | one=1; sensitivity_price=70.47072325554294790232279681; base_price_target=73.39903757472020465175790606 | 0.0 |
| F365 | `valuation.base.target_EV_to_FY2028_revenue` | target_enterprise_value ÷ FY2028_revenue | target_enterprise_value=957994.9506963499470218053017; FY2028_revenue=45723.2832 | 21.0 |
| F366 | `valuation.base.target_EV_to_FY2028_EBIT` | target_enterprise_value ÷ FY2028_EBIT | target_enterprise_value=957994.9506963499470218053017; FY2028_EBIT=11146.630906 | 85.9 |
| F367 | `valuation.current_EV_to_FY2028_revenue` | current_enterprise_value ÷ FY2028_revenue | current_enterprise_value=1859909.3; FY2028_revenue=45723.2832 | 40.7 |
| F368 | `valuation.current_EV_to_FY2028_EBIT` | current_enterprise_value ÷ FY2028_EBIT | current_enterprise_value=1859909.3; FY2028_EBIT=11146.630906 | 166.9 |
| F369 | `valuation.current_EV_premium_to_base_target_EV` | current_enterprise_value ÷ base_target_enterprise_value - one | current_enterprise_value=1859909.3; base_target_enterprise_value=957994.9506963499470218053017; one=1 | 0.9 |
| F370 | `valuation.dcf.FY2028_discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=1.3333333333 | 1.1 |
| F371 | `valuation.dcf.FY2028_PV_FCF` | FY2028_FCF ÷ discount_factor | FY2028_FCF=31.0845528; discount_factor=1.142395202714266041915937358 | 27.2 |
| F372 | `valuation.dcf.FY2029E.revenue` | prior_revenue × (one + growth) | prior_revenue=45723.2832; one_plus_growth=1.2 | 54,867.9 |
| F373 | `valuation.dcf.FY2029E.FCF` | revenue × FCF_margin | revenue=54867.93984; FCF_margin=0.08 | 4,389.4 |
| F374 | `valuation.dcf.FY2029E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=2.3333333333 | 1.3 |
| F375 | `valuation.dcf.FY2029E.PV_FCF` | FCF ÷ discount_factor | FCF=4389.4351872; discount_factor=1.26234669899926397631711078 | 3,477.2 |
| F376 | `valuation.dcf.FY2030E.revenue` | prior_revenue × (one + growth) | prior_revenue=54867.93984; one_plus_growth=1.16 | 63,646.8 |
| F377 | `valuation.dcf.FY2030E.FCF` | revenue × FCF_margin | revenue=63646.8102144; FCF_margin=0.16 | 10,183.5 |
| F378 | `valuation.dcf.FY2030E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=3.3333333333 | 1.4 |
| F379 | `valuation.dcf.FY2030E.PV_FCF` | FCF ÷ discount_factor | FCF=10183.489634304; discount_factor=1.394893102394186693830407412 | 7,300.6 |
| F380 | `valuation.dcf.FY2031E.revenue` | prior_revenue × (one + growth) | prior_revenue=63646.8102144; one_plus_growth=1.12 | 71,284.4 |
| F381 | `valuation.dcf.FY2031E.FCF` | revenue × FCF_margin | revenue=71284.427440128; FCF_margin=0.23 | 16,395.4 |
| F382 | `valuation.dcf.FY2031E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=4.3333333333 | 1.5 |
| F383 | `valuation.dcf.FY2031E.PV_FCF` | FCF ÷ discount_factor | FCF=16395.41831122944; discount_factor=1.54135687814557629668260019 | 10,637.0 |
| F384 | `valuation.dcf.FY2032E.revenue` | prior_revenue × (one + growth) | prior_revenue=71284.427440128; one_plus_growth=1.09 | 77,700.0 |
| F385 | `valuation.dcf.FY2032E.FCF` | revenue × FCF_margin | revenue=77700.02590973952; FCF_margin=0.28 | 21,756.0 |
| F386 | `valuation.dcf.FY2032E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=5.3333333333 | 1.7 |
| F387 | `valuation.dcf.FY2032E.PV_FCF` | FCF ÷ discount_factor | FCF=21756.0072547270656; discount_factor=1.70319935035086180783427321 | 12,773.6 |
| F388 | `valuation.dcf.FY2033E.revenue` | prior_revenue × (one + growth) | prior_revenue=77700.02590973952; one_plus_growth=1.06 | 82,362.0 |
| F389 | `valuation.dcf.FY2033E.FCF` | revenue × FCF_margin | revenue=82362.0274643238912; FCF_margin=0.31 | 25,532.2 |
| F390 | `valuation.dcf.FY2033E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=6.3333333333 | 1.9 |
| F391 | `valuation.dcf.FY2033E.PV_FCF` | FCF ÷ discount_factor | FCF=25532.228513940406272; discount_factor=1.882035282137702297656871897 | 13,566.3 |
| F392 | `valuation.dcf.terminal_value` | FY2033_FCF × (one + terminal_growth) ÷ (WACC - terminal_growth) | FY2033_FCF=25532.228513940406272; terminal_growth=0.035; WACC=0.105 | 377,512.2 |
| F393 | `valuation.dcf.terminal_discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=6.3333333333 | 1.9 |
| F394 | `valuation.dcf.PV_terminal_value` | terminal_value ÷ discount_factor | terminal_value=377512.235884690292736; discount_factor=1.882035282137702297656871897 | 200,587.2 |
| F395 | `valuation.dcf.enterprise_value` | PV_FY2028E_FCF + PV_FY2029E_FCF + PV_FY2030E_FCF + PV_FY2031E_FCF + PV_FY2032E_FCF + PV_FY2033E_FCF + PV_terminal_value | PV_FY2028E_FCF=27.20998191006480953383219085; PV_FY2029E_FCF=3477.202570957536368099163564; PV_FY2030E_FCF=7300.552004182338799991004044; PV_FY2031E_FCF=10637.00337260956150948915522; PV_FY2032E_FCF=12773.61176203202113986264085; PV_FY2033E_FCF=13566.2857950992958841592236; PV_terminal_value=200587.2256846824462872113776 | 248,369.1 |
| F396 | `valuation.dcf.equity_value` | enterprise_value + target_net_cash | enterprise_value=248369.0911714732647983463971; target_net_cash=38237.093752 | 286,606.2 |
| F397 | `valuation.dcf.price_per_share` | equity_value ÷ basic_shares_m | equity_value=286606.1849234732647983463971; basic_shares_m=13572.821625 | 21.1 |
| F398 | `valuation.dcf.terminal_value_share` | PV_terminal_value ÷ DCF_enterprise_value | PV_terminal_value=200587.2256846824462872113776; DCF_enterprise_value=248369.0911714732647983463971 | 0.8 |
| F399 | `valuation.dcf.exit_terminal_value` | FY2033_FCF × exit_FCF_multiple | FY2033_FCF=25532.228513940406272; exit_FCF_multiple=25 | 638,305.7 |
| F400 | `valuation.dcf.PV_exit_terminal_value` | exit_terminal_value ÷ discount_factor | exit_terminal_value=638305.7128485101568; discount_factor=1.882035282137702297656871897 | 339,157.1 |
| F401 | `valuation.dcf.exit_enterprise_value` | PV_FY2028E_FCF + PV_FY2029E_FCF + PV_FY2030E_FCF + PV_FY2031E_FCF + PV_FY2032E_FCF + PV_FY2033E_FCF + PV_exit_terminal_value | PV_FY2028E_FCF=27.20998191006480953383219085; PV_FY2029E_FCF=3477.202570957536368099163564; PV_FY2030E_FCF=7300.552004182338799991004044; PV_FY2031E_FCF=10637.00337260956150948915522; PV_FY2032E_FCF=12773.61176203202113986264085; PV_FY2033E_FCF=13566.2857950992958841592236; PV_exit_terminal_value=339157.1448774823971039805901 | 386,939.0 |
| F402 | `valuation.dcf.exit_equity_value` | enterprise_value + target_net_cash | enterprise_value=386939.0103642732156151156096; target_net_cash=38237.093752 | 425,176.1 |
| F403 | `valuation.dcf.exit_price_per_share` | equity_value ÷ basic_shares_m | equity_value=425176.1041162732156151156096; basic_shares_m=13572.821625 | 31.3 |
