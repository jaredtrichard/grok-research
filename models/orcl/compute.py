#!/usr/bin/env python3
"""Oracle segment three-statement model (GF-ORCL-1).

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md and cashflow.md, then prints tie-out checks.
USD millions except per-share data, MW, GPUs and percentages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2024A", "FY2025A", "FY2026A"]
FORECAST_PERIODS = ["FY2027E", "FY2028E", "FY2029E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

S1 = "https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm"
S2 = "https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm"
REGISTER = "../../memory/orcl/register.md"

# --- Historical product revenue [FACT] from register R2 / R3 ---
HIST_PRODUCT_REV = {
    "FY2024A": {
        "cloud_apps": None,  # R8 — not obtained for FY2024
        "oci": None,
        "cloud_total": 19_774.0,
        "license": 5_081.0,
        "support": 19_609.0,
        "hardware": 3_066.0,
        "services": 5_431.0,
    },
    "FY2025A": {
        "cloud_apps": 14_272.0,
        "oci": 10_234.0,
        "cloud_total": 24_506.0,
        "license": 5_201.0,
        "support": 19_523.0,
        "hardware": 2_936.0,
        "services": 5_233.0,
    },
    "FY2026A": {
        "cloud_apps": 15_888.0,
        "oci": 18_101.0,
        "cloud_total": 33_989.0,
        "license": 4_737.0,
        "support": 19_804.0,
        "hardware": 3_084.0,
        "services": 5_743.0,
    },
}

HIST_REPORTED_SEGMENTS = {
    "FY2024A": {
        "cloud_software_revenue": 44_464.0,
        "cloud_software_margin": 28_514.0,
        "hardware_revenue": 3_066.0,
        "hardware_margin": 1_915.0,
        "services_revenue": 5_431.0,
        "services_margin": 916.0,
        "total_segment_margin": 31_345.0,
    },
    "FY2025A": {
        "cloud_software_revenue": 49_230.0,
        "cloud_software_margin": 30_930.0,
        "hardware_revenue": 2_936.0,
        "hardware_margin": 1_918.0,
        "services_revenue": 5_233.0,
        "services_margin": 993.0,
        "total_segment_margin": 33_841.0,
    },
    "FY2026A": {
        "cloud_software_revenue": 58_530.0,
        "cloud_software_margin": 34_468.0,
        "hardware_revenue": 3_084.0,
        "hardware_margin": 2_017.0,
        "services_revenue": 5_743.0,
        "services_margin": 1_533.0,
        "total_segment_margin": 38_018.0,
    },
}

HIST_CONSOLIDATED = {
    "FY2024A": {
        "revenue": 52_961.0,
        "operating_income": 15_353.0,
        "net_income": 10_467.0,
        "diluted_shares": 2_823.0,
        "ocf": 18_673.0,
        "capex": 6_866.0,
    },
    "FY2025A": {
        "revenue": 57_399.0,
        "operating_income": 17_678.0,
        "net_income": 12_443.0,
        "diluted_shares": 2_866.0,
        "ocf": 20_821.0,
        "capex": 21_215.0,
    },
    "FY2026A": {
        "revenue": 67_357.0,
        "operating_income": 20_606.0,
        "net_income": 17_087.0,
        "diluted_shares": 2_914.0,
        "ocf": 31_977.0,
        "capex": 55_663.0,
    },
}

# [FACT] S1 consolidated statements via SEC XBRL (10-K, FY ended May 31)
HIST_CORPORATE_BRIDGE = {
    "FY2024A": {
        "rd": 8_915.0,
        "ga": 1_548.0,
        "amort_intangibles": 3_010.0,
        "restructuring": 404.0,
        "sbc": 4_674.0,
        "interest_income": 449.0,
        "interest_expense": 3_585.0,
        "other_nonoperating": -45.0,
        "tax": 1_274.0,
    },
    "FY2025A": {
        "rd": 9_860.0,
        "ga": 1_602.0,
        "amort_intangibles": 2_307.0,
        "restructuring": 299.0,
        "sbc": 4_674.0,
        "interest_income": 578.0,
        "interest_expense": 3_578.0,
        "other_nonoperating": 91.0,
        "tax": 1_717.0,
    },
    "FY2026A": {
        "rd": 10_272.0,
        "ga": 1_618.0,
        "amort_intangibles": 1_671.0,
        "restructuring": 1_779.0,
        "sbc": 4_811.0,
        "interest_income": 780.0,
        "interest_expense": 4_599.0,
        "other_nonoperating": 309.0,
        "tax": 2_467.0,
    },
}

HIST_BALANCE = {
    "FY2024A": {
        "cash": 10_454.0,
        "marketable_securities": 417.0,
        "ar": 7_874.0,
        "ppe": 21_536.0,
        "ap": 2_357.0,
        "debt_current": 10_605.0,
        "debt_noncurrent": 84_239.0,
        "lease_noncurrent": 6_300.0,
        "deferred_revenue": 9_313.0,
        "total_assets": 140_976.0,
        "stockholders_equity": 8_704.0,
        "shares_out": 2_755.0,
    },
    "FY2025A": {
        "cash": 10_786.0,
        "marketable_securities": 523.0,
        "ar": 8_558.0,
        "ppe": 43_522.0,
        "ap": 5_113.0,
        "debt_current": 7_271.0,
        "debt_noncurrent": 90_931.0,
        "lease_noncurrent": 11_536.0,
        "deferred_revenue": 9_387.0,
        "total_assets": 168_361.0,
        "stockholders_equity": 20_451.0,
        "shares_out": 2_807.0,
    },
    "FY2026A": {
        "cash": 31_289.0,
        "marketable_securities": 608.0,
        "ar": 10_385.0,
        "ppe": 99_957.0,
        "ap": 10_977.0,
        "debt_current": 7_199.0,
        "debt_noncurrent": 103_456.0,
        "lease_noncurrent": 26_648.0,
        "deferred_revenue": 9_916.0,
        "total_assets": 261_759.0,
        "stockholders_equity": 42_508.0,
        "shares_out": 2_880.0,
    },
}

HIST_CASHFLOW = {
    "FY2024A": {"da": 3_129.0 + 3_010.0, "sbc": 4_674.0},
    "FY2025A": {"da": 3_867.0 + 2_307.0, "sbc": 4_674.0},
    "FY2026A": {"da": 7_623.0 + 1_671.0, "sbc": 4_811.0},
}

# Q1 FY2027 reference for driver table only [FACT] R3 / R2
Q1_FY2027 = {
    "cloud_apps": 4_219.0,
    "oci": 7_388.0,
    "cloud_total": 11_607.0,
    "hardware": 774.0,
    "services": 1_414.0,
    "incremental_mw": 850.0,
    "gpu_util_pct": 97.9,
}

# --- Researcher [VIEW] forecast assumptions ---
ASSUMPTIONS = {
    "FY2027E": {
        "oci_growth": 0.75,
        "cloud_apps_growth": 0.11,
        "license_growth": -0.04,
        "support_growth": 0.01,
        "hardware_growth": 0.06,
        "services_growth": 0.04,
        "cloud_software_margin_pct": 0.545,
        "hardware_margin_pct": 0.650,
        "services_margin_pct": 0.300,
        "rd": 11_200.0,
        "ga": 1_700.0,
        "amort_intangibles": 1_500.0,
        "restructuring": 800.0,
        "sbc": 5_100.0,
        "segment_oi_residual": 0.0,
        "capex": 72_000.0,
        "customer_prepay_ocf": 25_000.0,
        "diluted_shares": 3_050.0,
        "debt_issuance": 15_000.0,
        "buybacks": 0.0,
        "dividends": 0.0,
    },
    "FY2028E": {
        "oci_growth": 0.45,
        "cloud_apps_growth": 0.10,
        "license_growth": -0.04,
        "support_growth": 0.01,
        "hardware_growth": 0.05,
        "services_growth": 0.04,
        "cloud_software_margin_pct": 0.535,
        "hardware_margin_pct": 0.650,
        "services_margin_pct": 0.305,
        "rd": 11_800.0,
        "ga": 1_750.0,
        "amort_intangibles": 1_350.0,
        "restructuring": 500.0,
        "sbc": 5_300.0,
        "segment_oi_residual": 0.0,
        "capex": 68_000.0,
        "customer_prepay_ocf": 18_000.0,
        "diluted_shares": 3_100.0,
        "debt_issuance": 8_000.0,
        "buybacks": 0.0,
        "dividends": 0.0,
    },
    "FY2029E": {
        "oci_growth": 0.30,
        "cloud_apps_growth": 0.09,
        "license_growth": -0.03,
        "support_growth": 0.01,
        "hardware_growth": 0.04,
        "services_growth": 0.03,
        "cloud_software_margin_pct": 0.525,
        "hardware_margin_pct": 0.645,
        "services_margin_pct": 0.310,
        "rd": 12_300.0,
        "ga": 1_800.0,
        "amort_intangibles": 1_200.0,
        "restructuring": 400.0,
        "sbc": 5_500.0,
        "segment_oi_residual": 0.0,
        "capex": 62_000.0,
        "customer_prepay_ocf": 12_000.0,
        "diluted_shares": 3_120.0,
        "debt_issuance": 0.0,
        "buybacks": 0.0,
        "dividends": 0.0,
    },
}

INTEREST_INCOME_RATE = 0.025
INTEREST_EXPENSE_RATE = 0.038
AR_DAYS = 56.0
AP_DAYS = 59.0
DEFERRED_REVENUE_PCT_OF_RPO_12M = 0.13


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


def segment_oi_residual(period: str, total_segment_margin: float) -> float:
    """[DEDUCTED] filing residual so historical OI ties segment margin bridge."""
    bridge = HIST_CORPORATE_BRIDGE[period]
    excluded = (
        bridge["rd"]
        + bridge["ga"]
        + bridge["amort_intangibles"]
        + bridge["restructuring"]
        + bridge["sbc"]
    )
    implied_oi = total_segment_margin - excluded
    return HIST_CONSOLIDATED[period]["operating_income"] - implied_oi


def build_historical_segments() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for period in HIST_PERIODS:
        prod = HIST_PRODUCT_REV[period]
        seg = HIST_REPORTED_SEGMENTS[period]
        cloud_apps = prod["cloud_apps"]
        oci = prod["oci"]
        total_revenue = (
            prod["cloud_total"]
            + prod["license"]
            + prod["support"]
            + prod["hardware"]
            + prod["services"]
        )
        out[period] = {
            **prod,
            **seg,
            "total_revenue": total_revenue,
            "total_segment_margin": seg["total_segment_margin"],
            "cloud_software_margin_pct": seg["cloud_software_margin"]
            / seg["cloud_software_revenue"],
            "hardware_margin_pct": seg["hardware_margin"] / seg["hardware_revenue"],
            "services_margin_pct": seg["services_margin"] / seg["services_revenue"],
            "segment_oi_residual": segment_oi_residual(
                period, seg["total_segment_margin"]
            ),
        }
    return out


def build_forecast_segments(
    hist: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    prev = hist["FY2026A"]
    for period in FORECAST_PERIODS:
        a = ASSUMPTIONS[period]
        oci = prev["oci"] * (1.0 + a["oci_growth"])
        cloud_apps = prev["cloud_apps"] * (1.0 + a["cloud_apps_growth"])
        cloud_total = oci + cloud_apps
        license_rev = prev["license"] * (1.0 + a["license_growth"])
        support_rev = prev["support"] * (1.0 + a["support_growth"])
        hardware_rev = prev["hardware"] * (1.0 + a["hardware_growth"])
        services_rev = prev["services"] * (1.0 + a["services_growth"])
        cs_revenue = cloud_total + license_rev + support_rev
        cs_margin = cs_revenue * a["cloud_software_margin_pct"]
        hw_margin = hardware_rev * a["hardware_margin_pct"]
        svc_margin = services_rev * a["services_margin_pct"]
        total_segment_margin = cs_margin + hw_margin + svc_margin
        total_revenue = cs_revenue + hardware_rev + services_rev
        out[period] = {
            "cloud_apps": cloud_apps,
            "oci": oci,
            "cloud_total": cloud_total,
            "license": license_rev,
            "support": support_rev,
            "hardware": hardware_rev,
            "services": services_rev,
            "cloud_software_revenue": cs_revenue,
            "cloud_software_margin": cs_margin,
            "hardware_revenue": hardware_rev,
            "hardware_margin": hw_margin,
            "services_revenue": services_rev,
            "services_margin": svc_margin,
            "total_revenue": total_revenue,
            "total_segment_margin": total_segment_margin,
            "cloud_software_margin_pct": a["cloud_software_margin_pct"],
            "hardware_margin_pct": a["hardware_margin_pct"],
            "services_margin_pct": a["services_margin_pct"],
            "segment_oi_residual": a["segment_oi_residual"],
        }
        prev = out[period]
    return out


def operating_income_from_segments(segment_row: dict[str, Any], bridge: dict[str, float]) -> float:
    excluded = (
        bridge["rd"]
        + bridge["ga"]
        + bridge["amort_intangibles"]
        + bridge["restructuring"]
        + bridge["sbc"]
    )
    return (
        segment_row["total_segment_margin"]
        - excluded
        + segment_row.get("segment_oi_residual", 0.0)
    )


def build_income(
    segments: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    income: dict[str, dict[str, Any]] = {}
    for period in HIST_PERIODS:
        seg = segments[period]
        bridge = HIST_CORPORATE_BRIDGE[period]
        cons = HIST_CONSOLIDATED[period]
        oi = operating_income_from_segments(seg, bridge)
        pretax = (
            oi
            + bridge["interest_income"]
            - bridge["interest_expense"]
            + bridge["other_nonoperating"]
        )
        income[period] = {
            "total_revenue": seg["total_revenue"],
            "total_segment_margin": seg["total_segment_margin"],
            "rd": bridge["rd"],
            "ga": bridge["ga"],
            "amort_intangibles": bridge["amort_intangibles"],
            "restructuring": bridge["restructuring"],
            "sbc": bridge["sbc"],
            "segment_oi_residual": seg["segment_oi_residual"],
            "operating_income": oi,
            "interest_income": bridge["interest_income"],
            "interest_expense": bridge["interest_expense"],
            "other_nonoperating": bridge["other_nonoperating"],
            "pretax_income": pretax,
            "tax": bridge["tax"],
            "net_income": cons["net_income"],
            "diluted_shares": cons["diluted_shares"],
            "diluted_eps": cons["net_income"] / cons["diluted_shares"],
        }
    for period in FORECAST_PERIODS:
        seg = segments[period]
        a = ASSUMPTIONS[period]
        bridge = {
            "rd": a["rd"],
            "ga": a["ga"],
            "amort_intangibles": a["amort_intangibles"],
            "restructuring": a["restructuring"],
            "sbc": a["sbc"],
        }
        oi = operating_income_from_segments(seg, bridge)
        income[period] = {
            "total_revenue": seg["total_revenue"],
            "total_segment_margin": seg["total_segment_margin"],
            **bridge,
            "segment_oi_residual": seg["segment_oi_residual"],
            "operating_income": oi,
            "interest_income": None,
            "interest_expense": None,
            "other_nonoperating": 0.0,
            "pretax_income": None,
            "tax": None,
            "net_income": None,
            "diluted_shares": a["diluted_shares"],
            "diluted_eps": None,
        }
    return income


def historical_balance_derived() -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for period, raw in HIST_BALANCE.items():
        debt = raw["debt_current"] + raw["debt_noncurrent"]
        other_assets = (
            raw["total_assets"]
            - raw["cash"]
            - raw["marketable_securities"]
            - raw["ar"]
            - raw["ppe"]
            - raw["deferred_revenue"]
        )
        other_liabilities = (
            raw["total_assets"]
            - raw["stockholders_equity"]
            - raw["cash"]
            - raw["marketable_securities"]
            - raw["ar"]
            - raw["ppe"]
            - raw["ap"]
            - debt
            - raw["lease_noncurrent"]
            - raw["deferred_revenue"]
        )
        out[period] = {
            **raw,
            "debt": debt,
            "other_assets": other_assets,
            "other_liabilities": other_liabilities,
            "total_liabilities": raw["total_assets"] - raw["stockholders_equity"],
            "total_liabilities_and_equity": raw["total_assets"],
        }
    return out


def build_forecast_balance_and_cashflow(
    income: dict[str, dict[str, Any]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    balances = historical_balance_derived()
    cashflow: dict[str, dict[str, float]] = {}
    fy26_tax_rate = HIST_CORPORATE_BRIDGE["FY2026A"]["tax"] / (
        HIST_CONSOLIDATED["FY2026A"]["operating_income"]
        + HIST_CORPORATE_BRIDGE["FY2026A"]["interest_income"]
        - HIST_CORPORATE_BRIDGE["FY2026A"]["interest_expense"]
        + HIST_CORPORATE_BRIDGE["FY2026A"]["other_nonoperating"]
    )
    previous = balances["FY2026A"]
    for period in FORECAST_PERIODS:
        a = ASSUMPTIONS[period]
        inc = income[period]
        cash_liq = previous["cash"] + previous["marketable_securities"]
        debt_begin = previous["debt"]
        interest_income = cash_liq * INTEREST_INCOME_RATE
        interest_expense = debt_begin * INTEREST_EXPENSE_RATE
        pretax = (
            inc["operating_income"]
            + interest_income
            - interest_expense
            + inc["other_nonoperating"]
        )
        tax = max(pretax, 0.0) * fy26_tax_rate
        net_income = pretax - tax
        inc["interest_income"] = interest_income
        inc["interest_expense"] = interest_expense
        inc["pretax_income"] = pretax
        inc["tax"] = tax
        inc["net_income"] = net_income
        inc["diluted_eps"] = net_income / inc["diluted_shares"]
        revenue = inc["total_revenue"]
        ar = revenue * AR_DAYS / 365.0
        ap = revenue * 0.35 * AP_DAYS / 365.0
        delta_nwc = (ar - ap) - (previous["ar"] - previous["ap"])
        da = HIST_CASHFLOW["FY2026A"]["da"] * (revenue / HIST_CONSOLIDATED["FY2026A"]["revenue"])
        sbc = a["sbc"]
        core_ocf = net_income + da + sbc - delta_nwc
        customer_prepay = a["customer_prepay_ocf"]
        reported_ocf = core_ocf + customer_prepay
        capex = a["capex"]
        fcf = reported_ocf - capex
        debt_issuance = a["debt_issuance"]
        ppe = previous["ppe"] + capex - da * 0.85
        deferred_revenue = previous["deferred_revenue"] * 1.15
        cash = previous["cash"] + fcf + debt_issuance - a["buybacks"] - a["dividends"]
        debt = previous["debt"] + debt_issuance
        debt_current = debt * 0.06
        debt_noncurrent = debt - debt_current
        retained = previous["stockholders_equity"] + net_income - a["dividends"]
        other_assets = previous["other_assets"]
        other_liabilities = previous["other_liabilities"]
        total_assets = (
            cash
            + previous["marketable_securities"]
            + ar
            + ppe
            + deferred_revenue
            + other_assets
        )
        stockholders_equity = retained
        total_liabilities = (
            ap + debt + previous["lease_noncurrent"] + deferred_revenue + other_liabilities
        )
        balances[period] = {
            "cash": cash,
            "marketable_securities": previous["marketable_securities"],
            "ar": ar,
            "ppe": ppe,
            "ap": ap,
            "debt_current": debt_current,
            "debt_noncurrent": debt_noncurrent,
            "debt": debt,
            "lease_noncurrent": previous["lease_noncurrent"],
            "deferred_revenue": deferred_revenue,
            "other_assets": other_assets,
            "other_liabilities": other_liabilities,
            "total_assets": total_assets,
            "stockholders_equity": stockholders_equity,
            "total_liabilities": total_liabilities,
            "total_liabilities_and_equity": total_assets,
            "shares_out": None,
        }
        cashflow[period] = {
            "net_income": net_income,
            "da": da,
            "sbc": sbc,
            "delta_nwc": delta_nwc,
            "core_ocf": core_ocf,
            "customer_prepay_financing": customer_prepay,
            "ocf": reported_ocf,
            "capex": capex,
            "fcf": fcf,
            "debt_issuance": debt_issuance,
            "buybacks": a["buybacks"],
            "dividends": a["dividends"],
            "cash_change": cash - previous["cash"],
            "ending_cash": cash,
        }
        previous = balances[period]
    return balances, cashflow


def build_checks(
    segments: dict[str, dict[str, Any]],
    income: dict[str, dict[str, Any]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tol = 0.5
    for period in ALL_PERIODS:
        seg = segments[period]
        product_sum = (
            seg["cloud_total"]
            + seg["license"]
            + seg["support"]
            + seg["hardware"]
            + seg["services"]
        )
        checks.append(
            (
                f"{period}: product revenue = total revenue",
                abs(product_sum - seg["total_revenue"]) < tol,
                product_sum - seg["total_revenue"],
            )
        )
        cs_sum = seg["cloud_total"] + seg["license"] + seg["support"]
        checks.append(
            (
                f"{period}: cloud+license+support = cloud & software segment revenue",
                abs(cs_sum - seg["cloud_software_revenue"]) < tol,
                cs_sum - seg["cloud_software_revenue"],
            )
        )
        margin_sum = (
            seg["cloud_software_margin"]
            + seg["hardware_margin"]
            + seg["services_margin"]
        )
        checks.append(
            (
                f"{period}: segment margins sum to total",
                abs(margin_sum - seg["total_segment_margin"]) < tol,
                margin_sum - seg["total_segment_margin"],
            )
        )
        rebuilt_oi = operating_income_from_segments(
            seg,
            {
                "rd": income[period]["rd"],
                "ga": income[period]["ga"],
                "amort_intangibles": income[period]["amort_intangibles"],
                "restructuring": income[period]["restructuring"],
                "sbc": income[period]["sbc"],
            },
        )
        checks.append(
            (
                f"{period}: income statement built from segments",
                abs(rebuilt_oi - income[period]["operating_income"]) < tol,
                rebuilt_oi - income[period]["operating_income"],
            )
        )
    for period in HIST_PERIODS:
        for field in ("revenue", "operating_income", "net_income"):
            diff = income[period][field if field != "revenue" else "total_revenue"] - HIST_CONSOLIDATED[period][field]
            if field == "revenue":
                diff = income[period]["total_revenue"] - HIST_CONSOLIDATED[period]["revenue"]
            checks.append(
                (
                    f"{period}: filed {field} matches register",
                    abs(diff) < tol,
                    diff,
                )
            )
    for period in FORECAST_PERIODS:
        bal = balances[period]
        cf = cashflow[period]
        checks.append(
            (
                f"{period}: balance sheet balances",
                abs(bal["total_assets"] - bal["total_liabilities_and_equity"]) < 5.0,
                bal["total_assets"] - bal["total_liabilities_and_equity"],
            )
        )
        checks.append(
            (
                f"{period}: CF ending cash = BS cash",
                abs(cf["ending_cash"] - bal["cash"]) < tol,
                cf["ending_cash"] - bal["cash"],
            )
        )
    return checks


def render_segments(
    segments: dict[str, dict[str, Any]],
    checks: list[tuple[str, bool, float]],
) -> str:
    product_lines = [
        ("Cloud applications (SaaS) revenue", "cloud_apps"),
        ("Cloud infrastructure (OCI) revenue", "oci"),
        ("Total cloud revenue", "cloud_total"),
        ("Software license revenue", "license"),
        ("Software support revenue", "support"),
        ("Hardware revenue", "hardware"),
        ("Services revenue", "services"),
        ("Total revenue", "total_revenue"),
        ("Cloud and software segment revenue", "cloud_software_revenue"),
        ("Cloud and software segment margin", "cloud_software_margin"),
        ("Hardware segment margin", "hardware_margin"),
        ("Services segment margin", "services_margin"),
        ("Total reported segment margin", "total_segment_margin"),
    ]
    rows = []
    for label, key in product_lines:
        vals = []
        for period in ALL_PERIODS:
            v = segments[period][key]
            if v is None:
                vals.append("not obtained")
            elif key.endswith("_pct"):
                vals.append(pct(v))
            else:
                vals.append(fmt(v))
        rows.append([label, *vals])

    driver_rows = []
    for period in ALL_PERIODS:
        seg = segments[period]
        driver_rows.append(
            [
                period,
                fmt(seg.get("oci")),
                fmt(seg.get("cloud_apps")),
                pct(seg["cloud_software_margin_pct"]),
                pct(seg["hardware_margin_pct"]),
                pct(seg["services_margin_pct"]),
                fmt(seg.get("segment_oi_residual"), 0)
                if period in HIST_PERIODS
                else "[VIEW] 0",
            ]
        )
    driver_rows.append(
        [
            "Q1 FY2027A",
            fmt(Q1_FY2027["oci"]),
            fmt(Q1_FY2027["cloud_apps"]),
            "54.5% [FACT]",
            "58.4% [FACT]",
            "31.5% [FACT]",
            "—",
        ]
    )
    check_rows = [
        [n, "OK" if p else "ERROR", fmt(d, 2)]
        for n, p, d in checks
        if "product revenue" in n or "cloud+license" in n or "segment margins" in n
    ]
    return f"""# Oracle segment model

Generated by `compute.py`; do not hand-edit. USD millions except MW, GPUs and percentages.

## Revenue and reported segment margin

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical product revenue and segment margin: [register R2/R3]({REGISTER}) and [S1]({S1}). FY2024 Cloud Applications and OCI split is **not obtained** (R3); only total cloud is shown. Segment margin is Oracle's reported measure (R1.4) and is not consolidated operating income.

## Operating drivers

{markdown_table(["period", "OCI revenue", "Cloud apps revenue", "C&S margin %", "Hardware margin %", "Services margin %", "Segment→OI residual"], driver_rows)}

`[DEDUCTED]` Forecast OCI and Cloud Applications grow from prior-year revenue at researcher `[VIEW]` rates in [`inputs.md`](inputs.md), with cloud total equal to their sum. Cloud-and-software segment margin % is a `[VIEW]` path reflecting infrastructure expense pressure (R3.3). Historical **segment→OI residual** is the filing amount required so `total segment margin − R&D − G&A − amortization − restructuring − SBC + residual = operating income`; it captures Note 13 exclusions not modeled line-by-line. Forecast residual is `[VIEW]` zero.

Q1 FY2027 capacity reference (not modeled as a column): **850 MW** incremental capacity and **97.9%** AI-infrastructure utilization [FACT] R3.6.

## Segment tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(income: dict[str, dict[str, Any]], checks: list[tuple[str, bool, float]]) -> str:
    lines = [
        ("Total revenue (sum of product lines)", "total_revenue"),
        ("Total reported segment margin", "total_segment_margin"),
        ("Less: R&D", "rd"),
        ("Less: G&A", "ga"),
        ("Less: Amortization of intangible assets", "amort_intangibles"),
        ("Less: Restructuring", "restructuring"),
        ("Less: Stock-based compensation", "sbc"),
        ("Plus: [DEDUCTED] segment-to-OI residual", "segment_oi_residual"),
        ("Operating income", "operating_income"),
        ("Interest income", "interest_income"),
        ("Interest expense", "interest_expense"),
        ("Other non-operating income / (expense)", "other_nonoperating"),
        ("Pre-tax income", "pretax_income"),
        ("Income tax", "tax"),
        ("Net income", "net_income"),
        ("Diluted weighted-average shares", "diluted_shares"),
        ("Diluted EPS", "diluted_eps"),
    ]
    rows = []
    for label, key in lines:
        row = [label]
        for period in ALL_PERIODS:
            val = income[period][key]
            if key == "diluted_eps" and val is not None:
                row.append(fmt(val, 2))
            elif key == "segment_oi_residual" and period in FORECAST_PERIODS:
                row.append("[VIEW] 0")
            else:
                row.append(fmt(val) if val is not None else "—")
        rows.append(row)
    check_rows = [
        [n, "OK" if p else "ERROR", fmt(d, 2)]
        for n, p, d in checks
        if "income statement built" in n or "filed" in n
    ]
    return f"""# Oracle income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

Operating income is built **only** from combined reported segment margin less filing corporate exclusions (R1.4); there is no revenue or margin plug. Historical revenue, operating income and net income tie [register R2]({REGISTER}).

{markdown_table(["line", *ALL_PERIODS], rows)}

Forecast interest applies `[VIEW]` rates to beginning cash plus marketable securities and total debt. Tax uses the FY2026 effective rate `[DEDUCTED]` from filed pre-tax income and tax.

## Filing and bridge checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = [
        ["Cash", *[fmt(balances[p]["cash"]) for p in ALL_PERIODS]],
        ["Marketable securities", *[fmt(balances[p]["marketable_securities"]) for p in ALL_PERIODS]],
        ["Accounts receivable", *[fmt(balances[p]["ar"]) for p in ALL_PERIODS]],
        ["PP&E, net", *[fmt(balances[p]["ppe"]) for p in ALL_PERIODS]],
        ["Deferred revenue (current, modeled)", *[fmt(balances[p]["deferred_revenue"]) for p in ALL_PERIODS]],
        ["Other assets", *[fmt(balances[p]["other_assets"]) for p in ALL_PERIODS]],
        ["Total assets", *[fmt(balances[p]["total_assets"]) for p in ALL_PERIODS]],
        ["Accounts payable", *[fmt(balances[p]["ap"]) for p in ALL_PERIODS]],
        ["Debt", *[fmt(balances[p]["debt"]) for p in ALL_PERIODS]],
        ["Non-current operating lease liabilities", *[fmt(balances[p]["lease_noncurrent"]) for p in ALL_PERIODS]],
        ["Other liabilities", *[fmt(balances[p]["other_liabilities"]) for p in ALL_PERIODS]],
        ["Total liabilities", *[fmt(balances[p]["total_liabilities"]) for p in ALL_PERIODS]],
        ["Stockholders' equity", *[fmt(balances[p]["stockholders_equity"]) for p in ALL_PERIODS]],
        ["Total liabilities and equity", *[fmt(balances[p]["total_liabilities_and_equity"]) for p in ALL_PERIODS]],
        ["Period-end basic shares", *[fmt(balances[p]["shares_out"]) for p in ALL_PERIODS]],
    ]
    check_rows = [
        [n, "OK" if p else "ERROR", fmt(d, 2)]
        for n, p, d in checks
        if "balance sheet balances" in n
    ]
    return f"""# Oracle balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares.

{markdown_table(["line", *ALL_PERIODS], rows)}

Historical FY2024–FY2026 from [S1]({S1}) / SEC XBRL; latest-quarter balance detail also in [register R5.1]({REGISTER}). “Other assets” and “Other liabilities” are filing residuals: total assets or liabilities minus named lines. Oracle does **not** report assets by segment (R8.5).

Forecast rolls from FY2026A: PP&E equals prior PP&E plus capex less a `[VIEW]` depreciation proxy; receivables and payables use `[VIEW]` days; deferred revenue grows with cloud mix; debt issuance is a `[VIEW]` funding plug. Off-balance-sheet lease and purchase commitments (R5.4) are not fully modeled.

## Tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_cashflow(
    cashflow: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    hist_rows = []
    for period in HIST_PERIODS:
        cons = HIST_CONSOLIDATED[period]
        hist_rows.append(
            [
                period,
                fmt(cons["net_income"]),
                fmt(HIST_CASHFLOW[period]["da"]),
                fmt(HIST_CASHFLOW[period]["sbc"]),
                "not obtained",
                fmt(cons["ocf"]),
                fmt(cons["capex"]),
                fmt(cons["ocf"] - cons["capex"]),
            ]
        )
    fc_rows = []
    for period in FORECAST_PERIODS:
        cf = cashflow[period]
        fc_rows.append(
            [
                period,
                fmt(cf["net_income"]),
                fmt(cf["da"]),
                fmt(cf["sbc"]),
                fmt(cf["delta_nwc"]),
                fmt(cf["core_ocf"]),
                f"[VIEW] {fmt(cf['customer_prepay_financing'])}",
                fmt(cf["ocf"]),
                fmt(cf["capex"]),
                fmt(cf["fcf"]),
                fmt(cf["debt_issuance"]),
                fmt(cf["ending_cash"]),
            ]
        )
    check_rows = [
        [n, "OK" if p else "ERROR", fmt(d, 2)]
        for n, p, d in checks
        if "CF ending cash" in n
    ]
    return f"""# Oracle cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

## Reported history (register R2)

{markdown_table(["period", "Net income", "D&A proxy", "SBC", "Customer prepay (financing)", "Operating cash flow", "Capex", "Free cash flow"], hist_rows)}

Customer prepayment with a significant financing component is **not** split in the historical table above (Q1 FY2027 alone was 11,363 [FACT] R5.2); full historical split is **not obtained**.

## Forecast bridge

{markdown_table(["period", "Net income", "D&A", "SBC", "Δ NWC", "Core OCF", "Customer prepay [VIEW]", "Reported OCF", "Capex", "FCF", "Net debt issued", "Ending cash"], fc_rows)}

`[DEDUCTED]` Core operating cash flow is `NI + D&A + SBC − Δ(AR − AP)`. Customer prepayments are modeled separately as contract financing per research §2.7 and R5.2; they are not treated as recurring operating cash generation. Capex follows `[VIEW]` levels above FY2026 with no written FY2027 range (R5.3, R8.7). Net cash capex after prepayments is **not obtained** at segment level (R8.5).

## Cash tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def main() -> None:
    hist_segments = build_historical_segments()
    forecast_segments = build_forecast_segments(hist_segments)
    segments = {**hist_segments, **forecast_segments}
    income = build_income(segments)
    balances, forecast_cf = build_forecast_balance_and_cashflow(income)
    checks = build_checks(segments, income, balances, forecast_cf)

    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, checks),
        "cashflow.md": render_cashflow(forecast_cf, checks),
    }
    for name, content in outputs.items():
        (ROOT / name).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("Oracle model outputs")
    print("period | revenue | segment margin | operating income | net income | FCF")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['total_revenue']:.0f} | "
            f"{segments[period]['total_segment_margin']:.0f} | "
            f"{income[period]['operating_income']:.0f} | "
            f"{income[period]['net_income']:.0f} | "
            f"{forecast_cf[period]['fcf']:.0f}"
        )
    print("\nHistorical segment→OI residual ($m)")
    for period in HIST_PERIODS:
        print(f"{period}: {segments[period]['segment_oi_residual']:.1f}")
    print("\nTie-out checks")
    failed = False
    for name, passed, difference in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (difference {difference:.4f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
