# Meta Platforms initiation research file

GF-META-1 · as of 2026-09-29 · name id `meta`

Read numeric facts in [`register.md`](register.md); this file owns driver structure and interpretation. No fact is intentionally duplicated here.

## 1. Business and reporting architecture

1. **[FACT] Family of Apps.** Facebook, Instagram, Messenger, WhatsApp, and other services comprise FoA. Revenue is disclosed as Advertising and Other; segment operating income is disclosed. See R1–R2.
2. **[FACT] Reality Labs.** RL includes virtual- and augmented-reality hardware, software, and content. Revenue and operating loss are disclosed, but product economics are not. See R1, R2, and R8.
3. **[FACT] Combined-segment income statement.** FoA operating income plus RL operating loss equals company operating income. The model starts with those reportable segments and does not allocate company profit using an invented corporate bucket.

## 2. Segment driver trees

### 2.1 FoA advertising

1. **[DEDUCTED] Revenue bridge:** delivered ad impressions × average price per ad. The filing supplies growth rates, not absolute units or price (R3 and R8.1).
2. **[DEDUCTED] Impression drivers:** DAP growth, time spent and engagement, surfaces eligible for ads, ad load/frequency, product mix, and regional mix.
3. **[DEDUCTED] Price drivers:** advertiser demand, measured return on ad spend, auction competition, targeting and measurement quality, conversion performance, format, geography, vertical mix, and FX.
4. **[FACT] Mix warning:** Asia-Pacific contributes faster impression growth at lower monetization, and Reels monetizes below Feed/Stories in the current disclosure. A volume beat need not produce equal price or margin leverage (R3.2).
5. **[VIEW] Forecast mechanism:** FY2026E–FY2028E advertising growth decelerates while remaining above mature-user growth because AI-assisted recommendation, creative generation, targeting, and measurement support engagement and advertiser returns. The exact assumptions live only in `models/meta/inputs.md`.

### 2.2 FoA Other

1. **[FACT] Revenue pools:** WhatsApp paid messaging, subscriptions including Meta Verified, developer payment fees, and other sources (R1.2).
2. **[DEDUCTED] Paid-messaging bridge:** business conversations × net price per delivered/qualified conversation, adjusted for region, category, free tiers, and partner economics.
3. **[DEDUCTED] Subscription bridge:** paid subscribers × realized ARPU, net of app-store fees, churn, promotions, and regional pricing.
4. **[VIEW] Forecast mechanism:** paid messaging and subscriptions grow faster than advertising but remain a small mix because volumes, ARPU, and product split are not disclosed. The model does not assign unsupported standalone margins.

### 2.3 Reality Labs

1. **[DEDUCTED] Hardware bridge:** AI-glasses units × realized revenue per unit plus Quest and other devices. Unit and ASP data are not obtained (R8.3).
2. **[DEDUCTED] Software/content bridge:** installed devices × attach/spend × Meta's net take. No standalone line is disclosed.
3. **[DEDUCTED] Loss bridge:** employee compensation + inventory and hardware cost + R&D + infrastructure + marketing/facilities − RL revenue.
4. **[VIEW] Forecast mechanism:** revenue scales from glasses, Quest, and ecosystem spend, but operating losses remain near the disclosed FY2026 frame before narrowing in FY2028E. The thesis does not require RL profitability within the forecast.

### 2.4 Corporate cost and AI infrastructure

1. **[DEDUCTED] R&D:** technical headcount and compensation, SBC, model training/inference, silicon, product engineering, safety/integrity, and RL development.
2. **[DEDUCTED] Cost of revenue:** data-center depreciation, servers/network, energy, content/partner costs, payments, and RL hardware cost.
3. **[DEDUCTED] Capex:** servers, accelerators, data centers, networking, land/buildings, and finance leases. The forecast uses the company capex range as a constraint, not a segment allocation.
4. **[VIEW] Operating shape:** AI infrastructure depresses near-term FoA margin and cash conversion before ad monetization and slower capex growth restore operating and free-cash-flow leverage.

## 3. How the segments change

| business | FY2026E–FY2028E model direction | economic mechanism | failure mode |
|---|---|---|---|
| FoA Advertising **[VIEW]** | double-digit growth decelerates | AI recommendation lifts engagement; AI ad tools lift conversion/auction demand; paid impressions and price both contribute | engagement stalls, signal loss, low-quality AI content, weak advertiser ROI, regulation |
| FoA Other **[VIEW]** | grows faster from a small base | more business messaging and paid subscriptions | pricing resistance, app-store economics, low business adoption, spam/integrity |
| Reality Labs **[VIEW]** | revenue grows; losses remain large before narrowing | AI glasses and ecosystem scale against a still-heavy R&D/hardware base | hardware demand, weak attach, component cost, platform delays |
| AI infrastructure **[VIEW]** | capex peaks before cash conversion improves | deployment supports recommendation and ads; D&A follows with a lag | underutilization, power/chip constraints, rapid obsolescence, returns below cost of capital |

## 4. Node map

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| User → FoA **[DEDUCTED]** | attention, content, social graph, and data signals rather than cash | engagement, creator supply, network density, recommendation quality | churn, harmful content, privacy/safety failures, product substitution |
| Advertiser → Meta **[FACT]** | auction-priced ad spend | reach, targeting, measurement, conversion, automated creative and campaign tools | poor ROI, signal restrictions, competition, macro demand, regulation |
| Business → WhatsApp / Meta **[DEDUCTED]** | paid messaging and business tools | high-intent customer interactions and global installed base | spam, low conversion, channel regulation, low willingness to pay |
| Subscriber → Meta **[FACT]** | Meta Verified and other subscription fees | identity/status, support, creator/business tooling | weak value proposition, churn, store commissions |
| Consumer → RL **[FACT]** | glasses/headset and content purchases | device design, AI assistant, operating platform, developer ecosystem | low units/usage, hardware losses, privacy concerns, weak content |
| Meta → chip, power, data-center, cloud, and network suppliers **[DEDUCTED]** | capex, leases, energy, and service fees | scarce accelerators, power, facilities, and deployment speed | shortages, cost inflation, construction delay, stranded capacity |
| Meta → employees / creators / partners **[DEDUCTED]** | compensation, SBC, rev-share, content and distribution costs | model/product talent and content supply | retention costs, dilution, partner dependence |
| Governments / platforms → Meta **[FACT]** | regulation, taxes, distribution and data-access rules | gatekeeping and legal permission to monetize | privacy/competition/youth rules, app-store restrictions, fines, product bans |

**[VIEW] Value concentration.** Reported value sits in FoA advertising operating profit. FoA Other and RL can broaden the revenue base, but the initiation valuation does not need an undisclosed product P&L or near-term RL breakeven.

## 5. What the model must take

| named input | register pointer | status |
|---|---|---|
| Advertising, FoA Other, RL revenue | R2 | obtained |
| FoA and RL operating contribution | R2 | obtained |
| Impressions and price growth | R3.1–R3.2 | growth rates obtained; absolute levels **not obtained** |
| DAP / ARPP / product engagement | R3.3–R3.4 | Family DAP/ARPP and selected product milestones obtained; WhatsApp/Messenger DAU/MAP and Family MAP **not obtained** |
| Functional opex, SBC, D&A | R4 | obtained at company level |
| Capex and expense outlook | R4.3 | obtained at company level |
| OCF, capex, FCF, repurchases | R5 | obtained |
| Cash, investments, debt, shares | R5.1–R5.4 | obtained |
| Geography | R6 | obtained |
| RL cumulative investment | R7.2 | **not obtained** |
| Segment capex/assets/cash flow | R8.4 | **not obtained** |
