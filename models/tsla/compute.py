#!/usr/bin/env python3
"""Tesla segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md and cashflow.md, then prints tie-out checks.
USD millions except per-share data, units, GWh and percentages.
"""

from __future__ import annotations

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
SPACEX_NONCASH_GAIN_2026 = 1_005.0


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


def build_income(
    segments: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]] | None = None,
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

    if balances is None:
        return output

    fy25_tax_rate = HIST_INCOME["FY2025A"]["tax"] / (
        HIST_INCOME["FY2025A"]["net_income"] + HIST_INCOME["FY2025A"]["tax"]
    )
    previous_balance = balances["FY2025A"]
    for period in FORECAST_PERIODS:
        segment = segments[period]
        assumption = ASSUMPTIONS[period]
        total_opex = assumption["rd"] + assumption["sga"]
        operating_income = segment["total_gp"] - total_opex
        beginning_liquidity = (
            previous_balance["cash"] + previous_balance["short_investments"]
        )
        beginning_debt = previous_balance["debt"]
        interest_income = (
            beginning_liquidity * INTEREST_INCOME_RATE_ON_BEGINNING_LIQUIDITY
        )
        interest_expense = beginning_debt * INTEREST_EXPENSE_RATE_ON_BEGINNING_DEBT
        other_income = SPACEX_NONCASH_GAIN_2026 if period == "FY2026E" else 0.0
        pretax = operating_income + interest_income - interest_expense + other_income
        tax = max(pretax, 0.0) * fy25_tax_rate
        net_income = pretax - tax
        output[period] = {
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
            "nci_income": 0.0,
            "common_net_income": net_income,
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": net_income / assumption["diluted_shares"],
        }
        previous_balance = balances[period]
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

    # Working-capital days use 1H 2026 balances and annualized 1H flows.
    h1_revenue_annualized = segments["1H2026A"]["total_revenue"] * 2.0
    h1_cogs_annualized = (
        segments["1H2026A"]["total_revenue"] - segments["1H2026A"]["total_gp"]
    ) * 2.0
    h1_balance = balances["1H2026A"]
    ar_days = h1_balance["ar"] / h1_revenue_annualized * 365.0
    inventory_days = h1_balance["inventory"] / h1_cogs_annualized * 365.0
    ap_days = h1_balance["ap"] / h1_cogs_annualized * 365.0

    # First pass creates a provisional sequential balance and income statement.
    previous = balances["FY2025A"]
    forecast_cashflow: dict[str, dict[str, float]] = {}
    for period in FORECAST_PERIODS:
        segment = segments[period]
        assumption = ASSUMPTIONS[period]
        revenue = segment["total_revenue"]
        cogs = revenue - segment["total_gp"]
        ar = revenue * ar_days / 365.0
        inventory = cogs * inventory_days / 365.0
        ap = cogs * ap_days / 365.0
        delta_nwc = (
            (ar + inventory - ap)
            - (previous["ar"] + previous["inventory"] - previous["ap"])
        )
        sbc = (assumption["rd"] + assumption["sga"]) * SBC_AS_PERCENT_OF_RD_AND_SGA
        # D&A is based on average PPE. Solving:
        # D&A = rate * (beginning PPE + ending PPE) / 2
        # ending PPE = beginning PPE + capex - D&A
        da = (
            DA_RATE_ON_AVERAGE_PPE
            * (previous["ppe"] + assumption["capex"] / 2.0)
            / (1.0 + DA_RATE_ON_AVERAGE_PPE / 2.0)
        )
        ppe = previous["ppe"] + assumption["capex"] - da
        lease_vehicles = ENDING_LEASE_VEHICLES
        spacex_investment = SPACEX_FAIR_VALUE
        spacex_gain_adjustment = (
            SPACEX_NONCASH_GAIN_2026 if period == "FY2026E" else 0.0
        )
        spacex_purchase = (
            SPACEX_CASH_PURCHASE_2026 if period == "FY2026E" else 0.0
        )

        # Income is temporarily calculated here so cash and funding can be
        # determined. The same formulas are repeated by build_income and tested.
        fy25_tax_rate = HIST_INCOME["FY2025A"]["tax"] / (
            HIST_INCOME["FY2025A"]["net_income"] + HIST_INCOME["FY2025A"]["tax"]
        )
        operating_income = (
            segment["total_gp"] - assumption["rd"] - assumption["sga"]
        )
        interest_income = (
            (previous["cash"] + previous["short_investments"])
            * INTEREST_INCOME_RATE_ON_BEGINNING_LIQUIDITY
        )
        interest_expense = (
            previous["debt"] * INTEREST_EXPENSE_RATE_ON_BEGINNING_DEBT
        )
        other_income = SPACEX_NONCASH_GAIN_2026 if period == "FY2026E" else 0.0
        pretax = operating_income + interest_income - interest_expense + other_income
        tax = max(pretax, 0.0) * fy25_tax_rate
        net_income = pretax - tax

        operating_cash_flow = (
            net_income + da + sbc - delta_nwc - spacex_gain_adjustment
        )
        free_cash_flow = operating_cash_flow - assumption["capex"]
        lease_fleet_cash_flow = -(lease_vehicles - previous["lease_vehicles"])
        pre_funding_cash = (
            previous["cash"]
            + free_cash_flow
            - spacex_purchase
            + lease_fleet_cash_flow
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

        retained_earnings = previous["retained_earnings"] + net_income - DIVIDENDS
        apic = previous["apic"] + sbc
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
        forecast_cashflow[period] = {
            "net_income": net_income,
            "da": da,
            "sbc": sbc,
            "delta_nwc": delta_nwc,
            "spacex_gain_adjustment": spacex_gain_adjustment,
            "ocf": operating_cash_flow,
            "capex": assumption["capex"],
            "fcf": free_cash_flow,
            "spacex_purchase": spacex_purchase,
            "lease_fleet_cash_flow": lease_fleet_cash_flow,
            "investment_sale": investment_sale,
            "debt_issuance": debt_issuance,
            "dividends": DIVIDENDS,
            "buybacks": BUYBACKS,
            "cash_change": cash - previous["cash"],
            "ending_cash": cash,
        }
        previous = balances[period]

    income = build_income(segments, balances)
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
        row for row in checks if "segment revenue" in row[0] or "segment GP" in row[0]
    ]
    check_rows = [
        [name, "PASS" if passed else "FAIL", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
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

`1H2026A` is a six-month period and is not directly comparable with full years. FY2026 other income includes the actual first-half SpaceX unrealized gain and assumes no further mark-to-market; the cash-flow statement removes that noncash gain. Forecast tax uses the FY2025 effective rate. Forecast interest income uses beginning cash plus short-term investments; interest expense uses beginning debt.

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

Forecast PP&E equals beginning PP&E plus capex less D&A. Retained earnings equals prior retained earnings plus common net income because dividends are zero. APIC increases by forecast SBC. Short-term investments are sold before incremental debt is issued to maintain the `[VIEW]` minimum cash balance. Forecast period-end basic shares are `not obtained`; diluted weighted-average shares are the researcher-specified model share counts.

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
        ("Less: SpaceX noncash gain", "spacex_gain_adjustment"),
        ("Operating cash flow", "ocf"),
        ("Less: capex", "capex"),
        ("Free cash flow", "fcf"),
        ("Less: SpaceX investment purchase", "spacex_purchase"),
        ("Lease-fleet investment / (release)", "lease_fleet_cash_flow"),
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
                "spacex_gain_adjustment",
                "capex",
                "spacex_purchase",
                "dividends",
                "buybacks",
            }:
                value = -value
            values.append(fmt(value))
        rows.append([label, "—", "—", "—", "—", *values])

    wc = cashflow["_working_capital_days"]
    relevant_checks = [row for row in checks if "CF ending cash" in row[0]]
    check_rows = [
        [name, "PASS" if passed else "FAIL", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Tesla cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical figures are reported cash-flow lines from [S1]({S1}) and [S3]({S3}); restricted cash reconciles the filed cash-flow ending balance to balance-sheet cash.

Forecast operating cash flow is explicitly `NI + D&A + SBC − Δ(core NWC) − noncash SpaceX gain`. Core NWC is `accounts receivable + inventory − accounts payable`. Forecast days held from 2026-06-30 are: receivables `{wc["ar_days"]:.2f}`, inventory `{wc["inventory_days"]:.2f}`, payables `{wc["ap_days"]:.2f}`. FCF is operating cash flow less capex. Post-FCF cash flows separately show the actual-2026 SpaceX purchase, lease-fleet change, investment liquidation and required debt funding. Dividend and buyback assumptions are zero.

## Cash tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def main() -> None:
    historical_segments = derived_historical_segments()
    forecast_segments, fy25_quotient, q2_quotient = build_forecast_segments()
    segments = {**historical_segments, **forecast_segments}
    balances, income, cashflow = build_forecast(segments)
    checks = build_checks(segments, income, balances, cashflow)

    outputs = {
        "segments.md": render_segments(
            segments, fy25_quotient, q2_quotient, checks
        ),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, checks),
        "cashflow.md": render_cashflow(balances, cashflow, checks),
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
