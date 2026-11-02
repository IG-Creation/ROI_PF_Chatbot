"""
Main FastAPI Application for ROI & PF Chatbot.
Provides REST API endpoints and serves the modern interactive dashboard.
"""

from typing import List, Optional
import io
import csv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path

from app.config import config
from app.chatbot.handler import handle_chat_message
from app.engine.roi import calculate_roi, calculate_npv, ROIResult, NPVResult
from app.engine.pf import calculate_profit_factor, calculate_pricing_factor, ProfitFactorResult, PricingFactorResult
from app.engine.pricing import (
    calculate_break_even,
    calculate_target_roi_pricing,
    calculate_price_elasticity,
    simulate_markdown_impact,
    BreakEvenResult,
    TargetROIPricingResult,
    ElasticityResult,
    MarkdownImpactResult,
)
from app.engine.simulator import simulate_pricing_scenarios, SimulationResult

app = FastAPI(
    title=config.app_name,
    version=config.version,
    description="Intelligent Chatbot for Analysing Managed Pricing, ROI, and Profit Factor (PF)",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = Path(__file__).resolve().parent / "static"


# --- Request & Response Models ---

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default_session"


class ROIRequest(BaseModel):
    cost: float
    gain: float
    years: Optional[float] = None
    annual_inflow: Optional[float] = None


class ProfitFactorRequest(BaseModel):
    gross_profit: float
    gross_loss: float


class PricingFactorRequest(BaseModel):
    unit_cost: float
    selling_price: Optional[float] = None
    target_pricing_factor: Optional[float] = None


class BreakEvenRequest(BaseModel):
    fixed_costs: float
    variable_cost_per_unit: float
    selling_price: float


class TargetROIPricingRequest(BaseModel):
    fixed_costs: float
    variable_cost_per_unit: float
    expected_units: float
    invested_capital: float
    target_roi_percent: float


class ElasticityRequest(BaseModel):
    old_price: float
    new_price: float
    old_quantity: float
    new_quantity: float


class MarkdownRequest(BaseModel):
    base_price: float
    unit_cost: float
    base_units: float
    discount_percent: float


class SimulationRequest(BaseModel):
    baseline_price: float
    unit_cost: float
    baseline_volume: float
    fixed_costs: Optional[float] = 0.0
    elasticity_assumed: Optional[float] = -1.2
    price_variations: Optional[List[float]] = None


# --- Endpoints ---

@app.get("/api/health")
def healthcheck():
    return {
        "status": "healthy",
        "app": config.app_name,
        "version": config.version,
    }


@app.post("/api/chat")
def chat_endpoint(req: ChatRequest):
    response = handle_chat_message(req.message, req.session_id or "default_session")
    return response.to_dict()


@app.post("/api/roi", response_model=ROIResult)
def direct_roi(req: ROIRequest):
    try:
        return calculate_roi(req.cost, req.gain, req.years, req.annual_inflow)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pf/profit-factor", response_model=ProfitFactorResult)
def direct_profit_factor(req: ProfitFactorRequest):
    try:
        return calculate_profit_factor(req.gross_profit, req.gross_loss)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pf/pricing-factor", response_model=PricingFactorResult)
def direct_pricing_factor(req: PricingFactorRequest):
    try:
        return calculate_pricing_factor(req.unit_cost, req.selling_price, req.target_pricing_factor)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pricing/break-even", response_model=BreakEvenResult)
def direct_break_even(req: BreakEvenRequest):
    try:
        return calculate_break_even(req.fixed_costs, req.variable_cost_per_unit, req.selling_price)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pricing/target-roi", response_model=TargetROIPricingResult)
def direct_target_roi_pricing(req: TargetROIPricingRequest):
    try:
        return calculate_target_roi_pricing(
            req.fixed_costs,
            req.variable_cost_per_unit,
            req.expected_units,
            req.invested_capital,
            req.target_roi_percent,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pricing/elasticity", response_model=ElasticityResult)
def direct_elasticity(req: ElasticityRequest):
    try:
        return calculate_price_elasticity(req.old_price, req.new_price, req.old_quantity, req.new_quantity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pricing/markdown", response_model=MarkdownImpactResult)
def direct_markdown(req: MarkdownRequest):
    try:
        return simulate_markdown_impact(req.base_price, req.unit_cost, req.base_units, req.discount_percent)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/pricing/simulate", response_model=SimulationResult)
def direct_simulate(req: SimulationRequest):
    try:
        return simulate_pricing_scenarios(
            req.baseline_price,
            req.unit_cost,
            req.baseline_volume,
            req.fixed_costs or 0.0,
            req.elasticity_assumed or -1.2,
            req.price_variations,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/upload/catalog")
async def upload_catalog(file: UploadFile = File(...)):
    """
    Process CSV catalog containing products, unit_cost, selling_price, units_sold.
    Outputs computed ROI, PF, margins, and health scorecards.
    """
    content = await file.read()
    decoded = content.decode("utf-8-sig", errors="replace")
    reader = csv.DictReader(io.StringIO(decoded))

    results = []
    total_cost = 0.0
    total_revenue = 0.0

    for idx, row in enumerate(reader, start=1):
        name = row.get("name") or row.get("product") or f"Product {idx}"
        try:
            cost = float(row.get("cost") or row.get("unit_cost") or 0.0)
            price = float(row.get("price") or row.get("selling_price") or 0.0)
            units = float(row.get("units") or row.get("volume") or row.get("quantity") or 1.0)
        except ValueError:
            continue

        if cost <= 0 or price <= 0:
            continue

        pf = price / cost
        margin_pct = ((price - cost) / price) * 100.0
        line_rev = price * units
        line_cost = cost * units
        line_profit = line_rev - line_cost
        line_roi = (line_profit / line_cost * 100.0) if line_cost > 0 else 0.0

        total_cost += line_cost
        total_revenue += line_rev

        results.append({
            "product": name,
            "unit_cost": round(cost, 2),
            "selling_price": round(price, 2),
            "units": round(units, 0),
            "pricing_factor": round(pf, 2),
            "gross_margin_percent": round(margin_pct, 2),
            "total_revenue": round(line_rev, 2),
            "total_profit": round(line_profit, 2),
            "roi_percent": round(line_roi, 2),
        })

    portfolio_profit = total_revenue - total_cost
    portfolio_roi = (portfolio_profit / total_cost * 100.0) if total_cost > 0 else 0.0
    portfolio_pf = (total_revenue / total_cost) if total_cost > 0 else 0.0

    return {
        "count": len(results),
        "total_revenue": round(total_revenue, 2),
        "total_cost": round(total_cost, 2),
        "total_profit": round(portfolio_profit, 2),
        "portfolio_roi_percent": round(portfolio_roi, 2),
        "portfolio_pricing_factor": round(portfolio_pf, 2),
        "products": results,
    }


# Serve static web frontend
ROOT_DIR = Path(__file__).resolve().parent.parent

# Serve PWA static assets & Lendy index.html
@app.get("/")
def serve_lendy_index():
    index_file = ROOT_DIR / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    if (STATIC_DIR / "index.html").exists():
        return FileResponse(str(STATIC_DIR / "index.html"))
    return {"message": "Lendy Loan Pricing Chatbot Ready"}

@app.get("/manifest.json")
def serve_manifest():
    manifest_file = ROOT_DIR / "manifest.json"
    if manifest_file.exists():
        return FileResponse(str(manifest_file), media_type="application/manifest+json")
    return {}

@app.get("/sw.js")
def serve_service_worker():
    sw_file = ROOT_DIR / "sw.js"
    if sw_file.exists():
        return FileResponse(str(sw_file), media_type="application/javascript")
    return ""

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
