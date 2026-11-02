# Lendy 🐱 — Intelligent Loan Pricing & Approval Chatbot

> **Enterprise-Grade Loan Pricing, Policy Matrix Engine & Approval Governance Chatbot.**
> Built as a single-file, dependency-free Progressive Web App (PWA) with responsive mobile-first UX, reducing-balance EMI engine, DTI risk analysis, and an animated robot-cat mascot ("Lendy").

![Tests](https://img.shields.io/badge/Tests-36%20Passed-brightgreen.svg)
![PWA](https://img.shields.io/badge/PWA-Installable-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Clean%20Vanilla%20JS-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🌟 Executive Overview

Lendy is a conversational fintech tool designed for commercial loan officers, credit managers, and underwriters. It automates:
1. **Conversational Data Collection**: Walks through customer parameters step-by-step with warm, encouraging dialogue and tappable quick-reply chips.
2. **Dynamic Ticket Sizing**: Automatically classifies loans into *Upto 5 Lacs* or *Above 5 Lacs* for Regular Secured Business Loans, or *All Ticket Size* for Working Capital and Hypothecation products.
3. **56-Row Policy Matrix Benchmark**: Instant lookup of standard **Base ROI (% p.a.)** and **Base Processing Fee (PF %)**.
4. **Approval Escalation Matrix**:
   - **ROI Deviation** ($Base - Requested$): Up to 2% (CBO), >2% to 4% (COO), >4% (CEO).
   - **PF Deviation** ($Base - Requested$): Up to 1% (CBO), >1% to 1.5% (COO), >1.5% (CEO).
   - **Higher Authority Rule**: If ROI and PF require different tiers, the final authority is the highest (`CEO > COO > CBO > None`).
   - **Rounding Tolerance**: Embedded $10^{-6}$ epsilon prevents floating point precision artifacts.
5. **Loan Analytics & Risk Engines**:
   - Reducing-balance monthly EMI ($EMI = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n - 1}$).
   - Monthly and upfront Processing Fee savings.
   - Debt-to-Income (DTI) ratio before and after, with configurable 50% prudent limit alerts.
6. **Animated Robot-Cat Mascot ("Lendy")**:
   - Inline SVG with 7 real-time expressive states: `idle`, `talking`, `thinking`, `surprised`, `happy`, `worried`, and `celebrating`.

---

## 🚀 How to Run

### Option 1: Double-Click / Direct Browser (Zero Dependencies)
Simply open [`index.html`](file:///c:/Users/ishga/OneDrive/Desktop/Chatbots/ROI%20%26%20PF%20Chatbot/index.html) in Chrome, Edge, Safari, or Firefox on desktop or mobile. No installation or server required!

### Option 2: Run via Python Server
```bash
# Using Python built-in HTTP server:
python -m http.server 8000

# Or using the included FastAPI server:
.\.venv\Scripts\python.exe run.py
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

---

## 🧪 Automated Test Suite (36/36 Passed)

Run the automated test suite verifying all 8 enterprise acceptance scenarios:

```bash
.\.venv\Scripts\pytest.exe -v
```

### Verified Acceptance Scenarios:
- **Case 1**: Regular Secured Business Loan (Above 5 Lacs, Documented, SORP, $\ge$700, 10L loan, Base ROI 18%, PF 2%):
  - Req ROI 16.5% $\rightarrow$ Deviation 1.5% $\rightarrow$ **CBO Approval**
  - Req ROI 15.0% $\rightarrow$ Deviation 3.0% $\rightarrow$ **COO Approval**
  - Req ROI 13.5% $\rightarrow$ Deviation 4.5% $\rightarrow$ **CEO Approval**
- **Case 2**: Same case with PF deviations:
  - Req PF 1.2% $\rightarrow$ Deviation 0.8% $\rightarrow$ **CBO Approval**
  - Req PF 0.4% $\rightarrow$ Deviation 1.6% $\rightarrow$ **CEO Approval**
- **Case 3**: Dual deviation (ROI 3.0% COO + PF 1.6% CEO) $\rightarrow$ Governed by highest authority: **CEO Approval**.
- **Case 4**: Premium pricing (Req ROI 19%, PF 2%) $\rightarrow$ **No Approval Needed**.
- **Case 5**: Reducing-balance EMI for 10L loan at 18% for 60m $\rightarrow$ **₹25,393/month**.
- **Case 6**: Income ₹80,000/m, existing ₹20,000, new EMI ₹25,393 $\rightarrow$ Current DTI 25.0%, Updated DTI 56.7% with **DTI Warning Alert**.
- **Case 7**: Annual income ₹12,00,000 correctly normalized to **₹1,00,000/month**.
- **Case 8**: Hypothecation Loan automatically skips Property Type question (defaults to `NA`).

---

## 📊 Benchmark Policy Matrix (56 Rows)

| Product | Ticket Size | Income Program | Property Type | Bureau Category | Base ROI % | Base PF % |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Regular Secured Business Loan | Upto 5 Lacs | Documented | SORP | $\ge$700 or NTC | 20.0% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Documented | SORP | <700 | 22.0% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Documented | Other | $\ge$700 or NTC | 22.0% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Documented | Other | <700 | 22.0% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Assessed / Hybrid / Semi | SORP | $\ge$700 or NTC | 21.0% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Assessed / Hybrid / Semi | SORP | <700 | 22.0% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Assessed / Hybrid / Semi | Other | $\ge$700 or NTC | 21.5% | 3.0% |
| Regular Secured Business Loan | Upto 5 Lacs | Assessed / Hybrid / Semi | Other | <700 | 22.0% | 3.0% |
| Regular Secured Business Loan | Above 5 Lacs | Documented | SORP | $\ge$700 or NTC | 18.0% | 2.0% |
| Regular Secured Business Loan | Above 5 Lacs | Documented | SORP | <700 | 20.0% | 2.0% |
| Regular Secured Business Loan | Above 5 Lacs | Documented | Other | $\ge$700 or NTC | 19.0% | 3.0% |
| Regular Secured Business Loan | Above 5 Lacs | Documented | Other | <700 | 20.0% | 3.0% |
| Regular Secured Business Loan | Above 5 Lacs | Assessed / Hybrid / Semi | SORP | $\ge$700 or NTC | 20.0% | 3.0% |
| Regular Secured Business Loan | Above 5 Lacs | Assessed / Hybrid / Semi | SORP | <700 | 20.5% | 3.0% |
| Regular Secured Business Loan | Above 5 Lacs | Assessed / Hybrid / Semi | Other | $\ge$700 or NTC | 20.0% | 3.0% |
| Regular Secured Business Loan | Above 5 Lacs | Assessed / Hybrid / Semi | Other | <700 | 21.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Documented | SORP | $\ge$700 or NTC | 22.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Documented | SORP | <700 | 24.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Documented | Other | $\ge$700 or NTC | 24.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Documented | Other | <700 | 24.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Assessed / Hybrid / Semi | SORP | $\ge$700 or NTC | 23.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Assessed / Hybrid / Semi | SORP | <700 | 24.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Assessed / Hybrid / Semi | Other | $\ge$700 or NTC | 24.0% | 3.0% |
| Secured Working Capital Term Loan | All Ticket Size | Assessed / Hybrid / Semi | Other | <700 | 24.0% | 3.0% |
| Hypothecation Loans | All Ticket Size | Documented | NA | $\ge$700 or NTC | 20.0% | 3.0% |
| Hypothecation Loans | All Ticket Size | Documented | NA | <700 | 22.0% | 3.0% |
| Hypothecation Loans | All Ticket Size | Assessed / Hybrid / Semi | NA | $\ge$700 or NTC | 22.0% | 3.0% |
| Hypothecation Loans | All Ticket Size | Assessed / Hybrid / Semi | NA | <700 | 22.0% | 3.0% |

---

## 📱 Mobile & PWA Features
- **100dvh & Safe-Area Insets**: Seamless display on iPhone notch / Dynamic Island and Android navigation bars.
- **VisualViewport Keyboard Shield**: Prevents sticky input and chips from being obscured when virtual mobile keyboards pop up.
- **Installable PWA**: Includes [`manifest.json`](file:///c:/Users/ishga/OneDrive/Desktop/Chatbots/ROI%20%26%20PF%20Chatbot/manifest.json) and [`sw.js`](file:///c:/Users/ishga/OneDrive/Desktop/Chatbots/ROI%20%26%20PF%20Chatbot/sw.js) for native offline installation on mobile and desktop.
- **Accessibility**: Includes `aria-live="polite"` regions, accessible color contrast ratios, and minimum 44px touch targets.
- **Async Guard Protection**: Restarting conversation mid-flow invalidates background async tokens to eliminate ghost or out-of-order messages.

---

## 📂 Project Structure

```
ROI_PF_Chatbot/
├── index.html                   # Complete Lendy Chatbot (Single-file HTML + CSS + JS)
├── manifest.json                # PWA Web Application Manifest
├── sw.js                        # PWA Offline Service Worker
├── run.py                       # Unified entrypoint runner
├── app/
│   ├── main.py                  # FastAPI Application (serves Lendy + API)
│   ├── config.py
│   └── engine/                  # Core calculation engines
├── tests/
│   ├── test_lendy_acceptance.py # 8/8 Acceptance test suite
│   ├── verify_lendy_matrix.py   # Matrix verification engine
│   └── test_api.py              # End-to-end API test suite
├── requirements.txt
└── README.md
```

---

## 📄 License
MIT License. Created for IG-Creation.
