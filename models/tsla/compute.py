#!/usr/bin/env python3
"""Tesla segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md and cashflow.md, then prints tie-out checks.
USD millions except per-share data, units, GWh and percentages.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

S1 = "https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm"
S3 = "https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm"
S2023 = "https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm"
REGISTER = "../../memory/tsla/register.md"


# Raw historical inputs. No derived values are typed into these dictionaries.
HIST_SEGMENTS = {
    "FY2023A": {
        "auto_total_revenue": 82_419.0,
        "auto_total_gp": 16_030.0,
        "credits_revenue": 1_790.0,
        "services_revenue": 8_319.0,
        "services_gp": 489.0,
        "energy_revenue": 6_035.0,
        "energy_gp": 1_141.0,
        "deliveries_k": 1_808.581,
        "production_k": 1_845.985,
        "storage_gwh": 14.7,
    },
    "FY2024A": {
        "auto_total_revenue": 77_070.0,
        "auto_total_gp": 14_197.0,
        "credits_revenue": 2_763.0,
        "services_revenue": 10_534.0,
        "services_gp": 613.0,
        "energy_revenue": 10_086.0,
        "energy_gp": 2_640.0,
        "deliveries_k": 1_789.226,
        "production_k": 1_773.443,
        "storage_gwh": 31.4,
    },
    "FY2025A": {
        "auto_total_revenue": 69_526.0,
        "auto_total_gp": 12_361.0,
        "credits_revenue": 1_993.0,
        "services_revenue": 12_530.0,
        "services_gp": 931.0,
        "energy_revenue": 12_771.0,
        "energy_gp": 3_802.0,
        "deliveries_k": 1_636.129,
        "production_k": 1_654.667,
        "storage_gwh": 46.7,
    },
    "1H2026A": {
        "auto_total_revenue": 36_750.0,
        "auto_total_gp": 6_885.0,
        "credits_revenue": 526.0,
        "services_revenue": 8_326.0,
        "services_gp": 994.0,
        "energy_revenue": 5_547.0,
        "energy_gp": 1_592.0,
        "deliveries_k": 838.149,
        "production_k": 860.144,
        "storage_gwh": 22.3,
    },
}

HIST_INCOME = {
    "FY2023A": {
        "rd": 3_969.0,
        "sga": 4_800.0,
        "restructuring": 0.0,
        "interest_income": 1_066.0,
        "interest_expense": 156.0,
        "other_income": 172.0,
        "tax": -5_001.0,
        "net_income": 14_974.0,
        "nci_income": -23.0,
        "common_net_income": 14_997.0,
        "diluted_shares": 3_485.0,
    },
    "FY2024A": {
        "rd": 4_540.0,
        "sga": 5_150.0,
        "restructuring": 684.0,
        "interest_income": 1_569.0,
        "interest_expense": 350.0,
        "other_income": 695.0,
        "tax": 1_837.0,
        "net_income": 7_153.0,
        "nci_income": 62.0,
        "common_net_income": 7_091.0,
        "diluted_shares": 3_498.0,
    },
    "FY2025A": {
        "rd": 6_411.0,
        "sga": 5_834.0,
        "restructuring": 494.0,
        "interest_income": 1_680.0,
        "interest_expense": 338.0,
        "other_income": -419.0,
        "tax": 1_423.0,
        "net_income": 3_855.0,
        "nci_income": 61.0,
        "common_net_income": 3_794.0,
        "diluted_shares": 3_528.0,
    },
    "1H2026A": {
        "rd": 4_317.0,
        "sga": 3_815.0,
        "restructuring": 0.0,
        "interest_income": 856.0,
        "interest_expense": 173.0,
        "other_income": 55.0,
        "tax": 458.0,
        "net_income": 1_619.0,
        "nci_income": 28.0,
        "common_net_income": 1_591.0,
        "diluted_shares": 3_538.0,
    },
}

HIST_BALANCE = {
    "FY2023A": {
        "cash": 16_398.0,
        "short_investments": 12_696.0,
        "ar": 3_508.0,
        "inventory": 13_626.0,
        "lease_vehicles": 5_989.0,
        "ppe": 29_725.0,
        "spacex_investment": 0.0,
        "total_assets": 106_618.0,
        "ap": 14_431.0,
        "debt_current": 2_373.0,
        "debt_long": 2_857.0,
        "total_liabilities": 43_009.0,
        "common_stock": 3.0,
        "apic": 34_892.0,
        "aoci": -143.0,
        "retained_earnings": 27_882.0,
        "stockholders_equity": 62_634.0,
        "other_equity": 975.0,
        "shares_out": 3_185.0,
    },
    "FY2024A": {
        "cash": 16_139.0,
        "short_investments": 20_424.0,
        "ar": 4_418.0,
        "inventory": 12_017.0,
        "lease_vehicles": 5_581.0,
        "ppe": 35_836.0,
        "spacex_investment": 0.0,
        "total_assets": 122_070.0,
        "ap": 12_474.0,
        "debt_current": 2_456.0,
        "debt_long": 5_757.0,
        "total_liabilities": 48_390.0,
        "common_stock": 3.0,
        "apic": 38_371.0,
        "aoci": -670.0,
        "retained_earnings": 35_209.0,
        "stockholders_equity": 72_913.0,
        "other_equity": 767.0,
        "shares_out": 3_216.0,
    },
    "FY2025A": {
        "cash": 16_513.0,
        "short_investments": 27_546.0,
        "ar": 4_576.0,
        "inventory": 12_392.0,
        "lease_vehicles": 4_912.0,
        "ppe": 40_643.0,
        "spacex_investment": 0.0,
        "total_assets": 137_806.0,
        "ap": 13_371.0,
        "debt_current": 1_640.0,
        "debt_long": 6_736.0,
        "total_liabilities": 54_941.0,
        "common_stock": 3.0,
        "apic": 42_770.0,
        "aoci": 361.0,
        "retained_earnings": 39_003.0,
        "stockholders_equity": 82_137.0,
        "other_equity": 728.0,
        "shares_out": 3_751.0,
    },
    "1H2026A": {
        "cash": 15_219.0,
        "short_investments": 28_305.0,
        "ar": 4_087.0,
        "inventory": 13_752.0,
        "lease_vehicles": 4_253.0,
        "ppe": 47_255.0,
        "spacex_investment": 3_007.0,
        "total_assets": 148_524.0,
        "ap": 15_324.0,
        "debt_current": 1_418.0,
        "debt_long": 7_924.0,
        "total_liabilities": 61_005.0,
        "common_stock": 4.0,
        "apic": 45_859.0,
        "aoci": 401.0,
        "retained_earnings": 40_594.0,
        "stockholders_equity": 86_858.0,
        "other_equity": 661.0,
        "shares_out": 3_949.0,
    },
}

HIST_CASHFLOW = {
    "FY2023A": {
        "net_income": 14_974.0,
        "da": 4_667.0,
        "sbc": 1_812.0,
        "ocf": 13_256.0,
        "capex": 8_899.0,
        "net_investing": -15_584.0,
        "net_financing": 2_589.0,
        "fx": 4.0,
        "cash_change_restricted": 265.0,
        "ending_cash_restricted": 17_189.0,
    },
    "FY2024A": {
        "net_income": 7_153.0,
        "da": 5_368.0,
        "sbc": 1_999.0,
        "ocf": 14_923.0,
        "capex": 11_342.0,
        "net_investing": -18_787.0,
        "net_financing": 3_853.0,
        "fx": -141.0,
        "cash_change_restricted": -152.0,
        "ending_cash_restricted": 17_037.0,
    },
    "FY2025A": {
        "net_income": 3_855.0,
        "da": 6_148.0,
        "sbc": 2_825.0,
        "ocf": 14_747.0,
        "capex": 8_527.0,
        "net_investing": -15_478.0,
        "net_financing": 1_139.0,
        "fx": 171.0,
        "cash_change_restricted": 579.0,
        "ending_cash_restricted": 17_616.0,
    },
    "1H2026A": {
        "net_income": 1_619.0,
        "da": 3_209.0,
        "sbc": 2_181.0,
        "ocf": 8_634.0,
        "capex": 8_282.0,
        "net_investing": -10_951.0,
        "net_financing": 1_209.0,
        "fx": -83.0,
        "cash_change_restricted": -1_191.0,
        "ending_cash_restricted": 16_425.0,
    },
}

ASSUMPTIONS = {
    "FY2026E": {
        "deliveries_k": 1_720.0,
        "storage_gwh": 55.0,
        "energy_revenue_per_kwh": 240.0,
        "services_revenue": 16_800.0,
        "credits_revenue": 500.0,
        "auto_margin": 0.165,
        "energy_margin": 0.220,
        "services_margin": 0.130,
        "rd": 9_200.0,
        "sga": 7_800.0,
        "capex": 26_000.0,
        "diluted_shares": 3_620.0,
    },
    "FY2027E": {
        "deliveries_k": 1_850.0,
        "storage_gwh": 70.0,
        "energy_revenue_per_kwh": 230.0,
        "services_revenue": 19_000.0,
        "credits_revenue": 350.0,
        "auto_margin": 0.172,
        "energy_margin": 0.230,
        "services_margin": 0.135,
        "rd": 10_000.0,
        "sga": 8_200.0,
        "capex": 22_000.0,
        "diluted_shares": 3_700.0,
    },
    "FY2028E": {
        "deliveries_k": 2_000.0,
        "storage_gwh": 85.0,
        "energy_revenue_per_kwh": 220.0,
        "services_revenue": 21_500.0,
        "credits_revenue": 200.0,
        "auto_margin": 0.178,
        "energy_margin": 0.240,
        "services_margin": 0.140,
        "rd": 10_600.0,
        "sga": 8_600.0,
        "capex": 18_000.0,
        "diluted_shares": 3_780.0,
    },
}

# Additional [VIEW] assumptions needed to complete the three statements.
SBC_AS_PERCENT_OF_RD_AND_SGA = 0.25
DA_RATE_ON_AVERAGE_PPE = 0.12
INTEREST_INCOME_RATE_ON_BEGINNING_LIQUIDITY = 0.03
INTEREST_EXPENSE_RATE_ON_BEGINNING_DEBT = 0.04
MINIMUM_CASH = 5_000.0
DIVIDENDS = 0.0
BUYBACKS = 0.0
ENDING_LEASE_VEHICLES = 4_253.0
SPACEX_FAIR_VALUE = 3_007.0
SPACEX_CASH_PURCHASE_2026 = 2_002.0
DISCLOSED_INSTALLED_AUTO_CAPACITY_K = 2_375.0

VALUATION_DATE = date(2026, 8, 29)
LAST_PRICE_DATE = date(2026, 8, 28)
LAST_PRICE = 348.75
PT_SHARES = 3_949_547_394
OFFICIAL_EBIT_MULTIPLE = 20.0
THREE_YEAR_EBIT_MULTIPLE = 22.0
BEAR_EBIT_MULTIPLE = 10.0
BULL_EBIT_MULTIPLE = 30.0
DCF_WACC = 0.10
DCF_TERMINAL_GROWTH = 0.025
YAHOO_TSLA_HISTORY = "https://finance.yahoo.com/quote/TSLA/history/"


def fmt(value: Any, decimals: int = 0) -> str:
    if value is None:
        return "not obtained"
    if isinstance(value, str):
        return value
    if abs(value) < 0.0000001:
        return "—"
    rendered = f"{abs(value):,.{decimals}f}"
    return f"({rendered})" if value < 0 else rendered


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    top = "| " + " | ".join(headers) + " |"
    separator = "|" + "|".join("---" for _ in headers) + "|"
    body = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join([top, separator, *body])


def derived_historical_segments() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_SEGMENTS.items():
        auto_revenue = raw["auto_total_revenue"] - raw["credits_revenue"]
        auto_gp = raw["auto_total_gp"] - raw["credits_revenue"]
        output[period] = {
            **raw,
            "auto_revenue": auto_revenue,
            "auto_gp": auto_gp,
            "credits_gp": raw["credits_revenue"],
            "total_revenue": (
                auto_revenue
                + raw["credits_revenue"]
                + raw["energy_revenue"]
                + raw["services_revenue"]
            ),
            "total_gp": (
                auto_gp
                + raw["credits_revenue"]
                + raw["energy_gp"]
                + raw["services_gp"]
            ),
        }
    return output


def build_forecast_segments() -> tuple[dict[str, dict[str, float]], float, float]:
    fy25 = HIST_SEGMENTS["FY2025A"]
    q2_total_auto_revenue = 20_516.0
    q2_deliveries_k = 480.126
    fy25_revenue_per_delivery = fy25["auto_total_revenue"] / fy25["deliveries_k"]
    q2_revenue_per_delivery = q2_total_auto_revenue / q2_deliveries_k
    output: dict[str, dict[str, float]] = {}
    for period, assumption in ASSUMPTIONS.items():
        # This preserves the researcher-specified total auto-ex-services
        # revenue/delivery quotient while displaying credits separately.
        auto_total_revenue = assumption["deliveries_k"] * fy25_revenue_per_delivery
        auto_revenue = auto_total_revenue - assumption["credits_revenue"]
        # Unit conversion:
        # GWh * 1,000,000 kWh/GWh * $/kWh / 1,000,000 $/$m
        # simplifies exactly to GWh * $/kWh = $m.
        energy_revenue = (
            assumption["storage_gwh"]
            * 1_000_000.0
            * assumption["energy_revenue_per_kwh"]
            / 1_000_000.0
        )
        auto_gp = auto_revenue * assumption["auto_margin"]
        credits_gp = assumption["credits_revenue"]
        energy_gp = energy_revenue * assumption["energy_margin"]
        services_gp = assumption["services_revenue"] * assumption["services_margin"]
        output[period] = {
            "deliveries_k": assumption["deliveries_k"],
            "production_k": 0.0,
            "storage_gwh": assumption["storage_gwh"],
            "auto_total_revenue": auto_total_revenue,
            "auto_revenue": auto_revenue,
            "auto_gp": auto_gp,
            "credits_revenue": assumption["credits_revenue"],
            "credits_gp": credits_gp,
            "energy_revenue": energy_revenue,
            "energy_gp": energy_gp,
            "services_revenue": assumption["services_revenue"],
            "services_gp": services_gp,
            "total_revenue": (
                auto_revenue
                + assumption["credits_revenue"]
                + energy_revenue
                + assumption["services_revenue"]
            ),
            "total_gp": auto_gp + credits_gp + energy_gp + services_gp,
        }
    return output, fy25_revenue_per_delivery, q2_revenue_per_delivery


def build_historical_income(
    segments: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        segment = segments[period]
        raw = HIST_INCOME[period]
        total_opex = raw["rd"] + raw["sga"] + raw["restructuring"]
        operating_income = segment["total_gp"] - total_opex
        pretax = (
            operating_income
            + raw["interest_income"]
            - raw["interest_expense"]
            + raw["other_income"]
        )
        output[period] = {
            **raw,
            "total_revenue": segment["total_revenue"],
            "total_gp": segment["total_gp"],
            "total_opex": total_opex,
            "operating_income": operating_income,
            "pretax_income": pretax,
            "diluted_eps": raw["common_net_income"] / raw["diluted_shares"],
        }
    return output


def historical_balance_with_derived() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_BALANCE.items():
        debt = raw["debt_current"] + raw["debt_long"]
        other_assets = (
            raw["total_assets"]
            - raw["cash"]
            - raw["short_investments"]
            - raw["ar"]
            - raw["inventory"]
            - raw["lease_vehicles"]
            - raw["ppe"]
            - raw["spacex_investment"]
        )
        other_liabilities = raw["total_liabilities"] - raw["ap"] - debt
        output[period] = {
            **raw,
            "debt": debt,
            "other_assets": other_assets,
            "other_liabilities": other_liabilities,
            "total_liabilities_and_equity": (
                raw["total_liabilities"]
                + raw["stockholders_equity"]
                + raw["other_equity"]
            ),
        }
    return output


def build_forecast(
    segments: dict[str, dict[str, float]],
) -> tuple[
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
]:
    balances = historical_balance_with_derived()
    income = build_historical_income(segments)

    # Working-capital days use 1H 2026 balances and annualized 1H flows.
    h1_revenue_annualized = segments["1H2026A"]["total_revenue"] * 2.0
    h1_cogs_annualized = (
        segments["1H2026A"]["total_revenue"] - segments["1H2026A"]["total_gp"]
    ) * 2.0
    h1_balance = balances["1H2026A"]
    ar_days = h1_balance["ar"] / h1_revenue_annualized * 365.0
    inventory_days = h1_balance["inventory"] / h1_cogs_annualized * 365.0
    ap_days = h1_balance["ap"] / h1_cogs_annualized * 365.0

    fy25_tax_rate = HIST_INCOME["FY2025A"]["tax"] / (
        HIST_INCOME["FY2025A"]["net_income"] + HIST_INCOME["FY2025A"]["tax"]
    )
    forecast_cashflow: dict[str, dict[str, float]] = {}
    for period in FORECAST_PERIODS:
        segment = segments[period]
        assumption = ASSUMPTIONS[period]
        is_fy26 = period == "FY2026E"
        previous = balances["1H2026A"] if is_fy26 else balances[
            FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]
        ]
        prior_annual = balances["FY2025A"] if is_fy26 else previous
        revenue = segment["total_revenue"]
        cogs = revenue - segment["total_gp"]
        ar = revenue * ar_days / 365.0
        inventory = cogs * inventory_days / 365.0
        ap = cogs * ap_days / 365.0
        rollforward_delta_nwc = (
            (ar + inventory - ap)
            - (previous["ar"] + previous["inventory"] - previous["ap"])
        )
        annual_delta_nwc = (
            (ar + inventory - ap)
            - (
                prior_annual["ar"]
                + prior_annual["inventory"]
                - prior_annual["ap"]
            )
        )
        annual_sbc = (
            assumption["rd"] + assumption["sga"]
        ) * SBC_AS_PERCENT_OF_RD_AND_SGA
        rollforward_sbc = (
            annual_sbc - HIST_CASHFLOW["1H2026A"]["sbc"]
            if is_fy26
            else annual_sbc
        )

        # D&A is based on average PPE. Solving:
        # D&A = rate * (beginning PPE + ending PPE) / 2
        # ending PPE = beginning PPE + capex - D&A
        rollforward_capex = (
            assumption["capex"] - HIST_CASHFLOW["1H2026A"]["capex"]
            if is_fy26
            else assumption["capex"]
        )
        rollforward_da_rate = (
            DA_RATE_ON_AVERAGE_PPE / 2.0 if is_fy26 else DA_RATE_ON_AVERAGE_PPE
        )
        rollforward_da = (
            rollforward_da_rate
            * (previous["ppe"] + rollforward_capex / 2.0)
            / (1.0 + rollforward_da_rate / 2.0)
        )
        annual_da = (
            HIST_CASHFLOW["1H2026A"]["da"] + rollforward_da
            if is_fy26
            else rollforward_da
        )
        ppe = previous["ppe"] + rollforward_capex - rollforward_da
        lease_vehicles = ENDING_LEASE_VEHICLES
        spacex_investment = SPACEX_FAIR_VALUE

        total_opex = assumption["rd"] + assumption["sga"]
        operating_income = segment["total_gp"] - total_opex
        interest_income = (
            HIST_INCOME["1H2026A"]["interest_income"]
            + (
                previous["cash"] + previous["short_investments"]
            )
            * INTEREST_INCOME_RATE_ON_BEGINNING_LIQUIDITY
            / 2.0
            if is_fy26
            else (
                previous["cash"] + previous["short_investments"]
            )
            * INTEREST_INCOME_RATE_ON_BEGINNING_LIQUIDITY
        )
        interest_expense = (
            HIST_INCOME["1H2026A"]["interest_expense"]
            + previous["debt"] * INTEREST_EXPENSE_RATE_ON_BEGINNING_DEBT / 2.0
            if is_fy26
            else previous["debt"] * INTEREST_EXPENSE_RATE_ON_BEGINNING_DEBT
        )
        # FY2026 keeps reported 1H other income and assumes zero in 2H.
        # The SpaceX investment is held at its Q2 fair value thereafter.
        other_income = HIST_INCOME["1H2026A"]["other_income"] if is_fy26 else 0.0
        pretax = operating_income + interest_income - interest_expense + other_income
        tax = max(pretax, 0.0) * fy25_tax_rate
        net_income = pretax - tax
        nci_income = HIST_INCOME["1H2026A"]["nci_income"] if is_fy26 else 0.0
        common_net_income = net_income - nci_income
        income[period] = {
            "total_revenue": segment["total_revenue"],
            "total_gp": segment["total_gp"],
            "rd": assumption["rd"],
            "sga": assumption["sga"],
            "restructuring": 0.0,
            "total_opex": total_opex,
            "operating_income": operating_income,
            "interest_income": interest_income,
            "interest_expense": interest_expense,
            "other_income": other_income,
            "pretax_income": pretax,
            "tax": tax,
            "net_income": net_income,
            "nci_income": nci_income,
            "common_net_income": common_net_income,
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": common_net_income / assumption["diluted_shares"],
        }

        rollforward_net_income = (
            net_income - HIST_INCOME["1H2026A"]["net_income"]
            if is_fy26
            else net_income
        )
        rollforward_common_income = (
            common_net_income - HIST_INCOME["1H2026A"]["common_net_income"]
            if is_fy26
            else common_net_income
        )
        rollforward_ocf = (
            rollforward_net_income
            + rollforward_da
            + rollforward_sbc
            - rollforward_delta_nwc
        )
        rollforward_fcf = rollforward_ocf - rollforward_capex
        pre_funding_cash = (
            previous["cash"]
            + rollforward_fcf
        )
        investment_sale = min(
            max(MINIMUM_CASH - pre_funding_cash, 0.0),
            previous["short_investments"],
        )
        short_investments = previous["short_investments"] - investment_sale
        cash_after_investments = pre_funding_cash + investment_sale
        debt_issuance = max(MINIMUM_CASH - cash_after_investments, 0.0)
        debt = previous["debt"] + debt_issuance
        cash = cash_after_investments + debt_issuance - DIVIDENDS - BUYBACKS

        retained_earnings = (
            previous["retained_earnings"] + rollforward_common_income - DIVIDENDS
        )
        apic = previous["apic"] + rollforward_sbc
        common_stock = previous["common_stock"]
        aoci = previous["aoci"]
        stockholders_equity = common_stock + apic + aoci + retained_earnings
        other_assets = previous["other_assets"]
        other_liabilities = previous["other_liabilities"]
        total_assets = (
            cash
            + short_investments
            + ar
            + inventory
            + lease_vehicles
            + ppe
            + spacex_investment
            + other_assets
        )
        total_liabilities = ap + debt + other_liabilities
        total_liabilities_and_equity = (
            total_liabilities + stockholders_equity + previous["other_equity"]
        )

        balances[period] = {
            "cash": cash,
            "short_investments": short_investments,
            "ar": ar,
            "inventory": inventory,
            "lease_vehicles": lease_vehicles,
            "ppe": ppe,
            "spacex_investment": spacex_investment,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "ap": ap,
            "debt": debt,
            "debt_current": None,
            "debt_long": None,
            "other_liabilities": other_liabilities,
            "total_liabilities": total_liabilities,
            "common_stock": common_stock,
            "apic": apic,
            "aoci": aoci,
            "retained_earnings": retained_earnings,
            "stockholders_equity": stockholders_equity,
            "other_equity": previous["other_equity"],
            "total_liabilities_and_equity": total_liabilities_and_equity,
            "shares_out": None,
            "diluted_shares": assumption["diluted_shares"],
        }
        annual_ocf = (
            HIST_CASHFLOW["1H2026A"]["ocf"] + rollforward_ocf
            if is_fy26
            else rollforward_ocf
        )
        annual_fcf = annual_ocf - assumption["capex"]
        other_operating_adjustments = (
            annual_ocf
            - net_income
            - annual_da
            - annual_sbc
            + annual_delta_nwc
        )
        # Actual H1 post-FCF cash items not separately forecast:
        # net investing ex-capex/SpaceX + financing + FX
        # less the increase in restricted cash.
        h1_restricted_cash_change = (
            (
                HIST_CASHFLOW["1H2026A"]["ending_cash_restricted"]
                - HIST_BALANCE["1H2026A"]["cash"]
            )
            - (
                HIST_CASHFLOW["FY2025A"]["ending_cash_restricted"]
                - HIST_BALANCE["FY2025A"]["cash"]
            )
        )
        h1_other_post_fcf = (
            HIST_CASHFLOW["1H2026A"]["net_investing"]
            + HIST_CASHFLOW["1H2026A"]["capex"]
            + SPACEX_CASH_PURCHASE_2026
            + HIST_CASHFLOW["1H2026A"]["net_financing"]
            + HIST_CASHFLOW["1H2026A"]["fx"]
            - h1_restricted_cash_change
        ) if is_fy26 else 0.0
        forecast_cashflow[period] = {
            "net_income": net_income,
            "da": annual_da,
            "sbc": annual_sbc,
            "delta_nwc": annual_delta_nwc,
            "other_operating_adjustments": other_operating_adjustments,
            "ocf": annual_ocf,
            "capex": assumption["capex"],
            "fcf": annual_fcf,
            "spacex_purchase": (
                SPACEX_CASH_PURCHASE_2026 if is_fy26 else 0.0
            ),
            "other_post_fcf": h1_other_post_fcf,
            "investment_sale": investment_sale,
            "debt_issuance": debt_issuance,
            "dividends": DIVIDENDS,
            "buybacks": BUYBACKS,
            "cash_change": cash - prior_annual["cash"],
            "ending_cash": cash,
        }
    return balances, income, {
        **forecast_cashflow,
        "_working_capital_days": {
            "ar_days": ar_days,
            "inventory_days": inventory_days,
            "ap_days": ap_days,
        },
    }


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tolerance = 0.02
    for period in ALL_PERIODS:
        segment = segments[period]
        revenue_sum = (
            segment["auto_revenue"]
            + segment["credits_revenue"]
            + segment["energy_revenue"]
            + segment["services_revenue"]
        )
        gp_sum = (
            segment["auto_gp"]
            + segment["credits_gp"]
            + segment["energy_gp"]
            + segment["services_gp"]
        )
        checks.append(
            (f"{period}: segment revenue = company revenue", abs(revenue_sum - income[period]["total_revenue"]) < tolerance, revenue_sum - income[period]["total_revenue"])
        )
        checks.append(
            (f"{period}: segment GP = company GP", abs(gp_sum - income[period]["total_gp"]) < tolerance, gp_sum - income[period]["total_gp"])
        )
        if period in FORECAST_PERIODS:
            capacity_headroom = (
                DISCLOSED_INSTALLED_AUTO_CAPACITY_K - segment["deliveries_k"]
            )
            checks.append(
                (
                    f"{period}: deliveries do not exceed disclosed installed capacity",
                    capacity_headroom >= 0.0,
                    capacity_headroom,
                )
            )

    historical_expected = {
        "FY2023A": (96_773.0, 17_660.0, 8_891.0, 14_997.0),
        "FY2024A": (97_690.0, 17_450.0, 7_076.0, 7_091.0),
        "FY2025A": (94_827.0, 17_094.0, 4_355.0, 3_794.0),
        "1H2026A": (50_623.0, 9_471.0, 1_339.0, 1_591.0),
    }
    for period, expected in historical_expected.items():
        actual = (
            income[period]["total_revenue"],
            income[period]["total_gp"],
            income[period]["operating_income"],
            income[period]["common_net_income"],
        )
        difference = max(abs(a - e) for a, e in zip(actual, expected))
        checks.append(
            (f"{period}: historical IS matches filing", difference < tolerance, difference)
        )

    previous = balances["FY2025A"]
    for period in FORECAST_PERIODS:
        balance = balances[period]
        cf = cashflow[period]
        checks.append(
            (
                f"{period}: balance sheet balances",
                abs(balance["total_assets"] - balance["total_liabilities_and_equity"])
                < tolerance,
                balance["total_assets"] - balance["total_liabilities_and_equity"],
            )
        )
        checks.append(
            (
                f"{period}: CF ending cash = BS cash",
                abs(cf["ending_cash"] - balance["cash"]) < tolerance,
                cf["ending_cash"] - balance["cash"],
            )
        )
        cash_bridge = (
            cf["fcf"]
            - cf["spacex_purchase"]
            + cf["other_post_fcf"]
            + cf["investment_sale"]
            + cf["debt_issuance"]
            - cf["dividends"]
            - cf["buybacks"]
        )
        checks.append(
            (
                f"{period}: cash-flow bridge = change in cash",
                abs(cash_bridge - cf["cash_change"]) < tolerance,
                cash_bridge - cf["cash_change"],
            )
        )
        expected_re = previous["retained_earnings"] + income[period]["common_net_income"]
        checks.append(
            (
                f"{period}: IS NI flows to retained earnings",
                abs(expected_re - balance["retained_earnings"]) < tolerance,
                expected_re - balance["retained_earnings"],
            )
        )
        checks.append(
            (
                f"{period}: forecast NI formula consistent",
                abs(cf["net_income"] - income[period]["net_income"]) < tolerance,
                cf["net_income"] - income[period]["net_income"],
            )
        )
        previous = balance
    return checks


def render_segments(
    segments: dict[str, dict[str, float]],
    fy25_quotient: float,
    q2_quotient: float,
    checks: list[tuple[str, bool, float]],
) -> str:
    rows: list[list[str]] = []
    segment_rows = [
        ("Automotive vehicles + leasing revenue", "auto_revenue"),
        ("Automotive vehicles + leasing gross profit", "auto_gp"),
        ("Regulatory-credit revenue", "credits_revenue"),
        ("Regulatory-credit gross profit", "credits_gp"),
        ("Energy revenue", "energy_revenue"),
        ("Energy gross profit", "energy_gp"),
        ("Services and other revenue", "services_revenue"),
        ("Services and other gross profit", "services_gp"),
        ("Company revenue", "total_revenue"),
        ("Company gross profit", "total_gp"),
    ]
    for label, key in segment_rows:
        rows.append([label] + [fmt(segments[p][key]) for p in ALL_PERIODS])

    driver_rows = []
    for period in ALL_PERIODS:
        segment = segments[period]
        assumption = ASSUMPTIONS.get(period)
        driver_rows.append(
            [
                period,
                fmt(segment["production_k"], 1)
                if period in HIST_PERIODS
                else "not obtained",
                fmt(segment["deliveries_k"], 1),
                fmt(segment["storage_gwh"], 1),
                fmt(assumption["energy_revenue_per_kwh"], 0)
                if assumption
                else "not obtained",
                pct(assumption["auto_margin"]) if assumption else "actual",
                pct(assumption["energy_margin"]) if assumption else "actual",
                pct(assumption["services_margin"]) if assumption else "actual",
            ]
        )

    relevant_checks = [
        row
        for row in checks
        if "segment revenue" in row[0]
        or "segment GP" in row[0]
        or "installed capacity" in row[0]
    ]
    check_rows = [
        [name, "PASS" if passed else "FAIL", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    implied_h2_deliveries = (
        ASSUMPTIONS["FY2026E"]["deliveries_k"]
        - HIST_SEGMENTS["1H2026A"]["deliveries_k"]
    )
    return f"""# Tesla segment model

Generated by `compute.py`; do not hand-edit. USD millions except units, GWh, $/kWh and percentages.

## Revenue and gross profit

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical source: [register R2/R3]({REGISTER}) and [S1]({S1}) / [S3]({S3}). Credits are shown separately and treated as 100% gross profit because their cost is `not obtained`.

## Operating drivers

{markdown_table(["period", "production (k)", "deliveries (k)", "storage (GWh)", "Energy revenue ($/kWh)", "Auto GM", "Energy GM", "Services GM"], driver_rows)}

`[DEDUCTED]` FY2025 total auto-ex-services revenue per delivery used by every forecast year:
`69,526 / 1,636.129k = {fy25_quotient:.6f} $m per 1k deliveries`, equivalent to `${fy25_quotient:.3f}k per delivery`.

Q2 2026 cross-check: `20,516 / 480.126k = {q2_quotient:.6f} $m per 1k deliveries`, equivalent to `${q2_quotient:.3f}k per delivery`. These are working revenue quotients, not ASPs. Forecast Automotive vehicles + leasing revenue equals deliveries times the FY2025 quotient less separately modeled credits.

FY2026 deliveries imply `1,720.0k − 838.149k = {implied_h2_deliveries:.3f}k` in 2H 2026. Forecast deliveries remain below the disclosed aggregate installed annual automotive capacity floor of `{DISCLOSED_INSTALLED_AUTO_CAPACITY_K:,.0f}k`; this is a capacity ceiling check, not a production forecast.

Energy unit conversion is dimensionally:
`$m = GWh × 1,000,000 kWh/GWh × $/kWh ÷ 1,000,000 $/$m = GWh × $/kWh`.
Multiplying the final simplified expression by another 1,000 would overstate revenue 1,000-fold.

Robotaxi, incremental FSD and Optimus commercial revenue are zero in the base forecast because standalone economics are `not obtained` (R8.3).

## Segment tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = []
    line_items = [
        ("Revenue: Automotive vehicles + leasing", "auto_revenue"),
        ("Revenue: Regulatory credits", "credits_revenue"),
        ("Revenue: Energy", "energy_revenue"),
        ("Revenue: Services and other", "services_revenue"),
        ("Total revenue", "total_revenue"),
        ("Gross profit: Automotive vehicles + leasing", "auto_gp"),
        ("Gross profit: Regulatory credits", "credits_gp"),
        ("Gross profit: Energy", "energy_gp"),
        ("Gross profit: Services and other", "services_gp"),
        ("Total gross profit", "total_gp"),
    ]
    for label, key in line_items:
        if key in {"auto_revenue", "credits_revenue", "energy_revenue", "services_revenue", "auto_gp", "credits_gp", "energy_gp", "services_gp"}:
            continue
        rows.append([label] + [fmt(income[p][key]) for p in ALL_PERIODS])

    detailed_rows = [
        ["Total revenue"] + [fmt(income[p]["total_revenue"]) for p in ALL_PERIODS],
        ["Total gross profit"] + [fmt(income[p]["total_gp"]) for p in ALL_PERIODS],
        ["R&D"] + [fmt(income[p]["rd"]) for p in ALL_PERIODS],
        ["SG&A"] + [fmt(income[p]["sga"]) for p in ALL_PERIODS],
        ["Restructuring and other"]
        + [fmt(income[p]["restructuring"]) for p in ALL_PERIODS],
        ["Total operating expense"]
        + [fmt(income[p]["total_opex"]) for p in ALL_PERIODS],
        ["Operating income"]
        + [fmt(income[p]["operating_income"]) for p in ALL_PERIODS],
        ["Interest income"]
        + [fmt(income[p]["interest_income"]) for p in ALL_PERIODS],
        ["Interest expense"]
        + [fmt(-income[p]["interest_expense"]) for p in ALL_PERIODS],
        ["Other income / (expense)"]
        + [fmt(income[p]["other_income"]) for p in ALL_PERIODS],
        ["Pre-tax income"] + [fmt(income[p]["pretax_income"]) for p in ALL_PERIODS],
        ["Tax provision / (benefit)"]
        + [fmt(income[p]["tax"]) for p in ALL_PERIODS],
        ["Net income"] + [fmt(income[p]["net_income"]) for p in ALL_PERIODS],
        ["NCI income"] + [fmt(income[p]["nci_income"]) for p in ALL_PERIODS],
        ["Net income attributable to common"]
        + [fmt(income[p]["common_net_income"]) for p in ALL_PERIODS],
        ["Diluted weighted-average shares"]
        + [fmt(income[p]["diluted_shares"]) for p in ALL_PERIODS],
        ["Diluted EPS"] + [fmt(income[p]["diluted_eps"], 2) for p in ALL_PERIODS],
    ]
    historical_checks = [row for row in checks if "historical IS" in row[0]]
    check_rows = [
        [name, "PASS" if passed else "FAIL", fmt(difference, 2)]
        for name, passed, difference in historical_checks
    ]
    return f"""# Tesla income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

Company revenue and gross profit are sourced only from the four segment lines in [`segments.md`](segments.md); there is no revenue or gross-profit plug.

{markdown_table(["line", *ALL_PERIODS], detailed_rows)}

`1H2026A` is a six-month period and is not directly comparable with full years. FY2026 other income holds reported 1H other income and assumes zero in 2H, including no further SpaceX mark-to-market. FY2026 interest combines reported 1H with a 2H run-rate on the June balance; later years use beginning cash/investments and debt. Forecast tax uses the FY2025 effective rate.

## Historical filing checks

{markdown_table(["check", "status", "maximum difference"], check_rows)}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = [
        ["Cash"] + [fmt(balances[p]["cash"]) for p in ALL_PERIODS],
        ["Short-term investments"]
        + [fmt(balances[p]["short_investments"]) for p in ALL_PERIODS],
        ["Accounts receivable"] + [fmt(balances[p]["ar"]) for p in ALL_PERIODS],
        ["Inventory"] + [fmt(balances[p]["inventory"]) for p in ALL_PERIODS],
        ["Operating-lease vehicles"]
        + [fmt(balances[p]["lease_vehicles"]) for p in ALL_PERIODS],
        ["PP&E, net"] + [fmt(balances[p]["ppe"]) for p in ALL_PERIODS],
        ["SpaceX investment"]
        + [fmt(balances[p]["spacex_investment"]) for p in ALL_PERIODS],
        ["Other assets"] + [fmt(balances[p]["other_assets"]) for p in ALL_PERIODS],
        ["Total assets"] + [fmt(balances[p]["total_assets"]) for p in ALL_PERIODS],
        ["Accounts payable"] + [fmt(balances[p]["ap"]) for p in ALL_PERIODS],
        ["Debt and finance leases"]
        + [fmt(balances[p]["debt"]) for p in ALL_PERIODS],
        ["Other liabilities"]
        + [fmt(balances[p]["other_liabilities"]) for p in ALL_PERIODS],
        ["Total liabilities"]
        + [fmt(balances[p]["total_liabilities"]) for p in ALL_PERIODS],
        ["Additional paid-in capital"]
        + [fmt(balances[p]["apic"]) for p in ALL_PERIODS],
        ["Retained earnings"]
        + [fmt(balances[p]["retained_earnings"]) for p in ALL_PERIODS],
        ["AOCI and common stock"]
        + [
            fmt(balances[p]["aoci"] + balances[p]["common_stock"])
            for p in ALL_PERIODS
        ],
        ["Stockholders' equity"]
        + [fmt(balances[p]["stockholders_equity"]) for p in ALL_PERIODS],
        ["Other equity / NCI"]
        + [fmt(balances[p]["other_equity"]) for p in ALL_PERIODS],
        ["Total liabilities and equity"]
        + [fmt(balances[p]["total_liabilities_and_equity"]) for p in ALL_PERIODS],
        ["Period-end basic shares"]
        + [fmt(balances[p]["shares_out"]) for p in ALL_PERIODS],
        ["Diluted WAS used in model"]
        + [
            fmt(
                income[p]["diluted_shares"]
                if p in HIST_PERIODS
                else balances[p]["diluted_shares"]
            )
            for p in ALL_PERIODS
        ],
    ]
    relevant_checks = [
        row
        for row in checks
        if "balance sheet balances" in row[0]
        or "retained earnings" in row[0]
    ]
    check_rows = [
        [name, "PASS" if passed else "FAIL", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Tesla balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares.

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical FY2023 comes from the [FY2023 10-K]({S2023}); FY2024–FY2025 from [S1]({S1}); and 1H2026 from [S3]({S3}). “Other assets,” “Other liabilities,” and “Other equity / NCI” aggregate reported residual lines; the script calculates them from the filed totals.

FY2026 year-end balance-sheet lines roll forward from 2026-06-30 using the implied 2H portion of annual capex, D&A, SBC and net income; later years roll annually. PP&E equals beginning PP&E plus capex less D&A. Retained earnings receives common net income because dividends are zero. APIC increases by forecast SBC. Short-term investments are sold before incremental debt is issued to maintain the `[VIEW]` minimum cash balance. Forecast period-end basic shares are `not obtained`; diluted weighted-average shares are the researcher-specified model share counts.

## Tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_cashflow(
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows: list[list[str]] = []
    historical_lines = [
        ("Net income", "net_income"),
        ("D&A and impairment", "da"),
        ("SBC", "sbc"),
        ("Reported operating cash flow", "ocf"),
        ("Capex", "capex"),
        ("Free cash flow", "fcf"),
        ("Reported net investing cash flow", "net_investing"),
        ("Reported net financing cash flow", "net_financing"),
        ("FX effect", "fx"),
        ("Change in cash and restricted cash", "cash_change_restricted"),
        ("Ending cash and restricted cash", "ending_cash_restricted"),
        ("Ending balance-sheet cash", "bs_cash"),
        ("Restricted-cash reconciliation", "restricted_cash"),
    ]
    hist_derived: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        raw = HIST_CASHFLOW[period]
        hist_derived[period] = {
            **raw,
            "fcf": raw["ocf"] - raw["capex"],
            "bs_cash": balances[period]["cash"],
            "restricted_cash": raw["ending_cash_restricted"] - balances[period]["cash"],
        }
    for label, key in historical_lines:
        rows.append(
            [label]
            + [fmt(hist_derived[p][key]) for p in HIST_PERIODS]
            + ["—", "—", "—"]
        )

    forecast_lines = [
        ("Net income", "net_income"),
        ("D&A and impairment", "da"),
        ("SBC", "sbc"),
        ("Less: increase in core NWC", "delta_nwc"),
        ("Other operating / noncash adjustments", "other_operating_adjustments"),
        ("Operating cash flow", "ocf"),
        ("Less: capex", "capex"),
        ("Free cash flow", "fcf"),
        ("Less: SpaceX investment purchase", "spacex_purchase"),
        ("Other investing / financing / FX", "other_post_fcf"),
        ("Short-term investment maturities / sales", "investment_sale"),
        ("Net debt issuance", "debt_issuance"),
        ("Dividends", "dividends"),
        ("Buybacks", "buybacks"),
        ("Change in cash", "cash_change"),
        ("Ending cash", "ending_cash"),
    ]
    for label, key in forecast_lines:
        values = []
        for p in FORECAST_PERIODS:
            value = cashflow[p][key]
            if key in {
                "delta_nwc",
                "capex",
                "spacex_purchase",
                "dividends",
                "buybacks",
            }:
                value = -value
            values.append(fmt(value))
        rows.append([label, "—", "—", "—", "—", *values])

    wc = cashflow["_working_capital_days"]
    relevant_checks = [
        row
        for row in checks
        if "CF ending cash" in row[0] or "cash-flow bridge" in row[0]
    ]
    check_rows = [
        [name, "PASS" if passed else "FAIL", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Tesla cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical figures are reported cash-flow lines from [S1]({S1}) and [S3]({S3}); restricted cash reconciles the filed cash-flow ending balance to balance-sheet cash.

Forecast operating cash flow is explicitly `NI + D&A + SBC − Δ(core NWC) + other operating/noncash adjustments`. Core NWC is `accounts receivable + inventory − accounts payable`. Forecast days held from 2026-06-30 are: receivables `{wc["ar_days"]:.2f}`, inventory `{wc["inventory_days"]:.2f}`, payables `{wc["ap_days"]:.2f}`. FY2026 combines reported 1H operating cash flow with an explicit 2H roll-forward; its “other” lines aggregate the already-reported 1H non-core operating, investing, financing, FX and restricted-cash movements. FCF is operating cash flow less capex. Post-FCF cash flows separately show the actual-2026 SpaceX purchase, investment liquidation and required debt funding. Dividend and buyback assumptions are zero.

## Cash tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def valuation(
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> tuple[str, dict[str, float]]:
    """Compute and render the prescribed valuation and non-official checks."""

    shares_m = PT_SHARES / 1_000_000.0

    official_ebit = income["FY2027E"]["operating_income"]
    official_operating_ev = official_ebit * OFFICIAL_EBIT_MULTIPLE
    official_net_cash = (
        balances["FY2026E"]["cash"]
        + balances["FY2026E"]["short_investments"]
        - balances["FY2026E"]["debt"]
    )
    official_equity_value = (
        official_operating_ev + official_net_cash + SPACEX_FAIR_VALUE
    )
    official_pt = official_equity_value / shares_m

    three_year_operating_ev = (
        income["FY2028E"]["operating_income"] * THREE_YEAR_EBIT_MULTIPLE
    )
    exit_net_cash = (
        balances["FY2028E"]["cash"]
        + balances["FY2028E"]["short_investments"]
        - balances["FY2028E"]["debt"]
    )
    three_year_equity_value = (
        three_year_operating_ev + exit_net_cash + SPACEX_FAIR_VALUE
    )
    three_year_value = three_year_equity_value / shares_m

    bear_operating_ev = income["FY2027E"]["operating_income"] * BEAR_EBIT_MULTIPLE
    bear_equity_value = bear_operating_ev + official_net_cash + SPACEX_FAIR_VALUE
    bear_value = bear_equity_value / shares_m

    bull_operating_ev = income["FY2028E"]["operating_income"] * BULL_EBIT_MULTIPLE
    bull_equity_value = bull_operating_ev + exit_net_cash + SPACEX_FAIR_VALUE
    bull_value = bull_equity_value / shares_m

    residual_per_share = LAST_PRICE - official_pt
    market_cap = LAST_PRICE * PT_SHARES / 1_000_000.0
    q2_net_cash = (
        HIST_BALANCE["1H2026A"]["cash"]
        + HIST_BALANCE["1H2026A"]["short_investments"]
        - (
            HIST_BALANCE["1H2026A"]["debt_current"]
            + HIST_BALANCE["1H2026A"]["debt_long"]
        )
    )
    current_operating_ev = market_cap - q2_net_cash - SPACEX_FAIR_VALUE
    current_multiples: dict[str, float] = {}
    for period in ("FY2026E", "FY2028E"):
        current_multiples[f"{period}_revenue"] = (
            current_operating_ev / income[period]["total_revenue"]
        )
        current_multiples[f"{period}_ebit"] = (
            current_operating_ev / income[period]["operating_income"]
        )
        current_multiples[f"{period}_ni"] = (
            current_operating_ev / income[period]["common_net_income"]
        )

    fy25_tax_rate = HIST_INCOME["FY2025A"]["tax"] / (
        HIST_INCOME["FY2025A"]["net_income"] + HIST_INCOME["FY2025A"]["tax"]
    )
    ufcf: dict[str, float] = {}
    for period in FORECAST_PERIODS:
        after_tax_interest_expense = (
            income[period]["interest_expense"] * (1.0 - fy25_tax_rate)
        )
        after_tax_interest_income = (
            income[period]["interest_income"] * (1.0 - fy25_tax_rate)
        )
        ufcf[period] = (
            cashflow[period]["fcf"]
            + after_tax_interest_expense
            - after_tax_interest_income
        )

    # FY2026 uses the midpoint of the remaining period after the valuation date.
    cash_flow_dates = {
        "FY2026E": date(2026, 10, 31),
        "FY2027E": date(2027, 6, 30),
        "FY2028E": date(2028, 6, 30),
    }
    discount_years = {
        period: (cash_flow_dates[period] - VALUATION_DATE).days / 365.0
        for period in FORECAST_PERIODS
    }
    discount_factors = {
        period: (1.0 + DCF_WACC) ** discount_years[period]
        for period in FORECAST_PERIODS
    }
    pv_ufcf = {
        period: ufcf[period] / discount_factors[period]
        for period in FORECAST_PERIODS
    }
    terminal_nopat = income["FY2028E"]["operating_income"] * (
        1.0 - fy25_tax_rate
    )
    terminal_value = (
        terminal_nopat
        * (1.0 + DCF_TERMINAL_GROWTH)
        / (DCF_WACC - DCF_TERMINAL_GROWTH)
    )
    terminal_date = date(2028, 12, 31)
    terminal_years = (terminal_date - VALUATION_DATE).days / 365.0
    pv_terminal = terminal_value / ((1.0 + DCF_WACC) ** terminal_years)
    dcf_enterprise_value = sum(pv_ufcf.values()) + pv_terminal
    dcf_equity_value = dcf_enterprise_value + official_net_cash + SPACEX_FAIR_VALUE
    dcf_value = dcf_equity_value / shares_m
    terminal_share_of_positive_components = pv_terminal / (
        pv_terminal + official_net_cash + SPACEX_FAIR_VALUE
    )

    bridge_rows = [
        [
            "FY2027E operating income",
            "income.md",
            fmt(official_ebit, 1),
        ],
        ["Selected EV / EBIT", "[VIEW]", f"{OFFICIAL_EBIT_MULTIPLE:.1f}x"],
        [
            "Operating enterprise value",
            "EBIT × multiple",
            fmt(official_operating_ev, 1),
        ],
        [
            "YE2026E cash + short-term investments − debt",
            "balance.md",
            fmt(official_net_cash, 1),
        ],
        ["Tesla-held SpaceX stake", "R6.2; held at filing FV", fmt(SPACEX_FAIR_VALUE, 1)],
        ["Equity value", "EV + net cash + stake", fmt(official_equity_value, 1)],
        ["Shares outstanding (m)", "R5.3; not diluted WAS", fmt(shares_m, 3)],
        ["Official 12-month PT / share", "Equity value ÷ shares", f"${official_pt:.2f}"],
    ]

    setup_rows = [
        ["Valuation as-of", VALUATION_DATE.isoformat()],
        ["Last close", f"${LAST_PRICE:.2f} on {LAST_PRICE_DATE.isoformat()}"],
        [
            "Last-price source",
            f"[Yahoo Finance historical]({YAHOO_TSLA_HISTORY})",
        ],
        ["PT denominator", f"{PT_SHARES:,} shares outstanding on 2026-07-16 (R5.3)"],
        [
            "Method",
            "20.0× FY2027E operating income + YE2026E net cash + SpaceX filing FV",
        ],
    ]

    check_rows = [
        [
            "3-year / FY2028 exit",
            f"{THREE_YEAR_EBIT_MULTIPLE:.1f}× FY2028E EBIT + YE2028E net cash + stake",
            f"${three_year_value:.2f}",
        ],
        [
            "Bear",
            f"{BEAR_EBIT_MULTIPLE:.1f}× FY2027E EBIT + YE2026E net cash + stake",
            f"${bear_value:.2f}",
        ],
        [
            "Bull — modeled businesses only",
            f"{BULL_EBIT_MULTIPLE:.1f}× FY2028E EBIT + YE2028E net cash + stake",
            f"${bull_value:.2f}",
        ],
        [
            "DCF",
            f"{pct(DCF_WACC)} WACC; {pct(DCF_TERMINAL_GROWTH)} terminal growth",
            f"${dcf_value:.2f}",
        ],
    ]

    current_multiple_rows = [
        [
            "Market capitalization",
            "Last price × filing shares",
            fmt(market_cap, 1),
        ],
        [
            "2026-06-30 net cash",
            "Cash + STI − debt",
            fmt(q2_net_cash, 1),
        ],
        ["SpaceX stake", "R6.2", fmt(SPACEX_FAIR_VALUE, 1)],
        [
            "Current operating EV",
            "Market cap − net cash − stake",
            fmt(current_operating_ev, 1),
        ],
        [
            "EV / FY2026E revenue",
            "Current operating EV ÷ revenue",
            f"{current_multiples['FY2026E_revenue']:.1f}x",
        ],
        [
            "EV / FY2028E revenue",
            "Current operating EV ÷ revenue",
            f"{current_multiples['FY2028E_revenue']:.1f}x",
        ],
        [
            "EV / FY2026E EBIT",
            "Current operating EV ÷ operating income",
            f"{current_multiples['FY2026E_ebit']:.1f}x",
        ],
        [
            "EV / FY2028E EBIT",
            "Current operating EV ÷ operating income",
            f"{current_multiples['FY2028E_ebit']:.1f}x",
        ],
        [
            "EV / FY2026E common NI",
            "Current operating EV ÷ common NI",
            f"{current_multiples['FY2026E_ni']:.1f}x",
        ],
        [
            "EV / FY2028E common NI",
            "Current operating EV ÷ common NI",
            f"{current_multiples['FY2028E_ni']:.1f}x",
        ],
    ]

    dcf_rows = []
    for period in FORECAST_PERIODS:
        dcf_rows.append(
            [
                period,
                fmt(cashflow[period]["fcf"], 1),
                fmt(
                    income[period]["interest_expense"]
                    * (1.0 - fy25_tax_rate),
                    1,
                ),
                fmt(
                    -income[period]["interest_income"]
                    * (1.0 - fy25_tax_rate),
                    1,
                ),
                fmt(ufcf[period], 1),
                f"{discount_years[period]:.3f}",
                fmt(pv_ufcf[period], 1),
            ]
        )
    dcf_rows.extend(
        [
            [
                "Terminal",
                "—",
                "—",
                "—",
                fmt(terminal_value, 1),
                f"{terminal_years:.3f}",
                fmt(pv_terminal, 1),
            ],
            [
                "DCF enterprise value",
                "—",
                "—",
                "—",
                "—",
                "—",
                fmt(dcf_enterprise_value, 1),
            ],
            [
                "DCF equity value",
                "add YE2026E net cash + stake",
                "—",
                "—",
                "—",
                "—",
                fmt(dcf_equity_value, 1),
            ],
        ]
    )

    peer_rows = [
        [
            "GM",
            "0.5x",
            "51.1x",
            "2026-08-07",
            "[ValueSense](https://valuesense.io/ticker/gm/intrinsic-value)",
        ],
        [
            "F",
            "1.0x",
            "(26.7x)",
            "2026-08-25",
            "[ValueSense](https://valuesense.io/ticker/f/intrinsic-value)",
        ],
        [
            "TM",
            "1.34x",
            "18.95x",
            "retrieved 2026-08-29",
            "[StockAnalysis](https://stockanalysis.com/stocks/tm/statistics/)",
        ],
        [
            "BYD (1211.HK)",
            "1.04x",
            "18.93x",
            "retrieved 2026-08-29",
            "[StockAnalysis](https://stockanalysis.com/quote/hkg/1211/statistics/)",
        ],
        [
            "RIVN",
            "3.5x",
            "(5.8x)",
            "2026-08-13",
            "[ValueSense](https://valuesense.io/ticker/rivn/intrinsic-value)",
        ],
        [
            "FLNC — storage",
            "0.80x",
            "not obtained",
            "2026-08-28",
            "[StockAnalysis](https://stockanalysis.com/stocks/flnc/statistics/)",
        ],
        [
            "ENPH — solar/storage",
            "3.50x",
            "40.07x",
            "2026-08-28",
            "[StockAnalysis](https://stockanalysis.com/stocks/enph/statistics/)",
        ],
    ]

    content = f"""# Tesla valuation

At the ${LAST_PRICE:.2f} last close, the modeled-business official 12-month value in the bridge leaves most of the market price as unmodeled optionality rather than earnings included in this model.

## Official method and as-of

{markdown_table(["item", "value"], setup_rows)}

Robotaxi, incremental FSD and Optimus commercial revenue remain zero. No NPV for those businesses enters the official method.

## Official EV bridge

{markdown_table(["item", "basis", "$m except per share"], bridge_rows)}

The 20.0× FY2027E EBIT multiple is a `[VIEW]`: a premium to mature global auto framing, but not a software multiple. The modeled earned profit comes from Automotive, Energy and Services, while AI opex and capex compress FY2026–FY2027 EBIT and free cash flow.

## Checks — not additional official targets

{markdown_table(["check", "method", "value / share"], check_rows)}

The 3-year, bear and bull checks contain only the modeled businesses, net cash and Tesla-held SpaceX stake. They contain no autonomous-driving, FSD or Optimus NPV.

## DCF check

{markdown_table(["period", "FCF", "after-tax interest expense", "after-tax interest income", "UFCF / terminal value", "discount years", "present value"], dcf_rows)}

UFCF equals `FCF + after-tax interest expense − after-tax interest income`. FY2026 uses the midpoint of the remaining period after 2026-08-29; FY2027 and FY2028 use fiscal mid-year dates. Terminal value equals `FY2028E NOPAT × (1 + g) ÷ (WACC − g)`, where NOPAT uses the model’s FY2025 effective tax rate. Terminal value is {terminal_share_of_positive_components * 100:.1f}% of the positive terminal/net-cash/stake components because every explicit-year UFCF is negative; the DCF is therefore terminal-dominated and does not replace the official method.

## Current market-implied checks

{markdown_table(["item", "formula", "$m or multiple"], current_multiple_rows)}

**[DEDUCTED] Unmodeled residual per share:** `${LAST_PRICE:.2f} − modeled official value = ${residual_per_share:.2f}`. This is an arithmetic residual, not a Robotaxi valuation and not evidence that any specific optional business earns that amount.

## Comparable-company snapshot

{markdown_table(["company", "EV / Sales", "EV / EBIT", "as-of", "market source"], peer_rows)}

Negative peer EV/EBIT observations reflect negative trailing EBIT and are not economically meaningful positive valuation anchors. Fluence’s market page reports EV/EBIT as unavailable. The peer set is a framing check only; differing finance-company debt, leases, accounting, geography and business mix limit comparability.

## What would move the official value

- A sourced Robotaxi, FSD or Optimus P&L that can be added to the earned-profit model.
- A change in the FY2027E EBIT path generated by the segment and opex assumptions.
- A change in YE2026E cash, short-term investments or debt.
- A change in the selected 20.0× EBIT multiple.
"""

    summary = {
        "official_pt": official_pt,
        "residual": residual_per_share,
        "three_year": three_year_value,
        "bear": bear_value,
        "bull": bull_value,
        "dcf": dcf_value,
    }
    return content, summary


def main() -> None:
    historical_segments = derived_historical_segments()
    forecast_segments, fy25_quotient, q2_quotient = build_forecast_segments()
    segments = {**historical_segments, **forecast_segments}
    balances, income, cashflow = build_forecast(segments)
    checks = build_checks(segments, income, balances, cashflow)
    valuation_markdown, valuation_summary = valuation(income, balances, cashflow)

    outputs = {
        "segments.md": render_segments(
            segments, fy25_quotient, q2_quotient, checks
        ),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, checks),
        "cashflow.md": render_cashflow(balances, cashflow, checks),
        "valuation.md": valuation_markdown,
    }
    for filename, content in outputs.items():
        (ROOT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("Tesla model outputs")
    print("period | revenue | gross profit | operating income | common NI | FCF | diluted EPS")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['total_revenue']:.1f} | "
            f"{income[period]['total_gp']:.1f} | "
            f"{income[period]['operating_income']:.1f} | "
            f"{income[period]['common_net_income']:.1f} | "
            f"{cashflow[period]['fcf']:.1f} | "
            f"{income[period]['diluted_eps']:.2f}"
        )
    print("\nValuation outputs")
    print(f"Official 12-month PT | ${valuation_summary['official_pt']:.2f}")
    print(f"Unmodeled residual | ${valuation_summary['residual']:.2f}")
    print(f"3-year check | ${valuation_summary['three_year']:.2f}")
    print(f"Bear check | ${valuation_summary['bear']:.2f}")
    print(f"Bull check | ${valuation_summary['bull']:.2f}")
    print(f"DCF check | ${valuation_summary['dcf']:.2f}")
    print("\nTie-out checks")
    failed = False
    for name, passed, difference in checks:
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {name} (difference {difference:.6f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
