# ROI & PF Chatbot 📈

> **Intelligent Chatbot & Analytics Engine for Managed Pricing, Return on Investment (ROI), and Profit / Pricing Factor (PF).**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.162%2B-green.svg)
![Tests](https://img.shields.io/badge/Tests-26%20Passed-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

---

## 🎯 Key Capabilities

1. **Return on Investment (ROI) Suite**:
   - **Simple ROI**: Exact percentage returns, net dollar profits, and profitability status.
   - **Annualized ROI (CAGR)**: Compounded annual returns over multi-year horizons.
   - **Payback Period**: Duration required to recoup capital outlays.
   - **Net Present Value (NPV)**: Discounted cash flows analysis against hurdle rates.

2. **Profit Factor & Pricing Factor (PF) Suite**:
   - **Profit Factor ($PF$)**: $\frac{\text{Gross Profit}}{\text{Gross Loss}}$ ratio assessment with industry health benchmarks.
   - **Managed Pricing Factor**: Multiplier on unit cost ($PF = \frac{P}{C}$), Keystone markup tiering, and gross margin calculations.

3. **Managed Pricing Analytics**:
   - **Break-Even Volume & Revenue**: Unit contribution margin and overhead coverage threshold.
   - **Target ROI Pricing**: Back-solve optimal selling price from capital investment and desired ROI %.
   - **Price Elasticity of Demand (PED)**: Midpoint formula demand sensitivity and revenue impact direction.
   - **Discount / Markdown Hurdle**: Required volume surge needed to preserve gross profit after price cuts.

4. **Interactive Multi-Scenario Simulator**:
   - Dynamic sensitivity grid across price shifts (-20% to +20%) with demand elasticity.
   - Identifies optimal price points for maximum dollar profit and maximum capital efficiency.
   - Visualized with interactive Chart.js bar & trend graphs.

5. **Conversational Chatbot**:
   - Understands natural language queries (e.g., *"Calculate ROI for $25k cost and $42k return"*).
   - Conversational memory preserves context across multiple turns.
   - Works 100% offline with zero external API dependencies (optional LLM grounding via `GEMINI_API_KEY`).

6. **Bulk Catalog Upload**:
   - Upload CSV catalogs containing `product, unit_cost, selling_price, volume` for immediate portfolio analytics.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10 or higher (compatible with Python 3.14).

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/IG-Creation/ROI_PF_Chatbot.git
cd ROI_PF_Chatbot

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Launch the Application

#### Option A: Web Dashboard (Recommended)
```bash
python run.py
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

#### Option B: Terminal CLI Mode
```bash
python run.py --cli
```

---

## 🧪 Running Tests

The test suite covers unit calculations, financial validations, conversational intent extraction, and API endpoints:

```bash
pytest -v
```

---

## 📡 REST API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | Service health status |
| `POST` | `/api/chat` | Conversational NLP query interface |
| `POST` | `/api/roi` | Direct ROI calculation |
| `POST` | `/api/pf/profit-factor` | Gross Profit / Loss analysis |
| `POST` | `/api/pf/pricing-factor` | Unit cost & pricing factor markup |
| `POST` | `/api/pricing/break-even` | Fixed cost & contribution margin |
| `POST` | `/api/pricing/target-roi` | Price recommendation for ROI target |
| `POST` | `/api/pricing/elasticity` | Price elasticity of demand |
| `POST` | `/api/pricing/markdown` | Discount impact & volume hurdle |
| `POST` | `/api/pricing/simulate` | Multi-scenario sensitivity grid |
| `POST` | `/api/upload/catalog` | Bulk CSV portfolio processing |

---

## 📂 Project Architecture

```
ROI_PF_Chatbot/
├── app/
│   ├── chatbot/          # NLP intent classification & dialogue manager
│   │   ├── dialogue.py
│   │   ├── handler.py
│   │   └── intent.py
│   ├── engine/           # Mathematical finance & pricing engines
│   │   ├── pf.py
│   │   ├── pricing.py
│   │   ├── roi.py
│   │   └── simulator.py
│   ├── static/           # Modern Web Dashboard (HTML/CSS/JS + Chart.js)
│   │   ├── app.js
│   │   ├── index.html
│   │   └── style.css
│   ├── config.py         # App configuration
│   └── main.py           # FastAPI application
├── examples/             # Sample datasets
│   └── catalog_sample.csv
├── tests/                # Automated pytest suite (26 tests)
│   ├── test_api.py
│   ├── test_chatbot.py
│   ├── test_pf.py
│   ├── test_pricing.py
│   ├── test_roi.py
│   └── test_simulator.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py                # Unified launcher (Web & CLI)
```

---

## 📄 License
MIT License. Created by IG-Creation.
