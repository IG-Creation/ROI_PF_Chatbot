"""
ROI (Return on Investment) calculation engine.
Provides calculations for simple ROI, annualized ROI, payback period, and NPV.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class ROIResult(BaseModel):
    initial_cost: float
    total_gain: float
    net_profit: float
    roi_percent: float
    annualized_roi_percent: Optional[float] = None
    payback_years: Optional[float] = None
    interpretation: str
    is_profitable: bool


class NPVResult(BaseModel):
    initial_investment: float
    discount_rate_percent: float
    cash_flows: List[float]
    npv: float
    is_viable: bool
    interpretation: str


def calculate_roi(
    cost: float,
    gain: float,
    years: Optional[float] = None,
    annual_inflow: Optional[float] = None,
) -> ROIResult:
    """
    Calculate Return on Investment.

    :param cost: Total initial investment / cost incurred (> 0).
    :param gain: Total final value or total revenue / return generated.
    :param years: Optional duration in years for annualized calculation.
    :param annual_inflow: Optional average annual positive cash inflow for payback period.
    """
    if cost <= 0:
        raise ValueError("Initial cost must be greater than zero.")

    net_profit = gain - cost
    roi_percent = (net_profit / cost) * 100.0

    annualized_roi_percent = None
    if years and years > 0:
        # Annualized ROI formula: ((gain / cost) ** (1 / years) - 1) * 100
        # If gain is positive:
        if gain > 0:
            annualized_roi_percent = ((gain / cost) ** (1.0 / years) - 1.0) * 100.0
        else:
            annualized_roi_percent = -100.0

    payback_years = None
    if annual_inflow and annual_inflow > 0:
        payback_years = cost / annual_inflow
    elif years and years > 0 and net_profit > 0:
        annual_avg = net_profit / years
        payback_years = cost / (cost / years + annual_avg) if (cost / years + annual_avg) > 0 else None

    # Interpretation
    is_profitable = net_profit > 0
    if roi_percent > 100:
        interpretation = "Exceptional return: the investment more than doubled initial outlay."
    elif roi_percent > 25:
        interpretation = "Strong positive return with healthy capital efficiency."
    elif roi_percent > 0:
        interpretation = "Modest positive return; investment yielded a net gain."
    elif roi_percent == 0:
        interpretation = "Break-even: investment neither gained nor lost value."
    else:
        interpretation = "Negative return: investment produced a net loss."

    return ROIResult(
        initial_cost=round(cost, 2),
        total_gain=round(gain, 2),
        net_profit=round(net_profit, 2),
        roi_percent=round(roi_percent, 2),
        annualized_roi_percent=round(annualized_roi_percent, 2) if annualized_roi_percent is not None else None,
        payback_years=round(payback_years, 2) if payback_years is not None else None,
        interpretation=interpretation,
        is_profitable=is_profitable,
    )


def calculate_npv(
    initial_investment: float,
    discount_rate_percent: float,
    cash_flows: List[float],
) -> NPVResult:
    """
    Calculate Net Present Value (NPV).

    :param initial_investment: Upfront capital outlay (positive float).
    :param discount_rate_percent: Annual discount/hurdle rate in percent (e.g. 8.0 for 8%).
    :param cash_flows: Projected net cash flows for successive periods (years).
    """
    if discount_rate_percent < -100:
        raise ValueError("Discount rate cannot be less than -100%.")

    r = discount_rate_percent / 100.0
    present_values = []
    for t, flow in enumerate(cash_flows, start=1):
        pv = flow / ((1.0 + r) ** t)
        present_values.append(pv)

    npv = sum(present_values) - initial_investment
    is_viable = npv > 0

    if npv > 0:
        interpretation = f"Positive NPV of ${round(npv, 2):,}. The project adds net economic value above hurdle rate."
    elif npv == 0:
        interpretation = "Zero NPV. The project exactly meets the required rate of return."
    else:
        interpretation = f"Negative NPV of ${round(npv, 2):,}. Expected return is below the hurdle rate."

    return NPVResult(
        initial_investment=round(initial_investment, 2),
        discount_rate_percent=round(discount_rate_percent, 2),
        cash_flows=[round(c, 2) for c in cash_flows],
        npv=round(npv, 2),
        is_viable=is_viable,
        interpretation=interpretation,
    )
