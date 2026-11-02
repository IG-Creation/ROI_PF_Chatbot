"""
Intent classifier and entity extractor for financial & pricing queries.
"""

import re
from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel


class IntentType(str, Enum):
    CALCULATE_ROI = "CALCULATE_ROI"
    CALCULATE_PF = "CALCULATE_PF"
    CALCULATE_PRICING_FACTOR = "CALCULATE_PRICING_FACTOR"
    BREAK_EVEN = "BREAK_EVEN"
    TARGET_ROI_PRICING = "TARGET_ROI_PRICING"
    PRICE_ELASTICITY = "PRICE_ELASTICITY"
    MARKDOWN_SIMULATION = "MARKDOWN_SIMULATION"
    SCENARIO_SIMULATION = "SCENARIO_SIMULATION"
    EXPLAIN_CONCEPT = "EXPLAIN_CONCEPT"
    HELP = "HELP"
    GREETING = "GREETING"
    UNKNOWN = "UNKNOWN"


class ExtractedEntities(BaseModel):
    cost: Optional[float] = None
    gain: Optional[float] = None
    price: Optional[float] = None
    old_price: Optional[float] = None
    new_price: Optional[float] = None
    gross_profit: Optional[float] = None
    gross_loss: Optional[float] = None
    pf: Optional[float] = None
    years: Optional[float] = None
    fixed_costs: Optional[float] = None
    variable_cost: Optional[float] = None
    volume: Optional[float] = None
    old_volume: Optional[float] = None
    new_volume: Optional[float] = None
    capital: Optional[float] = None
    target_roi: Optional[float] = None
    discount: Optional[float] = None
    raw_numbers: list[float] = []


def parse_number_with_suffix(text: str) -> Optional[float]:
    """Parse string representation of numbers including 'k', 'm', commas, and dollar signs."""
    clean = text.replace("$", "").replace(",", "").strip()
    multiplier = 1.0
    if clean.lower().endswith("k"):
        multiplier = 1_000.0
        clean = clean[:-1]
    elif clean.lower().endswith("m"):
        multiplier = 1_000_000.0
        clean = clean[:-1]
    elif clean.lower().endswith("b"):
        multiplier = 1_000_000_000.0
        clean = clean[:-1]

    try:
        return float(clean) * multiplier
    except ValueError:
        return None


def extract_entities(text: str) -> ExtractedEntities:
    """Extract financial and pricing numbers and slots from text."""
    entities = ExtractedEntities()

    # Find all general numbers
    raw_num_matches = re.findall(r"\$?\b\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?\b", text)
    for m in raw_num_matches:
        val = parse_number_with_suffix(m)
        if val is not None:
            entities.raw_numbers.append(val)

    # Cost / Investment pattern
    cost_match = re.search(
        r"(?:cost|invested|investment|outlay|capital invested|expense|spend)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if cost_match:
        entities.cost = parse_number_with_suffix(cost_match.group(1))

    # Gain / Return / Revenue pattern
    gain_match = re.search(
        r"(?:gain|return|returns|revenue|final value|generated|inflow)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if gain_match:
        entities.gain = parse_number_with_suffix(gain_match.group(1))

    # Price pattern
    price_match = re.search(
        r"(?:selling price|unit price|price)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if price_match:
        entities.price = parse_number_with_suffix(price_match.group(1))

    # Gross Profit pattern
    gp_match = re.search(
        r"(?:gross profit|gross gain|total profit|profits|wins)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if gp_match:
        entities.gross_profit = parse_number_with_suffix(gp_match.group(1))

    # Gross Loss pattern
    gl_match = re.search(
        r"(?:gross loss|total loss|losses|loss)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if gl_match:
        entities.gross_loss = parse_number_with_suffix(gl_match.group(1))

    # Fixed costs
    fixed_match = re.search(
        r"(?:fixed costs?|overhead)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if fixed_match:
        entities.fixed_costs = parse_number_with_suffix(fixed_match.group(1))

    # Variable cost
    var_match = re.search(
        r"(?:variable cost|unit cost|cost per unit)\s*(?:of|is|was|:|=)?\s*\$?(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if var_match:
        entities.variable_cost = parse_number_with_suffix(var_match.group(1))

    # Volume / Quantity
    vol_match = re.search(
        r"(?:volume|quantity|units|units sold)\s*(?:of|is|was|:|=)?\s*(\d+(?:,\d{3})*(?:\.\d+)?(?:[kKmMbB])?)",
        text,
        re.IGNORECASE,
    )
    if vol_match:
        entities.volume = parse_number_with_suffix(vol_match.group(1))

    # Discount percent
    disc_match = re.search(
        r"(?:discount|markdown)\s*(?:of|is|was|:|=)?\s*(\d+(?:\.\d+)?)\s*%",
        text,
        re.IGNORECASE,
    )
    if disc_match:
        entities.discount = float(disc_match.group(1))

    # Target ROI
    target_roi_match = re.search(
        r"(?:target roi|desired roi|roi target)\s*(?:of|is|was|:|=)?\s*(\d+(?:\.\d+)?)\s*%",
        text,
        re.IGNORECASE,
    )
    if target_roi_match:
        entities.target_roi = float(target_roi_match.group(1))

    # Years / Duration
    years_match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:years?|yrs?|yr)",
        text,
        re.IGNORECASE,
    )
    if years_match:
        entities.years = float(years_match.group(1))

    # Pricing Factor / PF target
    pf_match = re.search(
        r"(?:pf|profit factor|pricing factor|markup factor)\s*(?:of|is|was|:|=)?\s*(\d+(?:\.\d+)?)",
        text,
        re.IGNORECASE,
    )
    if pf_match:
        entities.pf = float(pf_match.group(1))

    # Old and new prices for elasticity (e.g. from 50 to 60)
    price_change_match = re.search(
        r"(?:price|from)\s*\$?(\d+(?:\.\d+)?)\s*(?:to|increased to|dropped to|changed to)\s*\$?(\d+(?:\.\d+)?)",
        text,
        re.IGNORECASE,
    )
    if price_change_match:
        entities.old_price = float(price_change_match.group(1))
        entities.new_price = float(price_change_match.group(2))

    # Old and new quantities for elasticity (e.g. volume from 1000 to 800)
    qty_change_match = re.search(
        r"(?:volume|units|demand|sales)\s*(?:from)?\s*(\d+(?:\.\d+)?)\s*(?:to|dropped to|fell to|rose to)\s*(\d+(?:\.\d+)?)",
        text,
        re.IGNORECASE,
    )
    if qty_change_match:
        entities.old_volume = float(qty_change_match.group(1))
        entities.new_volume = float(qty_change_match.group(2))

    return entities


def classify_intent(text: str) -> IntentType:
    """Classify the user intent from text."""
    lower = text.lower().strip()

    # Greetings
    if re.search(r"^(hi|hello|hey|greetings|good morning|good evening|good afternoon)\b", lower):
        return IntentType.GREETING

    # Help
    if re.search(r"^(help|what can you do|features|guide|menu|options|\?)$", lower) or "how do i use" in lower:
        return IntentType.HELP

    # Explanations
    if re.search(r"(what is|explain|difference between|how to calculate|formula for)\s+(roi|pf|profit factor|pricing factor|elasticity|break even)", lower):
        return IntentType.EXPLAIN_CONCEPT

    # Break-even
    if "break even" in lower or "breakeven" in lower:
        return IntentType.BREAK_EVEN

    # Elasticity
    if "elasticity" in lower or "ped" in lower or ("price changed" in lower and "volume" in lower):
        return IntentType.PRICE_ELASTICITY

    # Markdown / Discount simulation
    if "discount" in lower or "markdown" in lower or "sale price" in lower:
        return IntentType.MARKDOWN_SIMULATION

    # Target ROI pricing
    if ("target roi" in lower or "desired roi" in lower) and ("price" in lower or "charge" in lower or "set price" in lower):
        return IntentType.TARGET_ROI_PRICING

    # Scenario simulation
    if "scenario" in lower or "simulate" in lower or "what if" in lower or "sensitivity" in lower:
        return IntentType.SCENARIO_SIMULATION

    # Profit Factor (Gross profit / Gross loss)
    if ("profit factor" in lower) or ("gross loss" in lower or "gross profit" in lower) or (re.search(r"\bpf\b", lower) and ("gain" in lower or "loss" in lower)):
        return IntentType.CALCULATE_PF

    # Pricing Factor (Cost * multiplier)
    if ("pricing factor" in lower) or ("markup" in lower) or ("multiplier" in lower) or (re.search(r"\bpf\b", lower) and "cost" in lower):
        return IntentType.CALCULATE_PRICING_FACTOR

    # ROI
    if "roi" in lower or "return on investment" in lower or ("invested" in lower and "return" in lower):
        return IntentType.CALCULATE_ROI

    # General numbers fallback detection
    if "price" in lower and "cost" in lower:
        return IntentType.CALCULATE_PRICING_FACTOR
    if "profit" in lower and "loss" in lower:
        return IntentType.CALCULATE_PF
    if "cost" in lower and ("return" in lower or "gain" in lower):
        return IntentType.CALCULATE_ROI

    return IntentType.UNKNOWN
