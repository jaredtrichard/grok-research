# SpaceX valuation

as_of: 2026-08-30
target_date: 2027-08-30
units: USD millions except per-share data, shares and operating drivers
generator: `compute.py`

## Price target

| item | value | basis |
| --- | ---: | --- |
| **12-month base price target** | **$85.77 [DEDUCTED F350]** | Segment SOTP discounted to 2027-08-30 |
| Last sale | $141.50 [FACT] | Nasdaq `lastTradeTimestamp` 2026-08-27 |
| Implied change | -39.4% [DEDUCTED F351] | Price target ÷ last sale − one |
| Basic shares | 13,834.6 million [DEDUCTED F313] | Post-Cursor plus pending EchoStar shares; fully diluted shares not obtained |
| Load-bearing method | SOTP | Connectivity EBIT including pending spectrum/mobile, Space revenue including Starship, AI invested-capital conversion, and Cursor EBIT |

The target is generated from the segment model and named valuation inputs below. It is not fitted to the last sale.

## Load-bearing SOTP — base bridge

| piece | metric | metric value | valuation input | FY2028 value | 12-month value |
| --- | --- | ---: | --- | ---: | ---: |
| Connectivity | FY2028E scenario EBIT | $14,180.9 [DEDUCTED F337] | 70× EBIT [VIEW; as_of 2026-08-30; not a filing line] | $992,663.4 [DEDUCTED F338] | $868,931.7 [DEDUCTED F352] |
| Space | FY2028E launch plus Starship commercial revenue | $12,084.5 [DEDUCTED F340] | 12× revenue [VIEW; as_of 2026-08-30; not a filing line] | $145,013.8 [DEDUCTED F341] | $126,938.4 [DEDUCTED F353] |
| AI core | Cumulative FY2026E–FY2028E AI capex | $96,551.0 [DEDUCTED F329] | 2× capital, then 20% Customer B haircut [VIEW; as_of 2026-08-30; not a filing line] | $154,481.6 [DEDUCTED F343] | $135,226.1 [DEDUCTED F354] |
| Cursor | FY2028E Cursor EBIT | $750.0 [DEDUCTED F344] | 40× EBIT [VIEW; as_of 2026-08-30; not a filing line] | $30,000.0 [DEDUCTED F345] | $26,260.6 [DEDUCTED F355] |
| **Enterprise value** | Sum of pieces |  |  | $1,322,158.8 [DEDUCTED F346] | $1,157,356.8 [DEDUCTED F348] |
| Net cash | Target-date base cash bridge |  |  |  | $29,213.6 [DEDUCTED F328] |
| **Equity value** | Target EV + net cash |  |  |  | $1,186,570.4 [DEDUCTED F349] |
| **Price target** | Equity value ÷ basic shares | 13,834.6 [DEDUCTED F313] |  |  | $85.8 [DEDUCTED F350] |

Target net cash uses FY2026E ending liquidity less debt and eight months of FY2027E FCF, with no new financing. The pending EchoStar cash and share consideration is included. Cursor P&L is included; synergy premium is zero.

## Bear / base / bull assumptions

| scenario | driver | assumption | treatment |
| --- | --- | --- | --- |
| Bear | Connectivity subscribers / ARPU | 17.0m → 20.0m / $54.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` explicit subscriber and ARPU paths |
| Bear | Enterprise & Government factor | 85.0% of base [VIEW; as_of 2026-08-30; not a filing line] | Starshield remains embedded; standalone P&L not obtained |
| Bear | Connectivity exit EBIT multiple | 40.0× [VIEW; as_of 2026-08-30; not a filing line] | Selected SOTP input; primary-source peer multiple not obtained |
| Bear | Space multiple / Starship flights / $ per flight | 8.0× / 10.0 / $120.0 [VIEW; as_of 2026-08-30; not a filing line] | Non-zero Starship commercial view; list price not obtained |
| Bear | AI capital conversion / Customer B haircut | 0.75× / 40.0% [VIEW; as_of 2026-08-30; not a filing line] | AI capex conversion with explicit concentration haircut |
| Bear | Cursor revenue / EBIT margin / exit EBIT multiple | $2,000.0 / -10.0% / 20.0× [VIEW; as_of 2026-08-30; not a filing line] | Cursor P&L and value view; no synergy premium |
| Bear | WACC / years to FY2028 | 13.5% / 1.3 [VIEW; as_of 2026-08-30; not a filing line] | Discount FY2028 segment values to the 12-month target date |
| Base | Connectivity subscribers / ARPU | 18.0m → 22.5m / $59.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` explicit subscriber and ARPU paths |
| Base | Enterprise & Government factor | 100.0% of base [VIEW; as_of 2026-08-30; not a filing line] | Starshield remains embedded; standalone P&L not obtained |
| Base | Connectivity exit EBIT multiple | 70.0× [VIEW; as_of 2026-08-30; not a filing line] | Selected SOTP input; primary-source peer multiple not obtained |
| Base | Space multiple / Starship flights / $ per flight | 12.0× / 50.0 / $140.0 [VIEW; as_of 2026-08-30; not a filing line] | Non-zero Starship commercial view; list price not obtained |
| Base | AI capital conversion / Customer B haircut | 2.0× / 20.0% [VIEW; as_of 2026-08-30; not a filing line] | AI capex conversion with explicit concentration haircut |
| Base | Cursor revenue / EBIT margin / exit EBIT multiple | $5,000.0 / 15.0% / 40.0× [VIEW; as_of 2026-08-30; not a filing line] | Cursor P&L and value view; no synergy premium |
| Base | WACC / years to FY2028 | 10.5% / 1.3 [VIEW; as_of 2026-08-30; not a filing line] | Discount FY2028 segment values to the 12-month target date |
| Bull | Connectivity subscribers / ARPU | 19.0m → 25.0m / $65.0 [VIEW; as_of 2026-08-30; not a filing line] | `research.md` explicit subscriber and ARPU paths |
| Bull | Enterprise & Government factor | 115.0% of base [VIEW; as_of 2026-08-30; not a filing line] | Starshield remains embedded; standalone P&L not obtained |
| Bull | Connectivity exit EBIT multiple | 95.0× [VIEW; as_of 2026-08-30; not a filing line] | Selected SOTP input; primary-source peer multiple not obtained |
| Bull | Space multiple / Starship flights / $ per flight | 20.0× / 100.0 / $160.0 [VIEW; as_of 2026-08-30; not a filing line] | Non-zero Starship commercial view; list price not obtained |
| Bull | AI capital conversion / Customer B haircut | 7.0× / 5.0% [VIEW; as_of 2026-08-30; not a filing line] | AI capex conversion with explicit concentration haircut |
| Bull | Cursor revenue / EBIT margin / exit EBIT multiple | $8,000.0 / 25.0% / 60.0× [VIEW; as_of 2026-08-30; not a filing line] | Cursor P&L and value view; no synergy premium |
| Bull | WACC / years to FY2028 | 9.0% / 1.3 [VIEW; as_of 2026-08-30; not a filing line] | Discount FY2028 segment values to the 12-month target date |

Starship commercial revenue is non-zero in every scenario. Bull and bear change Starship cadence/yield, Cursor revenue/margin, Connectivity ARPU/net adds, Enterprise & Government realization, AI capex conversion, Customer B concentration haircut, exit multiples and WACC.

## Scenario outputs

| scenario | FY2028 Consumer revenue | FY2028 Connectivity EBIT | Starship revenue | Cursor EBIT | target EV | target equity | price / share | vs last sale |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bear | $11,988.0 [DEDUCTED F381] | $11,755.0 [DEDUCTED F385] | $1,200.0 [DEDUCTED F387] | $(200.0) [DEDUCTED F392] | $476,313.6 [DEDUCTED F396] | $505,527.2 [DEDUCTED F397] | $36.5 [DEDUCTED F398] | -74.2% [DEDUCTED F399] |
| Base | $14,337.0 [DEDUCTED F333] | $14,180.9 [DEDUCTED F337] | $7,000.0 [DEDUCTED F339] | $750.0 [DEDUCTED F344] | $1,157,356.8 [DEDUCTED F348] | $1,186,570.4 [DEDUCTED F349] | $85.8 [DEDUCTED F350] | -39.4% [DEDUCTED F351] |
| Bull | $17,160.0 [DEDUCTED F357] | $16,867.5 [DEDUCTED F361] | $16,000.0 [DEDUCTED F363] | $2,000.0 [DEDUCTED F368] | $2,483,733.8 [DEDUCTED F372] | $2,512,947.4 [DEDUCTED F373] | $181.6 [DEDUCTED F374] | 28.4% [DEDUCTED F375] |

## Dilution sensitivity — not known fully diluted shares

| item | value | treatment |
| --- | ---: | --- |
| Basic shares | 13,834.6 million [DEDUCTED F313] | Base denominator includes pending EchoStar shares |
| Potentially dilutive awards | 564.0 million [FACT] | Sensitivity only; treasury-stock-method dilution not obtained |
| Sensitivity shares | 14,398.6 [DEDUCTED F404] million | Basic plus all potentially dilutive awards |
| Sensitivity price / share | $82.4 [DEDUCTED F405] | Same base equity value |
| Price haircut | 3.9% [DEDUCTED F406] | Sensitivity price versus base |

The sensitivity does not assert that the awards are fully dilutive.

## What the last sale already prices

| measure | value | basis |
| --- | ---: | --- |
| Last sale | $141.50 [FACT] | Nasdaq `lastTradeTimestamp` 2026-08-27 |
| Current market capitalization | $1,920,554.3 [FACT] | `register.md` What is already priced |
| Current mixed-date enterprise value | $1,859,909.3 [DEDUCTED F327] | Market cap plus debt less cash and securities |
| Base target implied enterprise value | $1,157,356.8 [DEDUCTED F348] | Discounted SOTP pieces |
| Current EV / FY2028E revenue | 30.9× [DEDUCTED F409] | Current EV ÷ model revenue |
| Base target EV / FY2028E revenue | 19.2× [DEDUCTED F407] | Target EV ÷ model revenue |
| Current EV / FY2028E EBIT | 105.0× [DEDUCTED F410] | Current EV ÷ model EBIT |
| Base target EV / FY2028E EBIT | 65.3× [DEDUCTED F408] | Target EV ÷ model EBIT |
| Current EV premium to base target EV | 60.7% [DEDUCTED F411] | Same FY2028 model denominator |

## Consolidated DCF check — not load-bearing

Explicit model FCF is negative through FY2027E and turns positive in FY2028E. The extension makes the terminal auditable by fading consolidated revenue growth and FCF margins explicitly.

| period | revenue | fade assumption | FCF | PV FCF |
| --- | ---: | --- | ---: | ---: |
| FY2028E | $60,223.3 [DEDUCTED F167] | model | $2,330.1 [DEDUCTED F288] | $2,039.6 [DEDUCTED F413] |
| FY2029E | $72,267.9 [DEDUCTED F414] | 20.0% revenue growth / 8.0% FCF margin [VIEW; as_of 2026-08-30; not a filing line] | $5,781.4 [DEDUCTED F415] | $4,579.9 [DEDUCTED F417] |
| FY2030E | $83,830.8 [DEDUCTED F418] | 16.0% revenue growth / 16.0% FCF margin [VIEW; as_of 2026-08-30; not a filing line] | $13,412.9 [DEDUCTED F419] | $9,615.7 [DEDUCTED F421] |
| FY2031E | $93,890.5 [DEDUCTED F422] | 12.0% revenue growth / 23.0% FCF margin [VIEW; as_of 2026-08-30; not a filing line] | $21,594.8 [DEDUCTED F423] | $14,010.3 [DEDUCTED F425] |
| FY2032E | $102,340.7 [DEDUCTED F426] | 9.0% revenue growth / 28.0% FCF margin [VIEW; as_of 2026-08-30; not a filing line] | $28,655.4 [DEDUCTED F427] | $16,824.4 [DEDUCTED F429] |
| FY2033E | $108,481.1 [DEDUCTED F430] | 6.0% revenue growth / 31.0% FCF margin [VIEW; as_of 2026-08-30; not a filing line] | $33,629.1 [DEDUCTED F431] | $17,868.5 [DEDUCTED F433] |

| item | value | basis |
| --- | ---: | --- |
| WACC | 10.5% [VIEW; as_of 2026-08-30; not a filing line] | Named discount-rate input |
| Terminal growth | 3.5% [VIEW; as_of 2026-08-30; not a filing line] | Perpetuity-growth input |
| Exit FCF multiple | 25.0× [VIEW; as_of 2026-08-30; not a filing line] | Alternative terminal-value check |
| Perpetuity DCF enterprise value | $329,137.0 [DEDUCTED F437] | Extended explicit fade plus terminal value |
| Perpetuity DCF value / share | $25.9 [DEDUCTED F439] | Basic shares |
| PV terminal value / DCF EV | 80.3% [DEDUCTED F440] | Shows terminal dependence |
| Exit-multiple DCF enterprise value | $511,650.9 [DEDUCTED F443] | 25× FY2033E FCF terminal |
| Exit-multiple DCF value / share | $39.1 [DEDUCTED F445] | Basic shares |

## Comps check

| peer set | primary-source trading multiple | treatment |
| --- | --- | --- |
| Listed launch providers | **not obtained** | No filing/exchange-derived comparable EV multiple obtained |
| Satellite connectivity providers | **not obtained** | No filing/exchange-derived comparable EV multiple obtained |
| AI infrastructure / platform providers | **not obtained** | No filing/exchange-derived comparable EV multiple obtained |

No peer EV/EBITDA multiple is invented. Current and target implied multiples are shown in “What the last sale already prices.”

## Exclusions and gaps

- EchoStar consideration and shares are pending `[VIEW; as_of 2026-08-30; not a filing line]` base inputs; final closing mechanics remain **not obtained**.
- Cursor P&L is a forecast view inside AI; synergy premium is zero and filing revenue/margins remain **not obtained**.
- Starshield standalone P&L, launch list price, GPU-hours and utilization remain **not obtained**.
- Fully diluted shares remain **not obtained**; the award count is only a sensitivity.

## Valuation formula register

Every `[DEDUCTED]` cell above points to one of these formulas.

| id | output | expression | named inputs | result |
| --- | --- | --- | --- | --- |
| F327 | `valuation.current_enterprise_value` | current_market_cap + debt_and_finance_leases - cash - marketable_securities | current_market_cap=1920554.3; debt_and_finance_leases=39364; cash=93522; marketable_securities=6487 | 1,859,909.3 |
| F328 | `valuation.target_net_cash` | FY2026_ending_liquidity - debt + FY2027_FCF × months_to_target ÷ twelve_months | FY2026_ending_liquidity=77318.22; debt=39364; FY2027_FCF=(-13110.939372); months_to_target=8; twelve_months=12 | 29,213.6 |
| F329 | `valuation.ai_invested_capital` | FY2026E_AI_capex + FY2027E_AI_capex + FY2028E_AI_capex | FY2026E_AI_capex=41551; FY2027E_AI_capex=30000; FY2028E_AI_capex=25000 | 96,551.0 |
| F330 | `valuation.base_enterprise_and_spectrum_revenue` | Enterprise_and_Government + pending_spectrum_mobile_overlay | Enterprise_and_Government=10099.375; pending_spectrum_mobile_overlay=2500 | 12,599.4 |
| F331 | `valuation.base_space_core_revenue` | Launch_Services + Launch_and_Development | Launch_Services=3450; Launch_and_Development=1634.4832 | 5,084.5 |
| F332 | `valuation.base.average_subscribers` | (opening_subscribers + ending_subscribers) ÷ two | opening_subscribers_m=18; ending_subscribers_m=22.5; two=2 | 20.3 |
| F333 | `valuation.base.consumer_revenue` | average_subscribers × ARPU × twelve_months | average_subscribers_m=20.25; ARPU=59; twelve_months=12 | 14,337.0 |
| F334 | `valuation.base.enterprise_revenue` | base_enterprise_revenue × scenario_factor | base_enterprise_revenue=12599.375; scenario_factor=1 | 12,599.4 |
| F335 | `valuation.base.consumer_ebit_change` | (scenario_consumer_revenue - base_consumer_revenue) × incremental_margin | scenario_consumer_revenue=14337; base_consumer_revenue=14337; incremental_margin=0.55 | 0.0 |
| F336 | `valuation.base.enterprise_ebit_change` | (scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin | scenario_enterprise_revenue=12599.375; base_enterprise_revenue=12599.375; incremental_margin=0.6 | 0.0 |
| F337 | `valuation.base.connectivity_ebit` | base_connectivity_EBIT + consumer_EBIT_change + enterprise_EBIT_change | base_connectivity_EBIT=14180.90625; consumer_EBIT_change=0; enterprise_EBIT_change=0 | 14,180.9 |
| F338 | `valuation.base.connectivity_value_FY2028` | scenario_connectivity_EBIT × connectivity_exit_EBIT_multiple | scenario_connectivity_EBIT=14180.90625; connectivity_exit_EBIT_multiple=70 | 992,663.4 |
| F339 | `valuation.base.starship_commercial_revenue` | commercial_Starship_flights × assumed_revenue_per_flight | commercial_Starship_flights=50; assumed_revenue_per_flight=140 | 7,000.0 |
| F340 | `valuation.base.space_revenue` | modeled_launch_revenue + Starship_commercial_revenue | modeled_launch_revenue=5084.4832; Starship_commercial_revenue=7000 | 12,084.5 |
| F341 | `valuation.base.space_value_FY2028` | space_revenue × space_exit_revenue_multiple | space_revenue=12084.4832; space_exit_revenue_multiple=12 | 145,013.8 |
| F342 | `valuation.base.ai_gross_value_FY2028` | AI_invested_capital × AI_capital_conversion_multiple | AI_invested_capital=96551; AI_capital_conversion_multiple=2 | 193,102.0 |
| F343 | `valuation.base.ai_value_FY2028` | AI_gross_value × (one - Customer_B_haircut) | AI_gross_value=193102; Customer_B_haircut=0.2 | 154,481.6 |
| F344 | `valuation.base.cursor_EBIT` | Cursor_revenue × Cursor_EBIT_margin | Cursor_revenue=5000; Cursor_EBIT_margin=0.15 | 750.0 |
| F345 | `valuation.base.cursor_value_FY2028` | positive_Cursor_EBIT × Cursor_exit_EBIT_multiple | positive_Cursor_EBIT=750; Cursor_exit_EBIT_multiple=40 | 30,000.0 |
| F346 | `valuation.base.end_FY2028_enterprise_value` | Connectivity + Space + AI_core + Cursor | Connectivity=992663.4375; Space=145013.7984; AI_core=154481.6; Cursor=30000 | 1,322,158.8 |
| F347 | `valuation.base.discount_factor` | one_plus_WACC ^ years_from_target_to_FY2028 | one_plus_WACC=1.105; years_from_target_to_FY2028=1.3333333333 | 1.1 |
| F348 | `valuation.base.target_enterprise_value` | end_FY2028_enterprise_value ÷ discount_factor | end_FY2028_enterprise_value=1322158.8359; discount_factor=1.142395202714266041915937358 | 1,157,356.8 |
| F349 | `valuation.base.target_equity_value` | target_enterprise_value + target_net_cash | target_enterprise_value=1157356.782275193197143463203; target_net_cash=29213.593752 | 1,186,570.4 |
| F350 | `valuation.base.price_target` | target_equity_value ÷ basic_shares_m | target_equity_value=1186570.376027193197143463203; basic_shares_m=13834.621625 | 85.8 |
| F351 | `valuation.base.implied_change` | price_target ÷ last_sale - one | price_target=85.76818421134038041632838679; last_sale=141.5; one=1 | (0.4) |
| F352 | `valuation.base.pv_connectivity` | FY2028_connectivity_value ÷ discount_factor | FY2028_connectivity_value=992663.4375; discount_factor=1.142395202714266041915937358 | 868,931.7 |
| F353 | `valuation.base.pv_space` | FY2028_space_value ÷ discount_factor | FY2028_space_value=145013.7984; discount_factor=1.142395202714266041915937358 | 126,938.4 |
| F354 | `valuation.base.pv_ai` | FY2028_AI_value ÷ discount_factor | FY2028_AI_value=154481.6; discount_factor=1.142395202714266041915937358 | 135,226.1 |
| F355 | `valuation.base.pv_cursor` | FY2028_Cursor_value ÷ discount_factor | FY2028_Cursor_value=30000; discount_factor=1.142395202714266041915937358 | 26,260.6 |
| F356 | `valuation.bull.average_subscribers` | (opening_subscribers + ending_subscribers) ÷ two | opening_subscribers_m=19; ending_subscribers_m=25; two=2 | 22.0 |
| F357 | `valuation.bull.consumer_revenue` | average_subscribers × ARPU × twelve_months | average_subscribers_m=22; ARPU=65; twelve_months=12 | 17,160.0 |
| F358 | `valuation.bull.enterprise_revenue` | base_enterprise_revenue × scenario_factor | base_enterprise_revenue=12599.375; scenario_factor=1.15 | 14,489.3 |
| F359 | `valuation.bull.consumer_ebit_change` | (scenario_consumer_revenue - base_consumer_revenue) × incremental_margin | scenario_consumer_revenue=17160; base_consumer_revenue=14337; incremental_margin=0.55 | 1,552.7 |
| F360 | `valuation.bull.enterprise_ebit_change` | (scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin | scenario_enterprise_revenue=14489.28125; base_enterprise_revenue=12599.375; incremental_margin=0.6 | 1,133.9 |
| F361 | `valuation.bull.connectivity_ebit` | base_connectivity_EBIT + consumer_EBIT_change + enterprise_EBIT_change | base_connectivity_EBIT=14180.90625; consumer_EBIT_change=1552.65; enterprise_EBIT_change=1133.94375 | 16,867.5 |
| F362 | `valuation.bull.connectivity_value_FY2028` | scenario_connectivity_EBIT × connectivity_exit_EBIT_multiple | scenario_connectivity_EBIT=16867.5; connectivity_exit_EBIT_multiple=95 | 1,602,412.5 |
| F363 | `valuation.bull.starship_commercial_revenue` | commercial_Starship_flights × assumed_revenue_per_flight | commercial_Starship_flights=100; assumed_revenue_per_flight=160 | 16,000.0 |
| F364 | `valuation.bull.space_revenue` | modeled_launch_revenue + Starship_commercial_revenue | modeled_launch_revenue=5084.4832; Starship_commercial_revenue=16000 | 21,084.5 |
| F365 | `valuation.bull.space_value_FY2028` | space_revenue × space_exit_revenue_multiple | space_revenue=21084.4832; space_exit_revenue_multiple=20 | 421,689.7 |
| F366 | `valuation.bull.ai_gross_value_FY2028` | AI_invested_capital × AI_capital_conversion_multiple | AI_invested_capital=96551; AI_capital_conversion_multiple=7 | 675,857.0 |
| F367 | `valuation.bull.ai_value_FY2028` | AI_gross_value × (one - Customer_B_haircut) | AI_gross_value=675857; Customer_B_haircut=0.05 | 642,064.2 |
| F368 | `valuation.bull.cursor_EBIT` | Cursor_revenue × Cursor_EBIT_margin | Cursor_revenue=8000; Cursor_EBIT_margin=0.25 | 2,000.0 |
| F369 | `valuation.bull.cursor_value_FY2028` | positive_Cursor_EBIT × Cursor_exit_EBIT_multiple | positive_Cursor_EBIT=2000; Cursor_exit_EBIT_multiple=60 | 120,000.0 |
| F370 | `valuation.bull.end_FY2028_enterprise_value` | Connectivity + Space + AI_core + Cursor | Connectivity=1602412.5; Space=421689.664; AI_core=642064.15; Cursor=120000 | 2,786,166.3 |
| F371 | `valuation.bull.discount_factor` | one_plus_WACC ^ years_from_target_to_FY2028 | one_plus_WACC=1.09; years_from_target_to_FY2028=1.3333333333 | 1.1 |
| F372 | `valuation.bull.target_enterprise_value` | end_FY2028_enterprise_value ÷ discount_factor | end_FY2028_enterprise_value=2786166.314; discount_factor=1.121765288559719670594006561 | 2,483,733.8 |
| F373 | `valuation.bull.target_equity_value` | target_enterprise_value + target_net_cash | target_enterprise_value=2483733.756441396820973307609; target_net_cash=29213.593752 | 2,512,947.4 |
| F374 | `valuation.bull.price_target` | target_equity_value ÷ basic_shares_m | target_equity_value=2512947.350193396820973307609; basic_shares_m=13834.621625 | 181.6 |
| F375 | `valuation.bull.implied_change` | price_target ÷ last_sale - one | price_target=181.6419283670432020921502874; last_sale=141.5; one=1 | 0.3 |
| F376 | `valuation.bull.pv_connectivity` | FY2028_connectivity_value ÷ discount_factor | FY2028_connectivity_value=1602412.5; discount_factor=1.121765288559719670594006561 | 1,428,474.0 |
| F377 | `valuation.bull.pv_space` | FY2028_space_value ÷ discount_factor | FY2028_space_value=421689.664; discount_factor=1.121765288559719670594006561 | 375,916.1 |
| F378 | `valuation.bull.pv_ai` | FY2028_AI_value ÷ discount_factor | FY2028_AI_value=642064.15; discount_factor=1.121765288559719670594006561 | 572,369.4 |
| F379 | `valuation.bull.pv_cursor` | FY2028_Cursor_value ÷ discount_factor | FY2028_Cursor_value=120000; discount_factor=1.121765288559719670594006561 | 106,974.2 |
| F380 | `valuation.bear.average_subscribers` | (opening_subscribers + ending_subscribers) ÷ two | opening_subscribers_m=17; ending_subscribers_m=20; two=2 | 18.5 |
| F381 | `valuation.bear.consumer_revenue` | average_subscribers × ARPU × twelve_months | average_subscribers_m=18.5; ARPU=54; twelve_months=12 | 11,988.0 |
| F382 | `valuation.bear.enterprise_revenue` | base_enterprise_revenue × scenario_factor | base_enterprise_revenue=12599.375; scenario_factor=0.85 | 10,709.5 |
| F383 | `valuation.bear.consumer_ebit_change` | (scenario_consumer_revenue - base_consumer_revenue) × incremental_margin | scenario_consumer_revenue=11988; base_consumer_revenue=14337; incremental_margin=0.55 | (1,292.0) |
| F384 | `valuation.bear.enterprise_ebit_change` | (scenario_enterprise_revenue - base_enterprise_revenue) × incremental_margin | scenario_enterprise_revenue=10709.46875; base_enterprise_revenue=12599.375; incremental_margin=0.6 | (1,133.9) |
| F385 | `valuation.bear.connectivity_ebit` | base_connectivity_EBIT + consumer_EBIT_change + enterprise_EBIT_change | base_connectivity_EBIT=14180.90625; consumer_EBIT_change=(-1291.95); enterprise_EBIT_change=(-1133.94375) | 11,755.0 |
| F386 | `valuation.bear.connectivity_value_FY2028` | scenario_connectivity_EBIT × connectivity_exit_EBIT_multiple | scenario_connectivity_EBIT=11755.0125; connectivity_exit_EBIT_multiple=40 | 470,200.5 |
| F387 | `valuation.bear.starship_commercial_revenue` | commercial_Starship_flights × assumed_revenue_per_flight | commercial_Starship_flights=10; assumed_revenue_per_flight=120 | 1,200.0 |
| F388 | `valuation.bear.space_revenue` | modeled_launch_revenue + Starship_commercial_revenue | modeled_launch_revenue=5084.4832; Starship_commercial_revenue=1200 | 6,284.5 |
| F389 | `valuation.bear.space_value_FY2028` | space_revenue × space_exit_revenue_multiple | space_revenue=6284.4832; space_exit_revenue_multiple=8 | 50,275.9 |
| F390 | `valuation.bear.ai_gross_value_FY2028` | AI_invested_capital × AI_capital_conversion_multiple | AI_invested_capital=96551; AI_capital_conversion_multiple=0.75 | 72,413.3 |
| F391 | `valuation.bear.ai_value_FY2028` | AI_gross_value × (one - Customer_B_haircut) | AI_gross_value=72413.25; Customer_B_haircut=0.4 | 43,448.0 |
| F392 | `valuation.bear.cursor_EBIT` | Cursor_revenue × Cursor_EBIT_margin | Cursor_revenue=2000; Cursor_EBIT_margin=(-0.1) | (200.0) |
| F393 | `valuation.bear.cursor_value_FY2028` | positive_Cursor_EBIT × Cursor_exit_EBIT_multiple | positive_Cursor_EBIT=0; Cursor_exit_EBIT_multiple=20 | 0.0 |
| F394 | `valuation.bear.end_FY2028_enterprise_value` | Connectivity + Space + AI_core + Cursor | Connectivity=470200.5; Space=50275.8656; AI_core=43447.95; Cursor=0 | 563,924.3 |
| F395 | `valuation.bear.discount_factor` | one_plus_WACC ^ years_from_target_to_FY2028 | one_plus_WACC=1.135; years_from_target_to_FY2028=1.3333333333 | 1.2 |
| F396 | `valuation.bear.target_enterprise_value` | end_FY2028_enterprise_value ÷ discount_factor | end_FY2028_enterprise_value=563924.3156; discount_factor=1.183934879555245110264851961 | 476,313.6 |
| F397 | `valuation.bear.target_equity_value` | target_enterprise_value + target_net_cash | target_enterprise_value=476313.6261445754637073275403; target_net_cash=29213.593752 | 505,527.2 |
| F398 | `valuation.bear.price_target` | target_equity_value ÷ basic_shares_m | target_equity_value=505527.2198965754637073275403; basic_shares_m=13834.621625 | 36.5 |
| F399 | `valuation.bear.implied_change` | price_target ÷ last_sale - one | price_target=36.54073335717813415134348066; last_sale=141.5; one=1 | (0.7) |
| F400 | `valuation.bear.pv_connectivity` | FY2028_connectivity_value ÷ discount_factor | FY2028_connectivity_value=470200.5; discount_factor=1.183934879555245110264851961 | 397,150.6 |
| F401 | `valuation.bear.pv_space` | FY2028_space_value ÷ discount_factor | FY2028_space_value=50275.8656; discount_factor=1.183934879555245110264851961 | 42,465.1 |
| F402 | `valuation.bear.pv_ai` | FY2028_AI_value ÷ discount_factor | FY2028_AI_value=43447.95; discount_factor=1.183934879555245110264851961 | 36,697.9 |
| F403 | `valuation.bear.pv_cursor` | FY2028_Cursor_value ÷ discount_factor | FY2028_Cursor_value=0; discount_factor=1.183934879555245110264851961 | 0.0 |
| F404 | `valuation.dilution_sensitivity_shares` | basic_shares_m + potentially_dilutive_awards_m | basic_shares_m=13834.621625; potentially_dilutive_awards_m=564 | 14,398.6 |
| F405 | `valuation.dilution_sensitivity_price` | base_target_equity_value ÷ basic_plus_potential_awards_m | base_target_equity_value=1186570.376027193197143463203; basic_plus_potential_awards_m=14398.621625 | 82.4 |
| F406 | `valuation.dilution_sensitivity_haircut` | one - sensitivity_price ÷ base_price_target | one=1; sensitivity_price=82.40860874953321770780702788; base_price_target=85.76818421134038041632838679 | 0.0 |
| F407 | `valuation.base.target_EV_to_FY2028_revenue` | target_enterprise_value ÷ FY2028_revenue | target_enterprise_value=1157356.782275193197143463203; FY2028_revenue=60223.2832 | 19.2 |
| F408 | `valuation.base.target_EV_to_FY2028_EBIT` | target_enterprise_value ÷ FY2028_EBIT | target_enterprise_value=1157356.782275193197143463203; FY2028_EBIT=17721.630906 | 65.3 |
| F409 | `valuation.current_EV_to_FY2028_revenue` | current_enterprise_value ÷ FY2028_revenue | current_enterprise_value=1859909.3; FY2028_revenue=60223.2832 | 30.9 |
| F410 | `valuation.current_EV_to_FY2028_EBIT` | current_enterprise_value ÷ FY2028_EBIT | current_enterprise_value=1859909.3; FY2028_EBIT=17721.630906 | 105.0 |
| F411 | `valuation.current_EV_premium_to_base_target_EV` | current_enterprise_value ÷ base_target_enterprise_value - one | current_enterprise_value=1859909.3; base_target_enterprise_value=1157356.782275193197143463203; one=1 | 0.6 |
| F412 | `valuation.dcf.FY2028_discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=1.3333333333 | 1.1 |
| F413 | `valuation.dcf.FY2028_PV_FCF` | FY2028_FCF ÷ discount_factor | FY2028_FCF=2330.0845528; discount_factor=1.142395202714266041915937358 | 2,039.6 |
| F414 | `valuation.dcf.FY2029E.revenue` | prior_revenue × (one + growth) | prior_revenue=60223.2832; one_plus_growth=1.2 | 72,267.9 |
| F415 | `valuation.dcf.FY2029E.FCF` | revenue × FCF_margin | revenue=72267.93984; FCF_margin=0.08 | 5,781.4 |
| F416 | `valuation.dcf.FY2029E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=2.3333333333 | 1.3 |
| F417 | `valuation.dcf.FY2029E.PV_FCF` | FCF ÷ discount_factor | FCF=5781.4351872; discount_factor=1.26234669899926397631711078 | 4,579.9 |
| F418 | `valuation.dcf.FY2030E.revenue` | prior_revenue × (one + growth) | prior_revenue=72267.93984; one_plus_growth=1.16 | 83,830.8 |
| F419 | `valuation.dcf.FY2030E.FCF` | revenue × FCF_margin | revenue=83830.8102144; FCF_margin=0.16 | 13,412.9 |
| F420 | `valuation.dcf.FY2030E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=3.3333333333 | 1.4 |
| F421 | `valuation.dcf.FY2030E.PV_FCF` | FCF ÷ discount_factor | FCF=13412.929634304; discount_factor=1.394893102394186693830407412 | 9,615.7 |
| F422 | `valuation.dcf.FY2031E.revenue` | prior_revenue × (one + growth) | prior_revenue=83830.8102144; one_plus_growth=1.12 | 93,890.5 |
| F423 | `valuation.dcf.FY2031E.FCF` | revenue × FCF_margin | revenue=93890.507440128; FCF_margin=0.23 | 21,594.8 |
| F424 | `valuation.dcf.FY2031E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=4.3333333333 | 1.5 |
| F425 | `valuation.dcf.FY2031E.PV_FCF` | FCF ÷ discount_factor | FCF=21594.81671122944; discount_factor=1.54135687814557629668260019 | 14,010.3 |
| F426 | `valuation.dcf.FY2032E.revenue` | prior_revenue × (one + growth) | prior_revenue=93890.507440128; one_plus_growth=1.09 | 102,340.7 |
| F427 | `valuation.dcf.FY2032E.FCF` | revenue × FCF_margin | revenue=102340.65310973952; FCF_margin=0.28 | 28,655.4 |
| F428 | `valuation.dcf.FY2032E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=5.3333333333 | 1.7 |
| F429 | `valuation.dcf.FY2032E.PV_FCF` | FCF ÷ discount_factor | FCF=28655.3828707270656; discount_factor=1.70319935035086180783427321 | 16,824.4 |
| F430 | `valuation.dcf.FY2033E.revenue` | prior_revenue × (one + growth) | prior_revenue=102340.65310973952; one_plus_growth=1.06 | 108,481.1 |
| F431 | `valuation.dcf.FY2033E.FCF` | revenue × FCF_margin | revenue=108481.0922963238912; FCF_margin=0.31 | 33,629.1 |
| F432 | `valuation.dcf.FY2033E.discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=6.3333333333 | 1.9 |
| F433 | `valuation.dcf.FY2033E.PV_FCF` | FCF ÷ discount_factor | FCF=33629.138611860406272; discount_factor=1.882035282137702297656871897 | 17,868.5 |
| F434 | `valuation.dcf.terminal_value` | FY2033_FCF × (one + terminal_growth) ÷ (WACC - terminal_growth) | FY2033_FCF=33629.138611860406272; terminal_growth=0.035; WACC=0.105 | 497,230.8 |
| F435 | `valuation.dcf.terminal_discount_factor` | one_plus_WACC ^ years | one_plus_WACC=1.105; years=6.3333333333 | 1.9 |
| F436 | `valuation.dcf.PV_terminal_value` | terminal_value ÷ discount_factor | terminal_value=497230.835189650292736; discount_factor=1.882035282137702297656871897 | 264,198.5 |
| F437 | `valuation.dcf.enterprise_value` | PV_FY2028E_FCF + PV_FY2029E_FCF + PV_FY2030E_FCF + PV_FY2031E_FCF + PV_FY2032E_FCF + PV_FY2033E_FCF + PV_terminal_value | PV_FY2028E_FCF=2039.64840474106648694191788; PV_FY2029E_FCF=4579.910726413972998997923514; PV_FY2030E_FCF=9615.74016767458584404993896; PV_FY2031E_FCF=14010.26395471138751938497894; PV_FY2032E_FCF=16824.44445791035007246230798; PV_FY2033E_FCF=17868.49530985565944993896057; PV_terminal_value=264198.466367151536152668917 | 329,137.0 |
| F438 | `valuation.dcf.equity_value` | enterprise_value + target_net_cash | enterprise_value=329136.9693884585585244449448; target_net_cash=29213.593752 | 358,350.6 |
| F439 | `valuation.dcf.price_per_share` | equity_value ÷ basic_shares_m | equity_value=358350.5631404585585244449448; basic_shares_m=13834.621625 | 25.9 |
| F440 | `valuation.dcf.terminal_value_share` | PV_terminal_value ÷ DCF_enterprise_value | PV_terminal_value=264198.466367151536152668917; DCF_enterprise_value=329136.9693884585585244449448 | 0.8 |
| F441 | `valuation.dcf.exit_terminal_value` | FY2033_FCF × exit_FCF_multiple | FY2033_FCF=33629.138611860406272; exit_FCF_multiple=25 | 840,728.5 |
| F442 | `valuation.dcf.PV_exit_terminal_value` | exit_terminal_value ÷ discount_factor | exit_terminal_value=840728.4652965101568; discount_factor=1.882035282137702297656871897 | 446,712.4 |
| F443 | `valuation.dcf.exit_enterprise_value` | PV_FY2028E_FCF + PV_FY2029E_FCF + PV_FY2030E_FCF + PV_FY2031E_FCF + PV_FY2032E_FCF + PV_FY2033E_FCF + PV_exit_terminal_value | PV_FY2028E_FCF=2039.64840474106648694191788; PV_FY2029E_FCF=4579.910726413972998997923514; PV_FY2030E_FCF=9615.74016767458584404993896; PV_FY2031E_FCF=14010.26395471138751938497894; PV_FY2032E_FCF=16824.44445791035007246230798; PV_FY2033E_FCF=17868.49530985565944993896057; PV_exit_terminal_value=446712.3827463914862484740143 | 511,650.9 |
| F444 | `valuation.dcf.exit_equity_value` | enterprise_value + target_net_cash | enterprise_value=511650.8857676985086202500421; target_net_cash=29213.593752 | 540,864.5 |
| F445 | `valuation.dcf.exit_price_per_share` | equity_value ÷ basic_shares_m | equity_value=540864.4795196985086202500421; basic_shares_m=13834.621625 | 39.1 |
