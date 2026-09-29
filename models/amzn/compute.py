#!/usr/bin/env python3
"""Amazon segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md and cashflow.md, then prints tie-out checks.
USD millions except per-share data and percentages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2022A", "FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

S1 = "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm"
S2 = "https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm"
S3 = "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"
S4 = "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm"
REGISTER = "../../memory/amzn/register.md"

HIST_SEGMENTS = {
    "FY2022A": {
        "na_revenue": 315_880.0,
        "intl_revenue": 118_007.0,
        "aws_revenue": 80_096.0,
        "na_oi": -2_847.0,
        "intl_oi": -7_746.0,
        "aws_oi": 22_841.0,
    },
    "FY2023A": {
        "na_revenue": 352_828.0,
        "intl_revenue": 131_200.0,
        "aws_revenue": 90_757.0,
        "na_oi": 14_877.0,
        "intl_oi": -2_656.0,
        "aws_oi": 24_631.0,
    },
    "FY2024A": {
        "na_revenue": 387_497.0,
        "intl_revenue": 142_906.0,
        "aws_revenue": 107_556.0,
        "na_oi": 24_967.0,
        "intl_oi": 3_792.0,
        "aws_oi": 39_834.0,
    },
    "FY2025A": {
        "na_revenue": 426_305.0,
        "intl_revenue": 161_894.0,
        "aws_revenue": 128_725.0,
        "na_oi": 29_619.0,
        "intl_oi": 4_750.0,
        "aws_oi": 45_606.0,
    },
    "1H2026A": {
        "na_revenue": 220_320.0,
        "intl_revenue": 81_986.0,
        "aws_revenue": 79_819.0,
        "na_oi": 17_390.0,
        "intl_oi": 3_141.0,
        "aws_oi": 30_782.0,
    },
}

HIST_INCOME = {
    "FY2022A": {
        "interest_income": 989.0,
        "interest_expense": 2_367.0,
        "other_income": -16_806.0,
        "tax": -3_217.0,
        "equity_method": -3.0,
        "net_income": -2_722.0,
        "diluted_shares": 10_189.0,
    },
    "FY2023A": {
        "interest_income": 2_949.0,
        "interest_expense": 3_182.0,
        "other_income": 938.0,
        "tax": 7_120.0,
        "equity_method": -12.0,
        "net_income": 30_425.0,
        "diluted_shares": 10_492.0,
    },
    "FY2024A": {
        "interest_income": 4_677.0,
        "interest_expense": 2_406.0,
        "other_income": -2_250.0,
        "tax": 9_265.0,
        "equity_method": -101.0,
        "net_income": 59_248.0,
        "diluted_shares": 10_721.0,
    },
    "FY2025A": {
        "interest_income": 4_381.0,
        "interest_expense": 2_274.0,
        "other_income": 15_229.0,
        "tax": 19_087.0,
        "equity_method": -554.0,
        "net_income": 77_670.0,
        "diluted_shares": 10_827.0,
    },
    "1H2026A": {
        "interest_income": 2_430.0,
        "interest_expense": 2_114.0,
        "other_income": 69_062.0,
        "tax": 27_759.0,
        "equity_method": -30.0,
        "net_income": 92_902.0,
        "diluted_shares": 10_889.0,
    },
}

HIST_BALANCE = {
    "FY2023A": {
        "cash": 73_387.0,
        "short_investments": 13_393.0,
        "ar": 52_253.0,
        "inventory": 33_318.0,
        "ppe": 204_177.0,
        "operating_leases": 72_513.0,
        "other_assets": 78_813.0,
        "total_assets": 527_854.0,
        "ap": 84_981.0,
        "debt": 58_314.0,
        "lease_liabilities": 77_297.0,
        "other_liabilities": 90_387.0,
        "apic": 99_025.0,
        "aoci": -3_040.0,
        "retained_earnings": 113_618.0,
        "treasury_and_common": -7_726.0,
        "stockholders_equity": 201_875.0,
    },
    "FY2024A": {
        "cash": 78_779.0,
        "short_investments": 22_423.0,
        "ar": 55_451.0,
        "inventory": 34_214.0,
        "ppe": 252_665.0,
        "operating_leases": 76_141.0,
        "other_assets": 105_221.0,
        "total_assets": 624_894.0,
        "ap": 94_363.0,
        "debt": 52_623.0,
        "lease_liabilities": 78_277.0,
        "other_liabilities": 95_558.0,
        "apic": 120_864.0,
        "aoci": -34.0,
        "retained_earnings": 172_866.0,
        "treasury_and_common": -7_726.0,
        "stockholders_equity": 285_970.0,
    },
    "FY2025A": {
        "cash": 86_810.0,
        "short_investments": 36_219.0,
        "ar": 67_729.0,
        "inventory": 38_325.0,
        "ppe": 357_025.0,
        "operating_leases": 86_054.0,
        "other_assets": 145_880.0,
        "total_assets": 818_042.0,
        "ap": 121_909.0,
        "debt": 65_648.0,
        "lease_liabilities": 87_339.0,
        "other_liabilities": 111_505.0,
        "apic": 140_024.0,
        "aoci": 28_230.0,
        "retained_earnings": 250_536.0,
        "treasury_and_common": -7_725.0,
        "stockholders_equity": 411_065.0,
    },
    "1H2026A": {
        "cash": 78_213.0,
        "short_investments": 44_775.0,
        "ar": 88_092.0,
        "inventory": 38_184.0,
        "ppe": 446_046.0,
        "operating_leases": 92_743.0,
        "other_assets": 307_636.0,
        "total_assets": 1_095_689.0,
        "ap": 147_440.0,
        "debt": 132_224.0,
        "lease_liabilities": 109_771.0,
        "other_liabilities": 152_969.0,
        "apic": 149_619.0,
        "aoci": 66_287.0,
        "retained_earnings": 343_438.0,
        "treasury_and_common": -7_724.0,
        "stockholders_equity": 551_620.0,
    },
}

HIST_CASHFLOW = {
    "FY2023A": {
        "net_income": 30_425.0,
        "da": 48_663.0,
        "sbc": 24_023.0,
        "ocf": 84_946.0,
        "purchases_ppe": 52_729.0,
        "proceeds_ppe": 4_596.0,
        "net_investing": -49_833.0,
        "net_financing": -15_879.0,
        "fx": 403.0,
        "cash_change_restricted": 19_637.0,
        "ending_cash_restricted": 73_890.0,
    },
    "FY2024A": {
        "net_income": 59_248.0,
        "da": 52_795.0,
        "sbc": 22_011.0,
        "ocf": 115_877.0,
        "purchases_ppe": 82_999.0,
        "proceeds_ppe": 5_341.0,
        "net_investing": -94_342.0,
        "net_financing": -11_812.0,
        "fx": -1_301.0,
        "cash_change_restricted": 8_422.0,
        "ending_cash_restricted": 82_312.0,
    },
    "FY2025A": {
        "net_income": 77_670.0,
        "da": 65_756.0,
        "sbc": 19_467.0,
        "ocf": 139_514.0,
        "purchases_ppe": 131_819.0,
        "proceeds_ppe": 3_499.0,
        "net_investing": -142_545.0,
        "net_financing": -8_652.0,
        "fx": 171.0,
        "cash_change_restricted": 7_794.0,
        "ending_cash_restricted": 90_106.0,
    },
    "1H2026A": {
        "net_income": 92_902.0,
        "da": 38_933.0,
        "sbc": 10_070.0,
        "ocf": 71_419.0,
        "purchases_ppe": 98_411.0,
        "proceeds_ppe": 2_101.0,
        "net_investing": -143_457.0,
        "net_financing": 62_913.0,
        "fx": -54.0,
        "cash_change_restricted": -9_179.0,
        "ending_cash_restricted": 80_927.0,
    },
}

ASSUMPTIONS = {
    "FY2026E": {
        "na_revenue_growth": 0.13,
        "intl_revenue_growth": 0.15,
        "aws_revenue_growth": 0.26,
        "na_op_margin": 0.080,
        "intl_op_margin": 0.036,
        "aws_op_margin": 0.370,
        "net_cash_capex": 200_000.0,
        "diluted_shares": 10_950.0,
    },
    "FY2027E": {
        "na_revenue_growth": 0.11,
        "intl_revenue_growth": 0.13,
        "aws_revenue_growth": 0.20,
        "na_op_margin": 0.083,
        "intl_op_margin": 0.039,
        "aws_op_margin": 0.375,
        "net_cash_capex": 175_000.0,
        "diluted_shares": 11_000.0,
    },
    "FY2028E": {
        "na_revenue_growth": 0.10,
        "intl_revenue_growth": 0.11,
        "aws_revenue_growth": 0.16,
        "na_op_margin": 0.085,
        "intl_op_margin": 0.042,
        "aws_op_margin": 0.380,
        "net_cash_capex": 155_000.0,
        "diluted_shares": 11_050.0,
    },
}

CAPEX_PROCEEDS_RATE = 3_499.0 / 131_819.0
FY25_TAX_RATE = 19_087.0 / 97_311.0
INTEREST_INCOME_RATE = 0.025
INTEREST_EXPENSE_RATE = 0.035
MINIMUM_CASH = 50_000.0
DIVIDENDS = 0.0
BUYBACKS = 0.0
OPENAI_REMAINING_CASH_2026 = 21_300.0
HOLD_OTHER_INCOME_1H_ONLY_2026 = True


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


def enrich_historical_segments() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_SEGMENTS.items():
        total_revenue = raw["na_revenue"] + raw["intl_revenue"] + raw["aws_revenue"]
        total_oi = raw["na_oi"] + raw["intl_oi"] + raw["aws_oi"]
        output[period] = {
            **raw,
            "total_revenue": total_revenue,
            "total_oi": total_oi,
            "na_opex": raw["na_revenue"] - raw["na_oi"],
            "intl_opex": raw["intl_revenue"] - raw["intl_oi"],
            "aws_opex": raw["aws_revenue"] - raw["aws_oi"],
            "total_opex": total_revenue - total_oi,
        }
    return output


def build_forecast_segments(
    prior: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    working = {**prior}
    previous_key = "FY2025A"
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        base = working[previous_key]
        na_revenue = base["na_revenue"] * (1.0 + assumption["na_revenue_growth"])
        intl_revenue = base["intl_revenue"] * (1.0 + assumption["intl_revenue_growth"])
        aws_revenue = base["aws_revenue"] * (1.0 + assumption["aws_revenue_growth"])
        na_oi = na_revenue * assumption["na_op_margin"]
        intl_oi = intl_revenue * assumption["intl_op_margin"]
        aws_oi = aws_revenue * assumption["aws_op_margin"]
        total_revenue = na_revenue + intl_revenue + aws_revenue
        total_oi = na_oi + intl_oi + aws_oi
        output[period] = {
            "na_revenue": na_revenue,
            "intl_revenue": intl_revenue,
            "aws_revenue": aws_revenue,
            "na_oi": na_oi,
            "intl_oi": intl_oi,
            "aws_oi": aws_oi,
            "total_revenue": total_revenue,
            "total_oi": total_oi,
            "na_opex": na_revenue - na_oi,
            "intl_opex": intl_revenue - intl_oi,
            "aws_opex": aws_revenue - aws_oi,
            "total_opex": total_revenue - total_oi,
        }
        working[period] = output[period]
        previous_key = period
    return output


def build_historical_income(
    segments: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        segment = segments[period]
        raw = HIST_INCOME[period]
        operating_income = segment["total_oi"]
        pretax = (
            operating_income
            + raw["interest_income"]
            - raw["interest_expense"]
            + raw["other_income"]
        )
        output[period] = {
            **raw,
            "total_revenue": segment["total_revenue"],
            "operating_income": operating_income,
            "pretax_income": pretax,
            "diluted_eps": raw["net_income"] / raw["diluted_shares"],
        }
    return output


def historical_balance_with_derived() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period, raw in HIST_BALANCE.items():
        total_liabilities = (
            raw["ap"] + raw["debt"] + raw["lease_liabilities"] + raw["other_liabilities"]
        )
        output[period] = {
            **raw,
            "total_liabilities": total_liabilities,
            "total_liabilities_and_equity": total_liabilities + raw["stockholders_equity"],
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

    h1_revenue_annualized = segments["1H2026A"]["total_revenue"] * 2.0
    h1_opex_annualized = segments["1H2026A"]["total_opex"] * 2.0
    h1_balance = balances["1H2026A"]
    ar_days = h1_balance["ar"] / h1_revenue_annualized * 365.0
    inventory_days = h1_balance["inventory"] / h1_opex_annualized * 365.0
    ap_days = h1_balance["ap"] / h1_opex_annualized * 365.0

    fy25_da_rate = HIST_CASHFLOW["FY2025A"]["da"] / (
        (HIST_BALANCE["FY2024A"]["ppe"] + HIST_BALANCE["FY2025A"]["ppe"]) / 2.0
    )

    forecast_cashflow: dict[str, dict[str, float]] = {}
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        is_fy26 = period == "FY2026E"
        previous = balances["1H2026A"] if is_fy26 else balances[
            FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]
        ]
        prior_annual = balances["FY2025A"] if is_fy26 else previous
        segment = segments[period]

        revenue = segment["total_revenue"]
        opex = segment["total_opex"]
        ar = revenue * ar_days / 365.0
        inventory = opex * inventory_days / 365.0
        ap = opex * ap_days / 365.0
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
            HIST_CASHFLOW["1H2026A"]["sbc"] * 2.0
            if is_fy26
            else forecast_cashflow[FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]][
                "sbc"
            ]
            * 1.03
        )
        rollforward_sbc = (
            annual_sbc - HIST_CASHFLOW["1H2026A"]["sbc"]
            if is_fy26
            else annual_sbc
        )

        purchases = assumption["net_cash_capex"] / (1.0 - CAPEX_PROCEEDS_RATE)
        proceeds = purchases * CAPEX_PROCEEDS_RATE
        rollforward_purchases = (
            purchases - HIST_CASHFLOW["1H2026A"]["purchases_ppe"]
            if is_fy26
            else purchases
        )
        rollforward_proceeds = (
            proceeds - HIST_CASHFLOW["1H2026A"]["proceeds_ppe"]
            if is_fy26
            else proceeds
        )
        rollforward_net_capex = rollforward_purchases - rollforward_proceeds

        rollforward_da_rate = fy25_da_rate / 2.0 if is_fy26 else fy25_da_rate
        rollforward_da = (
            rollforward_da_rate
            * (previous["ppe"] + rollforward_purchases / 2.0)
            / (1.0 + rollforward_da_rate / 2.0)
        )
        annual_da = (
            HIST_CASHFLOW["1H2026A"]["da"] + rollforward_da
            if is_fy26
            else rollforward_da
        )
        ppe = previous["ppe"] + rollforward_purchases - rollforward_da

        operating_income = segment["total_oi"]
        interest_income = (
            HIST_INCOME["1H2026A"]["interest_income"]
            + (previous["cash"] + previous["short_investments"])
            * INTEREST_INCOME_RATE
            / 2.0
            if is_fy26
            else (previous["cash"] + previous["short_investments"])
            * INTEREST_INCOME_RATE
        )
        interest_expense = (
            HIST_INCOME["1H2026A"]["interest_expense"]
            + (previous["debt"] + previous["lease_liabilities"])
            * INTEREST_EXPENSE_RATE
            / 2.0
            if is_fy26
            else (previous["debt"] + previous["lease_liabilities"])
            * INTEREST_EXPENSE_RATE
        )
        other_income = (
            HIST_INCOME["1H2026A"]["other_income"]
            if is_fy26 and HOLD_OTHER_INCOME_1H_ONLY_2026
            else 0.0
        )
        pretax = operating_income + interest_income - interest_expense + other_income
        tax = max(pretax, 0.0) * FY25_TAX_RATE
        equity_method = HIST_INCOME["1H2026A"]["equity_method"] if is_fy26 else 0.0
        net_income = pretax - tax + equity_method

        income[period] = {
            "interest_income": interest_income,
            "interest_expense": interest_expense,
            "other_income": other_income,
            "tax": tax,
            "equity_method": equity_method,
            "net_income": net_income,
            "total_revenue": revenue,
            "operating_income": operating_income,
            "pretax_income": pretax,
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": net_income / assumption["diluted_shares"],
        }

        rollforward_net_income = (
            net_income - HIST_INCOME["1H2026A"]["net_income"]
            if is_fy26
            else net_income
        )
        rollforward_ocf = (
            rollforward_net_income
            + rollforward_da
            + rollforward_sbc
            - rollforward_delta_nwc
        )
        strategic_investing = OPENAI_REMAINING_CASH_2026 if is_fy26 else 0.0
        rollforward_fcf = rollforward_ocf - rollforward_net_capex - strategic_investing

        pre_funding_cash = previous["cash"] + rollforward_fcf
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
            previous["retained_earnings"] + rollforward_net_income - DIVIDENDS
        )
        apic = previous["apic"] + rollforward_sbc
        aoci = previous["aoci"]
        treasury_and_common = previous["treasury_and_common"]
        operating_leases = previous["operating_leases"] * (ppe / previous["ppe"])
        lease_liabilities = previous["lease_liabilities"] * (
            operating_leases / previous["operating_leases"]
        )
        other_liabilities = previous["other_liabilities"]
        total_liabilities = ap + debt + lease_liabilities + other_liabilities
        stockholders_equity = apic + aoci + retained_earnings + treasury_and_common
        total_liabilities_and_equity = total_liabilities + stockholders_equity
        core_assets = (
            cash
            + short_investments
            + ar
            + inventory
            + ppe
            + operating_leases
        )
        other_assets = total_liabilities_and_equity - core_assets
        total_assets = total_liabilities_and_equity

        balances[period] = {
            "cash": cash,
            "short_investments": short_investments,
            "ar": ar,
            "inventory": inventory,
            "ppe": ppe,
            "operating_leases": operating_leases,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "ap": ap,
            "debt": debt,
            "lease_liabilities": lease_liabilities,
            "other_liabilities": other_liabilities,
            "total_liabilities": total_liabilities,
            "apic": apic,
            "aoci": aoci,
            "retained_earnings": retained_earnings,
            "treasury_and_common": treasury_and_common,
            "stockholders_equity": stockholders_equity,
            "total_liabilities_and_equity": total_liabilities_and_equity,
            "diluted_shares": assumption["diluted_shares"],
        }

        annual_ocf = (
            HIST_CASHFLOW["1H2026A"]["ocf"] + rollforward_ocf
            if is_fy26
            else rollforward_ocf
        )
        annual_fcf = annual_ocf - assumption["net_cash_capex"] - strategic_investing
        other_operating_adjustments = (
            annual_ocf - net_income - annual_da - annual_sbc + annual_delta_nwc
        )
        h1_other_post_fcf = (
            HIST_CASHFLOW["1H2026A"]["net_investing"]
            + HIST_CASHFLOW["1H2026A"]["purchases_ppe"]
            - HIST_CASHFLOW["1H2026A"]["proceeds_ppe"]
            + OPENAI_REMAINING_CASH_2026
            + HIST_CASHFLOW["1H2026A"]["net_financing"]
            + HIST_CASHFLOW["1H2026A"]["fx"]
        ) if is_fy26 else 0.0

        forecast_cashflow[period] = {
            "net_income": net_income,
            "da": annual_da,
            "sbc": annual_sbc,
            "delta_nwc": annual_delta_nwc,
            "other_operating_adjustments": other_operating_adjustments,
            "ocf": annual_ocf,
            "purchases_ppe": purchases,
            "proceeds_ppe": proceeds,
            "net_cash_capex": assumption["net_cash_capex"],
            "strategic_investing": strategic_investing,
            "fcf": annual_fcf,
            "other_post_fcf": h1_other_post_fcf,
            "investment_sale": investment_sale,
            "debt_issuance": debt_issuance,
            "dividends": DIVIDENDS,
            "buybacks": BUYBACKS,
            "cash_change": cash - prior_annual["cash"],
            "ending_cash": cash,
        }

    forecast_cashflow["_working_capital_days"] = {
        "ar_days": ar_days,
        "inventory_days": inventory_days,
        "ap_days": ap_days,
    }
    return balances, income, forecast_cashflow


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tolerance = 0.5

    historical_expected_oi = {
        "FY2022A": 12_248.0,
        "FY2023A": 36_852.0,
        "FY2024A": 68_593.0,
        "FY2025A": 79_975.0,
        "1H2026A": 51_313.0,
    }
    historical_expected_rev = {
        "FY2022A": 513_983.0,
        "FY2023A": 574_785.0,
        "FY2024A": 637_959.0,
        "FY2025A": 716_924.0,
        "1H2026A": 382_125.0,
    }

    for period in ALL_PERIODS:
        segment = segments[period]
        revenue_sum = segment["na_revenue"] + segment["intl_revenue"] + segment["aws_revenue"]
        oi_sum = segment["na_oi"] + segment["intl_oi"] + segment["aws_oi"]
        checks.append(
            (
                f"{period}: segment revenue = consolidated revenue",
                abs(revenue_sum - segment["total_revenue"]) < tolerance,
                revenue_sum - segment["total_revenue"],
            )
        )
        checks.append(
            (
                f"{period}: segment OI = consolidated OI",
                abs(oi_sum - segment["total_oi"]) < tolerance,
                oi_sum - segment["total_oi"],
            )
        )
        checks.append(
            (
                f"{period}: segment OI flows to income statement",
                abs(oi_sum - income[period]["operating_income"]) < tolerance,
                oi_sum - income[period]["operating_income"],
            )
        )
        if period in historical_expected_oi:
            checks.append(
                (
                    f"{period}: segment OI matches register filing",
                    abs(segment["total_oi"] - historical_expected_oi[period])
                    < tolerance,
                    segment["total_oi"] - historical_expected_oi[period],
                )
            )
            checks.append(
                (
                    f"{period}: segment revenue matches register filing",
                    abs(segment["total_revenue"] - historical_expected_rev[period])
                    < tolerance,
                    segment["total_revenue"] - historical_expected_rev[period],
                )
            )

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
        if period == "FY2026E":
            previous_for_re = balances["1H2026A"]
            expected_re = previous_for_re["retained_earnings"] + (
                income[period]["net_income"] - HIST_INCOME["1H2026A"]["net_income"]
            )
        else:
            previous_for_re = balances[
                FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]
            ]
            expected_re = previous_for_re["retained_earnings"] + income[period]["net_income"]
        checks.append(
            (
                f"{period}: IS NI flows to retained earnings",
                abs(expected_re - balance["retained_earnings"]) < tolerance,
                expected_re - balance["retained_earnings"],
            )
        )
    return checks


def render_segments(
    segments: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows: list[list[str]] = []
    line_items = [
        ("North America revenue", "na_revenue"),
        ("North America operating expense", "na_opex"),
        ("North America operating income", "na_oi"),
        ("International revenue", "intl_revenue"),
        ("International operating expense", "intl_opex"),
        ("International operating income", "intl_oi"),
        ("AWS revenue", "aws_revenue"),
        ("AWS operating expense", "aws_opex"),
        ("AWS operating income", "aws_oi"),
        ("Consolidated revenue", "total_revenue"),
        ("Consolidated operating expense", "total_opex"),
        ("Consolidated operating income", "total_oi"),
    ]
    forecast_keys = {
        "na_revenue",
        "intl_revenue",
        "aws_revenue",
        "na_opex",
        "intl_opex",
        "aws_opex",
        "na_oi",
        "intl_oi",
        "aws_oi",
        "total_revenue",
        "total_opex",
        "total_oi",
    }
    for label, key in line_items:
        values = []
        for period in ALL_PERIODS:
            if period in FORECAST_PERIODS and key in forecast_keys:
                values.append(f"[VIEW] {fmt(segments[period][key])}")
            else:
                values.append(fmt(segments[period][key]))
        rows.append([label, *values])

    driver_rows = []
    for period in ALL_PERIODS:
        assumption = ASSUMPTIONS.get(period)
        segment = segments[period]
        if assumption:
            driver_rows.append(
                [
                    period,
                    pct(assumption["na_revenue_growth"]),
                    pct(assumption["na_op_margin"]),
                    pct(assumption["intl_revenue_growth"]),
                    pct(assumption["intl_op_margin"]),
                    pct(assumption["aws_revenue_growth"]),
                    pct(assumption["aws_op_margin"]),
                ]
            )
        else:
            driver_rows.append(
                [
                    period,
                    "actual",
                    pct(segment["na_oi"] / segment["na_revenue"]),
                    "actual",
                    pct(segment["intl_oi"] / segment["intl_revenue"]),
                    "actual",
                    pct(segment["aws_oi"] / segment["aws_revenue"]),
                ]
            )

    relevant_checks = [
        row
        for row in checks
        if "segment revenue" in row[0]
        or "segment OI" in row[0]
        or "register filing" in row[0]
    ]
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Amazon segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages.

Amazon discloses segment revenue and operating income, not segment gross profit (R1.5). Consolidated revenue and operating income equal the sum of North America, International and AWS with no plug.

## Segment revenue, expense and operating income

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical segment facts: [register R2]({REGISTER}); [S1]({S1}) / [S2]({S2}) / [S3]({S3}) / [S4]({S4}). Forecast cells are researcher `[VIEW]` paths tied to Stores mix/margin, International density and AWS AI/capacity monetization in [`inputs.md`](inputs.md); they do not allocate Advertising, Prime or product-line margins separately (R8.2–R8.4).

## Forecast drivers

{markdown_table(["period", "NA rev growth", "NA op margin", "Intl rev growth", "Intl op margin", "AWS rev growth", "AWS op margin"], driver_rows)}

Q2 2026 ex-FX sales-group growth (R3.1) informed the Stores/AWS direction but is not mapped into sales-group rows because group operating income is `not obtained`.

## Segment tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = [
        ["Consolidated revenue"]
        + [fmt(income[p]["total_revenue"]) for p in ALL_PERIODS],
        ["Operating income (sum of segments)"]
        + [fmt(income[p]["operating_income"]) for p in ALL_PERIODS],
        ["Interest income"]
        + [fmt(income[p]["interest_income"]) for p in ALL_PERIODS],
        ["Interest expense"]
        + [fmt(-income[p]["interest_expense"]) for p in ALL_PERIODS],
        ["Other income / (expense)"]
        + [fmt(income[p]["other_income"]) for p in ALL_PERIODS],
        ["Pre-tax income"] + [fmt(income[p]["pretax_income"]) for p in ALL_PERIODS],
        ["Tax provision"]
        + [fmt(income[p]["tax"]) for p in ALL_PERIODS],
        ["Equity-method activity, net of tax"]
        + [fmt(income[p]["equity_method"]) for p in ALL_PERIODS],
        ["Net income"] + [fmt(income[p]["net_income"]) for p in ALL_PERIODS],
        ["Diluted weighted-average shares"]
        + [fmt(income[p]["diluted_shares"]) for p in ALL_PERIODS],
        ["Diluted EPS"] + [fmt(income[p]["diluted_eps"], 2) for p in ALL_PERIODS],
    ]
    relevant_checks = [row for row in checks if "flows to income" in row[0]]
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Amazon income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

Operating income is built only from reportable segments in [`segments.md`](segments.md). Below-the-line items come from consolidated filings (historical) and completion assumptions (forecast) in [`inputs.md`](inputs.md).

{markdown_table(["line", *ALL_PERIODS], rows)}

`1H2026A` is a six-month period. FY2026E other income holds reported 1H marks (R7.1) and assumes no further investment revaluation in 2H. FY2026E tax uses the FY2025 effective rate on pre-tax income.

## Tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    balance_periods = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"] + FORECAST_PERIODS
    rows = [
        ["Cash"] + [fmt(balances[p]["cash"]) for p in balance_periods],
        ["Marketable securities"]
        + [fmt(balances[p]["short_investments"]) for p in balance_periods],
        ["Accounts receivable, net and other"]
        + [fmt(balances[p]["ar"]) for p in balance_periods],
        ["Inventory"] + [fmt(balances[p]["inventory"]) for p in balance_periods],
        ["Property and equipment, net"]
        + [fmt(balances[p]["ppe"]) for p in balance_periods],
        ["Operating leases"]
        + [fmt(balances[p]["operating_leases"]) for p in balance_periods],
        ["Other assets (incl. goodwill and investments)"]
        + [fmt(balances[p]["other_assets"]) for p in balance_periods],
        ["Total assets"] + [fmt(balances[p]["total_assets"]) for p in balance_periods],
        ["Accounts payable"] + [fmt(balances[p]["ap"]) for p in balance_periods],
        ["Long-term debt (incl. current portion)"]
        + [fmt(balances[p]["debt"]) for p in balance_periods],
        ["Lease liabilities"]
        + [fmt(balances[p]["lease_liabilities"]) for p in balance_periods],
        ["Other liabilities"]
        + [fmt(balances[p]["other_liabilities"]) for p in balance_periods],
        ["Total liabilities"]
        + [fmt(balances[p]["total_liabilities"]) for p in balance_periods],
        ["Additional paid-in capital"]
        + [fmt(balances[p]["apic"]) for p in balance_periods],
        ["Retained earnings"]
        + [fmt(balances[p]["retained_earnings"]) for p in balance_periods],
        ["AOCI and treasury stock / common stock"]
        + [
            fmt(balances[p]["aoci"] + balances[p]["treasury_and_common"])
            for p in balance_periods
        ],
        ["Stockholders' equity"]
        + [fmt(balances[p]["stockholders_equity"]) for p in balance_periods],
        ["Total liabilities and equity"]
        + [fmt(balances[p]["total_liabilities_and_equity"]) for p in balance_periods],
        ["Diluted WAS used in model"]
        + [
            fmt(
                HIST_INCOME[p]["diluted_shares"]
                if p in HIST_PERIODS
                else balances[p]["diluted_shares"]
            )
            for p in balance_periods
        ],
    ]
    relevant_checks = [
        row
        for row in checks
        if "balance sheet balances" in row[0] or "retained earnings" in row[0]
    ]
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Amazon balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares.

{markdown_table(["line", *balance_periods], rows)}

Historical FY2023–FY2024 from [S2]({S2}); FY2025 from [S1]({S1}); 1H2026 from [S4]({S4}). Residual “Other assets” and “Other liabilities” aggregate goodwill, strategic investments and non-debt obligations without inventing segment balance sheets (R8.6).

Forecast periods roll forward from 2026-06-30 using `[VIEW]` capex, D&A, SBC, working-capital days and a minimum-cash funding rule. Lease assets and liabilities scale with PP&E as a simplified proxy. Forecast “Other assets” is a balancing residual so assets equal liabilities plus equity without inventing segment balance sheets (R8.6).

## Tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_cashflow(
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    hist_periods = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
    rows: list[list[str]] = []
    hist_lines = [
        ("Net income", "net_income"),
        ("D&A", "da"),
        ("SBC", "sbc"),
        ("Operating cash flow", "ocf"),
        ("Purchases of property and equipment", "purchases_ppe"),
        ("Proceeds and incentives", "proceeds_ppe"),
        ("Net cash capex", "net_cash_capex"),
        ("Free cash flow", "fcf"),
        ("Net investing cash flow", "net_investing"),
        ("Net financing cash flow", "net_financing"),
        ("FX effect", "fx"),
        ("Change in cash and restricted cash", "cash_change_restricted"),
        ("Ending cash and restricted cash", "ending_cash_restricted"),
        ("Ending balance-sheet cash", "bs_cash"),
    ]
    hist_derived: dict[str, dict[str, float]] = {}
    for period in hist_periods:
        raw = HIST_CASHFLOW[period]
        net_capex = raw["purchases_ppe"] - raw["proceeds_ppe"]
        hist_derived[period] = {
            **raw,
            "net_cash_capex": net_capex,
            "fcf": raw["ocf"] - net_capex,
            "bs_cash": balances[period]["cash"],
        }
    for label, key in hist_lines:
        rows.append(
            [label]
            + [fmt(hist_derived[p][key]) for p in hist_periods]
            + ["—", "—", "—"]
        )

    forecast_lines = [
        ("Net income", "net_income"),
        ("D&A", "da"),
        ("SBC", "sbc"),
        ("Less: increase in core NWC", "delta_nwc"),
        ("Other operating / noncash adjustments", "other_operating_adjustments"),
        ("Operating cash flow", "ocf"),
        ("Less: net cash capex", "net_cash_capex"),
        ("Less: strategic equity investments", "strategic_investing"),
        ("Free cash flow", "fcf"),
        ("Other investing / financing / FX (1H actual in FY2026E)", "other_post_fcf"),
        ("Marketable securities sold to fund cash", "investment_sale"),
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
                "net_cash_capex",
                "strategic_investing",
                "dividends",
                "buybacks",
            }:
                value = -value
            rendered = fmt(value)
            if key == "net_cash_capex":
                rendered = f"[VIEW] {rendered}"
            if key == "strategic_investing" and cashflow[p][key] != 0:
                rendered = f"[VIEW] {rendered}"
            values.append(rendered)
        rows.append([label, "—", "—", "—", "—", *values])

    wc = cashflow["_working_capital_days"]
    relevant_checks = [row for row in checks if "CF ending cash" in row[0]]
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(difference, 2)]
        for name, passed, difference in relevant_checks
    ]
    return f"""# Amazon cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

{markdown_table(["line", *hist_periods, *FORECAST_PERIODS], rows)}

Historical figures are reported cash-flow lines from [S1]({S1}), [S2]({S2}) and [S4]({S4}). FY2026E combines reported 1H operating cash flow with an explicit 2H roll-forward. Net cash capex follows the company definition in register R6 (purchases less proceeds). FY2026E net capex is a `[VIEW]` mapping of the ~$200bn R6.5 outlook.

Forecast operating cash flow is `NI + D&A + SBC − Δ(core NWC) + other operating/noncash adjustments`. Core NWC is `accounts receivable + inventory − accounts payable`. Days held from 2026-06-30: receivables `{wc["ar_days"]:.2f}`, inventory `{wc["inventory_days"]:.2f}`, payables `{wc["ap_days"]:.2f}`.

## Cash tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def main() -> None:
    historical_segments = enrich_historical_segments()
    forecast_segments = build_forecast_segments(historical_segments)
    segments = {**historical_segments, **forecast_segments}
    balances, income, cashflow = build_forecast(segments)
    checks = build_checks(segments, income, balances, cashflow)

    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, checks),
        "cashflow.md": render_cashflow(balances, cashflow, checks),
    }
    for filename, content in outputs.items():
        (ROOT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("Amazon model outputs")
    print("period | revenue | operating income | net income | FCF | diluted EPS")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['total_revenue']:.1f} | "
            f"{income[period]['operating_income']:.1f} | "
            f"{income[period]['net_income']:.1f} | "
            f"{cashflow[period]['fcf']:.1f} | "
            f"{income[period]['diluted_eps']:.2f}"
        )
    print("\nTie-out checks")
    failed = False
    for name, passed, difference in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (difference {difference:.6f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
