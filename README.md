# Lendy 🐱✨ — 3D Loan Pricing & Approval AI Chatbot

> **Enterprise-Grade Loan Pricing, Policy Matrix Engine & Approval Governance Chatbot.**
> Built as a single-file, dependency-free Progressive Web App (PWA) with an interactive **3D/4D animated robot-cat companion**, vibrant multi-color theme switcher, reducing-balance EMI engine, DTI risk scoring, and mandatory credit floor policy overrides.

![Tests](https://img.shields.io/badge/Tests-37%20Passed-brightgreen.svg)
![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-blue.svg)
![PWA](https://img.shields.io/badge/PWA-Installable-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🌐 Live Public Link (Hosted on GitHub)

Access the live, public chatbot hosted securely on GitHub Pages:

### 🔗 **[https://ig-creation.github.io/ROI_PF_Chatbot/](https://ig-creation.github.io/ROI_PF_Chatbot/)**

> 🔒 **Privacy & Security Guarantee:**
> When sharing this link with clients, borrowers, or branch officers, **no local IP, PC file path, or personal details are exposed**. The application runs directly on GitHub's secure global cloud edge CDN.

---

## 🌟 Key Features & Visual Upgrades

### 1. 🎨 Multi-Color Radiant Themes & Glassmorphism
- **Ambient Glowing Mesh**: Floating backdrop light orbs create an iridescent modern fintech atmosphere.
- **Live Theme Palette Switcher**:
  - 🌌 **Cyber Neon**: Electric cyan, purple laser, neon emerald, and cyber pink.
  - 🌅 **Sunset Luxe**: Royal velvet, warm rose, fiery amber, and gold.
  - 💎 **Emerald Mint**: Mint green, lush teal, platinum, and luminous jade.
- **Glassmorphic Verdict Cards**: Translucent frosted panels with dynamic glowing borders and color-coded status badges.

### 2. 🐱 3D / 4D Moving Interactive Pet Companion ("Lendy")
Perched right beside the Send button and input bar with true 3D perspective depth:
- **Interactive 3D Head & Eye Tracking**: Head and pupils tilt and follow your cursor/touch in real-time.
- **Animated 3D Tail Wag & Ear Twitch**: Smooth physical animations while sitting.
- **Clickable Fun Micro-Interactions**: Tapping the pet makes it do a 360° 3D spin with floating hearts, speech bubbles, and happy purring!
- **Reactive Emotional Expressions**:
  - `idle`: Gentle blinking and smiling.
  - `talking`: Dynamic mouth movement during text generation.
  - `thinking`: Eyes tilted upward thoughtfully with pulsing antenna.
  - `surprised`: Wide glowing eyes and open "O" mouth upon benchmark lookup.
  - `happy`: Joyful curved eyes `^ ^`, blushing pink cheeks, and wagging tail.
  - `worried`: Slanted downward troubled eyes when CEO approval or DTI breach occurs.
  - `celebrating`: Party bounce mode with sparkling star eyes when standard rates pass.

---

## ⚖️ Credit Policy Matrix & Rectified Approval Rules

### 🏛️ Mandatory Absolute Floor Overrides (New Policy Rectifications):
1. **ROI Floor Rule**: If Requested ROI is **less than 15.00%**, it **automatically requires CEO Approval**, regardless of deviation or base rate.
2. **PF Floor Rule**: If Requested Processing Fee is **less than 1.50%**, it **automatically requires CEO Approval**, regardless of deviation or base rate.

### 📊 Standard Deviation Approval Bands (When above floors):
- **ROI Deviation** ($Base - Requested$):
  - $\le 0.00\%$: **No Approval Needed** (Standard / Premium)
  - Up to $2.00\%$: **CBO Approval** (Chief Business Officer)
  - $> 2.00\%$ up to $4.00\%$: **COO Approval** (Chief Operating Officer)
  - $> 4.00\%$: **CEO Approval** (Chief Executive Officer)
- **PF Deviation** ($Base - Requested$):
  - $\le 0.00\%$: **No Approval Needed**
  - Up to $1.00\%$: **CBO Approval**
  - $> 1.00\%$ up to $1.50\%$: **COO Approval**
  - $> 1.50\%$: **CEO Approval**
- **Governance Hierarchy**: If ROI and PF require different approvers, the final authority is governed by the highest level:
  $$\text{CEO (Level 3)} > \text{COO (Level 2)} > \text{CBO (Level 1)} > \text{None (Level 0)}$$
- **Rounding Tolerance**: $\varepsilon = 10^{-6}$ rounding tolerance protects against floating-point precision artifacts.

---

## 🧪 Automated Test Suite (37/37 Passed)

Run the automated test suite verifying all 8 enterprise acceptance scenarios and the new floor override rules:

```powershell
.\.venv\Scripts\pytest.exe -v
```

### Verified Acceptance Scenarios:
- **Case 1**: Regular Secured Business Loan (Above 5L, Documented, SORP, $\ge$700, Base ROI 18%, PF 2%):
  - Req ROI 16.5% $\rightarrow$ Deviation 1.5% $\rightarrow$ **CBO Approval**
  - Req ROI 15.0% $\rightarrow$ Deviation 3.0% $\rightarrow$ **COO Approval**
  - Req ROI 13.5% $\rightarrow$ Deviation 4.5% + Below 15% Floor $\rightarrow$ **CEO Approval**
- **Case 2**: Processing Fee deviations and Floor overrides:
  - Req PF 1.6% (above 1.5% floor, dev 0.4%) $\rightarrow$ **CBO Approval**
  - Req PF 1.2% (< 1.5% floor) $\rightarrow$ **CEO Approval (Floor Triggered)**
  - Req PF 0.4% (< 1.5% floor + dev 1.6%) $\rightarrow$ **CEO Approval**
- **Case 3**: Dual deviation (ROI 3.0% COO + PF 1.6% CEO) $\rightarrow$ Governed by highest authority: **CEO Approval**.
- **Case 4**: Premium pricing (Req ROI 19%, PF 2%) $\rightarrow$ **No Approval Needed**.
- **Case 5**: Reducing-balance EMI for 10L loan at 18% for 60m $\rightarrow$ **₹25,393/month**.
- **Case 6**: Income ₹80,000/m, existing ₹20,000, new EMI ₹25,393 $\rightarrow$ Current DTI 25.0%, Updated DTI 56.7% with **DTI Warning Alert**.
- **Case 7**: Annual income ₹12,00,000 correctly normalized to **₹1,00,000/month**.
- **Case 8**: Hypothecation Loan automatically skips Property Type question (defaults to `NA`).
- **Floor Test**: Base ROI 15.5%, Req ROI 14.5% (deviation only 1.0%, normally CBO) $\rightarrow$ **CEO Approval Mandated** due to 15.0% floor.

---

## 🚀 How to Run

### 1. Public Cloud (GitHub Pages)
Open directly: **`https://ig-creation.github.io/ROI_PF_Chatbot/`**

### 2. Standalone Local File
Double-click [`index.html`](file:///c:/Users/ishga/OneDrive/Desktop/Chatbots/ROI%20%26%20PF%20Chatbot/index.html) in your browser.

### 3. Local Python Server
```powershell
.\.venv\Scripts\python.exe run.py
```
Open `http://127.0.0.1:8000` in your browser.

---

## ⚙️ Enabling GitHub Pages (1-Minute Setup)

1. Push your repository:
   ```powershell
   git push -u origin main
   ```
2. On GitHub, navigate to:
   **`https://github.com/IG-Creation/ROI_PF_Chatbot`** $\rightarrow$ **Settings** $\rightarrow$ **Pages**
3. Under **Build and deployment**:
   - **Source**: Select **GitHub Actions** (the included `.github/workflows/deploy.yml` will automatically deploy it), OR select **Deploy from a branch** $\rightarrow$ Branch: `main` $\rightarrow$ Folder: `/ (root)` $\rightarrow$ Click **Save**.
4. In under 60 seconds, your public link is live at:
   **`https://ig-creation.github.io/ROI_PF_Chatbot/`**

---

## 📄 License
MIT License. Created for IG-Creation.
