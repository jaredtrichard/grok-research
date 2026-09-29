#!/usr/bin/env python3
"""Alphabet segment three-statement model.

All model arithmetic and generated markdown tables live here. Running this file
rewrites inputs.md, segments.md, income.md, balance.md, cashflow.md, and
valuation.md. It does not create a thesis. USD millions except per-share data
and shares.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import date
from pathlib import Path
from typing import Any, Iterator
from contextlib import contextmanager


ROOT = Path(__file__).resolve().parent
HIST_PERIODS = ["FY2023A", "FY2024A", "FY2025A", "1H2026A"]
FORECAST_PERIODS = ["FY2026E", "FY2027E", "FY2028E"]
ALL_PERIODS = HIST_PERIODS + FORECAST_PERIODS
REGISTER = "../../memory/googl/register.md"
RESEARCH = "../../memory/googl/research.md"


# Raw historical inputs copied from register R2-R7. No historical arithmetic is
# typed into output markdown.
HIST_PRODUCT_REVENUE = {
    "FY2023A": {
        "search": 175_033.0,
        "youtube_ads": 31_510.0,
        "network": 31_312.0,
        "spd": 34_688.0,
        "cloud": 33_088.0,
        "other_bets": 1_527.0,
        "hedges": 236.0,
    },
    "FY2024A": {
        "search": 198_084.0,
        "youtube_ads": 36_147.0,
        "network": 30_359.0,
        "spd": 40_340.0,
        "cloud": 43_229.0,
        "other_bets": 1_648.0,
        "hedges": 211.0,
    },
    "FY2025A": {
        "search": 224_532.0,
        "youtube_ads": 40_367.0,
        "network": 29_792.0,
        "spd": 48_030.0,
        "cloud": 58_705.0,
        "other_bets": 1_537.0,
        "hedges": -127.0,
    },
    "1H2026A": {
        "search": 123_670.0,
        "youtube_ads": 20_938.0,
        "network": 14_274.0,
        "spd": 25_295.0,
        "cloud": 44_796.0,
        "other_bets": 793.0,
        "hedges": -74.0,
    },
}

HIST_SEGMENT_OI = {
    "FY2023A": {
        "services_oi": 95_858.0,
        "cloud_oi": 1_716.0,
        "other_bets_oi": -4_095.0,
        "alphabet_oi": -9_186.0,
    },
    "FY2024A": {
        "services_oi": 121_263.0,
        "cloud_oi": 6_112.0,
        "other_bets_oi": -4_444.0,
        "alphabet_oi": -10_541.0,
    },
    "FY2025A": {
        "services_oi": 139_404.0,
        "cloud_oi": 13_910.0,
        "other_bets_oi": -7_515.0,
        "alphabet_oi": -16_760.0,
    },
    "1H2026A": {
        "services_oi": 80_133.0,
        "cloud_oi": 15_412.0,
        "other_bets_oi": -3_899.0,
        "alphabet_oi": -11_180.0,
    },
}

HIST_INCOME = {
    "FY2023A": {
        "revenue": 307_394.0,
        "cogs": 133_332.0,
        "rd": 45_427.0,
        "sales_marketing": 27_917.0,
        "ga": 16_425.0,
        "operating_income": 84_293.0,
        "other_income": 1_424.0,
        "pretax": 85_717.0,
        "tax": 11_922.0,
        "net_income": 73_795.0,
        "preferred_dividends": 0.0,
        "common_net_income": 73_795.0,
        "diluted_shares": 12_722.0,
        "diluted_eps": 5.80,
    },
    "FY2024A": {
        "revenue": 350_018.0,
        "cogs": 146_306.0,
        "rd": 49_326.0,
        "sales_marketing": 27_808.0,
        "ga": 14_188.0,
        "operating_income": 112_390.0,
        "other_income": 7_425.0,
        "pretax": 119_815.0,
        "tax": 19_697.0,
        "net_income": 100_118.0,
        "preferred_dividends": 0.0,
        "common_net_income": 100_118.0,
        "diluted_shares": 12_447.0,
        "diluted_eps": 8.04,
    },
    "FY2025A": {
        "revenue": 402_836.0,
        "cogs": 162_535.0,
        "rd": 61_087.0,
        "sales_marketing": 28_693.0,
        "ga": 21_482.0,
        "operating_income": 129_039.0,
        "other_income": 29_787.0,
        "pretax": 158_826.0,
        "tax": 26_656.0,
        "net_income": 132_170.0,
        "preferred_dividends": 0.0,
        "common_net_income": 132_170.0,
        "diluted_shares": 12_230.0,
        "diluted_eps": 10.81,
    },
    "1H2026A": {
        "revenue": 229_692.0,
        "cogs": 87_214.0,
        "rd": 35_251.0,
        "sales_marketing": 16_009.0,
        "ga": 10_752.0,
        "operating_income": 80_466.0,
        "other_income": 135_699.0,
        "pretax": 216_165.0,
        "tax": 41_394.0,
        "net_income": 174_771.0,
        "preferred_dividends": 86.0,
        "common_net_income": 174_685.0,
        "diluted_shares": 12_274.0,
        "diluted_eps": 14.24,
    },
}

HIST_BALANCE = {
    "FY2023A": {
        "cash": 24_048.0,
        "marketable": 86_868.0,
        "ar": 47_964.0,
        "inventory": 0.0,
        "other_current_assets": 12_650.0,
        "nonmarketable": 31_008.0,
        "deferred_tax_asset": 12_169.0,
        "ppe": 134_345.0,
        "lease_assets": 14_091.0,
        "goodwill_intangibles": 29_198.0,
        "other_noncurrent_assets": 10_051.0,
        "total_assets": 402_392.0,
        "ap": 7_493.0,
        "accrued_comp": 15_140.0,
        "accrued_current": 46_168.0,
        "accrued_revenue_share": 8_876.0,
        "deferred_revenue": 4_137.0,
        "current_debt": 0.0,
        "long_debt": 11_870.0,
        "tax_payable": 8_474.0,
        "deferred_tax_liability": 0.0,
        "lease_liability": 12_460.0,
        "other_long_liabilities": 4_395.0,
        "total_liabilities": 119_013.0,
        "preferred_apic": 0.0,
        "common_apic": 76_534.0,
        "aoci": -4_402.0,
        "retained_earnings": 211_247.0,
        "total_equity": 283_379.0,
        "shares_out": 12_460.0,
    },
    "FY2024A": {
        "cash": 23_466.0,
        "marketable": 72_191.0,
        "ar": 52_340.0,
        "inventory": 0.0,
        "other_current_assets": 15_714.0,
        "nonmarketable": 37_982.0,
        "deferred_tax_asset": 17_180.0,
        "ppe": 171_036.0,
        "lease_assets": 13_588.0,
        "goodwill_intangibles": 31_885.0,
        "other_noncurrent_assets": 14_874.0,
        "total_assets": 450_256.0,
        "ap": 7_987.0,
        "accrued_comp": 15_069.0,
        "accrued_current": 51_228.0,
        "accrued_revenue_share": 9_802.0,
        "deferred_revenue": 5_036.0,
        "current_debt": 0.0,
        "long_debt": 10_883.0,
        "tax_payable": 8_782.0,
        "deferred_tax_liability": 0.0,
        "lease_liability": 11_691.0,
        "other_long_liabilities": 4_694.0,
        "total_liabilities": 125_172.0,
        "preferred_apic": 0.0,
        "common_apic": 84_800.0,
        "aoci": -4_800.0,
        "retained_earnings": 245_084.0,
        "total_equity": 325_084.0,
        "shares_out": 12_211.0,
    },
    "FY2025A": {
        "cash": 30_708.0,
        "marketable": 96_135.0,
        "ar": 62_886.0,
        "inventory": 2_439.0,
        "other_current_assets": 13_870.0,
        "nonmarketable": 68_687.0,
        "deferred_tax_asset": 9_113.0,
        "ppe": 246_597.0,
        "lease_assets": 15_221.0,
        "goodwill_intangibles": 34_663.0,
        "other_noncurrent_assets": 14_962.0,
        "total_assets": 595_281.0,
        "ap": 12_200.0,
        "accrued_comp": 17_546.0,
        "accrued_current": 55_557.0,
        "accrued_revenue_share": 10_864.0,
        "deferred_revenue": 6_578.0,
        "current_debt": 1_996.0,
        "long_debt": 46_547.0,
        "tax_payable": 9_531.0,
        "deferred_tax_liability": 919.0,
        "lease_liability": 12_744.0,
        "other_long_liabilities": 7_530.0,
        "total_liabilities": 180_016.0,
        "preferred_apic": 0.0,
        "common_apic": 93_126.0,
        "aoci": -1_916.0,
        "retained_earnings": 324_055.0,
        "total_equity": 415_265.0,
        "shares_out": 12_088.0,
    },
    "1H2026A": {
        "cash": 55_911.0,
        "marketable": 186_563.0,
        "ar": 69_175.0,
        "inventory": 9_991.0,
        "other_current_assets": 21_884.0,
        "nonmarketable": 131_461.0,
        "deferred_tax_asset": 1_448.0,
        "ppe": 321_212.0,
        "lease_assets": 17_694.0,
        "goodwill_intangibles": 66_933.0,
        "other_noncurrent_assets": 39_711.0,
        "total_assets": 921_983.0,
        "ap": 20_258.0,
        "accrued_comp": 15_086.0,
        "accrued_current": 73_014.0,
        "accrued_revenue_share": 10_599.0,
        "deferred_revenue": 7_154.0,
        "current_debt": 1_999.0,
        "long_debt": 98_165.0,
        "tax_payable": 11_306.0,
        "deferred_tax_liability": 22_819.0,
        "lease_liability": 14_591.0,
        "other_long_liabilities": 8_511.0,
        "total_liabilities": 281_503.0,
        "preferred_apic": 18_023.0,
        "common_apic": 131_371.0,
        "aoci": -2_285.0,
        "retained_earnings": 493_371.0,
        "total_equity": 640_480.0,
        "shares_out": 12_230.0,
    },
}

HIST_CASHFLOW = {
    "FY2023A": {
        "net_income": 73_795.0,
        "da": 11_946.0,
        "sbc": 22_460.0,
        "deferred_tax": -7_763.0,
        "investment_gain_adjustment": -823.0,
        "ocf": 101_746.0,
        "capex": 32_251.0,
        "acquisitions": 495.0,
        "net_investing": -27_063.0,
        "repurchases": 61_504.0,
        "dividends": 0.0,
        "debt_issuance": 10_790.0,
        "debt_repayment": 11_550.0,
        "net_financing": -72_093.0,
        "fx": -421.0,
        "change_cash": 2_169.0,
    },
    "FY2024A": {
        "net_income": 100_118.0,
        "da": 15_311.0,
        "sbc": 22_785.0,
        "deferred_tax": -5_257.0,
        "investment_gain_adjustment": 2_671.0,
        "ocf": 125_299.0,
        "capex": 52_535.0,
        "acquisitions": 2_931.0,
        "net_investing": -45_536.0,
        "repurchases": 62_222.0,
        "dividends": 7_363.0,
        "debt_issuance": 13_589.0,
        "debt_repayment": 12_701.0,
        "net_financing": -79_733.0,
        "fx": -612.0,
        "change_cash": -582.0,
    },
    "FY2025A": {
        "net_income": 132_170.0,
        "da": 21_136.0,
        "sbc": 24_953.0,
        "deferred_tax": 8_348.0,
        "investment_gain_adjustment": 24_620.0,
        "ocf": 164_713.0,
        "capex": 91_447.0,
        "acquisitions": 1_592.0,
        "net_investing": -120_291.0,
        "repurchases": 45_709.0,
        "dividends": 10_049.0,
        "debt_issuance": 64_564.0,
        "debt_repayment": 32_427.0,
        "net_financing": -37_388.0,
        "fx": 208.0,
        "change_cash": 7_242.0,
    },
    "1H2026A": {
        "net_income": 174_771.0,
        "da": 13_586.0,
        "sbc": 14_708.0,
        "deferred_tax": 27_538.0,
        "investment_gain_adjustment": 135_803.0,
        "ocf": 84_859.0,
        "capex": 80_598.0,
        "acquisitions": 33_697.0,
        "net_investing": -145_822.0,
        "repurchases": 0.0,
        "dividends": 5_231.0,
        "stock_tax_withholding": 12_056.0,
        "debt_issuance": 56_226.0,
        "debt_repayment": 5_253.0,
        "common_issuance": 30_499.0,
        "preferred_issuance": 19_063.0,
        "net_financing": 86_320.0,
        "fx": -154.0,
        "change_cash": 25_203.0,
    },
}


# Researcher-specified forecast. Every assumption is a [VIEW].
ASSUMPTIONS = {
    "FY2026E": {
        "search_growth": 0.160,
        "youtube_growth": 0.120,
        "network_growth": -0.020,
        "spd_growth": 0.160,
        "cloud_revenue": 96_000.0,
        "other_bets_revenue": 1_600.0,
        "hedges": -74.0,
        "services_margin": 0.410,
        "cloud_margin": 0.340,
        "other_bets_oi": -8_500.0,
        "alphabet_oi": -23_000.0,
        "rd": 75_000.0,
        "sales_marketing": 34_000.0,
        "ga": 21_000.0,
        "capex": 200_000.0,
        "da": 30_000.0,
        "sbc": 32_000.0,
        "deferred_tax": 28_500.0,
        "investment_gain": 135_946.0,
        "income_misc": -1_247.0,
        "tax_rate": 0.191,
        "common_dividends": 11_000.0,
        "preferred_dividends": 700.0,
        "stock_tax_withholding": 24_000.0,
        "buybacks": 0.0,
        "diluted_shares": 12_350.0,
        "shares_out": 12_300.0,
    },
    "FY2027E": {
        "search_growth": 0.130,
        "youtube_growth": 0.110,
        "network_growth": -0.030,
        "spd_growth": 0.140,
        "cloud_growth": 0.450,
        "other_bets_revenue": 1_700.0,
        "hedges": 0.0,
        "services_margin": 0.405,
        "cloud_margin": 0.320,
        "other_bets_oi": -8_000.0,
        "alphabet_oi": -25_000.0,
        "rd": 91_000.0,
        "sales_marketing": 41_000.0,
        "ga": 23_000.0,
        "capex": 220_000.0,
        "da": 45_000.0,
        "sbc": 36_000.0,
        "deferred_tax": 0.0,
        "investment_gain": 0.0,
        "income_misc": 0.0,
        "tax_rate": 0.170,
        "common_dividends": 11_500.0,
        "preferred_dividends": 1_188.0,
        "stock_tax_withholding": 16_000.0,
        "buybacks": 0.0,
        "diluted_shares": 12_550.0,
        "shares_out": 12_450.0,
    },
    "FY2028E": {
        "search_growth": 0.110,
        "youtube_growth": 0.100,
        "network_growth": -0.040,
        "spd_growth": 0.120,
        "cloud_growth": 0.300,
        "other_bets_revenue": 2_000.0,
        "hedges": 0.0,
        "services_margin": 0.400,
        "cloud_margin": 0.340,
        "other_bets_oi": -7_000.0,
        "alphabet_oi": -27_000.0,
        "rd": 108_000.0,
        "sales_marketing": 48_000.0,
        "ga": 25_000.0,
        "capex": 210_000.0,
        "da": 62_000.0,
        "sbc": 40_000.0,
        "deferred_tax": 0.0,
        "investment_gain": 0.0,
        "income_misc": 0.0,
        "tax_rate": 0.170,
        "common_dividends": 12_000.0,
        "preferred_dividends": 1_188.0,
        "stock_tax_withholding": 18_000.0,
        "buybacks": 0.0,
        "diluted_shares": 12_750.0,
        "shares_out": 12_600.0,
    },
}

INTEREST_INCOME_RATE = 0.030
INTEREST_EXPENSE_RATE = 0.045
MINIMUM_CASH = 15_000.0

VALUATION_DATE = date(2026, 9, 29)
LAST_PRICE_DATE = date(2026, 9, 29)
LAST_PRICE = 340.92
LAST_PRICE_GOOG = 337.32
LAST_PRICE_SOURCE = (
    "https://finance.yahoo.com/quote/GOOGL/history/"
)
PT_SHARES_M = 12_230.0  # R5.3 common shares outstanding (m), 2026-07-15
DCF_WACC = 0.095  # [VIEW] unlevered cost of capital for mega-cap platform
TERMINAL_EBIT_MULTIPLE = 20.0  # [VIEW] FY2028E operating income exit multiple
TERMINAL_GROWTH_CHECK = 0.025  # [VIEW] Gordon cross-check only
BEAR_WACC = 0.105
BEAR_TERMINAL_MULTIPLE = 16.0
BULL_WACC = 0.085
BULL_TERMINAL_MULTIPLE = 23.0
MID_YEAR_DISCOUNT = [0.5, 1.5, 2.5]
TERMINAL_DISCOUNT_YEARS = 2.5


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


def table(headers: list[str], rows: list[list[Any]]) -> str:
    top = "| " + " | ".join(headers) + " |"
    separator = "|" + "|".join("---" for _ in headers) + "|"
    body = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join([top, separator, *body])


def sum_services(item: dict[str, float]) -> float:
    return item["search"] + item["youtube_ads"] + item["network"] + item["spd"]


def sum_revenue(item: dict[str, float]) -> float:
    return sum_services(item) + item["cloud"] + item["other_bets"] + item["hedges"]


def total_debt(item: dict[str, float]) -> float:
    return item["current_debt"] + item["long_debt"]


def operating_nwc(item: dict[str, float]) -> float:
    return (
        item["ar"]
        + item["inventory"]
        + item["other_current_assets"]
        - item["ap"]
        - item["accrued_comp"]
        - item["accrued_current"]
        - item["accrued_revenue_share"]
        - item["deferred_revenue"]
    )


def enrich_balance(item: dict[str, float]) -> dict[str, float]:
    output = dict(item)
    output["debt"] = total_debt(item)
    output["total_liabilities_equity"] = (
        item["total_liabilities"] + item["total_equity"]
    )
    return output


def build_segments() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    for period in HIST_PERIODS:
        product = dict(HIST_PRODUCT_REVENUE[period])
        oi = HIST_SEGMENT_OI[period]
        services_revenue = sum_services(product)
        revenue = sum_revenue(product)
        operating_income = sum(oi.values())
        output[period] = {
            **product,
            **oi,
            "services_revenue": services_revenue,
            "total_revenue": revenue,
            "operating_income": operating_income,
            "services_margin": oi["services_oi"] / services_revenue,
            "cloud_margin": oi["cloud_oi"] / product["cloud"],
        }

    previous = HIST_PRODUCT_REVENUE["FY2025A"]
    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        search = previous["search"] * (1.0 + assumption["search_growth"])
        youtube = previous["youtube_ads"] * (1.0 + assumption["youtube_growth"])
        network = previous["network"] * (1.0 + assumption["network_growth"])
        spd = previous["spd"] * (1.0 + assumption["spd_growth"])
        cloud = (
            assumption["cloud_revenue"]
            if period == "FY2026E"
            else previous["cloud"] * (1.0 + assumption["cloud_growth"])
        )
        product = {
            "search": search,
            "youtube_ads": youtube,
            "network": network,
            "spd": spd,
            "cloud": cloud,
            "other_bets": assumption["other_bets_revenue"],
            "hedges": assumption["hedges"],
        }
        services_revenue = sum_services(product)
        services_oi = services_revenue * assumption["services_margin"]
        cloud_oi = cloud * assumption["cloud_margin"]
        operating_income = (
            services_oi
            + cloud_oi
            + assumption["other_bets_oi"]
            + assumption["alphabet_oi"]
        )
        output[period] = {
            **product,
            "services_revenue": services_revenue,
            "total_revenue": sum_revenue(product),
            "services_oi": services_oi,
            "cloud_oi": cloud_oi,
            "other_bets_oi": assumption["other_bets_oi"],
            "alphabet_oi": assumption["alphabet_oi"],
            "operating_income": operating_income,
            "services_margin": assumption["services_margin"],
            "cloud_margin": assumption["cloud_margin"],
        }
        previous = product
    return output


def build_model(
    segments: dict[str, dict[str, float]],
) -> tuple[
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
]:
    income = {period: dict(HIST_INCOME[period]) for period in HIST_PERIODS}
    balances = {
        period: enrich_balance(HIST_BALANCE[period]) for period in HIST_PERIODS
    }
    cashflow: dict[str, dict[str, float]] = {
        period: dict(HIST_CASHFLOW[period]) for period in HIST_PERIODS
    }

    latest = balances["1H2026A"]
    ar_ratio = latest["ar"] / (HIST_INCOME["1H2026A"]["revenue"] * 2.0)
    inventory_ratio = latest["inventory"] / (
        HIST_INCOME["1H2026A"]["cogs"] * 2.0
    )
    ap_ratio = latest["ap"] / (HIST_INCOME["1H2026A"]["cogs"] * 2.0)
    revenue_share_ratio = latest["accrued_revenue_share"] / (
        (
            HIST_PRODUCT_REVENUE["1H2026A"]["search"]
            + HIST_PRODUCT_REVENUE["1H2026A"]["youtube_ads"]
            + HIST_PRODUCT_REVENUE["1H2026A"]["network"]
        )
        * 2.0
    )
    deferred_revenue_ratio = latest["deferred_revenue"] / (
        (
            HIST_PRODUCT_REVENUE["1H2026A"]["spd"]
            + HIST_PRODUCT_REVENUE["1H2026A"]["cloud"]
        )
        * 2.0
    )

    for period in FORECAST_PERIODS:
        assumption = ASSUMPTIONS[period]
        segment = segments[period]
        is_fy26 = period == "FY2026E"
        previous = (
            balances["1H2026A"]
            if is_fy26
            else balances[FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]]
        )

        rd = assumption["rd"]
        sales_marketing = assumption["sales_marketing"]
        ga = assumption["ga"]
        opex = rd + sales_marketing + ga
        cogs = segment["total_revenue"] - segment["operating_income"] - opex

        interest_income = (
            2_811.0
            + (previous["cash"] + previous["marketable"])
            * INTEREST_INCOME_RATE
            / 2.0
            if is_fy26
            else (previous["cash"] + previous["marketable"])
            * INTEREST_INCOME_RATE
        )
        interest_expense = (
            1_811.0
            + previous["debt"] * INTEREST_EXPENSE_RATE / 2.0
            if is_fy26
            else previous["debt"] * INTEREST_EXPENSE_RATE
        )
        other_income_before_marks = (
            interest_income - interest_expense + assumption["income_misc"]
        )
        other_income = other_income_before_marks + assumption["investment_gain"]
        pretax = segment["operating_income"] + other_income
        tax = pretax * assumption["tax_rate"]
        net_income = pretax - tax
        common_net_income = net_income - assumption["preferred_dividends"]
        recurring_pretax = segment["operating_income"] + other_income_before_marks
        recurring_tax = max(recurring_pretax, 0.0) * 0.17
        recurring_net_income = recurring_pretax - recurring_tax
        income[period] = {
            "revenue": segment["total_revenue"],
            "cogs": cogs,
            "rd": rd,
            "sales_marketing": sales_marketing,
            "ga": ga,
            "operating_income": segment["operating_income"],
            "interest_income": interest_income,
            "interest_expense": interest_expense,
            "income_misc": assumption["income_misc"],
            "other_income_before_marks": other_income_before_marks,
            "investment_gain": assumption["investment_gain"],
            "other_income": other_income,
            "pretax": pretax,
            "tax": tax,
            "net_income": net_income,
            "preferred_dividends": assumption["preferred_dividends"],
            "common_net_income": common_net_income,
            "recurring_pretax": recurring_pretax,
            "recurring_tax": recurring_tax,
            "recurring_net_income": recurring_net_income,
            "diluted_shares": assumption["diluted_shares"],
            "diluted_eps": common_net_income / assumption["diluted_shares"],
        }

        target = {
            "ar": segment["total_revenue"] * ar_ratio,
            "inventory": cogs * inventory_ratio,
            "other_current_assets": previous["other_current_assets"],
            "ap": cogs * ap_ratio,
            "accrued_comp": previous["accrued_comp"],
            "accrued_current": previous["accrued_current"],
            "accrued_revenue_share": (
                segment["search"] + segment["youtube_ads"] + segment["network"]
            )
            * revenue_share_ratio,
            "deferred_revenue": (segment["spd"] + segment["cloud"])
            * deferred_revenue_ratio,
        }
        target_nwc = (
            target["ar"]
            + target["inventory"]
            + target["other_current_assets"]
            - target["ap"]
            - target["accrued_comp"]
            - target["accrued_current"]
            - target["accrued_revenue_share"]
            - target["deferred_revenue"]
        )
        delta_nwc = target_nwc - operating_nwc(previous)

        roll_net_income = (
            net_income - HIST_INCOME["1H2026A"]["net_income"]
            if is_fy26
            else net_income
        )
        roll_da = (
            assumption["da"] - HIST_CASHFLOW["1H2026A"]["da"]
            if is_fy26
            else assumption["da"]
        )
        roll_sbc = (
            assumption["sbc"] - HIST_CASHFLOW["1H2026A"]["sbc"]
            if is_fy26
            else assumption["sbc"]
        )
        roll_deferred_tax = (
            assumption["deferred_tax"]
            - HIST_CASHFLOW["1H2026A"]["deferred_tax"]
            if is_fy26
            else assumption["deferred_tax"]
        )
        roll_investment_gain = 0.0 if is_fy26 else assumption["investment_gain"]
        roll_ocf = (
            roll_net_income
            + roll_da
            + roll_sbc
            + roll_deferred_tax
            - roll_investment_gain
            - delta_nwc
        )
        roll_capex = (
            assumption["capex"] - HIST_CASHFLOW["1H2026A"]["capex"]
            if is_fy26
            else assumption["capex"]
        )
        roll_common_dividends = (
            assumption["common_dividends"] - HIST_CASHFLOW["1H2026A"]["dividends"]
            if is_fy26
            else assumption["common_dividends"]
        )
        roll_preferred_dividends = (
            assumption["preferred_dividends"]
            if is_fy26
            else assumption["preferred_dividends"]
        )
        roll_withholding = (
            assumption["stock_tax_withholding"]
            - HIST_CASHFLOW["1H2026A"]["stock_tax_withholding"]
            if is_fy26
            else assumption["stock_tax_withholding"]
        )
        roll_buybacks = assumption["buybacks"]

        pre_funding_cash = (
            previous["cash"]
            + roll_ocf
            - roll_capex
            - roll_common_dividends
            - roll_preferred_dividends
            - roll_withholding
            - roll_buybacks
        )
        marketable_sale = min(
            max(MINIMUM_CASH - pre_funding_cash, 0.0),
            previous["marketable"],
        )
        cash_after_sale = pre_funding_cash + marketable_sale
        debt_issuance = max(MINIMUM_CASH - cash_after_sale, 0.0)
        cash = cash_after_sale + debt_issuance

        ppe = previous["ppe"] + roll_capex - roll_da
        common_apic = previous["common_apic"] + roll_sbc - roll_withholding
        retained_earnings = (
            previous["retained_earnings"]
            + roll_net_income
            - roll_common_dividends
            - roll_preferred_dividends
        )
        deferred_tax_liability = (
            previous["deferred_tax_liability"] + roll_deferred_tax
        )
        long_debt = previous["long_debt"] + debt_issuance

        balance = {
            "cash": cash,
            "marketable": previous["marketable"] - marketable_sale,
            "ar": target["ar"],
            "inventory": target["inventory"],
            "other_current_assets": target["other_current_assets"],
            "nonmarketable": previous["nonmarketable"],
            "deferred_tax_asset": previous["deferred_tax_asset"],
            "ppe": ppe,
            "lease_assets": previous["lease_assets"],
            "goodwill_intangibles": previous["goodwill_intangibles"],
            "other_noncurrent_assets": previous["other_noncurrent_assets"],
            "ap": target["ap"],
            "accrued_comp": target["accrued_comp"],
            "accrued_current": target["accrued_current"],
            "accrued_revenue_share": target["accrued_revenue_share"],
            "deferred_revenue": target["deferred_revenue"],
            "current_debt": previous["current_debt"],
            "long_debt": long_debt,
            "tax_payable": previous["tax_payable"],
            "deferred_tax_liability": deferred_tax_liability,
            "lease_liability": previous["lease_liability"],
            "other_long_liabilities": previous["other_long_liabilities"],
            "preferred_apic": previous["preferred_apic"],
            "common_apic": common_apic,
            "aoci": previous["aoci"],
            "retained_earnings": retained_earnings,
            "shares_out": assumption["shares_out"],
        }
        balance["total_assets"] = (
            balance["cash"]
            + balance["marketable"]
            + balance["ar"]
            + balance["inventory"]
            + balance["other_current_assets"]
            + balance["nonmarketable"]
            + balance["deferred_tax_asset"]
            + balance["ppe"]
            + balance["lease_assets"]
            + balance["goodwill_intangibles"]
            + balance["other_noncurrent_assets"]
        )
        balance["total_liabilities"] = (
            balance["ap"]
            + balance["accrued_comp"]
            + balance["accrued_current"]
            + balance["accrued_revenue_share"]
            + balance["deferred_revenue"]
            + balance["long_debt"]
            + balance["tax_payable"]
            + balance["deferred_tax_liability"]
            + balance["lease_liability"]
            + balance["other_long_liabilities"]
        )
        balance["total_equity"] = (
            balance["preferred_apic"]
            + balance["common_apic"]
            + balance["aoci"]
            + balance["retained_earnings"]
        )
        balance["debt"] = balance["current_debt"] + balance["long_debt"]
        balance["total_liabilities_equity"] = (
            balance["total_liabilities"] + balance["total_equity"]
        )
        balances[period] = balance

        annual_ocf = (
            HIST_CASHFLOW["1H2026A"]["ocf"] + roll_ocf if is_fy26 else roll_ocf
        )
        annual_fcf = annual_ocf - assumption["capex"]
        if is_fy26:
            h1_other_investing = (
                HIST_CASHFLOW["1H2026A"]["net_investing"]
                + HIST_CASHFLOW["1H2026A"]["capex"]
                + HIST_CASHFLOW["1H2026A"]["acquisitions"]
            )
            annual_net_investing = (
                -assumption["capex"]
                - HIST_CASHFLOW["1H2026A"]["acquisitions"]
                + h1_other_investing
                + marketable_sale
            )
            h1_other_financing = (
                HIST_CASHFLOW["1H2026A"]["net_financing"]
                - HIST_CASHFLOW["1H2026A"]["common_issuance"]
                - HIST_CASHFLOW["1H2026A"]["preferred_issuance"]
                - HIST_CASHFLOW["1H2026A"]["debt_issuance"]
                + HIST_CASHFLOW["1H2026A"]["debt_repayment"]
                + HIST_CASHFLOW["1H2026A"]["dividends"]
                + HIST_CASHFLOW["1H2026A"]["stock_tax_withholding"]
            )
            annual_net_financing = (
                HIST_CASHFLOW["1H2026A"]["common_issuance"]
                + HIST_CASHFLOW["1H2026A"]["preferred_issuance"]
                + HIST_CASHFLOW["1H2026A"]["debt_issuance"]
                - HIST_CASHFLOW["1H2026A"]["debt_repayment"]
                - assumption["common_dividends"]
                - assumption["preferred_dividends"]
                - assumption["stock_tax_withholding"]
                - assumption["buybacks"]
                + h1_other_financing
                + debt_issuance
            )
            fx = HIST_CASHFLOW["1H2026A"]["fx"]
            acquisitions = HIST_CASHFLOW["1H2026A"]["acquisitions"]
            common_issuance = HIST_CASHFLOW["1H2026A"]["common_issuance"]
            preferred_issuance = HIST_CASHFLOW["1H2026A"][
                "preferred_issuance"
            ]
            debt_issuance_total = (
                HIST_CASHFLOW["1H2026A"]["debt_issuance"] + debt_issuance
            )
            debt_repayment = HIST_CASHFLOW["1H2026A"]["debt_repayment"]
            other_investing = h1_other_investing + marketable_sale
            other_financing = h1_other_financing
        else:
            annual_net_investing = -assumption["capex"] + marketable_sale
            annual_net_financing = (
                debt_issuance
                - assumption["common_dividends"]
                - assumption["preferred_dividends"]
                - assumption["stock_tax_withholding"]
                - assumption["buybacks"]
            )
            fx = 0.0
            acquisitions = 0.0
            common_issuance = 0.0
            preferred_issuance = 0.0
            debt_issuance_total = debt_issuance
            debt_repayment = 0.0
            other_investing = marketable_sale
            other_financing = 0.0
        prior_annual_cash = (
            balances["FY2025A"]["cash"] if is_fy26 else previous["cash"]
        )
        change_cash = cash - prior_annual_cash
        cashflow[period] = {
            "net_income": net_income,
            "da": assumption["da"],
            "sbc": assumption["sbc"],
            "deferred_tax": assumption["deferred_tax"],
            "investment_gain_adjustment": assumption["investment_gain"],
            "delta_nwc": (
                target_nwc
                - (
                    operating_nwc(balances["FY2025A"])
                    if is_fy26
                    else operating_nwc(previous)
                )
            ),
            "ocf": annual_ocf,
            "capex": assumption["capex"],
            "fcf": annual_fcf,
            "acquisitions": acquisitions,
            "other_investing": other_investing,
            "net_investing": annual_net_investing,
            "common_issuance": common_issuance,
            "preferred_issuance": preferred_issuance,
            "debt_issuance": debt_issuance_total,
            "debt_repayment": debt_repayment,
            "stock_tax_withholding": assumption["stock_tax_withholding"],
            "common_dividends": assumption["common_dividends"],
            "preferred_dividends": assumption["preferred_dividends"],
            "repurchases": assumption["buybacks"],
            "other_financing": other_financing,
            "net_financing": annual_net_financing,
            "fx": fx,
            "marketable_sale": marketable_sale,
            "change_cash": change_cash,
            "ending_cash": cash,
        }

    cashflow["_ratios"] = {
        "ar_ratio": ar_ratio,
        "inventory_ratio": inventory_ratio,
        "ap_ratio": ap_ratio,
        "revenue_share_ratio": revenue_share_ratio,
        "deferred_revenue_ratio": deferred_revenue_ratio,
    }
    return income, balances, cashflow


def build_checks(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> list[tuple[str, bool, float]]:
    checks: list[tuple[str, bool, float]] = []
    tolerance = 0.05
    for period in ALL_PERIODS:
        revenue_diff = segments[period]["total_revenue"] - income[period]["revenue"]
        segment_oi_diff = (
            segments[period]["services_oi"]
            + segments[period]["cloud_oi"]
            + segments[period]["other_bets_oi"]
            + segments[period]["alphabet_oi"]
            - income[period]["operating_income"]
        )
        checks.append(
            (
                f"{period}: product revenue sums to company revenue",
                abs(revenue_diff) < tolerance,
                revenue_diff,
            )
        )
        checks.append(
            (
                f"{period}: segment operating income sums to company OI",
                abs(segment_oi_diff) < tolerance,
                segment_oi_diff,
            )
        )
        balance_diff = (
            balances[period]["total_assets"]
            - balances[period]["total_liabilities_equity"]
        )
        checks.append(
            (
                f"{period}: balance sheet balances",
                abs(balance_diff) < tolerance,
                balance_diff,
            )
        )
    for period in FORECAST_PERIODS:
        is_fy26 = period == "FY2026E"
        previous = (
            balances["1H2026A"]
            if is_fy26
            else balances[FORECAST_PERIODS[FORECAST_PERIODS.index(period) - 1]]
        )
        cf = cashflow[period]
        cash_diff = cf["ending_cash"] - balances[period]["cash"]
        checks.append(
            (
                f"{period}: cash-flow ending cash equals balance-sheet cash",
                abs(cash_diff) < tolerance,
                cash_diff,
            )
        )
        expected_ppe = previous["ppe"] + (
            ASSUMPTIONS[period]["capex"]
            - HIST_CASHFLOW["1H2026A"]["capex"]
            if is_fy26
            else ASSUMPTIONS[period]["capex"]
        ) - (
            ASSUMPTIONS[period]["da"] - HIST_CASHFLOW["1H2026A"]["da"]
            if is_fy26
            else ASSUMPTIONS[period]["da"]
        )
        ppe_diff = expected_ppe - balances[period]["ppe"]
        checks.append(
            (
                f"{period}: PP&E roll-forward ties",
                abs(ppe_diff) < tolerance,
                ppe_diff,
            )
        )
        prior_annual_cash = (
            balances["FY2025A"]["cash"] if is_fy26 else previous["cash"]
        )
        cash_bridge = (
            cf["ocf"] + cf["net_investing"] + cf["net_financing"] + cf["fx"]
        )
        bridge_diff = cash_bridge - (balances[period]["cash"] - prior_annual_cash)
        checks.append(
            (
                f"{period}: cash-flow bridge ties",
                abs(bridge_diff) < tolerance,
                bridge_diff,
            )
        )
    return checks


def render_inputs(cashflow: dict[str, dict[str, float]]) -> str:
    revenue_rows = []
    for period in FORECAST_PERIODS:
        item = ASSUMPTIONS[period]
        revenue_rows.append(
            [
                period,
                f"[VIEW] {pct(item['search_growth'])}",
                f"[VIEW] {pct(item['youtube_growth'])}",
                f"[VIEW] {pct(item['network_growth'])}",
                f"[VIEW] {pct(item['spd_growth'])}",
                (
                    f"[VIEW] {fmt(item['cloud_revenue'])}"
                    if period == "FY2026E"
                    else f"[VIEW] {pct(item['cloud_growth'])}"
                ),
                f"[VIEW] {fmt(item['other_bets_revenue'])}",
                f"[VIEW] {fmt(item['hedges'])}",
            ]
        )
    profit_rows = []
    for period in FORECAST_PERIODS:
        item = ASSUMPTIONS[period]
        profit_rows.append(
            [
                period,
                f"[VIEW] {pct(item['services_margin'])}",
                f"[VIEW] {pct(item['cloud_margin'])}",
                f"[VIEW] {fmt(item['other_bets_oi'])}",
                f"[VIEW] {fmt(item['alphabet_oi'])}",
                f"[VIEW] {fmt(item['rd'])}",
                f"[VIEW] {fmt(item['sales_marketing'])}",
                f"[VIEW] {fmt(item['ga'])}",
            ]
        )
    capital_rows = []
    for period in FORECAST_PERIODS:
        item = ASSUMPTIONS[period]
        capital_rows.append(
            [
                period,
                f"[VIEW] {fmt(item['capex'])}",
                f"[VIEW] {fmt(item['da'])}",
                f"[VIEW] {fmt(item['sbc'])}",
                f"[VIEW] {fmt(item['common_dividends'])}",
                f"[VIEW] {fmt(item['preferred_dividends'])}",
                f"[VIEW] {fmt(item['stock_tax_withholding'])}",
                f"[VIEW] {fmt(item['buybacks'])}",
                f"[VIEW] {fmt(item['diluted_shares'])}",
            ]
        )
    ratios = cashflow["_ratios"]
    return f"""# Alphabet model inputs

As of 2026-09-29. USD millions except percentages, per-share data and shares. Generated by `compute.py`; forecast assumptions are researcher `[VIEW]`s, while historicals are `[FACT]`s from the register. `not obtained` is not silently replaced with a fact.

## Source map

| source | model use |
|---|---|
| [Register R2]({REGISTER}#r2--revenue-by-product-family) | product and segment revenue history; click/price direction |
| [Register R3]({REGISTER}#r3--segment-profitability-and-expense-disclosure) | reported segment revenue and operating income |
| [Register R4]({REGISTER}#r4--consolidated-income-statement) | consolidated income statement and shares |
| [Register R5]({REGISTER}#r5--balance-sheet-and-cash-flow) | balance sheet, cash flow, capex, financing and headcount |
| [Register R6/R7]({REGISTER}#r6--cloud-backlog-and-operating-indicators) | Cloud backlog and TAC |
| [Register R8/R9]({REGISTER}#r8--competition-regulation-and-contingencies) | regulatory facts and explicit disclosure gaps |
| [Research driver map]({RESEARCH}#2-segment-driver-trees) | forecast mechanism by product and segment |

## Historical inputs

All FY2023–FY2025 and 1H2026 historical cells in the generated statements are `[FACT]`s from R2–R5. Product-level gross profit, Cloud product splits, YouTube subscription revenue, and segment capex/working capital are `not obtained` (R9.2, R9.5, R9.7); the model does not present them as facts.

## Product-revenue forecast

{table(["period", "Search growth", "YouTube ads growth", "Network growth", "subscriptions/platforms/devices growth", "Cloud revenue / growth", "Other Bets revenue", "hedges"], revenue_rows)}

- **[VIEW] Search:** AI features support query and monetization growth, while deceleration and remedy/TAC risk reduce the growth rate through the forecast. See R2.1–R2.2, R6.4 and R8.2.
- **[VIEW] YouTube ads:** direct-response, brand and living-room monetization sustain growth; engagement and ad-volume series remain `not obtained` (R9.2).
- **[VIEW] Network:** continued AdSense pressure outweighs AdMob and pricing support. See R2.1–R2.2.
- **[VIEW] Subscriptions/platforms/devices:** subscriptions remain the primary driver, but the product split is `not obtained` (R2.3, R9.4).
- **[VIEW] Cloud:** the FY2026 level and FY2027 acceleration reflect R6 backlog and TPU timing; FY2027 includes hardware/mix pressure without inventing a GCP/Workspace/TPU split.

## Segment profit and consolidated opex forecast

{table(["period", "Services OI margin", "Cloud OI margin", "Other Bets OI", "Alphabet-level OI", "R&D", "sales & marketing", "G&A"], profit_rows)}

Reported-segment operating income is forecast directly. Because product/segment COGS and functional opex are `not obtained` (R3.1/R9.7), consolidated forecast cost of revenue is the script-derived reconciliation from segment operating income after the explicit R&D, sales/marketing and G&A assumptions. It is labeled `[DEDUCTED]` in `income.md`, not represented as a disclosed product margin.

## Capital, cash return and shares

{table(["period", "capex", "D&A", "SBC", "common dividends", "preferred dividends", "stock-tax withholding", "buybacks", "diluted WAS"], capital_rows)}

- **[VIEW] Capex:** FY2026 uses the midpoint of the R5.8 guide; FY2027 increases again per management commentary before moderating in FY2028.
- **[VIEW] Buybacks:** zero while infrastructure investment and financing needs remain elevated despite the authorization in R5.2.
- **[VIEW] Shares:** diluted weighted-average shares include SBC and preferred/ATM dilution risk; forecast period-end basic shares are separate balance-sheet assumptions.
- **[VIEW] Investment marks:** FY2026 retains the reported 1H equity-security gain and assumes no 2H remeasurement; FY2027–FY2028 assume zero gains. R4.1.

## Completion assumptions

| input | treatment | class / pointer |
|---|---|---|
| Interest income | 3.0% of beginning cash plus marketable securities; FY2026 adds reported 1H | [VIEW]; R5 |
| Interest expense | 4.5% of beginning debt; FY2026 adds reported 1H | [VIEW]; R5.5 |
| Receivables / revenue | {pct(ratios['ar_ratio'])} | [DEDUCTED] 2026-06-30 run-rate; R5 |
| Inventory / COGS | {pct(ratios['inventory_ratio'])} | [DEDUCTED] 2026-06-30 run-rate; R5 |
| Payables / COGS | {pct(ratios['ap_ratio'])} | [DEDUCTED] 2026-06-30 run-rate; R5 |
| Accrued revenue share / ad revenue | {pct(ratios['revenue_share_ratio'])} | [DEDUCTED] 2026-06-30 run-rate; R5 |
| Deferred revenue / Cloud plus subscriptions revenue | {pct(ratios['deferred_revenue_ratio'])} | [DEDUCTED] 2026-06-30 run-rate; R5 |
| Other balance-sheet lines | hold at 2026-06-30 unless explicitly rolled | [VIEW] |
| Minimum cash | 15,000; sell marketable securities before issuing incremental debt | [VIEW] liquidity policy |

## Gaps

- Product-level Search, YouTube, Network, subscriptions and Cloud profit: `not obtained`.
- Segment COGS, capex, D&A, SBC, assets, liabilities and working capital: `not obtained`.
- Forecast product revenue is therefore built from explicit growth `[VIEW]`s; reported-segment operating income is forecast from explicit margin/loss `[VIEW]`s.
"""


def render_segments(
    segments: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = []
    line_items = [
        ("Google Search & other revenue", "search"),
        ("YouTube ads revenue", "youtube_ads"),
        ("Google Network revenue", "network"),
        ("Google subscriptions, platforms, and devices revenue", "spd"),
        ("Google Services revenue", "services_revenue"),
        ("Google Cloud revenue", "cloud"),
        ("Other Bets revenue", "other_bets"),
        ("Revenue hedging gains / (losses)", "hedges"),
        ("Total revenue", "total_revenue"),
        ("Google Services operating income", "services_oi"),
        ("Google Cloud operating income", "cloud_oi"),
        ("Other Bets operating income / (loss)", "other_bets_oi"),
        ("Alphabet-level activities operating income / (loss)", "alphabet_oi"),
        ("Total operating income", "operating_income"),
    ]
    for label, key in line_items:
        values = []
        for period in ALL_PERIODS:
            rendered = fmt(segments[period][key])
            values.append(
                f"[VIEW] {rendered}" if period in FORECAST_PERIODS else rendered
            )
        rows.append([label, *values])
    margin_rows = []
    for period in ALL_PERIODS:
        margin_rows.append(
            [
                period,
                (
                    f"[DEDUCTED] {pct(segments[period]['services_margin'])}"
                    if period in HIST_PERIODS
                    else f"[VIEW] {pct(segments[period]['services_margin'])}"
                ),
                (
                    f"[DEDUCTED] {pct(segments[period]['cloud_margin'])}"
                    if period in HIST_PERIODS
                    else f"[VIEW] {pct(segments[period]['cloud_margin'])}"
                ),
            ]
        )
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(diff, 2)]
        for name, passed, diff in checks
        if "product revenue" in name or "segment operating income" in name
    ]
    return f"""# Alphabet segment model

Generated by `compute.py`; do not hand-edit. USD millions except percentages. Historical cells are `[FACT]`; forecast cells are `[VIEW]`.

## Product and reported-segment build

{table(["line", *ALL_PERIODS], rows)}

Google Services revenue is the sum of Search & other, YouTube ads, Network, and subscriptions/platforms/devices. Total revenue adds Google Cloud, Other Bets and hedges. Total operating income is the sum of reported Google Services, Google Cloud, Other Bets and Alphabet-level activities; no operating-income plug is used.

## Reported-segment operating margins

{table(["period", "Google Services", "Google Cloud"], margin_rows)}

Product-level operating income is `not obtained`; only reported-segment operating income is modeled. Cloud product revenue and margins, YouTube subscription economics, and Other Bets company-level economics remain `not obtained` (R9.2, R9.5–R9.7).

## Segment checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_income(
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    rows = []
    lines = [
        ("Revenue", "revenue"),
        ("[DEDUCTED] Cost of revenue", "cogs"),
        ("[DEDUCTED] Gross profit", "gross_profit"),
        ("R&D", "rd"),
        ("Sales and marketing", "sales_marketing"),
        ("G&A", "ga"),
        ("Operating income", "operating_income"),
        ("Interest income", "interest_income"),
        ("Interest expense", "interest_expense_negative"),
        ("Other non-operating income / (expense), excluding investment marks", "income_misc"),
        ("Pre-tax income before investment remeasurement", "recurring_pretax"),
        ("Equity investment remeasurement gain", "investment_gain"),
        ("Other income / (expense), net", "other_income"),
        ("Pre-tax income", "pretax"),
        ("Tax provision", "tax"),
        ("Net income", "net_income"),
        ("Preferred dividends", "preferred_dividends"),
        ("Net income available to common", "common_net_income"),
        ("[DEDUCTED] Recurring net income before investment marks", "recurring_net_income"),
        ("Diluted weighted-average shares", "diluted_shares"),
        ("Diluted EPS", "diluted_eps"),
    ]
    for period in ALL_PERIODS:
        item = income[period]
        item["gross_profit"] = item["revenue"] - item["cogs"]
        if period in HIST_PERIODS:
            item.setdefault("interest_income", None)
            item.setdefault("interest_expense_negative", None)
            item.setdefault("income_misc", None)
            item.setdefault("investment_gain", None)
            item.setdefault("recurring_pretax", None)
            item.setdefault("recurring_net_income", None)
            item.setdefault("diluted_eps", item["common_net_income"] / item["diluted_shares"])
        else:
            item["interest_expense_negative"] = -item["interest_expense"]
    for label, key in lines:
        values = []
        for period in ALL_PERIODS:
            value = income[period].get(key)
            rendered = fmt(value, 2 if key == "diluted_eps" else 0)
            if key == "gross_profit":
                rendered = f"[DEDUCTED] {rendered}"
            elif period in FORECAST_PERIODS and key in {
                "cogs",
                "recurring_net_income",
            }:
                rendered = f"[DEDUCTED] {rendered}"
            elif period in FORECAST_PERIODS:
                rendered = f"[VIEW] {rendered}"
            values.append(rendered)
        rows.append([label, *values])
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(diff, 2)]
        for name, passed, diff in checks
        if "segment operating income" in name
    ]
    return f"""# Alphabet income statement

Generated by `compute.py`; do not hand-edit. USD millions except per-share data. Revenue and operating income are built from [`segments.md`](segments.md).

{table(["line", *ALL_PERIODS], rows)}

`1H2026A` is a six-month period. Historical interest and investment-gain components are not reproduced because the register owns the consolidated historical other-income line. Forecast cost of revenue is a transparent `[DEDUCTED]` reconciliation from segment operating income after explicit functional-opex `[VIEW]`s; product gross margins are `not obtained`.

FY2026 retains the reported first-half equity-security remeasurement and assumes no second-half mark. FY2027–FY2028 assume no remeasurement gain. “Recurring net income” excludes that mark and applies the recurring forecast tax rate; it is a model diagnostic, not a filed non-GAAP measure.

## Income checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_balance(
    balances: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    lines = [
        ("Cash and equivalents", "cash"),
        ("Marketable securities", "marketable"),
        ("Accounts receivable", "ar"),
        ("Inventory", "inventory"),
        ("Other current assets", "other_current_assets"),
        ("Non-marketable securities", "nonmarketable"),
        ("Deferred-tax assets", "deferred_tax_asset"),
        ("PP&E, net", "ppe"),
        ("Operating-lease assets", "lease_assets"),
        ("Goodwill and intangibles", "goodwill_intangibles"),
        ("Other non-current assets", "other_noncurrent_assets"),
        ("Total assets", "total_assets"),
        ("Accounts payable", "ap"),
        ("Accrued compensation", "accrued_comp"),
        ("Accrued expenses and other current liabilities", "accrued_current"),
        ("Accrued revenue share", "accrued_revenue_share"),
        ("Deferred revenue", "deferred_revenue"),
        ("Current debt (memo; included in accrued current liabilities)", "current_debt"),
        ("Long-term debt", "long_debt"),
        ("Income taxes payable", "tax_payable"),
        ("Deferred tax liability", "deferred_tax_liability"),
        ("Operating-lease liabilities", "lease_liability"),
        ("Other long-term liabilities", "other_long_liabilities"),
        ("Total liabilities", "total_liabilities"),
        ("Preferred stock and APIC", "preferred_apic"),
        ("Common stock and APIC", "common_apic"),
        ("AOCI", "aoci"),
        ("Retained earnings", "retained_earnings"),
        ("Total equity", "total_equity"),
        ("Total liabilities and equity", "total_liabilities_equity"),
        ("Period-end common shares", "shares_out"),
        ("Diluted WAS used in model", "diluted_shares"),
    ]
    rows = []
    for label, key in lines:
        values = []
        for period in ALL_PERIODS:
            value = (
                income[period]["diluted_shares"]
                if key == "diluted_shares"
                else balances[period].get(key)
            )
            rendered = fmt(value)
            values.append(
                f"[VIEW] {rendered}" if period in FORECAST_PERIODS else rendered
            )
        rows.append([label, *values])
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(diff, 2)]
        for name, passed, diff in checks
        if "balance sheet" in name or "PP&E" in name
    ]
    return f"""# Alphabet balance sheet

Generated by `compute.py`; do not hand-edit. USD millions except shares.

{table(["line", *ALL_PERIODS], rows)}

Historical aggregates come from register R5. FY2023–FY2024 inventory was not separately presented and remains inside other current assets. Forecast receivables, inventory, payables, accrued revenue share and deferred revenue use the run-rate ratios in `inputs.md`; other unmodeled balance-sheet lines are held at the latest filed balance.

PP&E rolls as beginning PP&E plus capex less D&A. APIC rolls by SBC less stock-tax withholding. Retained earnings receives net income less common and preferred dividends. Marketable securities are sold before incremental debt is issued to preserve the `[VIEW]` minimum cash balance.

## Balance checks

{table(["check", "status", "difference"], check_rows)}
"""


def render_cashflow(
    cashflow: dict[str, dict[str, float]],
    checks: list[tuple[str, bool, float]],
) -> str:
    lines = [
        ("Net income", "net_income"),
        ("D&A", "da"),
        ("SBC add-back", "sbc"),
        ("Deferred-tax adjustment", "deferred_tax"),
        ("Less: investment remeasurement gain", "investment_gain_adjustment"),
        ("Less: increase in operating NWC", "delta_nwc"),
        ("Operating cash flow", "ocf"),
        ("Capital expenditures", "capex"),
        ("Free cash flow", "fcf"),
        ("Acquisitions", "acquisitions"),
        ("Other investing / marketable-security sales", "other_investing"),
        ("Net investing cash flow", "net_investing"),
        ("Common-stock issuance", "common_issuance"),
        ("Preferred-stock issuance", "preferred_issuance"),
        ("Debt issuance", "debt_issuance"),
        ("Debt repayment", "debt_repayment"),
        ("Stock-award tax withholding", "stock_tax_withholding"),
        ("Common dividends", "common_dividends"),
        ("Preferred dividends", "preferred_dividends"),
        ("Share repurchases", "repurchases"),
        ("Other financing", "other_financing"),
        ("Net financing cash flow", "net_financing"),
        ("FX effect", "fx"),
        ("Change in cash", "change_cash"),
        ("Ending cash", "ending_cash"),
    ]
    rows = []
    for label, key in lines:
        values = []
        for period in ALL_PERIODS:
            item = cashflow[period]
            if period in HIST_PERIODS:
                if key == "fcf":
                    value = item["ocf"] - item["capex"]
                elif key == "ending_cash":
                    value = HIST_BALANCE[period]["cash"]
                elif key == "common_dividends":
                    value = item.get("dividends")
                else:
                    value = item.get(key)
            else:
                value = item.get(key)
            if key in {
                "investment_gain_adjustment",
                "delta_nwc",
                "capex",
                "acquisitions",
                "debt_repayment",
                "stock_tax_withholding",
                "common_dividends",
                "preferred_dividends",
                "repurchases",
            } and value is not None:
                value = -value
            rendered = fmt(value)
            values.append(
                f"[VIEW] {rendered}" if period in FORECAST_PERIODS else rendered
            )
        rows.append([label, *values])
    check_rows = [
        [name, "OK" if passed else "ERROR", fmt(diff, 2)]
        for name, passed, diff in checks
        if "cash-flow" in name
    ]
    return f"""# Alphabet cash-flow statement

Generated by `compute.py`; do not hand-edit. USD millions.

{table(["line", *ALL_PERIODS], rows)}

Forecast operating cash flow is `net income + D&A + SBC + deferred tax − investment remeasurement gain − Δ operating NWC`. This prevents the non-cash equity mark in R4.1 from being treated as cash generation. Free cash flow is operating cash flow less capex.

FY2026 combines reported 1H cash flow with an explicit 2H roll-forward. The capex assumption is the midpoint of R5.8 guidance. FY2027 capex rises again before moderating in FY2028. Buybacks remain zero; common/preferred dividends and stock-award tax withholding are funded before optional marketable-security sales and incremental debt.

## Cash checks

{table(["check", "status", "difference"], check_rows)}
"""


@contextmanager
def assumption_override(
    patch: dict[str, dict[str, float]],
) -> Iterator[None]:
    saved = deepcopy(ASSUMPTIONS)
    try:
        for period, changes in patch.items():
            ASSUMPTIONS[period].update(changes)
        yield
    finally:
        for period in FORECAST_PERIODS:
            ASSUMPTIONS[period] = saved[period]


def net_cash(balance: dict[str, float]) -> float:
    debt = balance.get("debt", total_debt(balance))
    return balance["cash"] + balance["marketable"] - debt


def unlevered_fcf(
    income: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    period: str,
) -> float:
    tax_rate = ASSUMPTIONS[period]["tax_rate"]
    operating_income = income[period]["operating_income"]
    nopat = operating_income * (1.0 - tax_rate)
    return (
        nopat
        + cashflow[period]["da"]
        - cashflow[period]["capex"]
        - cashflow[period]["delta_nwc"]
    )


def dcf_result(
    income: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    wacc: float,
    terminal_multiple: float,
) -> dict[str, float]:
    pv_explicit = 0.0
    ufcf: dict[str, float] = {}
    for index, period in enumerate(FORECAST_PERIODS):
        value = unlevered_fcf(income, cashflow, period)
        ufcf[period] = value
        discount = MID_YEAR_DISCOUNT[index]
        pv_explicit += value / ((1.0 + wacc) ** discount)
    terminal_ebit = income["FY2028E"]["operating_income"]
    terminal_value = terminal_ebit * terminal_multiple
    pv_terminal = terminal_value / ((1.0 + wacc) ** TERMINAL_DISCOUNT_YEARS)
    operating_ev = pv_explicit + pv_terminal
    bridge = balances["FY2028E"]
    net_cash_fy28 = net_cash(bridge)
    nonmarketable = bridge["nonmarketable"]
    equity_value = operating_ev + net_cash_fy28 + nonmarketable
    pt = equity_value / PT_SHARES_M
    terminal_ufcf = ufcf["FY2028E"]
    gordon_terminal = (
        terminal_ufcf * (1.0 + TERMINAL_GROWTH_CHECK)
    ) / (wacc - TERMINAL_GROWTH_CHECK)
    gordon_ev = pv_explicit + gordon_terminal / (
        (1.0 + wacc) ** TERMINAL_DISCOUNT_YEARS
    )
    gordon_equity = gordon_ev + net_cash_fy28 + nonmarketable
    return {
        "wacc": wacc,
        "terminal_multiple": terminal_multiple,
        "ufcf": ufcf,
        "pv_explicit": pv_explicit,
        "terminal_ebit": terminal_ebit,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "operating_ev": operating_ev,
        "net_cash_fy28": net_cash_fy28,
        "nonmarketable_fy28": nonmarketable,
        "equity_value": equity_value,
        "official_pt": pt,
        "gordon_equity_value": gordon_equity,
        "gordon_pt": gordon_equity / PT_SHARES_M,
    }


def sensitivity_pt(
    income: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    wacc: float,
    terminal_multiple: float,
) -> float:
    return dcf_result(income, cashflow, balances, wacc, terminal_multiple)[
        "official_pt"
    ]


def valuation(
    segments: dict[str, dict[str, float]],
    income: dict[str, dict[str, float]],
    balances: dict[str, dict[str, float]],
    cashflow: dict[str, dict[str, float]],
) -> tuple[str, dict[str, float]]:
    base = dcf_result(
        income, cashflow, balances, DCF_WACC, TERMINAL_EBIT_MULTIPLE
    )
    bear = dcf_result(
        income, cashflow, balances, BEAR_WACC, BEAR_TERMINAL_MULTIPLE
    )
    bull = dcf_result(
        income, cashflow, balances, BULL_WACC, BULL_TERMINAL_MULTIPLE
    )

    filing = HIST_BALANCE["1H2026A"]
    filing_net_cash = net_cash(filing)
    nonmarketable_filing = filing["nonmarketable"]
    market_cap = LAST_PRICE * PT_SHARES_M
    current_operating_ev = market_cap - filing_net_cash - nonmarketable_filing
    residual_per_share = LAST_PRICE - base["official_pt"]
    model_diluted_fy28 = income["FY2028E"]["diluted_shares"]

    wacc_grid = [0.085, 0.090, 0.095, 0.100, 0.105]
    terminal_grid = [16.0, 18.0, 20.0, 22.0, 24.0]
    wacc_terminal_rows = [
        [
            f"${sensitivity_pt(income, cashflow, balances, wacc, terminal):.2f}"
            for terminal in terminal_grid
        ]
        for wacc in wacc_grid
    ]

    search_cases = {
        "Base search growth": 0.0,
        "Search growth −200 bps": -0.02,
        "Search growth +200 bps": 0.02,
    }
    search_rows: list[list[str]] = []
    for label, delta in search_cases.items():
        if delta == 0.0:
            pt = base["official_pt"]
        else:
            patch = {
                period: {"search_growth": ASSUMPTIONS[period]["search_growth"] + delta}
                for period in FORECAST_PERIODS
            }
            with assumption_override(patch):
                seg = build_segments()
                inc, bal, cf = build_model(seg)
                pt = sensitivity_pt(
                    inc, cf, bal, DCF_WACC, TERMINAL_EBIT_MULTIPLE
                )
        search_rows.append([label, f"${pt:.2f}"])

    cloud_cases = {
        "Base cloud margin": 0.0,
        "Cloud margin −300 bps": -0.03,
        "Cloud margin +300 bps": 0.03,
    }
    cloud_rows: list[list[str]] = []
    for label, delta in cloud_cases.items():
        if delta == 0.0:
            pt = base["official_pt"]
        else:
            patch = {
                period: {"cloud_margin": ASSUMPTIONS[period]["cloud_margin"] + delta}
                for period in FORECAST_PERIODS
            }
            with assumption_override(patch):
                seg = build_segments()
                inc, bal, cf = build_model(seg)
                pt = sensitivity_pt(
                    inc, cf, bal, DCF_WACC, TERMINAL_EBIT_MULTIPLE
                )
        cloud_rows.append([label, f"${pt:.2f}"])

    capex_cases = {
        "Base capex": 0.0,
        "Capex +10% all years": 0.10,
        "Capex −10% all years": -0.10,
    }
    capex_rows: list[list[str]] = []
    for label, capex_pct in capex_cases.items():
        if capex_pct == 0.0:
            pt = base["official_pt"]
        else:
            patch = {
                period: {
                    "capex": ASSUMPTIONS[period]["capex"] * (1.0 + capex_pct)
                }
                for period in FORECAST_PERIODS
            }
            with assumption_override(patch):
                seg = build_segments()
                inc, bal, cf = build_model(seg)
                pt = sensitivity_pt(
                    inc, cf, bal, DCF_WACC, TERMINAL_EBIT_MULTIPLE
                )
        capex_rows.append([label, f"${pt:.2f}"])

    ufcf_rows = [
        [
            period,
            fmt(income[period]["operating_income"], 1),
            pct(ASSUMPTIONS[period]["tax_rate"]),
            fmt(base["ufcf"][period], 1),
            f"{MID_YEAR_DISCOUNT[index]:.1f}",
            fmt(
                base["ufcf"][period]
                / ((1.0 + DCF_WACC) ** MID_YEAR_DISCOUNT[index]),
                1,
            ),
        ]
        for index, period in enumerate(FORECAST_PERIODS)
    ]

    tape_multiples: dict[str, float] = {}
    for period in ("FY2026E", "FY2028E"):
        tape_multiples[f"{period}_rev"] = (
            current_operating_ev / income[period]["revenue"]
        )
        tape_multiples[f"{period}_oi"] = (
            current_operating_ev / income[period]["operating_income"]
        )
        tape_multiples[f"{period}_recurring_ni"] = (
            current_operating_ev / income[period]["recurring_net_income"]
        )

    comps = [
        ["GOOGL", f"${LAST_PRICE:.2f}", "8.93x", "17.7x", LAST_PRICE_DATE.isoformat(), LAST_PRICE_SOURCE],
        ["GOOG", f"${LAST_PRICE_GOOG:.2f}", "not obtained", "not obtained", LAST_PRICE_DATE.isoformat(), LAST_PRICE_SOURCE.replace("GOOGL", "GOOG")],
        ["META", "$738.79", "6.59x", "not obtained", "2026-09-29", "https://www.financecharts.com/compare/META,GOOGL,MSFT,AAPL/value/ev-to-sales"],
        ["MSFT", "$508.96", "11.55x", "not obtained", "2026-08-07", "https://tgmcharts.com/stocks/MSFT/ev-sales"],
        ["AMZN", "$246.67", "4.05x", "not obtained", "2026-08-07", "https://tgmcharts.com/stocks/MSFT/ev-sales"],
        ["AAPL", "$329.40", "10.00x", "not obtained", "2026-08-07", "https://tgmcharts.com/stocks/MSFT/ev-sales"],
    ]
    googl_model_ev_sales_fy28 = base["operating_ev"] / income["FY2028E"]["revenue"]
    googl_model_ev_oi_fy28 = base["operating_ev"] / income["FY2028E"]["operating_income"]

    content = f"""# Alphabet valuation

At the ${LAST_PRICE:.2f} Class A last close, the official operating DCF values recurring cash generation and a FY2028 operating-income exit multiple, then adds filing-balance net liquidity and non-marketable investments at modeled carrying value. The R4.1 equity-security remeasurement is excluded from unlevered free cash flow and from the operating-income path used for terminal value.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | {VALUATION_DATE.isoformat()} |
| Last close (Class A) | ${LAST_PRICE:.2f} on {LAST_PRICE_DATE.isoformat()} |
| Class C reference close | ${LAST_PRICE_GOOG:.2f} on {LAST_PRICE_DATE.isoformat()} |
| Last-price source | [Yahoo Finance historical]({LAST_PRICE_SOURCE}) |
| PT denominator | {fmt(PT_SHARES_M, 3)} million shares outstanding (R5.3, 2026-07-15) |
| Model diluted WAS FY2028E | {fmt(model_diluted_fy28, 1)} million (reference only) |
| Method | Unlevered FCF DCF (FY2026E–FY2028E) + FY2028E EBIT exit multiple |

## Key `[VIEW]` assumptions

| assumption | value | brief justification |
|---|---|---|
| WACC | {pct(DCF_WACC)} | Mega-cap platform with net liquidity; beta near market; no operating leverage from the Q2 equity mark. |
| Terminal value | {TERMINAL_EBIT_MULTIPLE:.1f}× FY2028E operating income | Premium to current tape-implied operating EV / FY2028E OI (~{tape_multiples['FY2028E_oi']:.1f}×) but below peak AI rerating; anchors on recurring segment earnings. |
| Gordon cross-check | {pct(TERMINAL_GROWTH_CHECK)} perpetual growth on FY2028E UFCF | Sanity check only; capex-heavy years make Gordon unreliable as the primary terminal. |
| Investment marks | Zero remeasurement FY2027E–FY2028E | Matches income.md; R4.1 treated as non-operating. |
| Non-marketable securities | Modeled flat at R2 filing carrying value | Separates operating DCF from equity stakes; not marked up again in the DCF. |

## What the tape must be paying for

| item | formula | $m or multiple |
|---|---|---|
| Last-price market capitalization | Last close × R5.3 shares | {fmt(market_cap, 1)} |
| 2026-06-30 net cash | Cash + marketable − debt (R2) | {fmt(filing_net_cash, 1)} |
| Non-marketable securities (carrying) | R2 balance sheet | {fmt(nonmarketable_filing, 1)} |
| Last-price operating EV | Market cap − net cash − non-marketable | {fmt(current_operating_ev, 1)} |
| Operating EV / FY2026E revenue | Tape operating EV ÷ model revenue | {tape_multiples['FY2026E_rev']:.1f}× |
| Operating EV / FY2028E revenue | Tape operating EV ÷ model revenue | {tape_multiples['FY2028E_rev']:.1f}× |
| Operating EV / FY2028E operating income | Tape operating EV ÷ model OI | {tape_multiples['FY2028E_oi']:.1f}× |
| Operating EV / FY2028E recurring net income | Tape operating EV ÷ recurring NI | {tape_multiples['FY2028E_recurring_ni']:.1f}× |

The tape’s operating EV embeds faster capex normalization and/or a higher terminal multiple than the base DCF: FY2026–FY2027 model unlevered FCF is deeply negative while Search and Cloud operating income still compound. The Q2 equity mark inflates reported net income but is stripped from operating cash flow in `cashflow.md` and from this DCF.

## Unlevered FCF bridge

Unlevered FCF = operating income × (1 − forecast cash tax rate) + D&A − capex − Δ operating NWC. Tax is applied to operating income only, not to R4.1 remeasurement.

{table(["period", "operating income", "cash tax rate", "[VIEW] UFCF", "mid-year t", "PV @ WACC"], ufcf_rows)}

## Operating DCF and equity bridge

| item | basis | $m except per share |
|---|---|---|
| PV explicit FY2026E–FY2028E UFCF | Mid-year discount at {pct(DCF_WACC)} | {fmt(base['pv_explicit'], 1)} |
| FY2028E operating income | income.md recurring path | {fmt(base['terminal_ebit'], 1)} |
| Terminal EV / EBIT | [VIEW] | {TERMINAL_EBIT_MULTIPLE:.1f}× |
| Terminal value | FY2028E OI × multiple | {fmt(base['terminal_value'], 1)} |
| PV terminal (t = {TERMINAL_DISCOUNT_YEARS:.1f}y) | Discounted at WACC | {fmt(base['pv_terminal'], 1)} |
| **Operating enterprise value** | PV explicit + PV terminal | **{fmt(base['operating_ev'], 1)}** |
| Plus FY2028E net cash | cash + marketable − debt | {fmt(base['net_cash_fy28'], 1)} |
| Plus FY2028E non-marketable securities | Balance sheet carrying value | {fmt(base['nonmarketable_fy28'], 1)} |
| **Official equity value** | Operating EV + net cash + investments | **{fmt(base['equity_value'], 1)}** |
| Shares outstanding (m) | R5.3 | {fmt(PT_SHARES_M, 3)} |
| **Official 12-month PT / share** | Equity value ÷ R5.3 shares | **${base['official_pt']:.2f}** |

Preferred stock (R5.4) is reflected in the balance sheet and dividends but mandatory-convertible conversion terms into common are **not obtained**; the PT denominator uses filed common shares outstanding, not fully converted preferred. Model diluted WAS ({fmt(model_diluted_fy28, 1)}m FY2028E) is shown for comparison.

## Gordon terminal cross-check (non-official)

| item | value |
|---|---|
| FY2028E UFCF | {fmt(base['ufcf']['FY2028E'], 1)} |
| [VIEW] perpetual growth | {pct(TERMINAL_GROWTH_CHECK)} |
| Implied Gordon equity value | {fmt(base['gordon_equity_value'], 1)} |
| Implied Gordon PT / share | ${base['gordon_pt']:.2f} |

Low near-term UFCF makes Gordon understate a capex cycle; the official terminal remains the EBIT exit multiple.

## Checks — not additional official targets

| check | method | value / share |
|---|---|---|
| Bear | WACC {pct(BEAR_WACC)} + {BEAR_TERMINAL_MULTIPLE:.0f}× FY2028E OI | ${bear['official_pt']:.2f} |
| Bull | WACC {pct(BULL_WACC)} + {BULL_TERMINAL_MULTIPLE:.0f}× FY2028E OI | ${bull['official_pt']:.2f} |
| Gordon cross-check | {pct(TERMINAL_GROWTH_CHECK)} on FY2028E UFCF | ${base['gordon_pt']:.2f} |

**[DEDUCTED] Tape residual per share:** `${LAST_PRICE:.2f} − official DCF = ${residual_per_share:.2f}`. Positive residual means the last price exceeds the base operating DCF on these `[VIEW]`s; it is not an instruction to raise or lower the model.

## Killing sensitivities

### WACC vs FY2028E EBIT exit multiple

{table(["WACC \\\\ multiple"] + [f"{multiple:.0f}×" for multiple in terminal_grid], [[f"{wacc*100:.1f}%", *row] for wacc, row in zip(wacc_grid, wacc_terminal_rows)])}

### Search growth (all forecast years)

{table(["case", "official PT / share"], search_rows)}

### Cloud segment margin (all forecast years)

{table(["case", "official PT / share"], cloud_rows)}

### Capex (all forecast years)

{table(["case", "official PT / share"], capex_rows)}

## Comparable-company snapshot (check only)

Trailing EV/Sales from third-party screens; prices on {LAST_PRICE_DATE.isoformat()} from Yahoo except where noted. GOOGL model-implied FY2028E operating EV / revenue = {googl_model_ev_sales_fy28:.1f}×; operating EV / FY2028E OI = {googl_model_ev_oi_fy28:.1f}×.

{table(["company", "last close", "EV / Sales", "EV / FY2028E model OI", "as-of", "source"], comps)}

Peer multiples mix trailing revenue with different fiscal calendars and include non-ad businesses; use as a framing check only.

## What would move the official value

- A sourced change to FY2026–FY2028 Search, YouTube, Cloud or capex `[VIEW]` paths in `inputs.md`.
- A change to WACC or the FY2028E EBIT exit multiple.
- A change to net cash or non-marketable carrying values on the forecast balance sheet.
- Preferred conversion terms (R5.4) that shift the share denominator materially.

## Blockers

- Mandatory-convertible preferred conversion ratio and fully diluted share count at conversion are **not obtained** in the register (R5.4); PT uses R5.3 outstanding shares with disclosure only.
- Peer EV/EBIT is **not obtained** on a consistent basis across the comp set; EV/Sales is shown where sourced.
"""
    summary = {
        "official_pt": base["official_pt"],
        "operating_ev": base["operating_ev"],
        "equity_value": base["equity_value"],
        "wacc": DCF_WACC,
        "terminal_multiple": TERMINAL_EBIT_MULTIPLE,
        "residual": residual_per_share,
        "bear_pt": bear["official_pt"],
        "bull_pt": bull["official_pt"],
    }
    return content, summary


def main() -> None:
    segments = build_segments()
    income, balances, cashflow = build_model(segments)
    checks = build_checks(segments, income, balances, cashflow)
    valuation_markdown, valuation_summary = valuation(
        segments, income, balances, cashflow
    )

    outputs = {
        "inputs.md": render_inputs(cashflow),
        "segments.md": render_segments(segments, checks),
        "income.md": render_income(income, checks),
        "balance.md": render_balance(balances, income, checks),
        "cashflow.md": render_cashflow(cashflow, checks),
        "valuation.md": valuation_markdown,
    }
    for filename, content in outputs.items():
        (ROOT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")

    print("Alphabet model outputs")
    print("period | revenue | operating income | FCF | diluted shares")
    for period in FORECAST_PERIODS:
        print(
            f"{period} | {income[period]['revenue']:.1f} | "
            f"{income[period]['operating_income']:.1f} | "
            f"{cashflow[period]['fcf']:.1f} | "
            f"{income[period]['diluted_shares']:.1f}"
        )
    print("\nTie-out checks")
    failed = False
    for name, passed, difference in checks:
        status = "OK" if passed else "ERROR"
        print(f"{status}: {name} (difference {difference:.6f})")
        failed = failed or not passed
    if failed:
        raise SystemExit("One or more model checks failed")

    print("\nValuation")
    print(f"WACC | {pct(valuation_summary['wacc'])}")
    print(f"Terminal EBIT multiple | {valuation_summary['terminal_multiple']:.1f}x")
    print(f"Operating EV | ${valuation_summary['operating_ev']:.1f}m")
    print(f"Official 12-month PT | ${valuation_summary['official_pt']:.2f}")
    print(f"[DEDUCTED] Tape residual | ${valuation_summary['residual']:.2f}")
    print(f"Bear check | ${valuation_summary['bear_pt']:.2f}")
    print(f"Bull check | ${valuation_summary['bull_pt']:.2f}")


if __name__ == "__main__":
    main()
