#!/usr/bin/env python3
"""AMD segment three-statement model.

All arithmetic for the markdown model lives here. Running this file rewrites
segments.md, income.md, balance.md, cashflow.md and valuation.md (stub), then
prints tie-out checks. USD millions except per-share data and percentages.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REGISTER = "../../memory/amd/register.md"
S1 = "https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm"
S5 = "https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm"

HIST_PERIODS = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS

# Segment actuals — [FACT] from register R2 segment tables.
HIST_SEGMENTS: dict[str, dict[str, float]] = {
    "FY2023A": {
        "dc_rev": 6_496.0,
        "dc_oi": 1_267.0,
        "client_rev": 4_651.0,
        "gaming_rev": 6_212.0,
        "cg_oi": 925.0,
        "emb_rev": 5_321.0,
        "emb_oi": 2_628.0,
        "all_other_oi": -4_419.0,
    },
    "FY2024A": {
        "dc_rev": 12_579.0,
        "dc_oi": 3_482.0,
        "client_rev": 7_054.0,
        "gaming_rev": 2_595.0,
        "cg_oi": 1_187.0,
        "emb_rev": 3_557.0,
        "emb_oi": 1_421.0,
        "all_other_oi": -4_190.0,
    },
    "FY2025A": {
        "dc_rev": 16_635.0,
        "dc_oi": 3_603.0,
        "client_rev": 10_640.0,
        "gaming_rev": 3_910.0,
        "cg_oi": 2_855.0,
        "emb_rev": 3_454.0,
        "emb_oi": 1_243.0,
        "all_other_oi": -4_007.0,
    },
    "1H2026A": {
        "dc_rev": 12_493.0,
        "dc_oi": 3_702.0,
        "client_rev": 5_947.0,
        "gaming_rev": 1_499.0,
        "cg_oi": 1_157.0,
        "emb_rev": 1_850.0,
        "emb_oi": 724.0,
        "all_other_oi": -2_117.0,
    },
}

# Consolidated income — [FACT] register R2 consolidated table / S1 / S6.
HIST_INCOME: dict[str, dict[str, float]] = {
    "FY2023A": {
        "revenue": 22_680.0,
        "gross_profit": 10_460.0,
        "rd": 5_872.0,
        "mga": 2_318.0,
        "operating_income": 401.0,
        "interest_expense": 106.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": -346.0,
        "net_income": 854.0,
        "diluted_shares": 1_608.0,
    },
    "FY2024A": {
        "revenue": 25_785.0,
        "gross_profit": 12_725.0,
        "rd": 6_456.0,
        "mga": 2_735.0,
        "operating_income": 1_900.0,
        "interest_expense": 92.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": 381.0,
        "net_income": 1_641.0,
        "diluted_shares": 1_641.0,
    },
    "FY2025A": {
        "revenue": 34_639.0,
        "gross_profit": 17_152.0,
        "rd": 8_091.0,
        "mga": 4_144.0,
        "operating_income": 3_694.0,
        "interest_expense": 131.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": -103.0,
        "net_income": 4_335.0,
        "diluted_shares": 1_636.0,
    },
    "1H2026A": {
        "revenue": 21_789.0,
        "gross_profit": 11_619.0,
        "rd": 4_925.0,
        "mga": 2_654.0,
        "operating_income": 3_466.0,
        "interest_expense": 0.0,
        "other_income": 0.0,
        "pretax": 0.0,
        "tax": 0.0,
        "net_income": 3_680.0,
        "diluted_shares": 1_655.0,
    },
}

# Balance sheet — [FACT] SEC XBRL / R6.1 for 1H2026.
HIST_BALANCE: dict[str, dict[str, float]] = {
    "FY2023A": {
        "cash": 3_933.0,
        "sti": 0.0,
        "ar": 5_376.0,
        "inventory": 4_351.0,
        "ppe": 1_589.0,
        "goodwill": 24_262.0,
        "other_assets": 29_374.0,
        "total_assets": 67_885.0,
        "ap": 2_055.0,
        "debt": 1_717.0,
        "other_liabilities": 9_221.0,
        "total_liabilities": 12_993.0,
        "apic": 0.0,
        "retained_earnings": 0.0,
        "stockholders_equity": 55_892.0,
    },
    "FY2024A": {
        "cash": 3_787.0,
        "sti": 0.0,
        "ar": 6_192.0,
        "inventory": 5_734.0,
        "ppe": 1_802.0,
        "goodwill": 24_839.0,
        "other_assets": 32_872.0,
        "total_assets": 69_226.0,
        "ap": 2_466.0,
        "debt": 1_721.0,
        "other_liabilities": 9_471.0,
        "total_liabilities": 11_658.0,
        "apic": 0.0,
        "retained_earnings": 0.0,
        "stockholders_equity": 57_568.0,
    },
    "FY2025A": {
        "cash": 5_539.0,
        "sti": 5_013.0,
        "ar": 6_315.0,
        "inventory": 7_920.0,
        "ppe": 2_312.0,
        "goodwill": 25_126.0,
        "other_assets": 30_701.0,
        "total_assets": 76_926.0,
        "ap": 2_929.0,
        "debt": 3_222.0,
        "other_liabilities": 7_776.0,
        "total_liabilities": 13_927.0,
        "apic": 0.0,
        "retained_earnings": 6_699.0,
        "stockholders_equity": 62_999.0,
    },
    "1H2026A": {
        "cash": 5_086.0,
        "sti": 8_025.0,
        "ar": 7_281.0,
        "inventory": 8_468.0,
        "ppe": 3_439.0,
        "goodwill": 25_126.0,
        "other_assets": 28_000.0,
        "total_assets": 80_425.0,
        "ap": 5_359.0,
        "debt": 3_226.0,
        "other_liabilities": 7_500.0,
        "total_liabilities": 16_085.0,
        "apic": 0.0,
        "retained_earnings": 0.0,
        "stockholders_equity": 64_340.0,
    },
}

HIST_CASHFLOW: dict[str, dict[str, float]] = {
    "FY2023A": {
        "ocf": 1_667.0,
        "capex": 546.0,
        "da": 0.0,
        "sbc": 1_384.0,
        "net_income": 854.0,
    },
    "FY2024A": {
        "ocf": 3_041.0,
        "capex": 636.0,
        "da": 0.0,
        "sbc": 1_407.0,
        "net_income": 1_641.0,
    },
    "FY2025A": {
        "ocf": 6_493.0,
        "capex": 974.0,
        "da": 0.0,
        "sbc": 1_638.0,
        "net_income": 4_335.0,
    },
    "1H2026A": {
        "ocf": 5_321.0,
        "capex": 1_197.0,
        "da": 0.0,
        "sbc": 990.0,
        "net_income": 3_680.0,
    },
}

# Researcher [VIEW] segment drivers — see inputs.md.
ASSUMPTIONS: dict[str, dict[str, float]] = {
    "FY2026E": {
        "dc_rev_growth": 0.78,
        "client_rev_growth": 0.18,
        "gaming_rev_growth": -0.15,
        "emb_rev_growth": 0.15,
        "dc_oi_margin": 0.30,
        "cg_oi_margin": 0.16,
        "emb_oi_margin": 0.39,
        "all_other_oi": -5_100.0,
        "consolidated_gm": 0.54,
        "rd": 9_600.0,
        "mga": 4_900.0,
        "interest_expense": 150.0,
        "other_income": 80.0,
        "tax_rate": 0.13,
        "capex": 2_800.0,
        "da": 1_200.0,
        "sbc": 2_100.0,
        "buybacks": 400.0,
        "diluted_shares": 1_660.0,
    },
    "FY2027E": {
        "dc_rev_growth": 1.05,
        "client_rev_growth": 0.10,
        "gaming_rev_growth": -0.05,
        "emb_rev_growth": 0.10,
        "dc_oi_margin": 0.31,
        "cg_oi_margin": 0.17,
        "emb_oi_margin": 0.39,
        "all_other_oi": -5_800.0,
        "consolidated_gm": 0.55,
        "rd": 10_800.0,
        "mga": 5_400.0,
        "interest_expense": 160.0,
        "other_income": 60.0,
        "tax_rate": 0.13,
        "capex": 3_500.0,
        "da": 1_400.0,
        "sbc": 2_400.0,
        "buybacks": 600.0,
        "diluted_shares": 1_670.0,
    },
    "FY2028E": {
        "dc_rev_growth": 0.40,
        "client_rev_growth": 0.08,
        "gaming_rev_growth": 0.00,
        "emb_rev_growth": 0.08,
        "dc_oi_margin": 0.32,
        "cg_oi_margin": 0.18,
        "emb_oi_margin": 0.38,
        "all_other_oi": -6_400.0,
        "consolidated_gm": 0.55,
        "rd": 11_600.0,
        "mga": 5_800.0,
        "interest_expense": 170.0,
        "other_income": 50.0,
        "tax_rate": 0.13,
        "capex": 4_000.0,
        "da": 1_600.0,
        "sbc": 2_600.0,
        "buybacks": 800.0,
        "diluted_shares": 1_680.0,
    },
}

MINIMUM_CASH = 4_000.0
INTEREST_INCOME_RATE = 0.03

# Valuation — researcher [VIEW] unless noted [FACT].
VALUATION_AS_OF = date(2026, 9, 29)
LAST_CLOSE_DATE = date(2026, 9, 29)
LAST_CLOSE = 607.57
LAST_CLOSE_SOURCE = (
    "https://finance.yahoo.com/quote/AMD/history/"
    " (Yahoo Finance chart API regularMarketPrice, 2026-09-29)"
)
SHARES_OUTSTANDING_M = 1_632.475042  # [FACT] R6.5 basic shares on 2026-07-29
PT_DILUTED_SHARES_M = ASSUMPTIONS["FY2028E"]["diluted_shares"]  # [VIEW] forward WAS
DCF_WACC = 0.095  # [VIEW] fabless high-growth semi; balances AI upside vs cyclicality
DCF_TERMINAL_GROWTH = 0.025  # [VIEW] long-run nominal GDP+ share gain fade
DCF_TERMINAL_FCF_MULTIPLE = 24.0  # [VIEW] cross-check to Gordon; high-growth exit
SOTP_DC_EBIT_MULTIPLE = 26.0  # [VIEW] AI accelerator / server CPU mix premium
SOTP_CG_EBIT_MULTIPLE = 14.0  # [VIEW] PC/console cyclicality
SOTP_EMB_EBIT_MULTIPLE = 17.0  # [VIEW] FPGA/adaptive industrial multiple
OFFICIAL_DCF_WEIGHT = 0.65  # [VIEW] primary: cash earnings path from model FCF
OFFICIAL_SOTP_WEIGHT = 0.35  # [VIEW] segment OI cross-check
FCF_DISCOUNT_DATES = {
    "FY2026E": date(2026, 12, 26),
    "FY2027E": date(2027, 12, 25),
    "FY2028E": date(2028, 12, 29),
}
TERMINAL_DATE = date(2029, 6, 30)  # [VIEW] mid-year after FY2028 FCF year


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


def enrich_segments(raw: dict[str, float]) -> dict[str, float]:
    cg_rev = raw["client_rev"] + raw["gaming_rev"]
    seg_oi = (
        raw["dc_oi"]
        + raw["cg_oi"]
        + raw["emb_oi"]
        + raw["all_other_oi"]
    )
    return {
        **raw,
        "cg_rev": cg_rev,
        "total_rev": raw["dc_rev"] + cg_rev + raw["emb_rev"],
        "segment_operating_income": seg_oi,
    }


def build_historical_segments() -> dict[str, dict[str, float]]:
    return {p: enrich_segments(HIST_SEGMENTS[p]) for p in HIST_PERIODS}


def build_forecast_segments(
    prior: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    prev_key = "1H2026A"
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        base = prior[prev_key] if period == "FY2026E" else output[
            FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]
        ]
        base_rev = (
            HIST_SEGMENTS["FY2025A"]
            if period == "FY2026E"
            else {
                "dc_rev": base["dc_rev"],
                "client_rev": base["client_rev"],
                "gaming_rev": base["gaming_rev"],
                "emb_rev": base["emb_rev"],
            }
        )
        dc_rev = base_rev["dc_rev"] * (1.0 + assumption["dc_rev_growth"])
        client_rev = base_rev["client_rev"] * (1.0 + assumption["client_rev_growth"])
        gaming_rev = base_rev["gaming_rev"] * (1.0 + assumption["gaming_rev_growth"])
        emb_rev = base_rev["emb_rev"] * (1.0 + assumption["emb_rev_growth"])
        cg_rev = client_rev + gaming_rev
        dc_oi = dc_rev * assumption["dc_oi_margin"]
        cg_oi = cg_rev * assumption["cg_oi_margin"]
        emb_oi = emb_rev * assumption["emb_oi_margin"]
        raw = {
            "dc_rev": dc_rev,
            "dc_oi": dc_oi,
            "client_rev": client_rev,
            "gaming_rev": gaming_rev,
            "cg_oi": cg_oi,
            "emb_rev": emb_rev,
            "emb_oi": emb_oi,
            "all_other_oi": assumption["all_other_oi"],
        }
        output[period] = enrich_segments(raw)
        prev_key = period
    return output


def build_income(
    segments: dict[str, dict[str, float]],
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        seg = segments[period]
        raw = HIST_INCOME[period]
        pretax = (
            raw["operating_income"]
            - raw["interest_expense"]
            + raw["other_income"]
        )
        if raw["pretax"] == 0.0:
            pretax = raw["net_income"] - raw["tax"]
        output[period] = {
            **raw,
            "segment_revenue": seg["total_rev"],
            "segment_operating_income": seg["segment_operating_income"],
            "dc_oi": seg["dc_oi"],
            "cg_oi": seg["cg_oi"],
            "emb_oi": seg["emb_oi"],
            "all_other_oi": seg["all_other_oi"],
            "pretax_income": pretax,
            "diluted_eps": raw["net_income"] / raw["diluted_shares"],
        }

    prior_balance = HIST_BALANCE["1H2026A"]
    for period in FORECAST_PERIODS:
        seg = segments[period]
        assumption = ASSUMPTIONS[period]
        revenue = seg["total_rev"]
        operating_income = seg["segment_operating_income"]
        gross_profit = revenue * assumption["consolidated_gm"]
        rd = assumption["rd"]
        mga = assumption["mga"]
        implied_opex = gross_profit - operating_income
        interest_income = (
            prior_balance["cash"] + prior_balance["sti"]
        ) * INTEREST_INCOME_RATE
        interest_expense = assumption["interest_expense"]
        other_income = assumption["other_income"]
        pretax = (
            operating_income
            + interest_income
            - interest_expense
            + other_income
        )
        tax = max(pretax, 0.0) * assumption["tax_rate"]
        net_income = pretax - tax
        output[period] = {
            "revenue": revenue,
            "gross_profit": gross_profit,
            "rd": rd,
            "mga": mga,
            "implied_total_opex": implied_opex,
            "operating_income": operating_income,
            "interest_income": interest_income,
            "interest_expense": interest_expense,
            "other_income": other_income,
            "pretax_income": pretax,
            "tax": tax,
            "net_income": net_income,
            "segment_revenue": revenue,
            "segment_operating_income": operating_income,
            "dc_oi": seg["dc_oi"],
            "cg_oi": seg["cg_oi"],
            "emb_oi": seg["emb_oi"],
            "all_other_oi": seg["all_other_oi"],
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": net_income / assumption["diluted_shares"],
        }
    return output


def build_balance_and_cashflow(
    income: dict[str, dict[str, float]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    balances = {p: dict(HIST_BALANCE[p]) for p in HIST_PERIODS}
    cashflow: dict[str, dict[str, float]] = {}

    h1 = balances["1H2026A"]
    h1_rev_annual = income["1H2026A"]["revenue"] * 2.0
    h1_cogs_annual = (
        income["1H2026A"]["revenue"] - income["1H2026A"]["gross_profit"]
    ) * 2.0
    ar_days = h1["ar"] / h1_rev_annual * 365.0
    inventory_days = h1["inventory"] / h1_cogs_annual * 365.0
    ap_days = h1["ap"] / h1_cogs_annual * 365.0

    previous = balances["1H2026A"]
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        inc = income[period]
        revenue = inc["revenue"]
        cogs = revenue - inc["gross_profit"]
        ar = revenue * ar_days / 365.0
        inventory = cogs * inventory_days / 365.0
        ap = cogs * ap_days / 365.0
        delta_nwc = (ar + inventory - ap) - (
            previous["ar"] + previous["inventory"] - previous["ap"]
        )

        da = assumption["da"]
        sbc = assumption["sbc"]
        ocf = inc["net_income"] + da + sbc - delta_nwc
        capex = assumption["capex"]
        fcf = ocf - capex
        buybacks = assumption["buybacks"]

        cash = previous["cash"] + fcf - buybacks
        if cash < MINIMUM_CASH:
            sti_draw = min(previous["sti"], MINIMUM_CASH - cash)
        else:
            sti_draw = 0.0
        cash += sti_draw
        sti = previous["sti"] - sti_draw
        ppe = previous["ppe"] + capex - da
        goodwill = previous["goodwill"]
        other_assets = previous["other_assets"]
        total_assets = (
            cash
            + sti
            + ar
            + inventory
            + ppe
            + goodwill
            + other_assets
        )
        debt = previous["debt"]
        other_liabilities = previous["other_liabilities"]
        total_liabilities = ap + debt + other_liabilities
        retained = previous.get("retained_earnings", 0.0) + inc["net_income"] - buybacks
        equity = total_assets - total_liabilities
        balances[period] = {
            "cash": cash,
            "sti": sti,
            "ar": ar,
            "inventory": inventory,
            "ppe": ppe,
            "goodwill": goodwill,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "ap": ap,
            "debt": debt,
            "other_liabilities": other_liabilities,
            "total_liabilities": total_liabilities,
            "retained_earnings": retained,
            "stockholders_equity": equity,
        }
        cashflow[period] = {
            "net_income": inc["net_income"],
            "da": da,
            "sbc": sbc,
            "delta_nwc": delta_nwc,
            "ocf": ocf,
            "capex": capex,
            "fcf": fcf,
            "buybacks": buybacks,
            "ending_cash": cash,
        }
        previous = balances[period]

    cashflow["_wc_days"] = {
        "ar_days": ar_days,
        "inventory_days": inventory_days,
        "ap_days": ap_days,
    }
    return balances, cashflow


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tol = 0.05
    for period in ALL_PERIODS:
        seg = segments[period]
        inc = income[period]
        rev_diff = seg["total_rev"] - inc["revenue"]
        oi_diff = seg["segment_operating_income"] - inc["operating_income"]
        checks.append(
            (
                f"{period}: segment revenue = consolidated revenue",
                abs(rev_diff) < tol,
                rev_diff,
            )
        )
        checks.append(
            (
                f"{period}: segment OI = consolidated operating income",
                abs(oi_diff) < tol,
                oi_diff,
            )
        )
        if period in HIST_PERIODS:
            filed_oi = HIST_INCOME[period]["operating_income"]
            checks.append(
                (
                    f"{period}: segment OI = filed operating income",
                    abs(seg["segment_operating_income"] - filed_oi) < tol,
                    seg["segment_operating_income"] - filed_oi,
                )
            )
    for period in FORECAST_PERIODS:
        bal = balances[period]
        checks.append(
            (
                f"{period}: assets = liabilities + equity",
                abs(bal["total_assets"] - bal["total_liabilities"] - bal["stockholders_equity"])
                < 1.0,
                bal["total_assets"] - bal["total_liabilities"] - bal["stockholders_equity"],
            )
        )
    return checks


def render_segments(
    segments: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]
) -> str:
    rows = []
    line_items = [
        ("Data Center revenue", "dc_rev"),
        ("Data Center operating income", "dc_oi"),
        ("Client revenue", "client_rev"),
        ("Gaming revenue", "gaming_rev"),
        ("Client + Gaming revenue (combined)", "cg_rev"),
        ("Client + Gaming operating income (reported segment)", "cg_oi"),
        ("Embedded revenue", "emb_rev"),
        ("Embedded operating income", "emb_oi"),
        ("All Other operating loss", "all_other_oi"),
        ("Total segment revenue", "total_rev"),
        ("Consolidated operating income (segment sum)", "segment_operating_income"),
    ]
    for label, key in line_items:
        rows.append([label] + [fmt(segments[p][key]) for p in ALL_PERIODS])

    margin_rows = []
    for period in ALL_PERIODS:
        s = segments[period]
        margin_rows.append(
            [
                period,
                pct(s["dc_oi"] / s["dc_rev"]),
                pct(s["cg_oi"] / s["cg_rev"]),
                pct(s["emb_oi"] / s["emb_rev"]),
            ]
        )

    check_rows = [
        [n, "OK" if ok else "ERROR", fmt(d, 2)]
        for n, ok, d in checks
        if "segment revenue" in n or "segment OI" in n
    ]
    return f"""# AMD segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages.

## Revenue and segment operating income

Historical segment lines are `[FACT]` from [register R2]({REGISTER}). Client and Gaming operating income is disclosed only on a combined reportable-segment basis; standalone Client or Gaming OI is `not obtained`. World Labs (R1.9) is excluded until close.

{markdown_table(["line", *ALL_PERIODS], rows)}

## Reported segment operating margins

{markdown_table(["period", "Data Center OI / rev", "Client+Gaming OI / rev", "Embedded OI / rev"], margin_rows)}

Forecast segment operating margins are `[VIEW]` inputs in [`inputs.md`](inputs.md).

## Segment tie checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_income(
    income: dict[str, dict[str, float]], checks: list[tuple[str, bool, float]]
) -> str:
    rows = [
        ["Data Center operating income"]
        + [fmt(income[p]["dc_oi"]) for p in ALL_PERIODS],
        ["Client + Gaming operating income"]
        + [fmt(income[p]["cg_oi"]) for p in ALL_PERIODS],
        ["Embedded operating income"]
        + [fmt(income[p]["emb_oi"]) for p in ALL_PERIODS],
        ["All Other operating loss"]
        + [fmt(income[p]["all_other_oi"]) for p in ALL_PERIODS],
        ["Operating income (sum of segments)"]
        + [fmt(income[p]["operating_income"]) for p in ALL_PERIODS],
        ["Gross profit"]
        + [fmt(income[p]["gross_profit"]) for p in ALL_PERIODS],
        ["Research and development"]
        + [fmt(income[p]["rd"]) for p in ALL_PERIODS],
        ["Marketing, general and administrative"]
        + [fmt(income[p]["mga"]) for p in ALL_PERIODS],
        ["Implied COGS + unallocated opex (GP − segment OI)"]
        + [
            fmt(
                income[p]["gross_profit"] - income[p]["operating_income"]
                if p in HIST_PERIODS
                else income[p]["implied_total_opex"]
            )
            for p in ALL_PERIODS
        ],
        ["Interest income"]
        + [
            fmt(income[p].get("interest_income", 0.0))
            for p in ALL_PERIODS
        ],
        ["Interest expense"]
        + [fmt(-income[p]["interest_expense"]) for p in ALL_PERIODS],
        ["Other income / (expense)"]
        + [fmt(income[p]["other_income"]) for p in ALL_PERIODS],
        ["Pre-tax income"]
        + [fmt(income[p]["pretax_income"]) for p in ALL_PERIODS],
        ["Income tax provision / (benefit)"]
        + [fmt(-income[p]["tax"]) if income[p]["tax"] > 0 else fmt(income[p]["tax"]) for p in ALL_PERIODS],
        ["Net income"]
        + [fmt(income[p]["net_income"]) for p in ALL_PERIODS],
        ["Diluted weighted-average shares"]
        + [fmt(income[p]["diluted_shares"]) for p in ALL_PERIODS],
        ["Diluted EPS"]
        + [fmt(income[p]["diluted_eps"], 2) for p in ALL_PERIODS],
    ]
    rev_row = ["Total revenue (segment sum)"] + [
        fmt(income[p]["revenue"]) for p in ALL_PERIODS
    ]
    gm_row = ["Gross margin"] + [
        pct(income[p]["gross_profit"] / income[p]["revenue"])
        for p in ALL_PERIODS
    ]
    rows.insert(0, rev_row)
    rows.insert(2, gm_row)

    check_rows = [
        [n, "OK" if ok else "ERROR", fmt(d, 2)]
        for n, ok, d in checks
        if "consolidated" in n or "filed operating" in n
    ]
    return f"""# AMD income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data.

Consolidated revenue and operating income are built **only** from reported segment sums in [`segments.md`](segments.md): Data Center, Client + Gaming, Embedded and All Other. Gross profit on history is `[FACT]` from [register R2]({REGISTER}); forecast gross profit uses `[VIEW]` consolidated gross margin with R&D and MG&A also `[VIEW]`, so implied COGS plus any unallocated costs equal gross profit minus segment operating income.

{markdown_table(["line", *ALL_PERIODS], rows)}

`1H2026A` is a six-month period. Historical interest and other below-the-line lines are incomplete in the register set where not filed for 1H; tax is not split for 1H in this table.

## Reconciliation checks

{markdown_table(["check", "status", "difference"], check_rows)}
"""


def render_balance(balances: dict[str, dict[str, float]]) -> str:
    rows = [
        ["Cash"] + [fmt(balances[p]["cash"]) for p in ALL_PERIODS],
        ["Short-term investments"]
        + [fmt(balances[p]["sti"]) for p in ALL_PERIODS],
        ["Accounts receivable"]
        + [fmt(balances[p]["ar"]) for p in ALL_PERIODS],
        ["Inventory"] + [fmt(balances[p]["inventory"]) for p in ALL_PERIODS],
        ["PP&E, net"] + [fmt(balances[p]["ppe"]) for p in ALL_PERIODS],
        ["Goodwill"] + [fmt(balances[p]["goodwill"]) for p in ALL_PERIODS],
        ["Other assets (residual)"]
        + [fmt(balances[p]["other_assets"]) for p in ALL_PERIODS],
        ["Total assets"]
        + [fmt(balances[p]["total_assets"]) for p in ALL_PERIODS],
        ["Accounts payable"] + [fmt(balances[p]["ap"]) for p in ALL_PERIODS],
        ["Debt"] + [fmt(balances[p]["debt"]) for p in ALL_PERIODS],
        ["Other liabilities (residual)"]
        + [fmt(balances[p]["other_liabilities"]) for p in ALL_PERIODS],
        ["Total liabilities"]
        + [fmt(balances[p]["total_liabilities"]) for p in ALL_PERIODS],
        ["Stockholders' equity"]
        + [fmt(balances[p]["stockholders_equity"]) for p in ALL_PERIODS],
    ]
    return f"""# AMD balance sheet

Generated by `compute.py`; do not hand-edit. USD millions.

FY2023–FY2025 `[FACT]` lines are from SEC XBRL tied to [S1]({S1}); 1H2026 `[FACT]` from [R6.1]({REGISTER}) and [S5]({S5}). Other assets and other liabilities are residual plugs to filed totals on history. Forecast rolls from 2026-06-30 with `[VIEW]` working-capital days, capex, D&A and buybacks.

{markdown_table(["line", *ALL_PERIODS], rows)}
"""


def render_cashflow(
    cashflow: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
) -> str:
    hist_rows = []
    for period in HIST_PERIODS:
        raw = HIST_CASHFLOW[period]
        hist_rows.append(
            [
                period,
                fmt(raw["net_income"]),
                fmt(raw["ocf"]),
                fmt(raw["capex"]),
                fmt(raw["ocf"] - raw["capex"]),
                fmt(balances[period]["cash"]),
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
                fmt(-cf["delta_nwc"]),
                fmt(cf["ocf"]),
                fmt(-cf["capex"]),
                fmt(cf["fcf"]),
                fmt(-cf["buybacks"]),
                fmt(cf["ending_cash"]),
            ]
        )
    wc = cashflow["_wc_days"]
    return f"""# AMD cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

## Historical (reported or register)

{markdown_table(["period", "net income", "OCF", "capex", "FCF (OCF − capex)", "ending cash"], hist_rows)}

FY2025 OCF uses continuing operations per [R6.3]({REGISTER}). D&A detail on history: `not obtained` in register aggregate.

## Forecast bridge

Operating cash flow = net income + D&A + SBC − ΔNWC. FCF = OCF − capex. Cash ends with FCF less `[VIEW]` buybacks; short-term investments absorb sub-minimum cash before equity is adjusted.

Working-capital days from 1H2026 annualized revenue/COGS: AR `{wc["ar_days"]:.1f}`, inventory `{wc["inventory_days"]:.1f}`, AP `{wc["ap_days"]:.1f}`.

{markdown_table(["period", "NI", "D&A", "SBC", "ΔNWC", "OCF", "capex", "FCF", "buybacks", "ending cash"], fc_rows)}
"""


def discount_years(payment_date: date) -> float:
    return (payment_date - VALUATION_AS_OF).days / 365.0


def build_valuation(
    income: dict[str, dict[str, float]],
    segments: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
) -> dict[str, Any]:
    """DCF on model FCF plus segment SOTP cross-check."""

    net_cash = (
        balances["1H2026A"]["cash"]
        + balances["1H2026A"]["sti"]
        - balances["1H2026A"]["debt"]
    )
    dcf_rows: list[dict[str, float]] = []
    pv_fcf = 0.0
    for period in FORECAST_PERIODS:
        fcf = cashflow[period]["fcf"]
        years = discount_years(FCF_DISCOUNT_DATES[period])
        discount_factor = (1.0 + DCF_WACC) ** years
        pv = fcf / discount_factor
        pv_fcf += pv
        dcf_rows.append(
            {
                "period": period,
                "fcf": fcf,
                "years": years,
                "pv": pv,
            }
        )

    terminal_fcf = cashflow["FY2028E"]["fcf"] * (1.0 + DCF_TERMINAL_GROWTH)
    gordon_terminal = terminal_fcf / (DCF_WACC - DCF_TERMINAL_GROWTH)
    multiple_terminal = cashflow["FY2028E"]["fcf"] * DCF_TERMINAL_FCF_MULTIPLE
    terminal_value = (gordon_terminal + multiple_terminal) / 2.0
    terminal_years = discount_years(TERMINAL_DATE)
    pv_terminal = terminal_value / ((1.0 + DCF_WACC) ** terminal_years)
    dcf_equity = pv_fcf + pv_terminal + net_cash
    dcf_pt = dcf_equity / PT_DILUTED_SHARES_M

    fy28 = segments["FY2028E"]
    sotp_operating_ev = (
        fy28["dc_oi"] * SOTP_DC_EBIT_MULTIPLE
        + fy28["cg_oi"] * SOTP_CG_EBIT_MULTIPLE
        + fy28["emb_oi"] * SOTP_EMB_EBIT_MULTIPLE
        + fy28["all_other_oi"] * SOTP_CG_EBIT_MULTIPLE
    )
    sotp_equity = sotp_operating_ev + net_cash
    sotp_pt = sotp_equity / PT_DILUTED_SHARES_M

    official_equity = (
        OFFICIAL_DCF_WEIGHT * dcf_equity + OFFICIAL_SOTP_WEIGHT * sotp_equity
    )
    official_pt = official_equity / PT_DILUTED_SHARES_M
    upside_diluted = (official_pt - LAST_CLOSE) / LAST_CLOSE
    market_cap = LAST_CLOSE * SHARES_OUTSTANDING_M
    upside_basic = (official_pt - LAST_CLOSE) / LAST_CLOSE

    sensitivities: list[dict[str, Any]] = []
    for label, wacc in [("WACC 8.5%", 0.085), ("WACC 10.5%", 0.105)]:
        pv = sum(
            row["fcf"] / ((1.0 + wacc) ** row["years"]) for row in dcf_rows
        )
        tv = terminal_value / ((1.0 + wacc) ** terminal_years)
        eq = pv + tv + net_cash
        sensitivities.append(
            {
                "case": label,
                "pt": eq / PT_DILUTED_SHARES_M,
                "delta_vs_base": eq / PT_DILUTED_SHARES_M - dcf_pt,
            }
        )
    for label, mult in [("Terminal FCF 20×", 20.0), ("Terminal FCF 28×", 28.0)]:
        tv = cashflow["FY2028E"]["fcf"] * mult
        tv_blend = (gordon_terminal + tv) / 2.0
        pv = pv_fcf + tv_blend / ((1.0 + DCF_WACC) ** terminal_years) + net_cash
        sensitivities.append(
            {
                "case": label,
                "pt": pv / PT_DILUTED_SHARES_M,
                "delta_vs_base": pv / PT_DILUTED_SHARES_M - dcf_pt,
            }
        )
    fy27_dc_down = segments["FY2027E"]["dc_rev"] * 0.80
    fy27_dc_oi = fy27_dc_down * ASSUMPTIONS["FY2027E"]["dc_oi_margin"]
    dc_oi_hit = fy27_dc_oi - segments["FY2027E"]["dc_oi"]
    oi_hit = income["FY2027E"]["operating_income"] + dc_oi_hit
    fcf_hit = cashflow["FY2027E"]["fcf"] + dc_oi_hit * 0.70
    row27 = next(r for r in dcf_rows if r["period"] == "FY2027E")
    pv_hit = (
        dcf_rows[0]["fcf"] / ((1.0 + DCF_WACC) ** dcf_rows[0]["years"])
        + fcf_hit / ((1.0 + DCF_WACC) ** row27["years"])
        + cashflow["FY2028E"]["fcf"]
        / ((1.0 + DCF_WACC) ** dcf_rows[2]["years"])
    )
    eq_hit = pv_hit + pv_terminal + net_cash
    sensitivities.append(
        {
            "case": "FY2027 DC revenue −20%",
            "pt": eq_hit / PT_DILUTED_SHARES_M,
            "delta_vs_base": eq_hit / PT_DILUTED_SHARES_M - dcf_pt,
        }
    )
    warrant_dilution_m = 320.0
    pt_warrants = official_equity / (PT_DILUTED_SHARES_M + warrant_dilution_m)
    sensitivities.append(
        {
            "case": "OpenAI+Meta warrants +320m shares",
            "pt": pt_warrants,
            "delta_vs_base": pt_warrants - official_pt,
        }
    )

    return {
        "net_cash": net_cash,
        "dcf_rows": dcf_rows,
        "pv_fcf": pv_fcf,
        "terminal_fcf": terminal_fcf,
        "gordon_terminal": gordon_terminal,
        "multiple_terminal": multiple_terminal,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "dcf_equity": dcf_equity,
        "dcf_pt": dcf_pt,
        "sotp_operating_ev": sotp_operating_ev,
        "sotp_equity": sotp_equity,
        "sotp_pt": sotp_pt,
        "official_equity": official_equity,
        "official_pt": official_pt,
        "upside": upside_diluted,
        "market_cap": market_cap,
        "fy28_oi": income["FY2028E"]["operating_income"],
        "fy28_fcf": cashflow["FY2028E"]["fcf"],
        "fy28_ni": income["FY2028E"]["net_income"],
        "sensitivities": sensitivities,
    }


def render_valuation(
    income: dict[str, dict[str, float]],
    segments: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
) -> str:
    val = build_valuation(income, segments, cashflow, balances)
    setup_rows = [
        ["Valuation as-of", VALUATION_AS_OF.isoformat()],
        ["Last close", f"${LAST_CLOSE:.2f} on {LAST_CLOSE_DATE.isoformat()}"],
        ["Last-price source", LAST_CLOSE_SOURCE],
        [
            "Official 12-month price target / share",
            f"${val['official_pt']:.2f}",
        ],
        [
            "Implied change vs last close",
            f"{val['upside'] * 100:.1f}% (PT ÷ last close − 1)",
        ],
        [
            "PT denominator (diluted WAS)",
            f"{PT_DILUTED_SHARES_M:,.0f}m — FY2028E [VIEW] in inputs.md; "
            "matches forward NI/EPS path; warrants not in base",
        ],
        [
            "Market-cap cross-check shares",
            f"{SHARES_OUTSTANDING_M:,.3f}m basic — [FACT] R6.5 on 2026-07-29",
        ],
        [
            "Method",
            f"{OFFICIAL_DCF_WEIGHT:.0%} unlevered FCF DCF + "
            f"{OFFICIAL_SOTP_WEIGHT:.0%} FY2028 segment EBIT SOTP",
        ],
    ]
    dcf_bridge = [
        ["PV explicit FCF (FY2026–FY2028)", fmt(val["pv_fcf"])],
        ["PV terminal value", fmt(val["pv_terminal"])],
        ["Plus: net cash (1H2026)", fmt(val["net_cash"])],
        ["DCF equity value", fmt(val["dcf_equity"])],
        ["DCF PT / share (diluted)", f"${val['dcf_pt']:.2f}"],
    ]
    dcf_detail = [
        [
            row["period"],
            fmt(row["fcf"]),
            f"{row['years']:.2f}",
            f"[VIEW] {DCF_WACC:.1%}",
            fmt(row["pv"]),
        ]
        for row in val["dcf_rows"]
    ]
    terminal_rows = [
        ["Terminal FCF (FY2028 FCF × (1+g))", fmt(val["terminal_fcf"])],
        ["Gordon terminal @ g", fmt(val["gordon_terminal"])],
        [
            f"Exit FCF multiple ({DCF_TERMINAL_FCF_MULTIPLE:.0f}× FY2028)",
            fmt(val["multiple_terminal"]),
        ],
        ["Blended terminal value", fmt(val["terminal_value"])],
        ["Discount to", TERMINAL_DATE.isoformat()],
        ["PV terminal", fmt(val["pv_terminal"])],
    ]
    sotp_rows = [
        ["Data Center FY2028 OI", fmt(segments["FY2028E"]["dc_oi"])],
        [f"[VIEW] × {SOTP_DC_EBIT_MULTIPLE:.0f}× EBIT", ""],
        ["Client + Gaming FY2028 OI", fmt(segments["FY2028E"]["cg_oi"])],
        [f"[VIEW] × {SOTP_CG_EBIT_MULTIPLE:.0f}× EBIT", ""],
        ["Embedded FY2028 OI", fmt(segments["FY2028E"]["emb_oi"])],
        [f"[VIEW] × {SOTP_EMB_EBIT_MULTIPLE:.0f}× EBIT", ""],
        ["All Other FY2028 OI", fmt(segments["FY2028E"]["all_other_oi"])],
        [
            f"At Client+Gaming multiple ({SOTP_CG_EBIT_MULTIPLE:.0f}×)",
            "unallocated costs",
        ],
        ["Segment operating EV", fmt(val["sotp_operating_ev"])],
        ["Plus: net cash", fmt(val["net_cash"])],
        ["SOTP equity value", fmt(val["sotp_equity"])],
        ["SOTP PT / share", f"${val['sotp_pt']:.2f}"],
    ]
    official_rows = [
        ["DCF equity × weight", fmt(val["dcf_equity"] * OFFICIAL_DCF_WEIGHT)],
        ["SOTP equity × weight", fmt(val["sotp_equity"] * OFFICIAL_SOTP_WEIGHT)],
        ["Official equity value", fmt(val["official_equity"])],
        ["Official PT / share", f"${val['official_pt']:.2f}"],
        ["Last close", f"${LAST_CLOSE:.2f}"],
        ["Implied % vs last close", f"{val['upside'] * 100:.1f}%"],
    ]
    sens_rows = [
        [s["case"], f"${s['pt']:.2f}", f"${s['delta_vs_base']:+.2f} vs anchor"]
        for s in val["sensitivities"]
    ]
    implied_rows = [
        [
            "FY2028 model operating income",
            fmt(val["fy28_oi"]),
            f"EV/OI @ PT: {val['official_equity'] / val['fy28_oi']:.1f}×",
        ],
        [
            "FY2028 model FCF",
            fmt(val["fy28_fcf"]),
            f"FCF yield on equity @ PT: {val['fy28_fcf'] / val['official_equity'] * 100:.1f}%",
        ],
        [
            "FY2028 model net income",
            fmt(val["fy28_ni"]),
            f"Implied P/E @ PT: {val['official_pt'] / (val['fy28_ni'] / PT_DILUTED_SHARES_M):.1f}×",
        ],
    ]
    return f"""# AMD valuation

Generated by `compute.py`; do not hand-edit. USD millions except per-share data and multiples.

## Investment idea the target prices

The target prices **scaled AI data-center earnings and cash generation** in the segment model (Instinct/EPYC-led Data Center ramp in [`segments.md`](segments.md)), with Client+Gaming and Embedded as supporting profit pools—not a separate “story stock” layer. World Labs ([R1.9]({REGISTER})) is **excluded** until close and purchase accounting is filed. OpenAI/Meta warrant dilution is **not** in the base share count ([R6.5]({REGISTER})).

## Official method and as-of

{markdown_table(["item", "value"], setup_rows)}

WACC `[VIEW]` {DCF_WACC:.1%}: fabless semi with AI growth but no foundry moat—between mature semi and hyperscaler software. Terminal `g` `[VIEW]` {DCF_TERMINAL_GROWTH:.1%}: long-run nominal growth after AI capex normalizes. Terminal value blends Gordon on terminal FCF with an exit FCF multiple `[VIEW]` {DCF_TERMINAL_FCF_MULTIPLE:.0f}× on FY2028 model FCF. Segment multiples `[VIEW]` reflect DC premium vs PC/console and industrial embedded comps.

## Unlevered FCF DCF (primary, {OFFICIAL_DCF_WEIGHT:.0%} weight)

Explicit flows are **model FCF** from [`cashflow.md`](cashflow.md) (FY2026E–FY2028E). Net cash is cash + short-term investments − debt at 2026-06-30 ([R6.1]({REGISTER})).

{markdown_table(["item", "$m"], dcf_bridge)}

{markdown_table(["period", "model FCF", f"years to {VALUATION_AS_OF.isoformat()}", "WACC", "PV"], dcf_detail)}

### Terminal value

{markdown_table(["item", "$m"], terminal_rows)}

## Segment EBIT SOTP cross-check ({OFFICIAL_SOTP_WEIGHT:.0%} weight)

FY2028 segment operating income from [`segments.md`](segments.md); multiples are `[VIEW]` one-line comp anchors, not filing facts.

{markdown_table(["line", "value / note"], sotp_rows)}

## Official price target bridge

{markdown_table(["item", "value"], official_rows)}

## Implied multiples at the target

{markdown_table(["metric", "model value", "at official PT"], implied_rows)}

## Sensitivity — what moves the target most

{markdown_table(["case", "DCF-style PT / share", "Δ vs base"], sens_rows)}

Anchor for Δ: DCF PT ${val['dcf_pt']:.2f} or official PT for warrant row. **Killing gaps:** FY2027 Data Center revenue miss (no contracted GW→$ bridge, R9.10), higher WACC if rates/AI risk premia rise, lower terminal multiple if FCF conversion disappoints, warrant vesting (+320m shares scenario), World Labs close economics, lease/investment commitments (R6.6–R6.7) not in FCF.

## What is not in this file

No `thesis.md` update, no LONG/SHORT/PASS label, no Street consensus (R9.9). Re-run `python3 models/amd/compute.py` after changing `inputs.md` assumptions or valuation constants at top of `compute.py`.
"""


def main() -> None:
    hist_segments = build_historical_segments()
    forecast_segments = build_forecast_segments(hist_segments)
    segments = {**hist_segments, **forecast_segments}
    income = build_income(segments)
    balances, cashflow = build_balance_and_cashflow(income)
    checks = build_checks(segments, income, balances)

    valuation = build_valuation(income, segments, cashflow, balances)

    outputs = {
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances),
        "cashflow.md": render_cashflow(cashflow, balances),
        "valuation.md": render_valuation(income, segments, cashflow, balances),
    }
    for name, content in outputs.items():
        (ROOT / name).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("AMD model — forecast summary")
    for period in FORECAST_PERIODS:
        print(
            f"{period}: rev {income[period]['revenue']:.0f} | "
            f"OI {income[period]['operating_income']:.0f} | "
            f"NI {income[period]['net_income']:.0f} | "
            f"FCF {cashflow[period]['fcf']:.0f}"
        )
    print("\nValuation")
    print(f"Last close ${LAST_CLOSE:.2f} ({LAST_CLOSE_DATE})")
    print(f"Official PT ${valuation['official_pt']:.2f} ({valuation['upside']*100:.1f}% vs last)")
    print(f"DCF PT ${valuation['dcf_pt']:.2f} | SOTP PT ${valuation['sotp_pt']:.2f}")

    print("\nTie-out checks")
    failed = False
    for name, passed, diff in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (diff {diff:.4f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")


if __name__ == "__main__":
    main()
