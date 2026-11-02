"""
PF (Profit Factor & Pricing Factor) calculation engine.
Provides calculations for:
1. Profit Factor (Trading/Operational: Gross Profit / Gross Loss)
2. Pricing Factor (Managed Pricing: Selling Price / Unit Cost, Markups, Margins)
"""

from typing import Optional
from pydantic import BaseModel


class ProfitFactorResult(BaseModel):
    gross_profit: float
    gross_loss: float
    net_profit: float
    profit_factor: float
    is_profitable: bool
    rating: str
    interpretation: str


class PricingFactorResult(BaseModel):
    unit_cost: float
    selling_price: float
    pricing_factor: float
    markup_percent: float
    gross_margin_percent: float
    unit_margin: float
    rating: str
    interpretation: str


def calculate_profit_factor(gross_profit: float, gross_loss: float) -> ProfitFactorResult:
    """
    Calculate Profit Factor: Gross Profit / Gross Loss.

    :param gross_profit: Total positive gains/profits (>= 0).
    :param gross_loss: Total losses incurred (>= 0).
    """
    if gross_profit < 0:
        raise ValueError("Gross profit cannot be negative.")
    if gross_loss < 0:
        raise ValueError("Gross loss cannot be negative.")

    net_profit = gross_profit - gross_loss

    if gross_loss == 0:
        if gross_profit == 0:
            pf = 0.0
            rating = "Neutral"
            interpretation = "No activity or gains/losses recorded."
        else:
            pf = float("inf")
            rating = "Flawless"
            interpretation = "Infinity: Zero losses with positive gross gains."
    else:
        pf = gross_profit / gross_loss
        if pf >= 3.0:
            rating = "Exceptional"
            interpretation = f"PF of {pf:.2f}: Outstanding performance, profits vastly outweigh losses."
        elif pf >= 2.0:
            rating = "Very Strong"
            interpretation = f"PF of {pf:.2f}: Highly profitable and resilient margin safety buffer."
        elif pf >= 1.5:
            rating = "Healthy"
            interpretation = f"PF of {pf:.2f}: Solid commercial profitability above benchmark standard."
        elif pf >= 1.0:
            rating = "Marginal"
            interpretation = f"PF of {pf:.2f}: Barely profitable; vulnerable to cost or loss spikes."
        else:
            rating = "Unprofitable"
            interpretation = f"PF of {pf:.2f}: Losses exceed gross gains. Strategy is losing capital."

    display_pf = 999.99 if pf == float("inf") else round(pf, 2)

    return ProfitFactorResult(
        gross_profit=round(gross_profit, 2),
        gross_loss=round(gross_loss, 2),
        net_profit=round(net_profit, 2),
        profit_factor=display_pf,
        is_profitable=net_profit > 0,
        rating=rating,
        interpretation=interpretation,
    )


def calculate_pricing_factor(
    unit_cost: float,
    selling_price: Optional[float] = None,
    target_pricing_factor: Optional[float] = None,
) -> PricingFactorResult:
    """
    Calculate or apply Pricing Factor (Price / Cost multiplier).

    :param unit_cost: Cost to acquire or produce one unit (> 0).
    :param selling_price: Current or proposed selling price.
    :param target_pricing_factor: Desired pricing multiplier (e.g. 1.8 for 1.8x cost).
    """
    if unit_cost <= 0:
        raise ValueError("Unit cost must be greater than zero.")

    if selling_price is not None and selling_price > 0:
        pf = selling_price / unit_cost
        price = selling_price
    elif target_pricing_factor is not None and target_pricing_factor > 0:
        pf = target_pricing_factor
        price = unit_cost * target_pricing_factor
    else:
        raise ValueError("Either selling_price or target_pricing_factor must be provided and > 0.")

    markup_percent = (pf - 1.0) * 100.0
    unit_margin = price - unit_cost
    gross_margin_percent = (unit_margin / price) * 100.0

    if pf >= 3.0:
        rating = "Premium / High-Tier"
        interpretation = f"{pf:.2f}x cost multiplier represents premium luxury or SaaS/software margins."
    elif pf >= 2.0:
        rating = "Keystone / Strong"
        interpretation = f"{pf:.2f}x cost matches standard keystone retail markup (50%+ gross margin)."
    elif pf >= 1.4:
        rating = "Standard Commercial"
        interpretation = f"{pf:.2f}x cost indicates competitive wholesale or manufactured goods pricing."
    elif pf >= 1.1:
        rating = "Low-Margin High-Volume"
        interpretation = f"{pf:.2f}x cost fits commodity or high-turnover grocery/discount commerce."
    elif pf >= 1.0:
        rating = "Razor-Thin"
        interpretation = f"{pf:.2f}x cost yields negligible profit margin; highly vulnerable to overhead."
    else:
        rating = "Negative Margin"
        interpretation = f"{pf:.2f}x cost sells below cost of production (loss leader)."

    return PricingFactorResult(
        unit_cost=round(unit_cost, 2),
        selling_price=round(price, 2),
        pricing_factor=round(pf, 2),
        markup_percent=round(markup_percent, 2),
        gross_margin_percent=round(gross_margin_percent, 2),
        unit_margin=round(unit_margin, 2),
        rating=rating,
        interpretation=interpretation,
    )
