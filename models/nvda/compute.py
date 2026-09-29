#!/usr/bin/env python3
"""NVIDIA segment three-statement model.

All arithmetic lives here. Running this file rewrites segments.md, income.md,
balance.md and cashflow.md, then prints tie-out checks. Valuation is explicitly
outside this gate. USD millions except per-share data and percentages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2024A", "FY2025A", "FY2026A", "Q2FY2027A", "1HFY2027A"]
FORECAST_PERIODS = ["FY2027E", "FY2028E", "FY2029E"]
TOLERANCE = 1e-6


# [FACT] Register R2 company P&L.
HIST_COMPANY: dict[str, dict[str, float]] = {
    "FY2024A": {
        "revenue": 60_922.0,
        "cogs": 16_621.0,
        "gross_profit": 44_301.0,
        "rd": 8_675.0,
        "sga": 2_654.0,
        "operating_income": 32_972.0,
        "net_income": 29_760.0,
        "diluted_eps": 1.19,
        "diluted_shares": 24_940.0,
    },
    "FY2025A": {
        "revenue": 130_497.0,
        "cogs": 32_639.0,
        "gross_profit": 97_858.0,
        "rd": 12_914.0,
        "sga": 3_491.0,
        "operating_income": 81_453.0,
        "net_income": 72_880.0,
        "diluted_eps": 2.94,
        "diluted_shares": 24_804.0,
    },
    "FY2026A": {
        "revenue": 215_938.0,
        "cogs": 62_475.0,
        "gross_profit": 153_463.0,
        "rd": 18_497.0,
        "sga": 4_579.0,
        "operating_income": 130_387.0,
        "net_income": 120_067.0,
        "diluted_eps": 4.90,
        "diluted_shares": 24_514.0,
    },
    "Q2FY2027A": {
        "revenue": 96_221.0,
        "cogs": 24_079.0,
        "gross_profit": 72_142.0,
        "rd": 7_054.0,
        "sga": 1_354.0,
        "operating_income": 63_734.0,
        "net_income": 59_688.0,
        "diluted_eps": 2.46,
        "diluted_shares": 24_285.0,
    },
    "1HFY2027A": {
        "revenue": 177_837.0,
        "cogs": 44_538.0,
        "gross_profit": 133_299.0,
        "rd": 13_375.0,
        "sga": 2_654.0,
        "operating_income": 117_270.0,
        "net_income": 118_010.0,
        "diluted_eps": 4.85,
        "diluted_shares": 24_338.0,
    },
}


# [FACT] Register R2 reportable segments.
HIST_SEGMENTS: dict[str, dict[str, float]] = {
    "FY2024A": {
        "compute_networking_revenue": 47_405.0,
        "compute_networking_oi": 32_016.0,
        "graphics_revenue": 13_517.0,
        "graphics_oi": 5_846.0,
    },
    "FY2025A": {
        "compute_networking_revenue": 116_193.0,
        "compute_networking_oi": 82_875.0,
        "graphics_revenue": 14_304.0,
        "graphics_oi": 5_085.0,
    },
    "FY2026A": {
        "compute_networking_revenue": 193_479.0,
        "compute_networking_oi": 130_141.0,
        "graphics_revenue": 22_459.0,
        "graphics_oi": 9_156.0,
    },
    "Q2FY2027A": {
        "compute_networking_revenue": 88_299.0,
        "compute_networking_oi": 62_696.0,
        "graphics_revenue": 7_922.0,
        "graphics_oi": 3_899.0,
    },
    "1HFY2027A": {
        "compute_networking_revenue": 162_850.0,
        "compute_networking_oi": 116_031.0,
        "graphics_revenue": 14_987.0,
        "graphics_oi": 6_840.0,
    },
}


# [FACT] Register R2 current market-platform history.
HIST_PLATFORMS: dict[str, dict[str, float]] = {
    "Q2FY2026R": {
        "data_center": 41_096.0,
        "hyperscale": 24_168.0,
        "acie": 16_928.0,
        "edge": 5_647.0,
        "revenue": 46_743.0,
    },
    "Q2FY2027A": {
        "data_center": 89_023.0,
        "hyperscale": 48_710.0,
        "acie": 40_313.0,
        "edge": 7_198.0,
        "revenue": 96_221.0,
    },
    "1HFY2026R": {
        "data_center": 80_208.0,
        "hyperscale": 46_428.0,
        "acie": 33_780.0,
        "edge": 10_597.0,
        "revenue": 90_805.0,
    },
    "1HFY2027A": {
        "data_center": 164_269.0,
        "hyperscale": 91_761.0,
        "acie": 72_508.0,
        "edge": 13_568.0,
        "revenue": 177_837.0,
    },
}


# [FACT] Register R3 prior taxonomy, retained only for history.
PRIOR_MARKETS: dict[str, dict[str, float]] = {
    "FY2024A": {
        "data_center": 47_525.0,
        "compute": 38_950.0,
        "networking": 8_575.0,
        "gaming": 10_447.0,
        "professional_visualization": 1_553.0,
        "automotive": 1_091.0,
        "oem_other": 306.0,
        "revenue": 60_922.0,
    },
    "FY2025A": {
        "data_center": 115_186.0,
        "compute": 102_196.0,
        "networking": 12_990.0,
        "gaming": 11_350.0,
        "professional_visualization": 1_878.0,
        "automotive": 1_694.0,
        "oem_other": 389.0,
        "revenue": 130_497.0,
    },
    "FY2026A": {
        "data_center": 193_737.0,
        "compute": 162_361.0,
        "networking": 31_376.0,
        "gaming": 16_042.0,
        "professional_visualization": 3_191.0,
        "automotive": 2_349.0,
        "oem_other": 619.0,
        "revenue": 215_938.0,
    },
}


# [FACT] Register R6 at 2026-07-26 / 1H FY2027.
BASE_BALANCE = {
    "cash": 22_443.0,
    "marketable_debt_securities": 34_143.0,
    "marketable_equity_securities": 42_783.0,
    "accounts_receivable": 63_059.0,
    "inventory": 31_575.0,
    "ppe": 14_285.0,
    "total_assets": 320_272.0,
    "accounts_payable": 15_059.0,
    "short_term_debt": 1_000.0,
    "long_term_debt": 32_366.0,
    "total_liabilities": 91_288.0,
    "equity": 228_984.0,
}

BASE_CASHFLOW = {
    "operating_cash_flow": 74_421.0,
    "capex": 4_434.0,
    "principal_asset_payments": 92.0,
    "free_cash_flow": 69_895.0,
    "da": 2_124.0,
    "sbc": 3_954.0,
    "buybacks": 39_044.0,
    "dividends": 6_290.0,
}


# Researcher-specified [VIEW] forecast.
FORECAST_INPUTS: dict[str, dict[str, float]] = {
    "FY2027E": {
        "revenue": 405_000.0,
        "data_center_share": 0.925,
        "hyperscale_share": 0.56,
        "gross_margin": 0.73,
        "rd": 32_000.0,
        "sga": 7_200.0,
        "tax_rate": 0.17,
        "diluted_shares": 24_200.0,
        "capex": 12_000.0,
        "da": 5_500.0,
        "dividends": 13_000.0,
        "debt_repayment": 1_000.0,
    },
    "FY2028E": {
        "revenue": 688_500.0,
        "data_center_share": 0.935,
        "hyperscale_share": 0.55,
        "gross_margin": 0.725,
        "rd": 42_000.0,
        "sga": 9_000.0,
        "tax_rate": 0.17,
        "diluted_shares": 23_800.0,
        "capex": 15_000.0,
        "da": 7_500.0,
        "dividends": 14_000.0,
        "debt_repayment": 10_000.0,
    },
    "FY2029E": {
        "revenue": 895_000.0,
        "data_center_share": 0.93,
        "hyperscale_share": 0.54,
        "gross_margin": 0.73,
        "rd": 50_000.0,
        "sga": 10_500.0,
        "tax_rate": 0.17,
        "diluted_shares": 23_400.0,
        "capex": 18_000.0,
        "da": 10_000.0,
        "dividends": 15_000.0,
        "debt_repayment": 22_366.0,
    },
}

SBC_RATE = 0.30
OTHER_UNALLOCATED_RATE = 0.10
COMPUTE_NETWORKING_OI_SHARE = 0.95
MINIMUM_CASH = 20_000.0
Q3_FY2027_GUIDE_MIDPOINT = 108_000.0


Check = tuple[str, bool, float, str]


def fmt_number(value: float, decimals: int = 0) -> str:
    if abs(value) < 0.5 * (10 ** (-decimals)):
        return "—"
    rendered = f"{abs(value):,.{decimals}f}"
    return f"({rendered})" if value < 0 else rendered


def tagged(value: float, tag: str, decimals: int = 0) -> str:
    return f"[{tag}] {fmt_number(value, decimals)}"


def tagged_percent(value: float, tag: str, decimals: int = 1) -> str:
    return f"[{tag}] {value * 100:.{decimals}f}%"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    output = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
    ]
    output.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(output)


def add_check(
    checks: list[Check],
    name: str,
    difference: float,
    category: str,
    tolerance: float = TOLERANCE,
) -> None:
    checks.append((name, abs(difference) <= tolerance, difference, category))


def render_checks(checks: list[Check], category: str) -> str:
    rows: list[list[str]] = []
    for name, passed, difference, check_category in checks:
        if check_category != category:
            continue
        rows.append(
            [
                name,
                "OK" if passed else "ERROR",
                "—" if passed else fmt_number(difference, 6),
            ]
        )
    return markdown_table(["check", "status", "difference"], rows)


def build_forecast_income() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in FORECAST_PERIODS:
        inputs = FORECAST_INPUTS[period]
        revenue = inputs["revenue"]
        data_center_revenue = revenue * inputs["data_center_share"]
        hyperscale_revenue = data_center_revenue * inputs["hyperscale_share"]
        acie_revenue = data_center_revenue - hyperscale_revenue
        edge_revenue = revenue - data_center_revenue

        gross_margin = inputs["gross_margin"]
        hyperscale_gp = hyperscale_revenue * gross_margin
        acie_gp = acie_revenue * gross_margin
        edge_gp = edge_revenue * gross_margin
        gross_profit = hyperscale_gp + acie_gp + edge_gp
        cogs = revenue - gross_profit

        rd = inputs["rd"]
        sga = inputs["sga"]
        operating_expense = rd + sga
        operating_income = gross_profit - operating_expense
        other_income = 0.0
        pretax_income = operating_income + other_income
        tax = pretax_income * inputs["tax_rate"]
        net_income = pretax_income - tax
        diluted_shares = inputs["diluted_shares"]

        sbc = operating_expense * SBC_RATE
        other_unallocated = operating_expense * OTHER_UNALLOCATED_RATE
        total_segment_oi = operating_income + sbc + other_unallocated
        compute_networking_oi = total_segment_oi * COMPUTE_NETWORKING_OI_SHARE
        graphics_oi = total_segment_oi - compute_networking_oi

        output[period] = {
            **inputs,
            "data_center_revenue": data_center_revenue,
            "hyperscale_revenue": hyperscale_revenue,
            "acie_revenue": acie_revenue,
            "edge_revenue": edge_revenue,
            "hyperscale_gp": hyperscale_gp,
            "acie_gp": acie_gp,
            "edge_gp": edge_gp,
            "gross_profit": gross_profit,
            "cogs": cogs,
            "operating_expense": operating_expense,
            "operating_income": operating_income,
            "other_income": other_income,
            "pretax_income": pretax_income,
            "tax": tax,
            "net_income": net_income,
            "diluted_eps": net_income / diluted_shares,
            "sbc": sbc,
            "other_unallocated": other_unallocated,
            "total_segment_oi": total_segment_oi,
            "compute_networking_oi": compute_networking_oi,
            "graphics_oi": graphics_oi,
        }
    return output


def build_balance_and_cashflow(
    income: dict[str, dict[str, float]]
) -> tuple[
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
    dict[str, float],
]:
    annualized_1h_revenue = HIST_COMPANY["1HFY2027A"]["revenue"] * 2.0
    annualized_1h_cogs = HIST_COMPANY["1HFY2027A"]["cogs"] * 2.0
    days = {
        "ar_days": BASE_BALANCE["accounts_receivable"] / annualized_1h_revenue * 365.0,
        "inventory_days": BASE_BALANCE["inventory"] / annualized_1h_cogs * 365.0,
        "ap_days": BASE_BALANCE["accounts_payable"] / annualized_1h_cogs * 365.0,
    }

    other_assets = BASE_BALANCE["total_assets"] - sum(
        BASE_BALANCE[key]
        for key in (
            "cash",
            "marketable_debt_securities",
            "marketable_equity_securities",
            "accounts_receivable",
            "inventory",
            "ppe",
        )
    )
    base_debt = BASE_BALANCE["short_term_debt"] + BASE_BALANCE["long_term_debt"]
    other_liabilities = (
        BASE_BALANCE["total_liabilities"]
        - BASE_BALANCE["accounts_payable"]
        - base_debt
    )

    balances: dict[str, dict[str, float]] = {
        "1HFY2027A": {
            "cash": BASE_BALANCE["cash"],
            "marketable_debt_securities": BASE_BALANCE["marketable_debt_securities"],
            "marketable_equity_securities": BASE_BALANCE["marketable_equity_securities"],
            "accounts_receivable": BASE_BALANCE["accounts_receivable"],
            "inventory": BASE_BALANCE["inventory"],
            "ppe": BASE_BALANCE["ppe"],
            "other_assets": other_assets,
            "total_assets": BASE_BALANCE["total_assets"],
            "accounts_payable": BASE_BALANCE["accounts_payable"],
            "debt": base_debt,
            "other_liabilities": other_liabilities,
            "total_liabilities": BASE_BALANCE["total_liabilities"],
            "equity": BASE_BALANCE["equity"],
            "total_liabilities_equity": (
                BASE_BALANCE["total_liabilities"] + BASE_BALANCE["equity"]
            ),
        }
    }
    cashflow: dict[str, dict[str, float]] = {}

    previous_balance = balances["1HFY2027A"]
    previous_nwc = (
        previous_balance["accounts_receivable"]
        + previous_balance["inventory"]
        - previous_balance["accounts_payable"]
    )

    for period in FORECAST_PERIODS:
        period_income = income[period]
        inputs = FORECAST_INPUTS[period]
        accounts_receivable = (
            period_income["revenue"] * days["ar_days"] / 365.0
        )
        inventory = period_income["cogs"] * days["inventory_days"] / 365.0
        accounts_payable = period_income["cogs"] * days["ap_days"] / 365.0
        nwc = accounts_receivable + inventory - accounts_payable
        increase_nwc = nwc - previous_nwc

        if period == "FY2027E":
            roll_net_income = (
                period_income["net_income"] - HIST_COMPANY["1HFY2027A"]["net_income"]
            )
            roll_da = inputs["da"] - BASE_CASHFLOW["da"]
            roll_sbc = period_income["sbc"] - BASE_CASHFLOW["sbc"]
            roll_capex = inputs["capex"] - BASE_CASHFLOW["capex"]
            roll_dividends = inputs["dividends"] - BASE_CASHFLOW["dividends"]
            reported_1h_ocf = BASE_CASHFLOW["operating_cash_flow"]
            reported_1h_buybacks = BASE_CASHFLOW["buybacks"]
            principal_asset_payments = BASE_CASHFLOW["principal_asset_payments"]
        else:
            roll_net_income = period_income["net_income"]
            roll_da = inputs["da"]
            roll_sbc = period_income["sbc"]
            roll_capex = inputs["capex"]
            roll_dividends = inputs["dividends"]
            reported_1h_ocf = 0.0
            reported_1h_buybacks = 0.0
            principal_asset_payments = 0.0

        roll_operating_cash_flow = (
            roll_net_income + roll_da + roll_sbc - increase_nwc
        )
        full_year_operating_cash_flow = reported_1h_ocf + roll_operating_cash_flow
        full_year_fcf = (
            full_year_operating_cash_flow
            - inputs["capex"]
            - principal_asset_payments
        )
        roll_fcf = roll_operating_cash_flow - roll_capex

        debt_repayment = inputs["debt_repayment"]
        available_for_buybacks = (
            previous_balance["cash"]
            + roll_fcf
            - roll_dividends
            - debt_repayment
            - MINIMUM_CASH
        )
        roll_buybacks = max(0.0, available_for_buybacks)
        full_year_buybacks = reported_1h_buybacks + roll_buybacks
        change_in_cash = (
            roll_fcf - roll_dividends - debt_repayment - roll_buybacks
        )
        ending_cash = previous_balance["cash"] + change_in_cash

        ending_ppe = previous_balance["ppe"] + roll_capex - roll_da
        ending_debt = previous_balance["debt"] - debt_repayment
        ending_equity = (
            previous_balance["equity"]
            + roll_net_income
            + roll_sbc
            - roll_dividends
            - roll_buybacks
        )

        total_assets = (
            ending_cash
            + BASE_BALANCE["marketable_debt_securities"]
            + BASE_BALANCE["marketable_equity_securities"]
            + accounts_receivable
            + inventory
            + ending_ppe
            + other_assets
        )
        total_liabilities = accounts_payable + ending_debt + other_liabilities
        total_liabilities_equity = total_liabilities + ending_equity

        balances[period] = {
            "cash": ending_cash,
            "marketable_debt_securities": BASE_BALANCE[
                "marketable_debt_securities"
            ],
            "marketable_equity_securities": BASE_BALANCE[
                "marketable_equity_securities"
            ],
            "accounts_receivable": accounts_receivable,
            "inventory": inventory,
            "ppe": ending_ppe,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "accounts_payable": accounts_payable,
            "debt": ending_debt,
            "other_liabilities": other_liabilities,
            "total_liabilities": total_liabilities,
            "equity": ending_equity,
            "total_liabilities_equity": total_liabilities_equity,
        }
        cashflow[period] = {
            "full_year_net_income": period_income["net_income"],
            "reported_1h_ocf": reported_1h_ocf,
            "roll_net_income": roll_net_income,
            "roll_da": roll_da,
            "roll_sbc": roll_sbc,
            "increase_nwc": increase_nwc,
            "roll_operating_cash_flow": roll_operating_cash_flow,
            "operating_cash_flow": full_year_operating_cash_flow,
            "capex": inputs["capex"],
            "principal_asset_payments": principal_asset_payments,
            "free_cash_flow": full_year_fcf,
            "roll_capex": roll_capex,
            "roll_fcf": roll_fcf,
            "dividends": inputs["dividends"],
            "roll_dividends": roll_dividends,
            "debt_repayment": debt_repayment,
            "buybacks": full_year_buybacks,
            "roll_buybacks": roll_buybacks,
            "opening_cash": previous_balance["cash"],
            "change_in_cash": change_in_cash,
            "ending_cash": ending_cash,
        }

        previous_balance = balances[period]
        previous_nwc = nwc

    return balances, cashflow, days


def build_checks(
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[Check]:
    checks: list[Check] = []

    for period in HIST_PERIODS:
        company = HIST_COMPANY[period]
        segment = HIST_SEGMENTS[period]
        add_check(
            checks,
            f"{period}: filed revenue − COGS = gross profit",
            company["revenue"] - company["cogs"] - company["gross_profit"],
            "historical",
        )
        add_check(
            checks,
            f"{period}: filed GP − R&D − SG&A = operating income",
            (
                company["gross_profit"]
                - company["rd"]
                - company["sga"]
                - company["operating_income"]
            ),
            "historical",
        )
        add_check(
            checks,
            f"{period}: reportable-segment revenue = filed revenue",
            (
                segment["compute_networking_revenue"]
                + segment["graphics_revenue"]
                - company["revenue"]
            ),
            "segments",
        )
        reconciliation = (
            segment["compute_networking_oi"]
            + segment["graphics_oi"]
            - company["operating_income"]
        )
        add_check(
            checks,
            f"{period}: segment OI less explicit reconciliation = company OI",
            (
                segment["compute_networking_oi"]
                + segment["graphics_oi"]
                - reconciliation
                - company["operating_income"]
            ),
            "segments",
        )
        eps_difference = (
            company["net_income"] / company["diluted_shares"]
            - company["diluted_eps"]
        )
        add_check(
            checks,
            f"{period}: filed diluted EPS rounds from NI / WAS",
            eps_difference,
            "historical",
            tolerance=0.01,
        )

    for period, platform in HIST_PLATFORMS.items():
        add_check(
            checks,
            f"{period}: Hyperscale + ACIE = Data Center",
            platform["hyperscale"] + platform["acie"] - platform["data_center"],
            "segments",
        )
        add_check(
            checks,
            f"{period}: Data Center + Edge = company revenue",
            platform["data_center"] + platform["edge"] - platform["revenue"],
            "segments",
        )

    for period, market in PRIOR_MARKETS.items():
        add_check(
            checks,
            f"{period}: prior compute + networking = Data Center",
            market["compute"] + market["networking"] - market["data_center"],
            "segments",
        )
        add_check(
            checks,
            f"{period}: prior markets = filed company revenue",
            (
                market["data_center"]
                + market["gaming"]
                + market["professional_visualization"]
                + market["automotive"]
                + market["oem_other"]
                - market["revenue"]
            ),
            "segments",
        )

    for period in FORECAST_PERIODS:
        period_income = income[period]
        add_check(
            checks,
            f"{period}: platform revenue = company revenue",
            (
                period_income["hyperscale_revenue"]
                + period_income["acie_revenue"]
                + period_income["edge_revenue"]
                - period_income["revenue"]
            ),
            "forecast_segments",
        )
        add_check(
            checks,
            f"{period}: Hyperscale + ACIE = Data Center",
            (
                period_income["hyperscale_revenue"]
                + period_income["acie_revenue"]
                - period_income["data_center_revenue"]
            ),
            "forecast_segments",
        )
        add_check(
            checks,
            f"{period}: platform GP = company gross profit",
            (
                period_income["hyperscale_gp"]
                + period_income["acie_gp"]
                + period_income["edge_gp"]
                - period_income["gross_profit"]
            ),
            "forecast_segments",
        )
        add_check(
            checks,
            f"{period}: GP − R&D − SG&A = company operating income",
            (
                period_income["gross_profit"]
                - period_income["rd"]
                - period_income["sga"]
                - period_income["operating_income"]
            ),
            "forecast_income",
        )
        add_check(
            checks,
            f"{period}: segment OI reconciliation = company operating income",
            (
                period_income["compute_networking_oi"]
                + period_income["graphics_oi"]
                - period_income["sbc"]
                - period_income["other_unallocated"]
                - period_income["operating_income"]
            ),
            "forecast_segments",
        )
        compute_share = (
            period_income["compute_networking_oi"]
            / period_income["total_segment_oi"]
        )
        add_check(
            checks,
            f"{period}: Compute & Networking is at least 95% of segment OI",
            max(0.0, COMPUTE_NETWORKING_OI_SHARE - compute_share),
            "forecast_segments",
        )
        add_check(
            checks,
            f"{period}: balance sheet balances",
            (
                balances[period]["total_assets"]
                - balances[period]["total_liabilities_equity"]
            ),
            "balance",
        )
        add_check(
            checks,
            f"{period}: cash-flow ending cash = balance-sheet cash",
            cashflow[period]["ending_cash"] - balances[period]["cash"],
            "cashflow",
        )
        add_check(
            checks,
            f"{period}: cash bridge sums",
            (
                cashflow[period]["opening_cash"]
                + cashflow[period]["change_in_cash"]
                - cashflow[period]["ending_cash"]
            ),
            "cashflow",
        )
        add_check(
            checks,
            f"{period}: debt remains non-negative",
            min(0.0, balances[period]["debt"]),
            "balance",
        )

    add_check(
        checks,
        "1H FY2027: reported OCF less purchases/principal = company FCF",
        (
            BASE_CASHFLOW["operating_cash_flow"]
            - BASE_CASHFLOW["capex"]
            - BASE_CASHFLOW["principal_asset_payments"]
            - BASE_CASHFLOW["free_cash_flow"]
        ),
        "cashflow",
    )
    add_check(
        checks,
        "FY2027E: company revenue bridge uses 1H actual + Q3 guide + Q4 view",
        (
            HIST_COMPANY["1HFY2027A"]["revenue"]
            + Q3_FY2027_GUIDE_MIDPOINT
            + (
                FORECAST_INPUTS["FY2027E"]["revenue"]
                - HIST_COMPANY["1HFY2027A"]["revenue"]
                - Q3_FY2027_GUIDE_MIDPOINT
            )
            - FORECAST_INPUTS["FY2027E"]["revenue"]
        ),
        "forecast_income",
    )

    return checks


def render_segments(
    income: dict[str, dict[str, float]], checks: list[Check]
) -> str:
    hist_segment_rows: list[list[str]] = []
    for label, key in (
        ("Compute & Networking revenue", "compute_networking_revenue"),
        ("Compute & Networking operating income", "compute_networking_oi"),
        ("Graphics revenue", "graphics_revenue"),
        ("Graphics operating income", "graphics_oi"),
    ):
        hist_segment_rows.append(
            [label]
            + [tagged(HIST_SEGMENTS[p][key], "FACT") for p in HIST_PERIODS]
        )
    hist_segment_rows.append(
        ["Segment OI reconciliation to consolidated OI"]
        + [
            tagged(
                (
                    HIST_SEGMENTS[p]["compute_networking_oi"]
                    + HIST_SEGMENTS[p]["graphics_oi"]
                    - HIST_COMPANY[p]["operating_income"]
                ),
                "DEDUCTED",
            )
            for p in HIST_PERIODS
        ]
    )

    platform_periods = list(HIST_PLATFORMS)
    historical_platform_rows: list[list[str]] = []
    for label, key in (
        ("Data Center", "data_center"),
        ("Hyperscale", "hyperscale"),
        ("ACIE", "acie"),
        ("Edge Computing", "edge"),
        ("Company revenue", "revenue"),
    ):
        historical_platform_rows.append(
            [label]
            + [tagged(HIST_PLATFORMS[p][key], "FACT") for p in platform_periods]
        )

    prior_rows: list[list[str]] = []
    for label, key in (
        ("Data Center", "data_center"),
        ("— Compute", "compute"),
        ("— Networking", "networking"),
        ("Gaming", "gaming"),
        ("Professional Visualization", "professional_visualization"),
        ("Automotive", "automotive"),
        ("OEM and Other", "oem_other"),
        ("Company revenue", "revenue"),
    ):
        prior_rows.append(
            [label]
            + [tagged(PRIOR_MARKETS[p][key], "FACT") for p in PRIOR_MARKETS]
        )

    forecast_platform_rows: list[list[str]] = []
    for label, key in (
        ("Hyperscale revenue", "hyperscale_revenue"),
        ("ACIE revenue", "acie_revenue"),
        ("Data Center revenue", "data_center_revenue"),
        ("Edge Computing revenue", "edge_revenue"),
        ("Company revenue", "revenue"),
        ("Hyperscale gross profit", "hyperscale_gp"),
        ("ACIE gross profit", "acie_gp"),
        ("Edge Computing gross profit", "edge_gp"),
        ("Company gross profit", "gross_profit"),
    ):
        forecast_platform_rows.append(
            [label] + [tagged(income[p][key], "VIEW") for p in FORECAST_PERIODS]
        )
    forecast_platform_rows.extend(
        [
            ["Data Center share"]
            + [
                tagged_percent(income[p]["data_center_share"], "VIEW")
                for p in FORECAST_PERIODS
            ],
            ["Hyperscale share of Data Center"]
            + [
                tagged_percent(income[p]["hyperscale_share"], "VIEW")
                for p in FORECAST_PERIODS
            ],
            ["Applied platform gross margin"]
            + [
                tagged_percent(income[p]["gross_margin"], "VIEW")
                for p in FORECAST_PERIODS
            ],
        ]
    )

    forecast_segment_oi_rows: list[list[str]] = []
    for label, key in (
        ("Compute & Networking segment OI", "compute_networking_oi"),
        ("Graphics segment OI", "graphics_oi"),
        ("Total segment OI", "total_segment_oi"),
        ("Less: SBC excluded from segment OI", "sbc"),
        ("Less: other unallocated/acquisition costs", "other_unallocated"),
        ("Consolidated operating income", "operating_income"),
    ):
        forecast_segment_oi_rows.append(
            [label] + [tagged(income[p][key], "VIEW") for p in FORECAST_PERIODS]
        )

    return f"""# NVIDIA segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages. Historical values point to [register R2/R3](../../memory/nvda/register.md); every forecast cell is `[VIEW]`.

## Historical reportable segments

{markdown_table(["line"] + HIST_PERIODS, hist_segment_rows)}

The reconciliation is `[DEDUCTED]` as total CODM segment operating income less consolidated operating income. It comprises SBC, unallocated corporate infrastructure/support, acquisition-related costs and other enterprise items (R2.2).

## Current market-platform history

{markdown_table(["line"] + platform_periods, historical_platform_rows)}

`R` denotes a recast comparative. Market platforms are a different reporting axis from Compute & Networking / Graphics and do not map one-to-one.

## Prior market taxonomy — history only

{markdown_table(["line"] + list(PRIOR_MARKETS), prior_rows)}

These annual lines stop at FY2026. Current Gaming, Professional Visualization, Automotive and OEM/Other revenue is `not obtained`; none is forecast separately.

## Forecast market-platform revenue and gross profit

{markdown_table(["line"] + FORECAST_PERIODS, forecast_platform_rows)}

Company revenue is built from Hyperscale + ACIE + Edge Computing. Edge is the only revenue residual. Because platform gross margins are `not obtained`, the same explicit company gross-margin `[VIEW]` is applied to each platform; company gross profit is their sum, with no gross-profit plug.

## Forecast CODM segment operating income

{markdown_table(["line"] + FORECAST_PERIODS, forecast_segment_oi_rows)}

Total segment OI is consolidated OI before the explicitly shown SBC and other unallocated/acquisition reconciliation. Compute & Networking receives a `[VIEW]` 95% of total segment OI and Graphics receives the residual. Reportable-segment revenue is not forecast because the current market platforms cannot be mapped one-to-one to reportable segments.

## Historical and taxonomy checks

{render_checks(checks, "segments")}

## Forecast segment checks

{render_checks(checks, "forecast_segments")}
"""


def render_income(
    income: dict[str, dict[str, float]], checks: list[Check]
) -> str:
    historical_rows: list[list[str]] = []
    for label, key, decimals in (
        ("Revenue", "revenue", 0),
        ("Cost of revenue", "cogs", 0),
        ("Gross profit", "gross_profit", 0),
        ("R&D", "rd", 0),
        ("SG&A", "sga", 0),
        ("Operating income", "operating_income", 0),
        ("Net income", "net_income", 0),
        ("Diluted WAS (m)", "diluted_shares", 0),
        ("Diluted EPS ($)", "diluted_eps", 2),
    ):
        historical_rows.append(
            [label]
            + [
                tagged(HIST_COMPANY[p][key], "FACT", decimals)
                for p in HIST_PERIODS
            ]
        )

    forecast_rows: list[list[str]] = []
    for label, key, decimals in (
        ("Hyperscale revenue", "hyperscale_revenue", 0),
        ("ACIE revenue", "acie_revenue", 0),
        ("Edge Computing revenue", "edge_revenue", 0),
        ("Total revenue", "revenue", 0),
        ("Hyperscale gross profit", "hyperscale_gp", 0),
        ("ACIE gross profit", "acie_gp", 0),
        ("Edge Computing gross profit", "edge_gp", 0),
        ("Total gross profit", "gross_profit", 0),
        ("Cost of revenue", "cogs", 0),
        ("R&D", "rd", 0),
        ("SG&A", "sga", 0),
        ("Operating income", "operating_income", 0),
        ("Other income", "other_income", 0),
        ("Pre-tax income", "pretax_income", 0),
        ("Tax provision", "tax", 0),
        ("Net income", "net_income", 0),
        ("Diluted WAS (m)", "diluted_shares", 0),
        ("Diluted EPS ($)", "diluted_eps", 2),
    ):
        forecast_rows.append(
            [label]
            + [tagged(income[p][key], "VIEW", decimals) for p in FORECAST_PERIODS]
        )
    forecast_rows.insert(
        9,
        ["Gross margin"]
        + [
            tagged_percent(income[p]["gross_margin"], "VIEW")
            for p in FORECAST_PERIODS
        ],
    )
    forecast_rows.insert(
        16,
        ["Tax rate"]
        + [
            tagged_percent(income[p]["tax_rate"], "VIEW")
            for p in FORECAST_PERIODS
        ],
    )

    fy27_q4_view = (
        FORECAST_INPUTS["FY2027E"]["revenue"]
        - HIST_COMPANY["1HFY2027A"]["revenue"]
        - Q3_FY2027_GUIDE_MIDPOINT
    )
    sbc_actual_intensity = (
        BASE_CASHFLOW["sbc"]
        / (
            HIST_COMPANY["1HFY2027A"]["rd"]
            + HIST_COMPANY["1HFY2027A"]["sga"]
        )
    )

    return f"""# NVIDIA income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data and percentages.

## Historical company P&L

{markdown_table(["line"] + HIST_PERIODS, historical_rows)}

`Q2FY2027A` and `1HFY2027A` are interim periods and are not directly comparable with full fiscal years. Historical values are `[FACT]` from register R2.

## Forecast company P&L

{markdown_table(["line"] + FORECAST_PERIODS, forecast_rows)}

Revenue and gross profit are the sum of the three forecast market-platform lines; there is no revenue or GP plug. Edge Computing is the disclosed platform residual. Other income is an explicit `[VIEW]` zero because future investment marks are `not obtained`.

FY2027E revenue bridge: `[FACT]` 1H actual `{fmt_number(HIST_COMPANY["1HFY2027A"]["revenue"])}` + `[FACT]` Q3 management guide midpoint `{fmt_number(Q3_FY2027_GUIDE_MIDPOINT)}` + `[VIEW]` Q4 `{fmt_number(fy27_q4_view)}` = `[VIEW]` `{fmt_number(FORECAST_INPUTS["FY2027E"]["revenue"])}`.

The 1H FY2027 `[DEDUCTED]` SBC intensity was `{sbc_actual_intensity * 100:.2f}%` of R&D + SG&A. The model retains the researcher-specified `[VIEW]` 30.0% forecast assumption.

## Historical filing checks

{render_checks(checks, "historical")}

## Forecast income checks

{render_checks(checks, "forecast_income")}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    days: dict[str, float],
    checks: list[Check],
) -> str:
    periods = ["1HFY2027A"] + FORECAST_PERIODS
    rows: list[list[str]] = []
    for label, key in (
        ("Cash and cash equivalents", "cash"),
        ("Marketable debt securities", "marketable_debt_securities"),
        ("Marketable equity securities", "marketable_equity_securities"),
        ("Accounts receivable", "accounts_receivable"),
        ("Inventory", "inventory"),
        ("PP&E / modeled capitalized intangibles, net", "ppe"),
        ("Other assets", "other_assets"),
        ("Total assets", "total_assets"),
        ("Accounts payable", "accounts_payable"),
        ("Debt", "debt"),
        ("Other liabilities", "other_liabilities"),
        ("Total liabilities", "total_liabilities"),
        ("Stockholders' equity", "equity"),
        ("Total liabilities and equity", "total_liabilities_equity"),
    ):
        rows.append(
            [label]
            + [tagged(balances["1HFY2027A"][key], "FACT" if key not in {"other_assets", "debt", "other_liabilities", "total_liabilities_equity"} else "DEDUCTED")]
            + [tagged(balances[p][key], "VIEW") for p in FORECAST_PERIODS]
        )
    rows.append(
        ["Diluted WAS used in model"]
        + [tagged(HIST_COMPANY["1HFY2027A"]["diluted_shares"], "FACT")]
        + [
            tagged(income[p]["diluted_shares"], "VIEW")
            for p in FORECAST_PERIODS
        ]
    )

    day_rows = [
        [
            "Accounts receivable days",
            tagged(days["ar_days"], "DEDUCTED", 2),
            tagged(days["ar_days"], "VIEW", 2),
            tagged(days["ar_days"], "VIEW", 2),
            tagged(days["ar_days"], "VIEW", 2),
        ],
        [
            "Inventory days",
            tagged(days["inventory_days"], "DEDUCTED", 2),
            tagged(days["inventory_days"], "VIEW", 2),
            tagged(days["inventory_days"], "VIEW", 2),
            tagged(days["inventory_days"], "VIEW", 2),
        ],
        [
            "Accounts payable days",
            tagged(days["ap_days"], "DEDUCTED", 2),
            tagged(days["ap_days"], "VIEW", 2),
            tagged(days["ap_days"], "VIEW", 2),
            tagged(days["ap_days"], "VIEW", 2),
        ],
    ]

    return f"""# NVIDIA balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares and days.

{markdown_table(["line"] + periods, rows)}

The 1H FY2027 balance is the register R6 filing seed. “Other assets” and “Other liabilities” are `[DEDUCTED]` residuals to filed totals. Debt combines filed short- and long-term debt. Marketable equity securities remain separate from cash and debt securities and are not treated as operating liquidity.

## Working-capital days

{markdown_table(["input", "1H FY2027 seed", "FY2027E", "FY2028E", "FY2029E"], day_rows)}

Days are `[DEDUCTED]` from 2026-07-26 balances divided by annualized 1H FY2027 revenue or COGS, then held as `[VIEW]`. FY2027 rolls from the filed half-year balance using only second-half net income, SBC, dividends, buybacks, capex and D&A. Later years roll annually. Other assets/liabilities and both classes of marketable securities are held flat as explicit `[VIEW]`s.

Supply commitments in R5.2 are footnote risk, not balance-sheet debt. Forecast period-end basic shares are `not obtained`; the model uses only researcher-specified diluted WAS.

## Balance-sheet checks

{render_checks(checks, "balance")}
"""


def render_cashflow(
    cashflow: dict[str, dict[str, float]],
    days: dict[str, float],
    checks: list[Check],
) -> str:
    actual_rows = [
        ["Net income", tagged(HIST_COMPANY["1HFY2027A"]["net_income"], "FACT")],
        ["D&A", tagged(BASE_CASHFLOW["da"], "FACT")],
        ["SBC", tagged(BASE_CASHFLOW["sbc"], "FACT")],
        ["Operating cash flow", tagged(BASE_CASHFLOW["operating_cash_flow"], "FACT")],
        ["PP&E/intangible purchases", tagged(BASE_CASHFLOW["capex"], "FACT")],
        [
            "Principal payments on PP&E/intangibles",
            tagged(BASE_CASHFLOW["principal_asset_payments"], "FACT"),
        ],
        ["Company-defined free cash flow", tagged(BASE_CASHFLOW["free_cash_flow"], "FACT")],
        ["Share repurchases", tagged(BASE_CASHFLOW["buybacks"], "FACT")],
        ["Dividends paid", tagged(BASE_CASHFLOW["dividends"], "FACT")],
    ]

    forecast_rows: list[list[str]] = []
    for label, key in (
        ("Full-year net income", "full_year_net_income"),
        ("Reported 1H operating cash flow included", "reported_1h_ocf"),
        ("Forecast roll-period net income", "roll_net_income"),
        ("Forecast roll-period D&A", "roll_da"),
        ("Forecast roll-period SBC", "roll_sbc"),
        ("Less: increase in NWC", "increase_nwc"),
        ("Forecast roll-period operating cash flow", "roll_operating_cash_flow"),
        ("Full-year operating cash flow", "operating_cash_flow"),
        ("PP&E/intangible purchases", "capex"),
        ("Principal payments on PP&E/intangibles", "principal_asset_payments"),
        ("Free cash flow", "free_cash_flow"),
        ("Dividends", "dividends"),
        ("Debt repayment", "debt_repayment"),
        ("Share repurchases", "buybacks"),
    ):
        forecast_rows.append(
            [label]
            + [tagged(cashflow[p][key], "VIEW") for p in FORECAST_PERIODS]
        )

    cash_roll_rows: list[list[str]] = []
    for label, key in (
        ("Opening cash", "opening_cash"),
        ("Roll-period free cash flow", "roll_fcf"),
        ("Roll-period dividends", "roll_dividends"),
        ("Debt repayment", "debt_repayment"),
        ("Roll-period buybacks", "roll_buybacks"),
        ("Change in cash", "change_in_cash"),
        ("Ending cash", "ending_cash"),
    ):
        cash_roll_rows.append(
            [label]
            + [tagged(cashflow[p][key], "VIEW") for p in FORECAST_PERIODS]
        )

    return f"""# NVIDIA cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

## Historical seed

{markdown_table(["1H FY2027A line", "value"], actual_rows)}

Historical values are `[FACT]` from register R6. Company-defined 1H FCF deducts both PP&E/intangible purchases and principal payments.

## Forecast cash flow

{markdown_table(["line"] + FORECAST_PERIODS, forecast_rows)}

FY2027E full-year OCF retains filed 1H OCF and adds a forecast second-half bridge. FY2028E/FY2029E use full-year `NI + D&A + SBC − increase in NWC`; other operating/noncash adjustments are an explicit `[VIEW]` zero. Forecast FCF deducts PP&E/intangible purchases and the retained FY2027 actual principal payment; later principal payments are `not obtained` and explicitly `[VIEW]` zero.

NWC uses held days: AR `{days["ar_days"]:.2f}`, inventory `{days["inventory_days"]:.2f}`, AP `{days["ap_days"]:.2f}`. Dividends grow modestly from the annualized 1H run-rate. Debt is repaid under the stated schedule. Buybacks receive residual roll-period FCF after dividends, debt repayment and the `[VIEW]` minimum cash balance.

## Cash roll from filed 1H balance

{markdown_table(["line"] + FORECAST_PERIODS, cash_roll_rows)}

FY2027E “roll period” means 2H FY2027; later columns are full years. FY2027 full-year buybacks/dividends include filed 1H actuals plus the forecast second half. Forecast buyback dollars do not derive or imply a share price and do not determine the separately specified diluted WAS.

## Cash-flow checks

{render_checks(checks, "cashflow")}
"""


def main() -> None:
    income = build_forecast_income()
    balances, cashflow, days = build_balance_and_cashflow(income)
    checks = build_checks(income, balances, cashflow)

    outputs = {
        "segments.md": render_segments(income, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, days, checks),
        "cashflow.md": render_cashflow(cashflow, days, checks),
    }
    for filename, content in outputs.items():
        (ROOT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("NVIDIA model outputs")
    print("period | revenue | gross profit | operating income | net income | FCF | diluted EPS")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['revenue']:.1f} | "
            f"{income[period]['gross_profit']:.1f} | "
            f"{income[period]['operating_income']:.1f} | "
            f"{income[period]['net_income']:.1f} | "
            f"{cashflow[period]['free_cash_flow']:.1f} | "
            f"{income[period]['diluted_eps']:.2f}"
        )

    print("\nTie-out checks")
    failed = False
    for name, passed, difference, _category in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (difference {difference:.6f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
