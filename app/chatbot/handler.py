"""
Chatbot Request Handler and Response Generator.
Processes incoming natural language messages, dispatches to engines,
and formats markdown responses with structured data.
"""

from typing import Any, Dict, Optional
from app.chatbot.dialogue import session_manager
from app.chatbot.intent import IntentType, classify_intent, extract_entities
from app.engine.roi import calculate_roi
from app.engine.pf import calculate_profit_factor, calculate_pricing_factor
from app.engine.pricing import (
    calculate_break_even,
    calculate_target_roi_pricing,
    calculate_price_elasticity,
    simulate_markdown_impact,
)
from app.engine.simulator import simulate_pricing_scenarios


class ChatResponse:
    def __init__(self, message: str, intent: str, data: Optional[Dict[str, Any]] = None):
        self.message = message
        self.intent = intent
        self.data = data or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "intent": self.intent,
            "data": self.data,
        }


def format_roi_response(result) -> str:
    annualized_str = (
        f"- **Annualized ROI:** `{result.annualized_roi_percent:+.2f}%` per year\n"
        if result.annualized_roi_percent is not None
        else ""
    )
    payback_str = (
        f"- **Payback Period:** `{result.payback_years:.1f} years`\n"
        if result.payback_years is not None
        else ""
    )

    badge = "🟢 **Profitable**" if result.is_profitable else "🔴 **Unprofitable**"

    return f"""### 📊 Return on Investment (ROI) Analysis

{badge} — {result.interpretation}

| Metric | Value |
| :--- | :--- |
| **Initial Investment** | `${result.initial_cost:,.2f}` |
| **Total Gain / Revenue** | `${result.total_gain:,.2f}` |
| **Net Profit** | `${result.net_profit:,.2f}` |
| **Simple ROI** | `+{result.roi_percent:.2f}%` |

{annualized_str}{payback_str}
> **Formula:** `ROI = ((Gain - Cost) / Cost) * 100%`
"""


def format_profit_factor_response(result) -> str:
    badge = "🟢 **Healthy**" if result.is_profitable else "🔴 **Caution**"
    return f"""### 📈 Profit Factor (PF) Analysis

{badge} — **Rating:** `{result.rating}`
{result.interpretation}

| Metric | Value |
| :--- | :--- |
| **Gross Profit (Gains)** | `${result.gross_profit:,.2f}` |
| **Gross Loss (Losses)** | `${result.gross_loss:,.2f}` |
| **Net Result** | `${result.net_profit:,.2f}` |
| **Profit Factor (PF)** | `{result.profit_factor:.2f}` |

> **Benchmark Standard:**
> - `PF > 2.0`: Excellent profit cushion
> - `1.5 - 2.0`: Solid performance
> - `1.0 - 1.5`: Marginal stability
> - `< 1.0`: Unprofitable operations
"""


def format_pricing_factor_response(result) -> str:
    return f"""### 🏷️ Managed Pricing Factor (PF) Analysis

**Tier Classification:** `{result.rating}`
{result.interpretation}

| Metric | Value |
| :--- | :--- |
| **Unit Cost** | `${result.unit_cost:,.2f}` |
| **Selling Price** | `${result.selling_price:,.2f}` |
| **Pricing Factor (PF)** | `{result.pricing_factor:.2f}x` |
| **Gross Margin** | `{result.gross_margin_percent:.2f}%` |
| **Markup on Cost** | `{result.markup_percent:.2f}%` |
| **Profit per Unit** | `${result.unit_margin:,.2f}` |

> **Formulas:**
> - `Pricing Factor = Price / Cost`
> - `Gross Margin = ((Price - Cost) / Price) * 100%`
> - `Markup = ((Price - Cost) / Cost) * 100%`
"""


def format_break_even_response(result) -> str:
    return f"""### ⚖️ Break-Even Analysis

{result.interpretation}

| Metric | Value |
| :--- | :--- |
| **Fixed Costs** | `${result.fixed_costs:,.2f}` |
| **Variable Cost / Unit** | `${result.variable_cost_per_unit:,.2f}` |
| **Selling Price** | `${result.selling_price:,.2f}` |
| **Unit Contribution Margin** | `${result.contribution_margin:,.2f}` |
| **Contribution Margin Ratio** | `{result.contribution_margin_ratio:.2f}%` |
| **Break-Even Units** | `{result.break_even_units:,.0f} units` |
| **Break-Even Revenue** | `${result.break_even_revenue:,.2f}` |
"""


def format_target_roi_pricing_response(result) -> str:
    return f"""### 🎯 Target ROI Pricing Analysis

To attain your **{result.target_roi_percent:.1f}% target ROI** on **${result.invested_capital:,.2f}** capital:

| Metric | Value |
| :--- | :--- |
| **Recommended Selling Price** | `${result.recommended_price:,.2f}` |
| **Expected Units** | `{result.expected_units:,.0f}` |
| **Fixed Overhead** | `${result.fixed_costs:,.2f}` |
| **Unit Variable Cost** | `${result.variable_cost_per_unit:,.2f}` |
| **Total Production Cost** | `${result.total_cost:,.2f}` |
| **Projected Gross Revenue** | `${result.total_revenue:,.2f}` |
| **Projected Net Profit** | `${result.projected_profit:,.2f}` |
| **Markup on Total Cost** | `{result.markup_on_cost_percent:.2f}%` |
"""


def format_elasticity_response(result) -> str:
    return f"""### 📉 Price Elasticity of Demand (PED)

**Classification:** `{result.elasticity_type}`
{result.revenue_impact_summary}

| Parameter | Before | After | Change |
| :--- | :--- | :--- | :--- |
| **Price** | `${result.old_price:,.2f}` | `${result.new_price:,.2f}` | `{result.price_change_percent:+.1f}%` |
| **Demand (Units)** | `{result.old_quantity:,.0f}` | `{result.new_quantity:,.0f}` | `{result.quantity_change_percent:+.1f}%` |
| **Elasticity Coefficient** | — | — | **`{result.elasticity:.3f}`** |
"""


def format_markdown_response(result) -> str:
    warn_str = f"\n> ⚠️ **Warning:** {result.warning}\n" if result.warning else ""
    return f"""### 🏷️ Discount & Markdown Impact Analysis

Applying a **{result.discount_percent:.1f}% discount** reduces the price from `${result.base_price:,.2f}` to `${result.discounted_price:,.2f}`.
{warn_str}
| Metric | Baseline | Discounted |
| :--- | :--- | :--- |
| **Price** | `${result.base_price:,.2f}` | `${result.discounted_price:,.2f}` |
| **Unit Margin** | `${result.base_price - result.unit_cost:,.2f}` | `${result.new_unit_margin:,.2f}` |
| **Base Gross Profit** | `${result.base_gross_profit:,.2f}` | — |
| **Required Sales Volume** | `{result.base_units:,.0f} units` | **`{result.required_units_to_maintain_profit:,.0f} units`** |
| **Volume Growth Needed** | Baseline | **`+{result.volume_increase_needed_percent:.1f}%`** |

> **Key Rule:** To maintain identical profit after a {result.discount_percent:.0f}% discount, you must sell **{result.volume_increase_needed_percent:.1f}% more units**.
"""


def format_simulation_response(result) -> str:
    rows = []
    for s in result.scenarios:
        rows.append(
            f"| {s.label} | ${s.price:.2f} | {s.estimated_volume:,.0f} | ${s.revenue:,.2f} | ${s.net_profit:,.2f} | {s.roi_percent:+.1f}% | {s.pricing_factor:.2f}x |"
        )
    table = "\n".join(rows)

    return f"""### 🔬 Pricing & ROI Scenario Simulation

{result.summary}

| Scenario | Price | Est. Volume | Revenue | Net Profit | ROI % | PF |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
{table}

- **Optimal Profit:** `{result.optimal_profit_scenario.label}` price `${result.optimal_profit_scenario.price:.2f}` produces `${result.optimal_profit_scenario.net_profit:,.2f}` profit.
- **Optimal ROI:** `{result.optimal_roi_scenario.label}` price produces `{result.optimal_roi_scenario.roi_percent:.1f}%` ROI.
"""


def get_help_message() -> str:
    return """### 🤖 ROI & Managed Pricing Chatbot

I can assist you with comprehensive pricing management, return on investment, and profit factor analytics.

#### 💡 Examples you can ask me:
1. **ROI Analysis:**
   - `"Calculate ROI for $20,000 cost and $35,000 return over 2 years"`
   - `"What is my ROI if I invest 50k and make 85k?"`
2. **Profit Factor (Trading / Operational PF):**
   - `"Calculate profit factor: gross profit 60k, gross loss 20k"`
   - `"My wins are 45,000 and losses are 15,000, what is my PF?"`
3. **Managed Pricing Factor (Multiplier & Markup):**
   - `"Cost is $40, selling price is $75, calculate pricing factor and margins"`
   - `"My unit cost is $25 and target PF is 2.2, what should my price be?"`
4. **Break-Even Analysis:**
   - `"Break even: fixed costs 30000, variable cost 15, price 35"`
5. **Target ROI Pricing:**
   - `"Target ROI pricing: fixed 20000, unit cost 12, volume 5000, capital 40000, target ROI 25%"`
6. **Price Elasticity:**
   - `"Price changed from $50 to $60, demand dropped from 1000 to 820, calculate elasticity"`
7. **Discount / Markdown Simulator:**
   - `"Simulate 15% discount on $100 price with unit cost $60 and 500 units"`
8. **Multi-Scenario Sensitivity Simulation:**
   - `"Simulate scenarios: price 50, cost 25, volume 1000, fixed costs 10000"`

Type any query or select a quick preset from the dashboard!
"""


def get_concept_explanation(text: str) -> str:
    lower = text.lower()
    if "roi" in lower:
        return """### 📘 Understanding Return on Investment (ROI)

**ROI** measures the percentage profitability of an investment relative to its cost.

- **Formula:** `ROI = ((Total Gains - Cost) / Cost) * 100%`
- **Annualized ROI:** Compounded annual growth rate over $t$ years: `((Gain / Cost)^(1/t) - 1) * 100%`
- **Application in Pricing:** Evaluate marketing campaigns, product launches, capital tooling, and pricing strategy yield.
"""
    elif "profit factor" in lower:
        return """### 📘 Understanding Profit Factor (PF)

**Profit Factor** measures trading and operational profitability by comparing gross profits to gross losses.

- **Formula:** `PF = Gross Profits / Gross Losses`
- **Benchmark:**
  - `PF > 2.0`: Superior strategy resilience
  - `PF 1.5 - 2.0`: Robust standard
  - `PF 1.0`: Break-even
  - `PF < 1.0`: Net loss
"""
    elif "pricing factor" in lower or "markup" in lower:
        return """### 📘 Understanding Pricing Factor (PF)

In managed pricing, **Pricing Factor** is the price multiplier applied to unit cost.

- **Formula:** `Pricing Factor = Selling Price / Unit Cost`
- **Gross Margin:** `((Price - Cost) / Price) * 100% = ((PF - 1) / PF) * 100%`
- **Keystone Pricing:** Standard 2.0x factor produces a 50% gross margin.
"""
    elif "elasticity" in lower:
        return """### 📘 Understanding Price Elasticity of Demand (PED)

**Price Elasticity** measures how sensitive buyers are to a price adjustment.

- **Formula (Midpoint):** `Ed = (% Change in Quantity Demanded) / (% Change in Price)`
- **Interpretation:**
  - `|Ed| > 1 (Elastic):` Price hikes hurt total revenue. Discounts boost revenue.
  - `|Ed| < 1 (Inelastic):` High pricing power; price hikes expand total revenue.
"""
    elif "break even" in lower:
        return """### 📘 Understanding Break-Even Analysis

Break-even identifies the sales volume where revenues exactly equal total costs (0 net profit).

- **Unit Contribution Margin:** `Selling Price - Unit Variable Cost`
- **Break-Even Units:** `Fixed Overhead / Contribution Margin`
- **Break-Even Revenue:** `Break-Even Units * Selling Price`
"""
    return get_help_message()


def handle_chat_message(user_message: str, session_id: str = "default_session") -> ChatResponse:
    """Main conversational entrypoint."""
    session = session_manager.get_or_create(session_id)
    session.add_message("user", user_message)

    text = user_message.strip()
    if not text:
        resp = ChatResponse(
            message="Please provide a query or select a calculation preset.",
            intent=IntentType.HELP.value,
        )
        session.add_message("assistant", resp.message)
        return resp

    intent = classify_intent(text)
    entities = extract_entities(text)

    # Contextual slot filling from last_context if missing in current utterance
    ctx = session.last_context

    # 1. Greetings
    if intent == IntentType.GREETING:
        msg = "👋 Hello! I am your **ROI & Managed Pricing Chatbot**. How can I help you analyze your pricing, ROI, margins, or profit factors today?"
        resp = ChatResponse(message=msg, intent=intent.value)
        session.add_message("assistant", resp.message)
        return resp

    # 2. Help
    if intent == IntentType.HELP:
        resp = ChatResponse(message=get_help_message(), intent=intent.value)
        session.add_message("assistant", resp.message)
        return resp

    # 3. Explanations
    if intent == IntentType.EXPLAIN_CONCEPT:
        msg = get_concept_explanation(text)
        resp = ChatResponse(message=msg, intent=intent.value)
        session.add_message("assistant", resp.message)
        return resp

    # 4. Break-even
    if intent == IntentType.BREAK_EVEN:
        fixed = entities.fixed_costs or ctx.get("fixed_costs")
        var_cost = entities.variable_cost or entities.cost or ctx.get("variable_cost") or ctx.get("cost")
        price = entities.price or ctx.get("price")

        # Fallback to positional raw numbers if named not found
        if (fixed is None or var_cost is None or price is None) and len(entities.raw_numbers) >= 3:
            fixed = fixed or entities.raw_numbers[0]
            var_cost = var_cost or entities.raw_numbers[1]
            price = price or entities.raw_numbers[2]

        if fixed is not None and var_cost is not None and price is not None:
            try:
                res = calculate_break_even(fixed, var_cost, price)
                session.update_context({
                    "fixed_costs": fixed,
                    "variable_cost": var_cost,
                    "price": price,
                })
                resp = ChatResponse(
                    message=format_break_even_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                msg = f"⚠️ Could not calculate break-even: {str(e)}"
                return ChatResponse(message=msg, intent=intent.value)
        else:
            msg = "To calculate break-even, please provide: **Fixed Costs**, **Variable Cost per Unit**, and **Selling Price**.\n*Example:* `Break even: fixed costs 25000, variable cost 10, price 30`"
            return ChatResponse(message=msg, intent=intent.value)

    # 5. Target ROI Pricing
    if intent == IntentType.TARGET_ROI_PRICING:
        fixed = entities.fixed_costs or ctx.get("fixed_costs") or 0.0
        var_cost = entities.variable_cost or entities.cost or ctx.get("variable_cost") or ctx.get("cost")
        vol = entities.volume or ctx.get("volume")
        capital = entities.capital or entities.cost or ctx.get("capital") or 0.0
        target_roi = entities.target_roi or 20.0

        if var_cost is not None and vol is not None:
            try:
                res = calculate_target_roi_pricing(
                    fixed_costs=fixed,
                    variable_cost_per_unit=var_cost,
                    expected_units=vol,
                    invested_capital=capital if capital > 0 else (fixed + var_cost * vol),
                    target_roi_percent=target_roi,
                )
                resp = ChatResponse(
                    message=format_target_roi_pricing_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error in Target ROI calculation: {str(e)}", intent=intent.value)
        else:
            msg = "Please provide **Unit Cost**, **Expected Volume**, and optionally **Fixed Costs** and **Target ROI %**.\n*Example:* `Target ROI pricing: unit cost 15, volume 2000, fixed 10000, target roi 30%`"
            return ChatResponse(message=msg, intent=intent.value)

    # 6. Price Elasticity
    if intent == IntentType.PRICE_ELASTICITY:
        p1 = entities.old_price
        p2 = entities.new_price
        q1 = entities.old_volume
        q2 = entities.new_volume

        # Raw number extraction if 4 numbers found
        if (p1 is None or p2 is None or q1 is None or q2 is None) and len(entities.raw_numbers) >= 4:
            p1, p2, q1, q2 = entities.raw_numbers[0], entities.raw_numbers[1], entities.raw_numbers[2], entities.raw_numbers[3]

        if p1 is not None and p2 is not None and q1 is not None and q2 is not None:
            try:
                res = calculate_price_elasticity(p1, p2, q1, q2)
                resp = ChatResponse(
                    message=format_elasticity_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error calculating elasticity: {str(e)}", intent=intent.value)
        else:
            msg = "Please provide old and new price, along with old and new quantity.\n*Example:* `Price changed from 50 to 60, volume dropped from 1000 to 850`"
            return ChatResponse(message=msg, intent=intent.value)

    # 7. Markdown & Discount Simulation
    if intent == IntentType.MARKDOWN_SIMULATION:
        price = entities.price or ctx.get("price")
        cost = entities.cost or entities.variable_cost or ctx.get("cost")
        vol = entities.volume or ctx.get("volume") or 100.0
        disc = entities.discount or 10.0

        if (price is None or cost is None) and len(entities.raw_numbers) >= 2:
            price = entities.raw_numbers[0]
            cost = entities.raw_numbers[1]

        if price is not None and cost is not None:
            try:
                res = simulate_markdown_impact(price, cost, vol, disc)
                resp = ChatResponse(
                    message=format_markdown_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error simulating markdown: {str(e)}", intent=intent.value)
        else:
            msg = "Please provide **Selling Price**, **Unit Cost**, and **Discount %**.\n*Example:* `Simulate 15% discount on price 80 with cost 50 and volume 500`"
            return ChatResponse(message=msg, intent=intent.value)

    # 8. Scenario Simulation
    if intent == IntentType.SCENARIO_SIMULATION:
        price = entities.price or ctx.get("price")
        cost = entities.cost or entities.variable_cost or ctx.get("cost")
        vol = entities.volume or ctx.get("volume") or 1000.0
        fixed = entities.fixed_costs or ctx.get("fixed_costs") or 0.0

        if (price is None or cost is None) and len(entities.raw_numbers) >= 2:
            price = entities.raw_numbers[0]
            cost = entities.raw_numbers[1]

        if price is not None and cost is not None:
            try:
                res = simulate_pricing_scenarios(price, cost, vol, fixed)
                resp = ChatResponse(
                    message=format_simulation_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error simulating scenarios: {str(e)}", intent=intent.value)
        else:
            msg = "To simulate scenarios, please specify base **price**, **cost**, and **volume**.\n*Example:* `Simulate scenarios: price 50, cost 25, volume 1000, fixed 5000`"
            return ChatResponse(message=msg, intent=intent.value)

    # 9. Profit Factor (Trading/Operational)
    if intent == IntentType.CALCULATE_PF:
        gp = entities.gross_profit
        gl = entities.gross_loss

        if (gp is None or gl is None) and len(entities.raw_numbers) >= 2:
            gp = entities.raw_numbers[0]
            gl = entities.raw_numbers[1]

        if gp is not None and gl is not None:
            try:
                res = calculate_profit_factor(gp, gl)
                session.update_context({"gross_profit": gp, "gross_loss": gl})
                resp = ChatResponse(
                    message=format_profit_factor_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error calculating Profit Factor: {str(e)}", intent=intent.value)
        else:
            msg = "Please provide **Gross Profit** and **Gross Loss**.\n*Example:* `Calculate profit factor: gross profit 50,000, gross loss 20,000`"
            return ChatResponse(message=msg, intent=intent.value)

    # 10. Pricing Factor (Price / Cost multiplier)
    if intent == IntentType.CALCULATE_PRICING_FACTOR:
        cost = entities.cost or entities.variable_cost or ctx.get("cost")
        price = entities.price or ctx.get("price")
        target_pf = entities.pf

        if (cost is None or (price is None and target_pf is None)) and len(entities.raw_numbers) >= 2:
            cost = entities.raw_numbers[0]
            price = entities.raw_numbers[1]

        if cost is not None and (price is not None or target_pf is not None):
            try:
                res = calculate_pricing_factor(cost, selling_price=price, target_pricing_factor=target_pf)
                session.update_context({"cost": cost, "price": res.selling_price})
                resp = ChatResponse(
                    message=format_pricing_factor_response(res),
                    intent=intent.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error calculating Pricing Factor: {str(e)}", intent=intent.value)
        else:
            msg = "Please provide **Unit Cost** and either **Selling Price** or **Target PF** multiplier.\n*Example:* `Cost $30, selling price $65` or `Cost $40 with target PF 2.5`"
            return ChatResponse(message=msg, intent=intent.value)

    # 11. ROI Calculation
    if intent == IntentType.CALCULATE_ROI or len(entities.raw_numbers) >= 2:
        cost = entities.cost or ctx.get("cost")
        gain = entities.gain or ctx.get("gain")
        years = entities.years

        if (cost is None or gain is None) and len(entities.raw_numbers) >= 2:
            cost = entities.raw_numbers[0]
            gain = entities.raw_numbers[1]
            if len(entities.raw_numbers) >= 3 and years is None:
                years = entities.raw_numbers[2]

        if cost is not None and gain is not None:
            try:
                res = calculate_roi(cost, gain, years=years)
                session.update_context({"cost": cost, "gain": gain})
                resp = ChatResponse(
                    message=format_roi_response(res),
                    intent=IntentType.CALCULATE_ROI.value,
                    data=res.model_dump(),
                )
                session.add_message("assistant", resp.message, resp.data)
                return resp
            except Exception as e:
                return ChatResponse(message=f"⚠️ Error calculating ROI: {str(e)}", intent=IntentType.CALCULATE_ROI.value)
        else:
            msg = "To calculate ROI, please provide **Initial Cost** and **Total Gain/Return**.\n*Example:* `Calculate ROI on 20,000 cost and 35,000 return over 3 years`"
            return ChatResponse(message=msg, intent=IntentType.CALCULATE_ROI.value)

    # Fallback / Help
    resp = ChatResponse(
        message=f"I couldn't quite determine the exact calculation from that query.\n\n{get_help_message()}",
        intent=IntentType.UNKNOWN.value,
    )
    session.add_message("assistant", resp.message)
    return resp
