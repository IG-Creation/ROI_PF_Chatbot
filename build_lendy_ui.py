# -*- coding: utf-8 -*-
"""
Script to generate the upgraded, ultra-high-definition Lendy Chatbot UI.
Features:
- Dedicated floating 3D Robot Cat Companion (Image 2 & 3: pearl-white ceramic, DJ headphones, big glossy eyes, chest reactor)
- Automatic behavior cycle: 4 legs sitting, 2 legs standing, face washing with paw, laughing, thinking, alert
- No clicking needed, fully autonomous
- Glowing Cyber Circuit Motherboard phone wallpaper (Image 4) as default + 4 other rich themes
- Full multi-language dictionary (EN, HI, GU, ML)
- Complete sanctioned vs. requested loan evaluation flow with CEO floor overrides (<15% ROI, <1.5% PF)
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="en" data-theme="cyber-circuit">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Lendy 🐱 — 3D Smart Loan Pricing & Deviation Assistant</title>
  <link rel="manifest" href="./manifest.json">
  <meta name="theme-color" content="#0284c7">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="description" content="Lendy is an executive 3D loan pricing and deviation evaluation chatbot for credit managers and officers.">

  <style>
    /* ==========================================================================
       VIBRANT PHONE WALLPAPER THEMES & COLOR SYSTEM (INSPIRED BY USER IMAGES)
       ========================================================================== */
    :root, [data-theme="cyber-circuit"] {
      /* Theme 1: Cyber Circuit Motherboard (Exact match of User's Image 4) */
      --bg-base: #030712;
      --circuit-line: #00f0ff;
      --circuit-glow: rgba(0, 240, 255, 0.45);
      --circuit-sub: #0284c7;
      --panel-bg: rgba(6, 12, 28, 0.86);
      --card-bg: rgba(10, 20, 42, 0.78);
      --card-hover: rgba(14, 30, 64, 0.9);
      --border-line: rgba(0, 240, 255, 0.28);
      --border-glow: #00f0ff;
      --text-main: #ffffff;
      --text-muted: #bae6fd;
      --text-subtle: #38bdf8;
      --accent-primary: #00f0ff;
      --accent-secondary: #818cf8;
      --accent-hot: #f43f5e;
      --accent-emerald: #10b981;
      --color-green: #34d399;
      --color-green-bg: rgba(52, 211, 153, 0.22);
      --color-blue: #38bdf8;
      --color-blue-bg: rgba(56, 189, 248, 0.22);
      --color-amber: #fbbf24;
      --color-amber-bg: rgba(251, 191, 36, 0.22);
      --color-red: #f87171;
      --color-red-bg: rgba(248, 113, 113, 0.25);
      --btn-grad: linear-gradient(135deg, #00f0ff, #2563eb);
      --bubble-user-grad: linear-gradient(135deg, #0284c7, #4f46e5);
      --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", Roboto, sans-serif;
    }

    [data-theme="cosmic-nebula"] {
      /* Theme 2: Deep Cosmic Nebula & Stardust */
      --bg-base: #09021a;
      --circuit-line: #c084fc;
      --circuit-glow: rgba(192, 132, 252, 0.45);
      --circuit-sub: #7c3aed;
      --panel-bg: rgba(18, 8, 38, 0.88);
      --card-bg: rgba(30, 14, 62, 0.8);
      --card-hover: rgba(48, 22, 95, 0.92);
      --border-line: rgba(192, 132, 252, 0.3);
      --border-glow: #c084fc;
      --text-main: #ffffff;
      --text-muted: #f5d0fe;
      --text-subtle: #c084fc;
      --accent-primary: #c084fc;
      --accent-secondary: #60a5fa;
      --accent-hot: #f472b6;
      --accent-emerald: #34d399;
      --color-green: #34d399;
      --color-green-bg: rgba(52, 211, 153, 0.22);
      --color-blue: #60a5fa;
      --color-blue-bg: rgba(96, 165, 250, 0.22);
      --color-amber: #fbbf24;
      --color-amber-bg: rgba(251, 191, 36, 0.22);
      --color-red: #f87171;
      --color-red-bg: rgba(248, 113, 113, 0.25);
      --btn-grad: linear-gradient(135deg, #c084fc, #db2777);
      --bubble-user-grad: linear-gradient(135deg, #7c3aed, #c026d3);
    }

    [data-theme="neo-tokyo"] {
      /* Theme 3: Neo Tokyo Cyberpunk Skyline */
      --bg-base: #060814;
      --circuit-line: #f43f5e;
      --circuit-glow: rgba(244, 63, 94, 0.45);
      --circuit-sub: #06b6d4;
      --panel-bg: rgba(10, 14, 28, 0.88);
      --card-bg: rgba(20, 24, 46, 0.8);
      --card-hover: rgba(32, 38, 72, 0.92);
      --border-line: rgba(244, 63, 94, 0.3);
      --border-glow: #f43f5e;
      --text-main: #ffffff;
      --text-muted: #fecdd3;
      --text-subtle: #fda4af;
      --accent-primary: #f43f5e;
      --accent-secondary: #38bdf8;
      --accent-hot: #fbbf24;
      --accent-emerald: #10b981;
      --color-green: #34d399;
      --color-green-bg: rgba(52, 211, 153, 0.22);
      --color-blue: #38bdf8;
      --color-blue-bg: rgba(56, 189, 248, 0.22);
      --color-amber: #fbbf24;
      --color-amber-bg: rgba(251, 191, 36, 0.22);
      --color-red: #f87171;
      --color-red-bg: rgba(248, 113, 113, 0.25);
      --btn-grad: linear-gradient(135deg, #f43f5e, #8b5cf6);
      --bubble-user-grad: linear-gradient(135deg, #e11d48, #6366f1);
    }

    [data-theme="sunset-gold"] {
      /* Theme 4: Sunset Gold Obsidian */
      --bg-base: #0d0603;
      --circuit-line: #f59e0b;
      --circuit-glow: rgba(245, 158, 11, 0.45);
      --circuit-sub: #ea580c;
      --panel-bg: rgba(24, 10, 6, 0.88);
      --card-bg: rgba(42, 18, 10, 0.8);
      --card-hover: rgba(64, 28, 16, 0.92);
      --border-line: rgba(245, 158, 11, 0.3);
      --border-glow: #f59e0b;
      --text-main: #ffffff;
      --text-muted: #fef3c7;
      --text-subtle: #f59e0b;
      --accent-primary: #f59e0b;
      --accent-secondary: #f43f5e;
      --accent-hot: #ea580c;
      --accent-emerald: #10b981;
      --color-green: #34d399;
      --color-green-bg: rgba(52, 211, 153, 0.22);
      --color-blue: #38bdf8;
      --color-blue-bg: rgba(56, 189, 248, 0.22);
      --color-amber: #fbbf24;
      --color-amber-bg: rgba(251, 191, 36, 0.22);
      --color-red: #f87171;
      --color-red-bg: rgba(248, 113, 113, 0.25);
      --btn-grad: linear-gradient(135deg, #f59e0b, #e11d48);
      --bubble-user-grad: linear-gradient(135deg, #ea580c, #be123c);
    }

    [data-theme="emerald-matrix"] {
      /* Theme 5: Emerald Digital Matrix */
      --bg-base: #02120b;
      --circuit-line: #10b981;
      --circuit-glow: rgba(16, 185, 129, 0.45);
      --circuit-sub: #059669;
      --panel-bg: rgba(4, 26, 18, 0.88);
      --card-bg: rgba(8, 44, 30, 0.8);
      --card-hover: rgba(14, 68, 46, 0.92);
      --border-line: rgba(16, 185, 129, 0.3);
      --border-glow: #10b981;
      --text-main: #ffffff;
      --text-muted: #d1fae5;
      --text-subtle: #34d399;
      --accent-primary: #10b981;
      --accent-secondary: #06b6d4;
      --accent-hot: #f43f5e;
      --accent-emerald: #34d399;
      --color-green: #34d399;
      --color-green-bg: rgba(52, 211, 153, 0.22);
      --color-blue: #38bdf8;
      --color-blue-bg: rgba(56, 189, 248, 0.22);
      --color-amber: #fbbf24;
      --color-amber-bg: rgba(251, 191, 36, 0.22);
      --color-red: #f87171;
      --color-red-bg: rgba(248, 113, 113, 0.25);
      --btn-grad: linear-gradient(135deg, #10b981, #0284c7);
      --bubble-user-grad: linear-gradient(135deg, #059669, #0ea5e9);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html, body {
      width: 100%;
      height: 100%;
      height: 100dvh;
      overflow: hidden;
      background: var(--bg-base);
      color: var(--text-main);
      font-family: var(--font-stack);
      font-size: 15px;
      line-height: 1.5;
      position: relative;
    }

    body {
      display: flex;
      flex-direction: column;
      padding-top: env(safe-area-inset-top);
      padding-bottom: env(safe-area-inset-bottom);
      padding-left: env(safe-area-inset-left);
      padding-right: env(safe-area-inset-right);
    }

    /* ==========================================================================
       GLOWING CIRCUIT BOARD WALLPAPER BACKGROUND (EXACT MATCH OF USER IMAGE 4)
       ========================================================================== */
    .wallpaper-art {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
      background: var(--bg-base);
    }

    /* High-Definition SVG Circuit Board Wallpaper Pattern */
    .circuit-wallpaper-svg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      opacity: 0.85;
      object-fit: cover;
    }

    .bokeh-light {
      position: absolute;
      border-radius: 50%;
      filter: blur(80px);
      pointer-events: none;
      opacity: 0.45;
      animation: float-bokeh 16s infinite alternate ease-in-out;
    }

    .b1 { width: 360px; height: 360px; background: var(--circuit-glow); top: -60px; left: -40px; }
    .b2 { width: 420px; height: 420px; background: var(--circuit-sub); bottom: 10%; right: -60px; animation-duration: 20s; }

    @keyframes float-bokeh {
      0% { transform: translateY(0) scale(1); }
      100% { transform: translateY(45px) scale(1.15); }
    }

    /* Circuit light pulses running through traces */
    @keyframes circuit-pulse {
      0%, 100% { opacity: 0.3; stroke-dashoffset: 0; }
      50% { opacity: 0.9; stroke-dashoffset: -40; }
    }
    .circuit-stream {
      stroke-dasharray: 12, 28;
      animation: circuit-pulse 4s infinite linear;
    }

    /* ==========================================================================
       HEADER & NAVIGATION BAR
       ========================================================================== */
    .app-header {
      height: 70px;
      background: var(--panel-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--border-line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      flex-shrink: 0;
      z-index: 30;
      box-shadow: 0 4px 25px rgba(0, 0, 0, 0.6);
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .header-logo {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: var(--btn-grad);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      box-shadow: 0 0 16px var(--circuit-glow);
      border: 1px solid rgba(255, 255, 255, 0.25);
    }

    .header-titles h1 {
      font-size: 17px;
      font-weight: 800;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 6px;
      background: linear-gradient(135deg, var(--accent-primary), #ffffff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .header-titles p {
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .lang-selector-btn, .theme-selector-btn, .reset-btn {
      min-height: 38px;
      padding: 0 12px;
      background: var(--card-bg);
      border: 1px solid var(--border-line);
      border-radius: 9999px;
      color: var(--text-main);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      backdrop-filter: blur(10px);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    .lang-selector-btn:hover, .theme-selector-btn:hover, .reset-btn:hover {
      border-color: var(--border-glow);
      box-shadow: 0 0 12px var(--circuit-glow);
      transform: translateY(-1px);
    }

    /* ==========================================================================
       CHAT HISTORY CONTAINER
       ========================================================================== */
    .chat-container {
      flex: 1;
      overflow-y: auto;
      padding: 16px 16px 180px 16px; /* Bottom padding keeps room for floating companion */
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: relative;
      z-index: 10;
      scroll-behavior: smooth;
    }

    .chat-container::-webkit-scrollbar {
      width: 5px;
    }
    .chat-container::-webkit-scrollbar-thumb {
      background: var(--border-line);
      border-radius: 4px;
    }

    .message-row {
      display: flex;
      gap: 10px;
      max-width: 820px;
      width: 100%;
      margin: 0 auto;
    }

    .message-row.user {
      justify-content: flex-end;
    }

    .avatar-badge {
      width: 38px;
      height: 38px;
      border-radius: 12px;
      background: var(--btn-grad);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
      box-shadow: 0 0 14px var(--circuit-glow);
      border: 1px solid rgba(255, 255, 255, 0.25);
    }

    .message-bubble {
      padding: 14px 18px;
      border-radius: 18px;
      line-height: 1.55;
      font-size: 14.5px;
      position: relative;
      word-break: break-word;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }

    .message-row.bot .message-bubble {
      background: var(--card-bg);
      border: 1px solid var(--border-line);
      color: var(--text-main);
      border-top-left-radius: 4px;
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.5);
    }

    .message-row.user .message-bubble {
      background: var(--bubble-user-grad);
      color: #ffffff;
      border-top-right-radius: 4px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.25);
      font-weight: 500;
    }

    /* Typing Dots */
    .typing-dots {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 2px;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      background: var(--accent-primary);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--accent-primary);
      animation: dot-glow 1.4s infinite ease-in-out both;
    }

    .pulse-dot:nth-child(1) { animation-delay: -0.32s; }
    .pulse-dot:nth-child(2) { animation-delay: -0.16s; }

    @keyframes dot-glow {
      0%, 80%, 100% { transform: scale(0.4); opacity: 0.3; }
      40% { transform: scale(1.1); opacity: 1; }
    }

    /* ==========================================================================
       CARDS, STATUS & TABLES
       ========================================================================== */
    .status-card {
      background: var(--panel-bg);
      border: 1px solid var(--border-line);
      border-radius: 16px;
      overflow: hidden;
      margin-top: 12px;
      box-shadow: 0 10px 32px rgba(0, 0, 0, 0.6);
    }

    .status-card-header {
      padding: 14px 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 800;
      font-size: 15.5px;
      border-bottom: 1px solid var(--border-line);
    }

    .status-card-header.green {
      background: var(--color-green-bg);
      color: var(--color-green);
      border-bottom-color: rgba(52, 211, 153, 0.4);
      box-shadow: inset 0 0 20px rgba(52, 211, 153, 0.15);
    }

    .status-card-header.blue {
      background: var(--color-blue-bg);
      color: var(--color-blue);
      border-bottom-color: rgba(56, 189, 248, 0.4);
      box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.15);
    }

    .status-card-header.amber {
      background: var(--color-amber-bg);
      color: var(--color-amber);
      border-bottom-color: rgba(251, 191, 36, 0.4);
      box-shadow: inset 0 0 20px rgba(251, 191, 36, 0.15);
    }

    .status-card-header.red {
      background: var(--color-red-bg);
      color: var(--color-red);
      border-bottom-color: rgba(248, 113, 113, 0.4);
      box-shadow: inset 0 0 25px rgba(248, 113, 113, 0.25);
    }

    .status-card-body {
      padding: 14px 18px;
      background: rgba(255, 255, 255, 0.02);
      font-size: 13.5px;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-line);
      line-height: 1.6;
    }

    .status-card-body strong {
      color: var(--text-main);
    }

    .floor-badge {
      display: inline-block;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 800;
      background: var(--color-red-bg);
      color: var(--color-red);
      border: 1px solid rgba(248, 113, 113, 0.4);
      margin-bottom: 8px;
    }

    .comparison-table-wrapper {
      width: 100%;
      overflow-x: auto;
    }

    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }

    .comparison-table th, 
    .comparison-table td {
      padding: 12px 16px;
      text-align: left;
      border-bottom: 1px solid var(--border-line);
    }

    .comparison-table th {
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.05em;
    }

    .comparison-table td:last-child,
    .comparison-table th:last-child {
      text-align: right;
    }

    .tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 10px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
    }

    .tag-badge.favorable { background: var(--color-green-bg); color: var(--color-green); border: 1px solid rgba(52, 211, 153, 0.3); }
    .tag-badge.cbo { background: var(--color-blue-bg); color: var(--color-blue); border: 1px solid rgba(96, 165, 250, 0.3); }
    .tag-badge.coo { background: var(--color-amber-bg); color: var(--color-amber); border: 1px solid rgba(251, 191, 36, 0.3); }
    .tag-badge.ceo { background: var(--color-red-bg); color: var(--color-red); border: 1px solid rgba(248, 113, 113, 0.3); }

    .summary-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      padding: 14px;
      background: rgba(0, 0, 0, 0.3);
    }

    @media (min-width: 600px) {
      .summary-grid { grid-template-columns: repeat(4, 1fr); }
    }

    .stat-cell {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-line);
      border-radius: 12px;
      padding: 12px;
    }

    .stat-title {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-subtle);
      font-weight: 700;
      margin-bottom: 4px;
    }

    .stat-num {
      font-size: 18px;
      font-weight: 800;
      color: var(--text-main);
    }

    .stat-sub {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .alert-banner {
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      font-weight: 600;
    }

    .alert-banner.amber {
      background: var(--color-amber-bg);
      color: var(--color-amber);
      border-top: 1px solid rgba(251, 191, 36, 0.3);
    }

    /* ==========================================================================
       TAPPABLE CHIPS
       ========================================================================== */
    .chips-area {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 8px 16px;
      max-width: 820px;
      margin: 0 auto;
      z-index: 20;
    }

    .action-chip {
      min-height: 44px;
      padding: 0 16px;
      background: var(--card-bg);
      border: 1px solid var(--border-line);
      border-radius: 9999px;
      color: var(--text-main);
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      backdrop-filter: blur(14px);
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.35);
    }

    .action-chip:hover {
      background: var(--card-hover);
      border-color: var(--border-glow);
      transform: translateY(-2px);
      box-shadow: 0 0 14px var(--circuit-glow);
    }

    .action-chip:active {
      transform: translateY(0);
    }

    .action-chip.primary-glow {
      border-color: var(--accent-primary);
      box-shadow: 0 0 12px var(--circuit-glow);
      background: rgba(0, 240, 255, 0.12);
    }

    /* ==========================================================================
       DEDICATED 3D ROBOT CAT COMPANION STAGE (IMAGE 2 & 3 INSPIRED)
       Positioned gracefully floating above the input dock on the right
       ========================================================================== */
    .companion-dock {
      position: fixed;
      right: 18px;
      bottom: 76px; /* Sits right above input bar */
      width: 125px;
      height: 155px;
      z-index: 40;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
      pointer-events: none; /* Allows scrolling chat behind it */
    }

    /* Holographic Base Pedestal Ring */
    .holo-pedestal {
      position: absolute;
      bottom: 2px;
      width: 90px;
      height: 24px;
      border-radius: 50%;
      background: radial-gradient(ellipse, var(--circuit-glow) 0%, rgba(0, 240, 255, 0.1) 40%, transparent 70%);
      border: 1px solid var(--circuit-glow);
      box-shadow: 0 0 18px var(--circuit-glow);
      animation: holo-scan 3s infinite alternate ease-in-out;
      pointer-events: none;
    }

    @keyframes holo-scan {
      0% { transform: scale(0.95); opacity: 0.6; }
      100% { transform: scale(1.05); opacity: 1; box-shadow: 0 0 24px var(--border-glow); }
    }

    .robot-cat-interactive {
      position: relative;
      width: 110px;
      height: 140px;
      pointer-events: auto; /* Clickable & Hoverable */
      cursor: pointer;
      transform-origin: center bottom;
      transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    /* Cat Speech Bubble */
    .companion-speech {
      position: absolute;
      bottom: 142px;
      right: 6px;
      background: var(--panel-bg);
      border: 1px solid var(--border-glow);
      padding: 7px 14px;
      border-radius: 16px;
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-primary);
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transform: translateY(8px) scale(0.85);
      transition: all 0.28s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
      z-index: 50;
    }

    .companion-speech.active {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    .companion-speech::after {
      content: "";
      position: absolute;
      bottom: -6px;
      right: 36px;
      border-width: 6px 6px 0;
      border-style: solid;
      border-color: var(--border-glow) transparent transparent;
    }

    /* ==========================================================================
       LIFELIKE AUTONOMOUS ANIMATIONS: 4 LEGS <-> 2 LEGS, FACE WASHING, LAUGHING
       ========================================================================== */

    /* Breathing cycle */
    @keyframes cat-idle-breathe {
      0%, 100% { transform: translateY(0) scaleY(1); }
      50% { transform: translateY(-3px) scaleY(1.02); }
    }
    .anim-breathe {
      animation: cat-idle-breathe 2.6s infinite ease-in-out;
    }

    /* Tail swaying */
    @keyframes cat-tail-wag {
      0%, 100% { transform: rotate(0deg); }
      50% { transform: rotate(26deg); }
    }
    .anim-tail {
      transform-origin: 26px 105px;
      animation: cat-tail-wag 2s infinite ease-in-out;
    }

    /* Headphone ear-cups twitching */
    @keyframes ear-twitch {
      0%, 85%, 100% { transform: rotate(0deg); }
      90% { transform: rotate(-5deg); }
      95% { transform: rotate(4deg); }
    }
    .anim-headphones {
      transform-origin: 60px 45px;
      animation: ear-twitch 5s infinite;
    }

    /* Chest reactor light pulsation */
    @keyframes reactor-pulse {
      0%, 100% { opacity: 0.65; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.18); filter: drop-shadow(0 0 8px #00f0ff); }
    }
    .anim-core {
      transform-origin: 60px 88px;
      animation: reactor-pulse 1.8s infinite ease-in-out;
    }

    /* Talking mouth jaw animation */
    @keyframes cat-talk-jaw {
      0%, 100% { transform: scaleY(1); }
      50% { transform: scaleY(1.9); }
    }
    .talking-now .mouth-jaw {
      animation: cat-talk-jaw 0.22s infinite alternate ease-in-out;
      transform-origin: center;
    }

    /* Face Washing / Paw Grooming Animation (Exact match of User's Request!) */
    @keyframes paw-wash-face {
      0% { transform: translate(0, 0) rotate(0deg); }
      20% { transform: translate(-10px, -24px) rotate(-35deg); }
      40% { transform: translate(-16px, -28px) rotate(-45deg); }
      60% { transform: translate(-8px, -20px) rotate(-30deg); }
      80% { transform: translate(-14px, -26px) rotate(-40deg); }
      100% { transform: translate(0, 0) rotate(0deg); }
    }
    .washing-face .arm-right-paw {
      animation: paw-wash-face 1.8s infinite ease-in-out !important;
      transform-origin: 78px 84px;
    }

    /* Head tilts blissfully during face-wash */
    @keyframes head-tilt-wash {
      0%, 100% { transform: rotate(0deg); }
      50% { transform: rotate(6deg) translateY(-2px); }
    }
    .washing-face .cat-head-group {
      animation: head-tilt-wash 1.8s infinite ease-in-out;
      transform-origin: 60px 48px;
    }

    /* Laughing / Giggling like Talking Tom */
    @keyframes cat-laugh-bounce {
      0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
      20% { transform: translateY(-7px) rotate(-4deg) scale(1.08); }
      40% { transform: translateY(0) rotate(4deg) scale(1.04); }
      60% { transform: translateY(-8px) rotate(-3deg) scale(1.1); }
      80% { transform: translateY(-2px) rotate(2deg) scale(1.05); }
    }
    .laughing-now {
      animation: cat-laugh-bounce 0.65s infinite ease-in-out !important;
    }

    /* Posture transitions between 4 legs and 2 legs */
    .posture-4legs .torso-body {
      transform: translateY(10px) scaleY(0.9);
      transform-origin: center bottom;
      transition: transform 0.4s ease;
    }
    .posture-4legs .hind-standing-legs {
      opacity: 0;
      transition: opacity 0.3s;
    }
    .posture-4legs .hind-folded-legs {
      opacity: 1;
      transition: opacity 0.3s;
    }
    .posture-4legs .front-paws-floor {
      opacity: 1;
      transition: opacity 0.3s;
    }

    .posture-2legs .torso-body {
      transform: translateY(0) scaleY(1);
      transform-origin: center bottom;
      transition: transform 0.4s ease;
    }
    .posture-2legs .hind-standing-legs {
      opacity: 1;
      transition: opacity 0.3s;
    }
    .posture-2legs .hind-folded-legs {
      opacity: 0;
      transition: opacity 0.3s;
    }
    .posture-2legs .front-paws-floor {
      opacity: 0;
      transition: opacity 0.3s;
    }

    /* ==========================================================================
       STICKY BOTTOM INPUT BAR (SPACIOUS FULL WIDTH)
       ========================================================================== */
    .input-bar-container {
      background: var(--panel-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-top: 1px solid var(--border-line);
      padding: 10px 16px;
      flex-shrink: 0;
      z-index: 30;
      position: relative;
    }

    .input-row-wrapper {
      max-width: 820px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 12px;
      position: relative;
    }

    .input-field-wrapper {
      flex: 1;
      position: relative;
    }

    .chat-input {
      width: 100%;
      min-height: 48px;
      background: var(--card-bg);
      border: 1px solid var(--border-line);
      border-radius: 9999px;
      padding: 12px 22px;
      color: var(--text-main);
      font-size: 15px;
      font-family: inherit;
      outline: none;
      transition: all 0.2s ease;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4);
    }

    .chat-input:focus {
      border-color: var(--border-glow);
      box-shadow: 0 0 16px var(--circuit-glow);
    }

    .chat-input::placeholder {
      color: rgba(255, 255, 255, 0.4);
    }

    .send-action-btn {
      min-width: 48px;
      min-height: 48px;
      width: 48px;
      height: 48px;
      background: var(--btn-grad);
      color: #ffffff;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      flex-shrink: 0;
      box-shadow: 0 0 16px var(--circuit-glow);
    }

    .send-action-btn:hover {
      transform: scale(1.08);
      box-shadow: 0 0 22px var(--border-glow);
    }

    .send-action-btn:active {
      transform: scale(0.94);
    }

    .send-action-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }

    .send-action-btn svg {
      width: 20px;
      height: 20px;
      fill: none;
      stroke: currentColor;
      stroke-width: 2.3;
      stroke-linecap: round;
      stroke-linejoin: round;
      margin-left: 2px;
    }

    .input-hint-line {
      font-size: 11.5px;
      color: var(--text-muted);
      margin-top: 5px;
      text-align: center;
    }
  </style>
</head>
<body>

  <!-- ==========================================================================
       HIGH-TECH PRINTED CIRCUIT BOARD PHONE WALLPAPER (EXACT MATCH OF IMAGE 4)
       ========================================================================== -->
  <div class="wallpaper-art">
    <svg class="circuit-wallpaper-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1200" preserveAspectRatio="xMidYMid slice">
      <defs>
        <!-- Circuit Board Glow Filter -->
        <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>

        <!-- Dynamic Theme Gradients -->
        <linearGradient id="traceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="var(--circuit-line)" stop-opacity="0.9"/>
          <stop offset="50%" stop-color="var(--circuit-sub)" stop-opacity="0.7"/>
          <stop offset="100%" stop-color="var(--circuit-line)" stop-opacity="0.85"/>
        </linearGradient>
      </defs>

      <!-- Deep Grid Lines -->
      <g stroke="rgba(255,255,255,0.03)" stroke-width="1">
        <line x1="0" y1="150" x2="800" y2="150"/>
        <line x1="0" y1="300" x2="800" y2="300"/>
        <line x1="0" y1="450" x2="800" y2="450"/>
        <line x1="0" y1="600" x2="800" y2="600"/>
        <line x1="0" y1="750" x2="800" y2="750"/>
        <line x1="0" y1="900" x2="800" y2="900"/>
        <line x1="0" y1="1050" x2="800" y2="1050"/>
        <line x1="160" y1="0" x2="160" y2="1200"/>
        <line x1="320" y1="0" x2="320" y2="1200"/>
        <line x1="480" y1="0" x2="480" y2="1200"/>
        <line x1="640" y1="0" x2="640" y2="1200"/>
      </g>

      <!-- Motherboard IC Microchips & SMD Pads -->
      <g fill="rgba(0,0,0,0.55)" stroke="var(--circuit-line)" stroke-width="1.8" filter="url(#neonGlow)">
        <rect x="120" y="220" width="80" height="80" rx="6"/>
        <rect x="580" y="380" width="100" height="120" rx="8"/>
        <rect x="220" y="680" width="110" height="90" rx="6"/>
        <rect x="520" y="850" width="90" height="90" rx="8"/>
        <rect x="80" y="960" width="70" height="70" rx="4"/>
      </g>

      <!-- Chip Pins & SMT Footprints -->
      <g stroke="var(--circuit-sub)" stroke-width="1.5">
        <line x1="110" y1="240" x2="120" y2="240"/>
        <line x1="110" y1="260" x2="120" y2="260"/>
        <line x1="110" y1="280" x2="120" y2="280"/>
        <line x1="200" y1="240" x2="210" y2="240"/>
        <line x1="200" y1="260" x2="210" y2="260"/>
        <line x1="200" y1="280" x2="210" y2="280"/>
        <line x1="580" y1="410" x2="570" y2="410"/>
        <line x1="580" y1="440" x2="570" y2="440"/>
        <line x1="580" y1="470" x2="570" y2="470"/>
        <line x1="680" y1="410" x2="690" y2="410"/>
        <line x1="680" y1="440" x2="690" y2="440"/>
        <line x1="680" y1="470" x2="690" y2="470"/>
      </g>

      <!-- Intricate Printed Circuit Traces (45-degree angled paths like Image 4) -->
      <g fill="none" stroke="url(#traceGrad)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" filter="url(#neonGlow)">
        <!-- Trace Group 1 -->
        <path d="M60,60 L140,60 L200,120 L200,220"/>
        <path d="M160,20 L240,100 L360,100 L420,160 L420,320 L500,400 L580,400"/>
        <path d="M720,80 L660,140 L660,280 L620,320 L620,380"/>
        <path d="M300,40 L450,40 L520,110 L520,240"/>
        
        <!-- Trace Group 2 (Center Data Highway) -->
        <path d="M160,300 L160,420 L260,520 L380,520 L440,580 L440,740"/>
        <path d="M200,260 L280,260 L340,320 L340,460 L460,580 L580,580"/>
        <path d="M630,500 L630,640 L540,730 L400,730 L330,800 L330,880"/>
        <path d="M680,460 L740,520 L740,760 L650,850 L610,850"/>

        <!-- Trace Group 3 (Lower Motherboard Bus) -->
        <path d="M80,620 L150,620 L220,690 L220,770 L160,830 L160,960"/>
        <path d="M270,770 L270,900 L360,990 L520,990 L560,940"/>
        <path d="M440,740 L440,860 L490,910 L520,910"/>
        <path d="M120,960 L120,880 L60,820 L60,700"/>
        <path d="M570,940 L570,1080 L480,1170 L200,1170"/>
        <path d="M610,890 L710,890 L760,940 L760,1120"/>
      </g>

      <!-- Pulsing Data Stream Packets -->
      <g fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" class="circuit-stream">
        <path d="M160,20 L240,100 L360,100 L420,160 L420,320 L500,400 L580,400"/>
        <path d="M160,300 L160,420 L260,520 L380,520 L440,580 L440,740"/>
        <path d="M270,770 L270,900 L360,990 L520,990 L560,940"/>
      </g>

      <!-- Circular Solder Vias & Golden Nodes (Matching Image 4) -->
      <g fill="var(--circuit-line)" stroke="#ffffff" stroke-width="1.5" filter="url(#neonGlow)">
        <circle cx="60" cy="60" r="4.5"/>
        <circle cx="160" cy="20" r="4.5"/>
        <circle cx="720" cy="80" r="4.5"/>
        <circle cx="300" cy="40" r="4.5"/>
        <circle cx="520" cy="240" r="4.5"/>
        <circle cx="580" cy="580" r="4.5"/>
        <circle cx="740" cy="760" r="4.5"/>
        <circle cx="80" cy="620" r="4.5"/>
        <circle cx="60" cy="700" r="4.5"/>
        <circle cx="760" cy="1120" r="4.5"/>
        <circle cx="200" cy="1170" r="4.5"/>
      </g>
    </svg>

    <!-- Ambient Glowing Bokeh Orbs -->
    <div class="bokeh-light b1"></div>
    <div class="bokeh-light b2"></div>
  </div>

  <!-- Header -->
  <header class="app-header">
    <div class="header-left">
      <div class="header-logo">🐱</div>
      <div class="header-titles">
        <h1>
          <span>Lendy AI</span>
          <span style="font-size: 11px; font-weight: normal; color: var(--color-green);">● Online</span>
        </h1>
        <p id="appSubtitle">Executive Loan Pricing & Deviation Assistant</p>
      </div>
    </div>

    <div class="header-actions">
      <!-- Multi-Language Selector -->
      <button class="lang-selector-btn" id="langBtn" onclick="cycleLanguage()" title="Switch Language">
        <span>🌐</span>
        <span id="currentLangLabel">English</span>
      </button>

      <!-- Wallpaper Theme Selector -->
      <button class="theme-selector-btn" id="themeBtn" onclick="cycleWallpaperTheme()" title="Switch Phone Wallpaper">
        <span id="themeEmoji">⚡</span>
      </button>

      <!-- Restart Session -->
      <button class="reset-btn" onclick="restartSession()" title="Restart Session">
        <span>🔄</span>
      </button>
    </div>
  </header>

  <!-- Chat History Stream -->
  <main class="chat-container" id="chatContainer" aria-live="polite"></main>

  <!-- Quick Reply Tappable Chips -->
  <div class="chips-area" id="chipsArea" role="group" aria-label="Quick response options"></div>

  <!-- ==========================================================================
       DEDICATED 3D ROBOT CAT COMPANION STAGE (IMAGE 2 & 3 INSPIRED)
       Perched proudly on its floating holographic dock above the input dock!
       ========================================================================== -->
  <div class="companion-dock" id="companionDock">
    <!-- Holographic Scanner Pedestal Base -->
    <div class="holo-pedestal"></div>

    <!-- Live Speech Bubble -->
    <div class="companion-speech" id="companionBubble">Ready to price! 🐾</div>

    <!-- 3D Robot Cat Companion (Autonomous Animations: 4 legs, 2 legs, face-wash, laugh) -->
    <div class="robot-cat-interactive anim-breathe posture-2legs" id="robotCat" onclick="catInteractedManually()" title="I'm Lendy! I automatically react, stand, and wash my face!">
      <svg viewBox="0 0 120 150" style="width: 100%; height: 100%; overflow: visible;">
        <defs>
          <!-- Pearl-White Glossy Ceramic Shading (Image 3) -->
          <linearGradient id="whiteCeramic" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="45%" stop-color="#f8fafc"/>
            <stop offset="80%" stop-color="#e2e8f0"/>
            <stop offset="100%" stop-color="#94a3b8"/>
          </linearGradient>

          <!-- Specular Curved Highlight -->
          <linearGradient id="glossHighlight" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="0.85"/>
            <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
          </linearGradient>

          <!-- Headphone Outer Ring (Orange Glow - Image 3) -->
          <linearGradient id="hpOrange" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fbbf24"/>
            <stop offset="100%" stop-color="#ea580c"/>
          </linearGradient>

          <!-- Headphone Center (Electric Cyan - Image 3) -->
          <radialGradient id="hpCyan" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#67e8f9"/>
            <stop offset="70%" stop-color="#0284c7"/>
            <stop offset="100%" stop-color="#0c4a6e"/>
          </radialGradient>

          <!-- Large Expressive Anime Eyes (Image 2 & 3) -->
          <radialGradient id="eyeIris" cx="45%" cy="45%" r="55%">
            <stop offset="0%" stop-color="#67e8f9"/>
            <stop offset="50%" stop-color="#0284c7"/>
            <stop offset="85%" stop-color="#082f49"/>
            <stop offset="100%" stop-color="#020617"/>
          </radialGradient>
        </defs>

        <!-- Swaying Expressive Cyber Tail -->
        <g class="anim-tail">
          <path d="M26,108 Q6,120 4,96 Q2,74 20,68" fill="none" stroke="url(#whiteCeramic)" stroke-width="8" stroke-linecap="round"/>
          <circle cx="20" cy="68" r="5" fill="#00f0ff" filter="drop-shadow(0 0 6px #00f0ff)"/>
        </g>

        <!-- Standing Hind Legs / Feet (posture-2legs) -->
        <g class="hind-standing-legs">
          <ellipse cx="42" cy="132" rx="11" ry="8" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.8"/>
          <ellipse cx="78" cy="132" rx="11" ry="8" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.8"/>
          <!-- Soft paw pads -->
          <circle cx="38" cy="134" r="2.5" fill="#38bdf8"/>
          <circle cx="43" cy="135" r="2.5" fill="#38bdf8"/>
          <circle cx="48" cy="134" r="2.5" fill="#38bdf8"/>
          <circle cx="74" cy="134" r="2.5" fill="#38bdf8"/>
          <circle cx="79" cy="135" r="2.5" fill="#38bdf8"/>
          <circle cx="84" cy="134" r="2.5" fill="#38bdf8"/>
        </g>

        <!-- Crouched Hind Legs for Sitting (posture-4legs) -->
        <g class="hind-folded-legs" style="opacity: 0;">
          <ellipse cx="30" cy="122" rx="14" ry="10" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.8"/>
          <ellipse cx="90" cy="122" rx="14" ry="10" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.8"/>
        </g>

        <!-- Upright Pearlescent Ceramic Torso -->
        <g class="torso-body">
          <ellipse cx="60" cy="94" rx="28" ry="34" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="2"/>
          <path d="M48,70 Q60,65 72,70 Q80,95 70,118 Q60,124 50,118 Q40,95 48,70 Z" fill="#ffffff" opacity="0.9"/>

          <!-- Glowing Chest Power Core Reactor (Image 3) -->
          <g class="anim-core" id="chestReactor">
            <circle cx="60" cy="88" r="8" fill="none" stroke="#00f0ff" stroke-width="2.5" filter="drop-shadow(0 0 6px #00f0ff)"/>
            <circle cx="60" cy="88" r="4.5" fill="#00f0ff"/>
            <circle cx="60" cy="104" r="4" fill="#00f0ff" opacity="0.8"/>
          </g>

          <!-- Golden Collar with Status Light -->
          <rect x="44" y="66" width="32" height="6" rx="3" fill="#f59e0b" stroke="#b45309" stroke-width="1"/>
          <circle cx="60" cy="72" r="5" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2" filter="drop-shadow(0 0 4px #38bdf8)"/>

          <!-- Front Paws for 4-legs Sitting Mode -->
          <g class="front-paws-floor" style="opacity: 0;">
            <ellipse cx="48" cy="132" rx="8" ry="6" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.5"/>
            <ellipse cx="72" cy="132" rx="8" ry="6" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.5"/>
          </g>

          <!-- Left Arm & Paw (Free to gesture) -->
          <g class="arm-left-paw">
            <path d="M34,76 Q20,92 30,104" fill="none" stroke="url(#whiteCeramic)" stroke-width="8" stroke-linecap="round"/>
            <circle cx="30" cy="104" r="5.5" fill="#ffffff" stroke="#64748b" stroke-width="1.5"/>
            <circle cx="30" cy="105" r="2.5" fill="#38bdf8"/>
          </g>

          <!-- Right Arm & Paw (Grooming / Washing Face / Gesturing) -->
          <g class="arm-right-paw" id="rightPawGroup">
            <path id="rightArmPath" d="M86,76 Q100,92 90,104" fill="none" stroke="url(#whiteCeramic)" stroke-width="8" stroke-linecap="round"/>
            <circle id="rightPawCirc" cx="90" cy="104" r="5.5" fill="#ffffff" stroke="#64748b" stroke-width="1.5"/>
            <circle cx="90" cy="105" r="2.5" fill="#38bdf8"/>
          </g>
        </g>

        <!-- Head, Cat Ears & Cyber DJ Headphones Group -->
        <g class="cat-head-group" id="headGroup">
          <!-- Cyber Headphones (White Arch Band + Orange/Cyan Ear-cups - Image 3) -->
          <g class="anim-headphones">
            <!-- White Headband Arc -->
            <path d="M22,36 Q60,4 98,36" fill="none" stroke="url(#whiteCeramic)" stroke-width="6.5" stroke-linecap="round"/>
            <path d="M26,34 Q60,8 94,34" fill="none" stroke="#64748b" stroke-width="1.5"/>

            <!-- Left DJ Ear-Cup -->
            <g transform="translate(10, 26)">
              <rect x="0" y="0" width="14" height="28" rx="7" fill="#1e293b" stroke="url(#hpOrange)" stroke-width="2.5" filter="drop-shadow(0 0 6px #f59e0b)"/>
              <circle cx="7" cy="14" r="4.5" fill="url(#hpCyan)"/>
            </g>

            <!-- Right DJ Ear-Cup -->
            <g transform="translate(96, 26)">
              <rect x="0" y="0" width="14" height="28" rx="7" fill="#1e293b" stroke="url(#hpOrange)" stroke-width="2.5" filter="drop-shadow(0 0 6px #f59e0b)"/>
              <circle cx="7" cy="14" r="4.5" fill="url(#hpCyan)"/>
            </g>

            <!-- Cat Ears with Neon Accents (Image 2) -->
            <polygon points="32,32 16,6 46,18" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.8"/>
            <polygon points="32,28 22,12 42,18" fill="#fda4af"/>
            <polygon points="88,32 104,6 74,18" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="1.8"/>
            <polygon points="88,28 98,12 78,18" fill="#fda4af"/>
          </g>

          <!-- Glossy Ceramic Robot Head (Image 3) -->
          <ellipse cx="60" cy="42" rx="30" ry="26" fill="url(#whiteCeramic)" stroke="#64748b" stroke-width="2"/>
          <ellipse cx="60" cy="24" rx="20" ry="8" fill="url(#glossHighlight)"/>

          <!-- Whiskers with Glowing Neon Tips -->
          <line x1="24" y1="46" x2="38" y2="48" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="24" cy="46" r="1.8" fill="#00f0ff"/>
          <line x1="22" y1="52" x2="37" y2="50" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="22" cy="52" r="1.8" fill="#00f0ff"/>

          <line x1="96" y1="46" x2="82" y2="48" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="96" cy="46" r="1.8" fill="#00f0ff"/>
          <line x1="98" y1="52" x2="83" y2="50" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="98" cy="52" r="1.8" fill="#00f0ff"/>

          <!-- Large Anime Glossy Eyes (Image 2 & 3) -->
          <!-- Left Eye -->
          <ellipse id="eyeLeft" cx="47" cy="38" rx="8" ry="10" fill="url(#eyeIris)" stroke="#0f172a" stroke-width="1.8"/>
          <ellipse id="pupilLeft" cx="47" cy="38" rx="3.5" ry="6.5" fill="#020617"/>
          <circle cx="45" cy="34" r="2.8" fill="#ffffff"/>
          <circle cx="49" cy="42" r="1.4" fill="#ffffff"/>

          <!-- Right Eye -->
          <ellipse id="eyeRight" cx="73" cy="38" rx="8" ry="10" fill="url(#eyeIris)" stroke="#0f172a" stroke-width="1.8"/>
          <ellipse id="pupilRight" cx="73" cy="38" rx="3.5" ry="6.5" fill="#020617"/>
          <circle cx="71" cy="34" r="2.8" fill="#ffffff"/>
          <circle cx="75" cy="42" r="1.4" fill="#ffffff"/>

          <!-- Cute Triangular Robot Nose -->
          <polygon points="57,47 63,47 60,51" fill="#f43f5e"/>

          <!-- Friendly Animated Mouth / Jaw (Image 3) -->
          <g class="mouth-jaw" id="mouthJaw">
            <path id="mouthLine" d="M53,52 Q60,58 67,52" fill="none" stroke="#0284c7" stroke-width="2.4" stroke-linecap="round"/>
          </g>

          <!-- Blushing Cheeks -->
          <ellipse cx="36" cy="48" rx="4.5" ry="2.8" fill="#f43f5e" opacity="0.35"/>
          <ellipse cx="84" cy="48" rx="4.5" ry="2.8" fill="#f43f5e" opacity="0.35"/>
        </g>
      </svg>
    </div>
  </div>

  <!-- Sticky Bottom Input Bar (Full Width & Spacious) -->
  <footer class="input-bar-container">
    <div class="input-row-wrapper">
      <div class="input-field-wrapper">
        <form id="inputForm" onsubmit="event.preventDefault(); submitInput();">
          <input 
            type="text" 
            id="userInput" 
            class="chat-input" 
            placeholder="Type your response here..." 
            autocomplete="off" 
            enterkeyhint="send"
            aria-label="User input"
          >
        </form>
      </div>

      <button 
        type="button" 
        id="sendBtn" 
        class="send-action-btn" 
        onclick="submitInput()" 
        aria-label="Send response" 
        title="Send"
      >
        <svg viewBox="0 0 24 24">
          <line x1="22" y1="2" x2="11" y2="13"/>
          <polygon points="22 2 15 22 11 13 2 9 22 2"/>
        </svg>
      </button>
    </div>
    <div class="input-hint-line" id="inputHint">Tap an option chip or type your input</div>
  </footer>

  <!-- ==========================================================================
       LOGIC, I18N, AND AUTONOMOUS COMPANION ENGINE
       ========================================================================== */
  -->
  <script>
    /* ==========================================================================
       MULTI-LANGUAGE LOCALIZATION DICTIONARY
       ========================================================================== */
    const I18N = {
      en: {
        code: "en", label: "English",
        subtitle: "Executive Loan Pricing & Deviation Assistant",
        welcome: "👋 Hello Officer! I'm <strong>Lendy</strong>, your credit pricing & policy approval copilot.<br><br>Let's evaluate current vs. requested loan parameters, check our 56-row policy matrix, and calculate precise EMI & DTI deviations.<br><br><strong>What is the customer or case reference name?</strong>",
        askProduct: "Which <strong>Loan Product</strong> is under review for",
        askIncomeProg: "Under which <strong>Income Program</strong> is this loan assessed?",
        askProperty: "What is the <strong>Property Type</strong> mortgaged?",
        askBureau: "What is the borrower's <strong>Bureau Category</strong>?",
        askSancAmount: "What is the <strong>Current Sanctioned Loan Amount</strong>?",
        askSancTenure: "What is the <strong>Current Sanctioned Tenure</strong>?",
        askSancRoi: "What is the <strong>Current Sanctioned ROI (% p.a.)</strong>?",
        askSancPf: "What is the <strong>Current Sanctioned Processing Fee (PF %)</strong>?",
        askIncomeFreq: "How would you like to enter the borrower's gross earnings?",
        askIncomeAmount: "Enter gross earnings amount for",
        askExistingEmis: "What are the borrower's <strong>total existing monthly EMIs / obligations</strong>? (0 if none)",
        sancStatusTitle: "📊 Current Sanctioned Status & Policy Benchmarks",
        sancEmiLabel: "Current Sanctioned EMI",
        currentDtiLabel: "Current DTI Ratio",
        baseRoiLabel: "Matrix Base ROI",
        basePfLabel: "Matrix Base PF",
        askReqRoi: "What is the borrower's <strong>Requested ROI (% p.a.)</strong>?",
        askReqPf: "What is the borrower's <strong>Requested Processing Fee (PF %)</strong>?",
        floorWarningRoi: "⚠️ Note: Per policy floor, any Requested ROI < 15% mandates CEO approval.",
        floorWarningPf: "⚠️ Note: Per policy floor, any Requested PF < 1.5% mandates CEO approval.",
        evalTitle: "🎯 Comprehensive Deviation & Approval Assessment",
        btnTryRates: "Try different Requested ROI/PF",
        btnNewCase: "Evaluate new customer",
        floorAlert: "🏛️ MANDATORY POLICY FLOOR BREACH TRIGGERED (CEO APPROVAL)",
        dtiAlertTitle: "⚠️ Prudent DTI Alert (>50%)",
        tableHeader: ["Parameter", "Matrix Benchmark", "Current Sanctioned", "Proposed Requested", "Deviation / Status"],
        monthly: "Monthly", annual: "Annual"
      },
      hi: {
        code: "hi", label: "हिंदी",
        subtitle: "ऋण मूल्य निर्धारण एवं विचलन मूल्यांकन सहायक",
        welcome: "👋 नमस्ते ऑफिसर! मैं <strong>लेंडी (Lendy)</strong> हूँ, आपका ऋण मूल्य निर्धारण एवं नीति अनुमोदन सहायक।<br><br>आइए स्वीकृत बनाम अनुरोधित ऋण शर्तों का मूल्यांकन करें, 56-पंक्ति मैट्रिक्स जांचें और ईएमआई तथा डीटीआई की सटीक गणना करें।<br><br><strong>ग्राहक का नाम या केस संदर्भ (Reference) क्या है?</strong>",
        askProduct: "के लिए कौन सा <strong>ऋण उत्पाद (Loan Product)</strong> चुनना चाहते हैं:",
        askIncomeProg: "यह ऋण किस <strong>आय कार्यक्रम (Income Program)</strong> के तहत मूल्यांकित है?",
        askProperty: "बंधक रखी गई <strong>संपत्ति का प्रकार (Property Type)</strong> क्या है?",
        askBureau: "उधारकर्ता की <strong>ब्यूरो श्रेणी (Bureau Category)</strong> क्या है?",
        askSancAmount: "वर्तमान <strong>स्वीकृत ऋण राशि (Sanctioned Loan Amount)</strong> कितनी है?",
        askSancTenure: "वर्तमान <strong>स्वीकृत अवधि (Sanctioned Tenure)</strong> कितनी है?",
        askSancRoi: "वर्तमान <strong>स्वीकृत ब्याज दर (Sanctioned ROI % p.a.)</strong> क्या है?",
        askSancPf: "वर्तमान <strong>स्वीकृत प्रोसेसिंग शुल्क (Sanctioned PF %)</strong> क्या है?",
        askIncomeFreq: "उधारकर्ता की कुल आय कैसे दर्ज करना चाहते हैं?",
        askIncomeAmount: "सकल आय दर्ज करें:",
        askExistingEmis: "उधारकर्ता की <strong>कुल मौजूदा मासिक ईएमआई / देयताएं</strong> कितनी हैं? (यदि कोई नहीं तो 0)",
        sancStatusTitle: "📊 वर्तमान स्वीकृत स्थिति एवं नीति बेंचमार्क",
        sancEmiLabel: "स्वीकृत ईएमआई",
        currentDtiLabel: "मौजूदा डीटीआई अनुपात",
        baseRoiLabel: "मैट्रिक्स बेस आरओआई",
        basePfLabel: "मैट्रिक्स बेस पीएफ",
        askReqRoi: "उधारकर्ता द्वारा <strong>अनुरोधित ब्याज दर (Requested ROI % p.a.)</strong> क्या है?",
        askReqPf: "उधारकर्ता द्वारा <strong>अनुरोधित प्रोसेसिंग शुल्क (Requested PF %)</strong> क्या है?",
        floorWarningRoi: "⚠️ ध्यान दें: नीतिगत न्यूनतम सीमा के अनुसार, 15% से कम ROI के लिए CEO अनुमोदन अनिवार्य है।",
        floorWarningPf: "⚠️ ध्यान दें: नीतिगत न्यूनतम सीमा के अनुसार, 1.5% से कम PF के लिए CEO अनुमोदन अनिवार्य है।",
        evalTitle: "🎯 संपूर्ण विचलन एवं अनुमोदन मूल्यांकन रिपोर्ट",
        btnTryRates: "अन्य ROI/PF दरें जांचें",
        btnNewCase: "नया केस दर्ज करें",
        floorAlert: "🏛️ नीतिगत न्यूनतम सीमा उल्लंघन (CEO अनुमोदन अनिवार्य)",
        dtiAlertTitle: "⚠️ उच्च डीटीआई चेतावनी (>50%)",
        tableHeader: ["पैरामीटर", "मैट्रिक्स बेंचमार्क", "वर्तमान स्वीकृत", "प्रस्तावित अनुरोध", "विचलन / प्राधिकारी"],
        monthly: "मासिक", annual: "वार्षिक"
      },
      gu: {
        code: "gu", label: "ગુજરાતી",
        subtitle: "લોન પ્રાઇસિંગ અને મંજૂરી સહાયક AI",
        welcome: "👋 નમસ્તે ઓફિસર! હું <strong>લેન્ડી (Lendy)</strong> છું, તમારો લોન પ્રાઇસિંગ અને પોલિસી એપ્રૂવલ સહાયક.<br><br>ચાલો મંજૂર અને માંગણી કરેલ લોન શરતોનું મૂલ્યાંકન કરીએ અને સચોટ EMI અને DTI ની ગણતરી કરીએ.<br><br><strong>ગ્રાહકનું નામ અથવા કેસ રેફરન્સ શું છે?</strong>",
        askProduct: "માટે કયું <strong>લોન પ્રોડક્ટ</strong> પસંદ કરશો?",
        askIncomeProg: "આ લોન કયા <strong>ઇન્કમ પ્રોગ્રામ</strong> હેઠળ છે?",
        askProperty: "મિલકતનો પ્રકાર <strong>(Property Type)</strong> શું છે?",
        askBureau: "ઉધાર લેનારની <strong>બ્યુરો કેટેગરી</strong> શું છે?",
        askSancAmount: "હાલમાં <strong>મંજૂર કરેલ લોનની રકમ (Sanctioned Amount)</strong> કેટલી છે?",
        askSancTenure: "હાલની <strong>મંજૂર મુદત (Sanctioned Tenure)</strong> કેટલી છે?",
        askSancRoi: "હાલનો <strong>મંજૂર વ્યાજ દર (Sanctioned ROI % p.a.)</strong> કેટલો છે?",
        askSancPf: "હાલની <strong>મંજૂર પ્રોસેસિંગ ફી (Sanctioned PF %)</strong> કેટલી છે?",
        askIncomeFreq: "કુલ આવક કેવી રીતે દાખલ કરવા માંગો છો?",
        askIncomeAmount: "આવક દાખલ કરો:",
        askExistingEmis: "ઉધાર લેનારની <strong>હાલની કુલ માસિક EMI</strong> કેટલી છે? (ન હોય તો 0)",
        sancStatusTitle: "📊 વર્તમાન મંજૂર સ્થિતિ અને પોલિસી બેન્ચમાર્ક",
        sancEmiLabel: "મંજૂર માસિક EMI",
        currentDtiLabel: "હાલનો DTI રેશિયો",
        baseRoiLabel: "મેટ્રિક્સ બેઝ ROI",
        basePfLabel: "મેટ્રિક્સ બેઝ PF",
        askReqRoi: "ગ્રાહક દ્વારા <strong>માંગણી કરેલ વ્યાજ દર (Requested ROI % p.a.)</strong> શું છે?",
        askReqPf: "ગ્રાહક દ્વારા <strong>માંગણી કરેલ પ્રોસેસિંગ ફી (Requested PF %)</strong> શું છે?",
        floorWarningRoi: "⚠️ નોંધ: પોલિસી મુજબ, 15% કરતા ઓછી ROI માટે CEO મંજૂરી ફરજિયાત છે.",
        floorWarningPf: "⚠️ નોંધ: પોલિસી મુજબ, 1.5% કરતા ઓછી PF માટે CEO મંજૂરી ફરજિયાત છે.",
        evalTitle: "🎯 સંપૂર્ણ વિચલન અને મંજૂરી અહેવાલ",
        btnTryRates: "અન્ય ROI/PF દરો ચકાસો",
        btnNewCase: "નવો કેસ દાખલ કરો",
        floorAlert: "🏛️ પોલિસી ફ્લોર ઉલ્લંઘન (CEO મંજૂરી ફરજિયાત)",
        dtiAlertTitle: "⚠️ ઊંચો DTI રેશિયો (>50%)",
        tableHeader: ["પરિમાણ", "મેટ્રિક્સ બેન્ચમાર્ક", "હાલ મંજૂર", "પ્રસ્તાવિત માંગણી", "વિચલન / મંજૂરી"],
        monthly: "માસિક", annual: "વાર્ષિક"
      },
      ml: {
        code: "ml", label: "മലയാളം",
        subtitle: "ലോൺ പ്രൈസിംഗ് & അപ്രൂവൽ അസിസ്റ്റന്റ്",
        welcome: "👋 നമസ്കാരം ഓഫീസർ! ഞാൻ <strong>ലെൻഡി (Lendy)</strong>. നിങ്ങളുടെ ലോൺ പ്രൈസിംഗ് അസിസ്റ്റന്റ്.<br><br>നമുക്ക് അനുവദിച്ചതും ആവശ്യപ്പെട്ടതുമായ ലോൺ നിബന്ധനകൾ താരതമ്യം ചെയ്ത് ശരിയായ ഇ.എം.ഐ, ഡി.ടി.ഐ എന്നിവ കണക്കാക്കാം.<br><br><strong>ഉപഭോക്താവിന്റെ പേര് അല്ലെങ്കിൽ കേസ് റഫറൻസ് നൽകുക:</strong>",
        askProduct: "തിരഞ്ഞെടുക്കേണ്ട <strong>ലോൺ പ്രൊഡക്റ്റ്</strong> ഏതാണ്:",
        askIncomeProg: "ഏത് <strong>ഇൻകം പ്രോഗ്രാം</strong> പ്രകാരമാണ് വിലയിരുത്തുന്നത്?",
        askProperty: "പണയപ്പെടുത്തുന്ന <strong>വസ്തുവിന്റെ തരം (Property Type)</strong> ഏതാണ്?",
        askBureau: "കടം വാങ്ങുന്നയാളുടെ <strong>ബ്യൂറോ കാറ്റഗറി</strong> എന്താണ്?",
        askSancAmount: "നിലവിൽ <strong>അനുവദിച്ച ലോൺ തുക (Sanctioned Amount)</strong> എത്രയാണ്?",
        askSancTenure: "നിലവിൽ <strong>അനുവദിച്ച കാലാവധി (Sanctioned Tenure)</strong> എത്രയാണ്?",
        askSancRoi: "നിലവിൽ <strong>അനുവദിച്ച പലിശ നിരക്ക് (Sanctioned ROI % p.a.)</strong> എത്രയാണ്?",
        askSancPf: "നിലവിൽ <strong>അനുവദിച്ച പ്രോസസ്സിംഗ് ഫീസ് (Sanctioned PF %)</strong> എത്രയാണ്?",
        askIncomeFreq: "വരുമാനം എങ്ങനെ രേഖപ്പെടുത്തണം?",
        askIncomeAmount: "മൊത്തം വരുമാനം നൽകുക:",
        askExistingEmis: "നിലവിലുള്ള <strong>പ്രതിമാസ ബാധ്യതകൾ / EMI</strong> എത്രയാണ്? (ഇല്ലെങ്കിൽ 0)",
        sancStatusTitle: "📊 നിലവിൽ അനുവദിച്ച നിബന്ധനകളും പോളിസി ബെഞ്ച്മാർക്കും",
        sancEmiLabel: "അനുവദിച്ച EMI",
        currentDtiLabel: "നിലവിലെ DTI അനുപാതം",
        baseRoiLabel: "പോളിസി ബേസ് ROI",
        basePfLabel: "പോളിസി ബേസ് PF",
        askReqRoi: "ആവശ്യപ്പെട്ട <strong>പലിശ നിരക്ക് (Requested ROI % p.a.)</strong> എത്രയാണ്?",
        askReqPf: "ആവശ്യപ്പെട്ട <strong>പ്രോസസ്സിംഗ് ഫീസ് (Requested PF %)</strong> എത്രയാണ്?",
        floorWarningRoi: "⚠️ ശ്രദ്ധിക്കുക: പോളിസി പ്രകാരം 15% താഴെയുള്ള ROI-ക്ക് CEO അംഗീകാരം നിർബന്ധമാണ്.",
        floorWarningPf: "⚠️ ശ്രദ്ധിക്കുക: പോളിസി പ്രകാരം 1.5% താഴെയുള്ള PF-ന് CEO അംഗീകാരം നിർബന്ധമാണ്.",
        evalTitle: "🎯 പൂർണ്ണ ഡീവിയേഷൻ & അപ്രൂവൽ റിപ്പോർട്ട്",
        btnTryRates: "മറ്റ് നിരക്കുകൾ പരിശോധിക്കുക",
        btnNewCase: "പുതിയ കേസ് രേഖപ്പെടുത്തുക",
        floorAlert: "🏛️ പോളിസി ഫ്ലോർ ലംഘനം (CEO അംഗീകാരം നിർബന്ധം)",
        dtiAlertTitle: "⚠️ ഉയർന്ന DTI മുന്നറിയിപ്പ് (>50%)",
        tableHeader: ["പരാമീറ്റർ", "പോളിസി ബെഞ്ച്മാർക്ക്", "നിലവിൽ അനുവദിച്ചത്", "നിർദ്ദേശിച്ചത്", "ഡീവിയേഷൻ / അതോറിറ്റി"],
        monthly: "പ്രതിമാസം", annual: "വാർഷികം"
      }
    };

    let currentLang = "en";
    function t(key) {
      const dict = I18N[currentLang] || I18N.en;
      return dict[key] !== undefined ? dict[key] : (I18N.en[key] || key);
    }

    function cycleLanguage() {
      const langs = ["en", "hi", "gu", "ml"];
      const nextIdx = (langs.indexOf(currentLang) + 1) % langs.length;
      setLanguage(langs[nextIdx]);
    }

    function setLanguage(langCode) {
      if (!I18N[langCode]) return;
      currentLang = langCode;
      document.getElementById("currentLangLabel").textContent = I18N[langCode].label;
      document.getElementById("appSubtitle").textContent = t("subtitle");
      companionSpeech(`Language set to ${I18N[langCode].label}! ✨`, 2200);
    }

    /* ==========================================================================
       WALLPAPER THEME ENGINE (5 VIBRANT PHONE WALLPAPERS)
       ========================================================================== */
    const WALLPAPER_THEMES = [
      { id: "cyber-circuit", name: "Cyber Circuit", emoji: "⚡" },
      { id: "cosmic-nebula", name: "Cosmic Nebula", emoji: "🌌" },
      { id: "neo-tokyo", name: "Neo Tokyo", emoji: "🏙️" },
      { id: "sunset-gold", name: "Sunset Gold", emoji: "🌅" },
      { id: "emerald-matrix", name: "Emerald Matrix", emoji: "🌿" }
    ];
    let currentThemeIdx = 0;

    function cycleWallpaperTheme() {
      currentThemeIdx = (currentThemeIdx + 1) % WALLPAPER_THEMES.length;
      const theme = WALLPAPER_THEMES[currentThemeIdx];
      document.documentElement.setAttribute("data-theme", theme.id);
      document.getElementById("themeEmoji").textContent = theme.emoji;
      localStorage.setItem("lendy_theme", theme.id);
      companionSpeech(`Wallpaper: ${theme.name}! 🎨`, 2000);
    }

    /* ==========================================================================
       BUSINESS RULES & 56-ROW POLICY MATRIX CONFIG
       ========================================================================== */
    const CONFIG = {
      APP_NAME: "Lendy Loan Pricing & Approval Assistant",
      DTI_LIMIT_PERCENT: 50.0,
      ROUNDING_TOLERANCE: 1e-6,
      ROI_FLOOR_PERCENT: 15.0,
      PF_FLOOR_PERCENT: 1.5,
      PRODUCTS: {
        R: "Regular Secured Business Loan",
        W: "Secured Working Capital Term Loan",
        H: "Hypothecation Loans"
      },
      APPROVERS: {
        NONE: { name: "No Approval Needed", level: 0, color: "green", tag: "favorable" },
        CBO:  { name: "CBO Approval", level: 1, color: "blue", tag: "cbo" },
        COO:  { name: "COO Approval", level: 2, color: "amber", tag: "coo" },
        CEO:  { name: "CEO Approval", level: 3, color: "red", tag: "ceo" }
      },
      MATRIX: [
        { product: "R", ticket: "U", income: "D", prop: "SORP", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "D", prop: "SORP", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "D", prop: "Other", bureau: "G", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "D", prop: "Other", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "A", prop: "SORP", bureau: "G", baseRoi: 21.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "A", prop: "SORP", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "A", prop: "Other", bureau: "G", baseRoi: 21.5, basePf: 3.0 },
        { product: "R", ticket: "U", income: "A", prop: "Other", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "Hy", prop: "SORP", bureau: "G", baseRoi: 21.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "Hy", prop: "SORP", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "Hy", prop: "Other", bureau: "G", baseRoi: 21.5, basePf: 3.0 },
        { product: "R", ticket: "U", income: "Hy", prop: "Other", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "S", prop: "SORP", bureau: "G", baseRoi: 21.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "S", prop: "SORP", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "R", ticket: "U", income: "S", prop: "Other", bureau: "G", baseRoi: 21.5, basePf: 3.0 },
        { product: "R", ticket: "U", income: "S", prop: "Other", bureau: "L", baseRoi: 22.0, basePf: 3.0 },

        { product: "R", ticket: "A", income: "D", prop: "SORP", bureau: "G", baseRoi: 18.0, basePf: 2.0 },
        { product: "R", ticket: "A", income: "D", prop: "SORP", bureau: "L", baseRoi: 20.0, basePf: 2.0 },
        { product: "R", ticket: "A", income: "D", prop: "Other", bureau: "G", baseRoi: 19.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "D", prop: "Other", bureau: "L", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "A", prop: "SORP", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "A", prop: "SORP", bureau: "L", baseRoi: 20.5, basePf: 3.0 },
        { product: "R", ticket: "A", income: "A", prop: "Other", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "A", prop: "Other", bureau: "L", baseRoi: 21.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "Hy", prop: "SORP", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "Hy", prop: "SORP", bureau: "L", baseRoi: 20.5, basePf: 3.0 },
        { product: "R", ticket: "A", income: "Hy", prop: "Other", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "Hy", prop: "Other", bureau: "L", baseRoi: 21.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "S", prop: "SORP", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "S", prop: "SORP", bureau: "L", baseRoi: 20.5, basePf: 3.0 },
        { product: "R", ticket: "A", income: "S", prop: "Other", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "R", ticket: "A", income: "S", prop: "Other", bureau: "L", baseRoi: 21.0, basePf: 3.0 },

        { product: "W", ticket: "L", income: "D", prop: "SORP", bureau: "G", baseRoi: 22.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "D", prop: "SORP", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "D", prop: "Other", bureau: "G", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "D", prop: "Other", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "A", prop: "SORP", bureau: "G", baseRoi: 23.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "A", prop: "SORP", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "A", prop: "Other", bureau: "G", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "A", prop: "Other", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "Hy", prop: "SORP", bureau: "G", baseRoi: 23.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "Hy", prop: "SORP", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "Hy", prop: "Other", bureau: "G", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "Hy", prop: "Other", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "S", prop: "SORP", bureau: "G", baseRoi: 23.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "S", prop: "SORP", bureau: "L", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "S", prop: "Other", bureau: "G", baseRoi: 24.0, basePf: 3.0 },
        { product: "W", ticket: "L", income: "S", prop: "Other", bureau: "L", baseRoi: 24.0, basePf: 3.0 },

        { product: "H", ticket: "L", income: "D", prop: "NA", bureau: "G", baseRoi: 20.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "D", prop: "NA", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "A", prop: "NA", bureau: "G", baseRoi: 22.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "A", prop: "NA", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "Hy", prop: "NA", bureau: "G", baseRoi: 22.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "Hy", prop: "NA", bureau: "L", baseRoi: 22.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "S", prop: "NA", bureau: "G", baseRoi: 22.0, basePf: 3.0 },
        { product: "H", ticket: "L", income: "S", prop: "NA", bureau: "L", baseRoi: 22.0, basePf: 3.0 }
      ]
    };

    /* ==========================================================================
       PURE FINANCIAL & APPROVAL LOGIC FUNCTIONS
       ========================================================================== */
    function lookupBaseRates(product, ticket, incomeProg, propType, bureau) {
      const match = CONFIG.MATRIX.find(m =>
        m.product === product &&
        m.ticket === ticket &&
        m.income === incomeProg &&
        m.prop === propType &&
        m.bureau === bureau
      );
      return match ? { baseRoi: match.baseRoi, basePf: match.basePf } : null;
    }

    function calculateReducingEMI(principal, annualRatePercent, tenureMonths) {
      if (!principal || principal <= 0 || !tenureMonths || tenureMonths <= 0) return 0;
      if (!annualRatePercent || annualRatePercent <= 0) return Math.round(principal / tenureMonths);
      const r = (annualRatePercent / 12.0) / 100.0;
      const factor = Math.pow(1 + r, tenureMonths);
      const emi = (principal * r * factor) / (factor - 1);
      return Math.round(emi);
    }
    const calculateEMI = calculateReducingEMI;

    function calculateDTI(existingEmis, newEmi, monthlyIncome) {
      if (!monthlyIncome || monthlyIncome <= 0) {
        return { currentDti: 0, updatedDti: 0, warning: false };
      }
      const cur = (existingEmis / monthlyIncome) * 100.0;
      const upd = ((existingEmis + newEmi) / monthlyIncome) * 100.0;
      return {
        currentDti: parseFloat(cur.toFixed(1)),
        updatedDti: parseFloat(upd.toFixed(1)),
        warning: upd > CONFIG.DTI_LIMIT_PERCENT
      };
    }

    function evaluateApproval(baseRoi, reqRoi, basePf, reqPf) {
      const tol = CONFIG.ROUNDING_TOLERANCE;
      const roiDev = baseRoi - reqRoi;
      const pfDev = basePf - reqPf;

      let roiApprover = CONFIG.APPROVERS.NONE;
      if (reqRoi < CONFIG.ROI_FLOOR_PERCENT - tol) {
        roiApprover = CONFIG.APPROVERS.CEO;
      } else if (roiDev > tol) {
        if (roiDev <= 2.0 + tol) roiApprover = CONFIG.APPROVERS.CBO;
        else if (roiDev <= 4.0 + tol) roiApprover = CONFIG.APPROVERS.COO;
        else roiApprover = CONFIG.APPROVERS.CEO;
      }

      let pfApprover = CONFIG.APPROVERS.NONE;
      if (reqPf < CONFIG.PF_FLOOR_PERCENT - tol) {
        pfApprover = CONFIG.APPROVERS.CEO;
      } else if (pfDev > tol) {
        if (pfDev <= 1.0 + tol) pfApprover = CONFIG.APPROVERS.CBO;
        else if (pfDev <= 1.5 + tol) pfApprover = CONFIG.APPROVERS.COO;
        else pfApprover = CONFIG.APPROVERS.CEO;
      }

      const finalLevel = Math.max(roiApprover.level, pfApprover.level);
      let finalApprover = CONFIG.APPROVERS.NONE;
      if (finalLevel === 3) finalApprover = CONFIG.APPROVERS.CEO;
      else if (finalLevel === 2) finalApprover = CONFIG.APPROVERS.COO;
      else if (finalLevel === 1) finalApprover = CONFIG.APPROVERS.CBO;

      const isRoiFloor = reqRoi < CONFIG.ROI_FLOOR_PERCENT - tol;
      const isPfFloor = reqPf < CONFIG.PF_FLOOR_PERCENT - tol;

      let explanation = "";
      if (isRoiFloor || isPfFloor) {
        explanation = `Mandatory CEO Approval required: Requested rate breached policy floors (ROI Floor: ${CONFIG.ROI_FLOOR_PERCENT}%, PF Floor: ${CONFIG.PF_FLOOR_PERCENT}%).`;
      } else if (finalApprover.level === 0) {
        explanation = "Proposed terms meet or exceed standard benchmark matrix. No pricing deviation approval required.";
      } else {
        const parts = [];
        if (roiApprover.level > 0) parts.push(`ROI concession of ${roiDev.toFixed(2)}% pts (${roiApprover.name.replace(' Approval','')})`);
        if (pfApprover.level > 0) parts.push(`PF concession of ${pfDev.toFixed(2)}% pts (${pfApprover.name.replace(' Approval','')})`);
        explanation = `${parts.join(" and ")} requires ${finalApprover.name}.`;
      }

      return {
        roiDeviation: parseFloat(roiDev.toFixed(4)),
        pfDeviation: parseFloat(pfDev.toFixed(4)),
        roiApprover,
        pfApprover,
        finalApprover,
        color: finalApprover.color,
        explanation,
        isFloorBreached: isRoiFloor || isPfFloor
      };
    }

    function formatINR(val) {
      if (val === null || val === undefined || isNaN(val)) return "₹0";
      const rounded = Math.round(val);
      const str = Math.abs(rounded).toString();
      let lastThree = str.substring(str.length - 3);
      const otherNumbers = str.substring(0, str.length - 3);
      if (otherNumbers !== '') {
        lastThree = ',' + lastThree;
      }
      const formatted = otherNumbers.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + lastThree;
      return (rounded < 0 ? "-₹" : "₹") + formatted;
    }

    function escapeHtml(str) {
      if (!str) return "";
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }

    function parseNumber(input) {
      if (!input) return null;
      let clean = String(input).toLowerCase().replace(/,/g, "").trim();
      const crMatch = clean.match(/([\d.]+)\s*(?:cr|crore|crores)/);
      if (crMatch) return parseFloat(crMatch[1]) * 10000000;
      const lacMatch = clean.match(/([\d.]+)\s*(?:lakh|lakhs|lac|lacs|l)/);
      if (lacMatch) return parseFloat(lacMatch[1]) * 100000;
      const numMatch = clean.match(/[\d.]+/);
      if (numMatch) {
        const parsed = parseFloat(numMatch[0]);
        return isNaN(parsed) ? null : parsed;
      }
      return null;
    }

    function parseTenureMonths(input) {
      if (!input) return null;
      const clean = String(input).toLowerCase().replace(/,/g, "").trim();
      const yrMatch = clean.match(/([\d.]+)\s*(?:year|years|yr|yrs|y)/);
      if (yrMatch) return Math.round(parseFloat(yrMatch[1]) * 12);
      const moMatch = clean.match(/(\d+)\s*(?:month|months|mo|mos|m)?/);
      if (moMatch) return parseInt(moMatch[1], 10);
      return null;
    }

    /* ==========================================================================
       AUTONOMOUS 3D ROBOT CAT COMPANION CONTROLLER
       Automatic cycle: 4 legs sitting, 2 legs standing, face washing with paw!
       No clicking required.
       ========================================================================== */
    const robotCat = document.getElementById("robotCat");
    const companionBubble = document.getElementById("companionBubble");
    const headGroup = document.getElementById("headGroup");
    const eyeLeft = document.getElementById("eyeLeft");
    const eyeRight = document.getElementById("eyeRight");
    const mouthLine = document.getElementById("mouthLine");

    let autoCycleTimer = null;
    const AUTONOMOUS_ACTIONS = [
      "posture-4legs",
      "action-wash-face",
      "posture-2legs",
      "action-wash-face",
      "action-laugh",
      "posture-4legs"
    ];
    let autoActionIndex = 0;

    function companionSpeech(text, durationMs = 2800) {
      if (!companionBubble) return;
      companionBubble.textContent = text;
      companionBubble.classList.add("active");
      setTimeout(() => companionBubble.classList.remove("active"), durationMs);
    }

    function setCatVisualState(stateName) {
      if (!robotCat) return;

      // Reset dynamic action classes
      robotCat.classList.remove("washing-face", "laughing-now", "talking-now", "posture-4legs", "posture-2legs");

      switch (stateName) {
        case "wash-face":
          robotCat.classList.add("washing-face", "posture-2legs");
          // Adorable crescent squinting eyes while washing face
          eyeLeft.setAttribute("ry", "3"); eyeRight.setAttribute("ry", "3");
          mouthLine.setAttribute("d", "M54,52 Q60,57 66,52");
          companionSpeech("Washing my face! 🐾", 2400);
          break;

        case "four-legs":
          robotCat.classList.add("posture-4legs");
          eyeLeft.setAttribute("ry", "9"); eyeRight.setAttribute("ry", "9");
          mouthLine.setAttribute("d", "M53,52 Q60,57 67,52");
          break;

        case "two-legs":
          robotCat.classList.add("posture-2legs");
          eyeLeft.setAttribute("ry", "10"); eyeRight.setAttribute("ry", "10");
          mouthLine.setAttribute("d", "M53,52 Q60,58 67,52");
          break;

        case "laughing":
          robotCat.classList.add("laughing-now", "posture-2legs");
          eyeLeft.setAttribute("ry", "3.5"); eyeRight.setAttribute("ry", "3.5");
          mouthLine.setAttribute("d", "M52,50 Q60,63 68,50 Z");
          mouthLine.setAttribute("fill", "#0284c7");
          companionSpeech("Hehehe! Purrrr! 😸", 2200);
          break;

        case "talking":
          robotCat.classList.add("talking-now", "posture-2legs");
          eyeLeft.setAttribute("ry", "9"); eyeRight.setAttribute("ry", "9");
          mouthLine.setAttribute("d", "M52,51 Q60,59 68,51");
          mouthLine.setAttribute("fill", "none");
          break;

        case "thinking":
          robotCat.classList.add("posture-2legs");
          eyeLeft.setAttribute("ry", "7"); eyeRight.setAttribute("ry", "7");
          mouthLine.setAttribute("d", "M54,53 L66,53");
          mouthLine.setAttribute("fill", "none");
          break;

        case "worried":
          robotCat.classList.add("posture-2legs");
          eyeLeft.setAttribute("ry", "11"); eyeRight.setAttribute("ry", "11");
          mouthLine.setAttribute("d", "M53,55 Q60,49 67,55");
          mouthLine.setAttribute("fill", "none");
          companionSpeech("Floor breach alert! 🏛️", 2600);
          break;

        case "celebrating":
          robotCat.classList.add("laughing-now", "posture-2legs");
          eyeLeft.setAttribute("ry", "4"); eyeRight.setAttribute("ry", "4");
          mouthLine.setAttribute("d", "M51,50 Q60,65 69,50 Z");
          mouthLine.setAttribute("fill", "#00f0ff");
          companionSpeech("Approved without deviation! 🎉", 2800);
          break;

        default:
          robotCat.classList.add("posture-2legs");
          eyeLeft.setAttribute("ry", "10"); eyeRight.setAttribute("ry", "10");
          mouthLine.setAttribute("d", "M53,52 Q60,58 67,52");
          mouthLine.setAttribute("fill", "none");
          break;
      }
    }

    // Fully autonomous life-cycle loop (Switches automatically every 5-6s)
    function startAutonomousCatLifeCycle() {
      if (autoCycleTimer) clearInterval(autoCycleTimer);
      autoCycleTimer = setInterval(() => {
        // Only run autonomous idle behaviors if no active calculation or typing row
        const isTyping = document.querySelector(".typing-row");
        if (!isTyping) {
          autoActionIndex = (autoActionIndex + 1) % AUTONOMOUS_ACTIONS.length;
          const action = AUTONOMOUS_ACTIONS[autoActionIndex];
          if (action === "action-wash-face") {
            setCatVisualState("wash-face");
            setTimeout(() => setCatVisualState("two-legs"), 3500);
          } else if (action === "posture-4legs") {
            setCatVisualState("four-legs");
          } else if (action === "action-laugh") {
            setCatVisualState("laughing");
            setTimeout(() => setCatVisualState("two-legs"), 2400);
          } else {
            setCatVisualState("two-legs");
          }
        }
      }, 5500);
    }

    function catInteractedManually() {
      // 360 Spin and Face-wash when tapped (optional bonus, not required)
      if (robotCat) {
        robotCat.style.transition = "transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1)";
        robotCat.style.transform = "rotateY(360deg) scale(1.15)";
        setTimeout(() => {
          robotCat.style.transition = "transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)";
          robotCat.style.transform = "rotateY(0deg) scale(1)";
        }, 600);
      }
      setCatVisualState("wash-face");
      setTimeout(() => setCatVisualState("two-legs"), 3000);
    }

    /* Parallax Cursor & Touch Tracking */
    document.addEventListener("mousemove", (e) => {
      if (!robotCat) return;
      const rect = robotCat.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const dx = (e.clientX - centerX) / window.innerWidth;
      const dy = (e.clientY - centerY) / window.innerHeight;
      
      const pupilL = document.getElementById("pupilLeft");
      const pupilR = document.getElementById("pupilRight");
      if (pupilL && pupilR) {
        pupilL.setAttribute("cx", String(47 + dx * 4));
        pupilL.setAttribute("cy", String(38 + dy * 3));
        pupilR.setAttribute("cx", String(73 + dx * 4));
        pupilR.setAttribute("cy", String(38 + dy * 3));
      }
    });

    /* ==========================================================================
       CONVERSATIONAL FLOW STATE MACHINE (AUDIENCE: EXECUTIVE / CREDIT OFFICER)
       ========================================================================== */
    const chatContainer = document.getElementById("chatContainer");
    const chipsArea = document.getElementById("chipsArea");
    const userInput = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");
    const inputHint = document.getElementById("inputHint");

    let conversationToken = 0;
    let session = {
      caseName: "", product: "", incomeProgram: "", propertyType: "",
      bureau: "", baseRoi: 0, basePf: 0, ticketSize: "",
      sancAmount: 0, sancTenure: 0, sancRoi: 0, sancPf: 0, sancEmi: 0,
      incomeFreq: "Monthly", monthlyIncome: 0, existingEmis: 0, currentDti: 0,
      reqRoi: 0, reqPf: 0, step: "CASE_NAME"
    };

    const STEPS = {
      CASE_NAME: "CASE_NAME",
      PRODUCT: "PRODUCT",
      INCOME_PROGRAM: "INCOME_PROGRAM",
      PROPERTY_TYPE: "PROPERTY_TYPE",
      BUREAU: "BUREAU",
      SANC_AMOUNT: "SANC_AMOUNT",
      SANC_TENURE: "SANC_TENURE",
      SANC_ROI: "SANC_ROI",
      SANC_PF: "SANC_PF",
      INCOME_FREQ: "INCOME_FREQ",
      INCOME_AMOUNT: "INCOME_AMOUNT",
      EXISTING_EMIS: "EXISTING_EMIS",
      REQ_ROI: "REQ_ROI",
      REQ_PF: "REQ_PF",
      COMPLETED: "COMPLETED"
    };

    function scrollChatToBottom() {
      requestAnimationFrame(() => { chatContainer.scrollTop = chatContainer.scrollHeight; });
    }

    function appendUserMessage(text) {
      const row = document.createElement("div");
      row.className = "message-row user";
      row.innerHTML = `<div class="message-bubble">${escapeHtml(text)}</div>`;
      chatContainer.appendChild(row);
      scrollChatToBottom();
    }

    function appendBotMessage(htmlContent, chips = [], catMood = "two-legs", delayMs = 380) {
      const currentToken = conversationToken;
      setCatVisualState("thinking");

      const typingRow = document.createElement("div");
      typingRow.className = "message-row bot typing-row";
      typingRow.innerHTML = `
        <div class="avatar-badge">🐱</div>
        <div class="message-bubble">
          <div class="typing-dots">
            <span class="pulse-dot"></span><span class="pulse-dot"></span><span class="pulse-dot"></span>
          </div>
        </div>`;
      chatContainer.appendChild(typingRow);
      scrollChatToBottom();

      userInput.disabled = true;
      sendBtn.disabled = true;
      chipsArea.innerHTML = "";

      setTimeout(() => {
        if (currentToken !== conversationToken) return;
        typingRow.remove();
        setCatVisualState("talking");

        const msgRow = document.createElement("div");
        msgRow.className = "message-row bot";
        msgRow.innerHTML = `
          <div class="avatar-badge">🐱</div>
          <div class="message-bubble">${htmlContent}</div>`;
        chatContainer.appendChild(msgRow);

        renderChips(chips);
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
        scrollChatToBottom();

        setTimeout(() => {
          if (currentToken === conversationToken) setCatVisualState(catMood);
        }, 550);
      }, delayMs);
    }

    function renderChips(chips) {
      chipsArea.innerHTML = "";
      if (!chips || chips.length === 0) {
        chipsArea.style.display = "none";
        return;
      }
      chipsArea.style.display = "flex";
      chips.forEach(chip => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = `action-chip ${chip.primary ? 'primary-glow' : ''}`;
        btn.innerHTML = `${chip.icon ? chip.icon + ' ' : ''}<span>${escapeHtml(chip.label)}</span>`;
        btn.onclick = () => onChipSelected(chip.value !== undefined ? chip.value : chip.label);
        chipsArea.appendChild(btn);
      });
    }

    function onChipSelected(val) { handleStepInput(val); }
    function submitInput() {
      const text = userInput.value.trim();
      if (!text) return;
      handleStepInput(text);
      userInput.value = "";
    }

    function startConversation() {
      session = {
        caseName: "", product: "", incomeProgram: "", propertyType: "",
        bureau: "", baseRoi: 0, basePf: 0, ticketSize: "",
        sancAmount: 0, sancTenure: 0, sancRoi: 0, sancPf: 0, sancEmi: 0,
        incomeFreq: "Monthly", monthlyIncome: 0, existingEmis: 0, currentDti: 0,
        reqRoi: 0, reqPf: 0, step: STEPS.CASE_NAME
      };
      chatContainer.innerHTML = "";
      inputHint.textContent = "Enter proposal / customer name";
      userInput.placeholder = "e.g. Ramesh Patel, Proposal #402...";

      appendBotMessage(t("welcome"), [], "two-legs", 200);
    }

    function restartSession() {
      conversationToken++;
      setCatVisualState("two-legs");
      companionSpeech("Session restarted! 🚀", 1800);
      startConversation();
    }

    /* ==========================================================================
       CONVERSATIONAL STEP HANDLER
       ========================================================================== */
    function handleStepInput(rawInput) {
      const clean = String(rawInput).trim();
      if (!clean) return;
      appendUserMessage(clean);

      switch (session.step) {
        case STEPS.CASE_NAME:
          session.caseName = clean;
          session.step = STEPS.PRODUCT;
          inputHint.textContent = "Select loan product";
          userInput.placeholder = "Choose or type product name...";
          appendBotMessage(
            `${t("askProduct")} <strong>${escapeHtml(session.caseName)}</strong>:`,
            [
              { label: "Regular Secured Business Loan", value: "R", primary: true },
              { label: "Secured Working Capital Term Loan", value: "W" },
              { label: "Hypothecation Loans", value: "H" }
            ], "talking"
          );
          break;

        case STEPS.PRODUCT:
          let prodCode = null;
          const cleanUpper = clean.toUpperCase();
          if (cleanUpper === "R" || cleanUpper.includes("REGULAR") || cleanUpper.includes("BUSINESS")) prodCode = "R";
          else if (cleanUpper === "W" || cleanUpper.includes("WORKING") || cleanUpper.includes("CAPITAL")) prodCode = "W";
          else if (cleanUpper === "H" || cleanUpper.includes("HYPOTHECATION")) prodCode = "H";

          if (!prodCode) {
            appendBotMessage(`Please pick one of our products below:`, [
              { label: "Regular Secured Business Loan", value: "R" },
              { label: "Secured Working Capital Term Loan", value: "W" },
              { label: "Hypothecation Loans", value: "H" }
            ], "worried");
            return;
          }
          session.product = prodCode;
          session.step = STEPS.INCOME_PROGRAM;
          inputHint.textContent = "Select income program";
          userInput.placeholder = "Choose or type income program...";
          appendBotMessage(
            `${t("askIncomeProg")}`,
            [
              { label: "Documented", value: "D", primary: true },
              { label: "Assessed", value: "A" },
              { label: "Hybrid", value: "Hy" },
              { label: "Semi Documented", value: "S" }
            ], "talking"
          );
          break;

        case STEPS.INCOME_PROGRAM:
          let incProg = null;
          const incUpper = clean.toUpperCase();
          if (incUpper === "D" || incUpper.includes("DOCUM") && !incUpper.includes("SEMI")) incProg = "D";
          else if (incUpper === "A" || incUpper.includes("ASSESS")) incProg = "A";
          else if (incUpper === "HY" || incUpper.includes("HYBRID")) incProg = "Hy";
          else if (incUpper === "S" || incUpper.includes("SEMI")) incProg = "S";

          if (!incProg) {
            appendBotMessage(`Please choose a valid Income Program:`, [
              { label: "Documented", value: "D" },
              { label: "Assessed", value: "A" },
              { label: "Hybrid", value: "Hy" },
              { label: "Semi Documented", value: "S" }
            ], "worried");
            return;
          }
          session.incomeProgram = incProg;

          if (session.product === "H") {
            session.propertyType = "NA";
            session.step = STEPS.BUREAU;
            inputHint.textContent = "Select bureau category";
            userInput.placeholder = "Choose bureau category...";
            appendBotMessage(
              `Property type is <em>Not Applicable (NA)</em> for Hypothecation. 🚗<br><br>${t("askBureau")}`,
              [
                { label: ">=700 or NTC", value: "G", primary: true },
                { label: "<700", value: "L" }
              ], "talking"
            );
          } else {
            session.step = STEPS.PROPERTY_TYPE;
            inputHint.textContent = "Select property type";
            userInput.placeholder = "SORP or Other...";
            appendBotMessage(
              `${t("askProperty")}`,
              [
                { label: "SORP (Self Occupied Residential)", value: "SORP", primary: true },
                { label: "Other", value: "Other" }
              ], "talking"
            );
          }
          break;

        case STEPS.PROPERTY_TYPE:
          let propType = null;
          const propUpper = clean.toUpperCase();
          if (propUpper.includes("SORP") || propUpper.includes("RESIDENTIAL") || propUpper.includes("SELF")) propType = "SORP";
          else if (propUpper.includes("OTHER") || propUpper.includes("COMMERCIAL")) propType = "Other";

          if (!propType) {
            appendBotMessage(`Please select either SORP or Other:`, [
              { label: "SORP", value: "SORP" }, { label: "Other", value: "Other" }
            ], "worried");
            return;
          }
          session.propertyType = propType;
          session.step = STEPS.BUREAU;
          inputHint.textContent = "Select bureau category";
          userInput.placeholder = "Choose bureau score category...";
          appendBotMessage(
            `${t("askBureau")}`,
            [
              { label: ">=700 or NTC", value: "G", primary: true },
              { label: "<700", value: "L" }
            ], "talking"
          );
          break;

        case STEPS.BUREAU:
          let burCode = null;
          const burUpper = clean.toUpperCase();
          if (burUpper.includes(">=700") || burUpper.includes("NTC") || burUpper === "G" || burUpper.includes("700+")) burCode = "G";
          else if (burUpper.includes("<700") || burUpper === "L" || burUpper.includes("BELOW")) burCode = "L";

          if (!burCode) {
            appendBotMessage(`Please select a Bureau category:`, [
              { label: ">=700 or NTC", value: "G" }, { label: "<700", value: "L" }
            ], "worried");
            return;
          }
          session.bureau = burCode;
          session.step = STEPS.SANC_AMOUNT;
          inputHint.textContent = "Enter sanctioned loan amount (e.g. 10 Lakhs, 15,00,000)";
          userInput.placeholder = "e.g. 5 lakh, 10,00,000, 1.2 cr...";
          appendBotMessage(
            `Borrower profile captured! 📁<br><br>${t("askSancAmount")}`,
            [
              { label: "₹4,50,000 (≤ 5L)", value: "450000" },
              { label: "₹10,00,000 (> 5L)", value: "1000000", primary: true },
              { label: "₹25,00,000", value: "2500000" }
            ], "talking"
          );
          break;

        case STEPS.SANC_AMOUNT:
          const parsedSancAmt = parseNumber(clean);
          if (!parsedSancAmt || parsedSancAmt <= 0) {
            appendBotMessage(`Please enter a valid loan amount (e.g. <em>"10,00,000"</em> or <em>"15 lakh"</em>):`, [], "worried");
            return;
          }
          session.sancAmount = parsedSancAmt;

          if (session.product === "R") {
            session.ticketSize = session.sancAmount <= 500000 ? "U" : "A";
          } else {
            session.ticketSize = "L";
          }

          session.step = STEPS.SANC_TENURE;
          inputHint.textContent = "Enter sanctioned tenure (e.g. 60 months, 5 years)";
          userInput.placeholder = "e.g. 36 months, 5 years...";
          appendBotMessage(
            `Sanctioned Amount: <strong>${formatINR(session.sancAmount)}</strong> (${session.ticketSize === "U" ? "Upto 5 Lacs" : (session.ticketSize === "A" ? "Above 5 Lacs" : "All Ticket")}). 💰<br><br>${t("askSancTenure")}`,
            [
              { label: "36 Months (3 Yrs)", value: "36" },
              { label: "60 Months (5 Yrs)", value: "60", primary: true },
              { label: "84 Months (7 Yrs)", value: "84" }
            ], "talking"
          );
          break;

        case STEPS.SANC_TENURE:
          const parsedTen = parseTenureMonths(clean);
          if (!parsedTen || parsedTen < 3 || parsedTen > 360) {
            appendBotMessage(`Please enter a realistic tenure between 3 and 360 months (e.g. <em>"60 months"</em> or <em>"5 years"</em>):`, [], "worried");
            return;
          }
          session.sancTenure = parsedTen;
          session.step = STEPS.SANC_ROI;
          inputHint.textContent = "Enter sanctioned ROI % p.a. (e.g. 18.0%, 19.5)";
          userInput.placeholder = "e.g. 18.0%, 19.5%...";
          appendBotMessage(
            `Sanctioned Tenure: <strong>${session.sancTenure} months</strong>. ⏳<br><br>${t("askSancRoi")}`,
            [
              { label: "18.0%", value: "18.0", primary: true },
              { label: "19.5%", value: "19.5" },
              { label: "21.0%", value: "21.0" }
            ], "talking"
          );
          break;

        case STEPS.SANC_ROI:
          const numSancRoi = parseFloat(clean.replace(/%/g, ""));
          if (isNaN(numSancRoi) || numSancRoi <= 0 || numSancRoi > 60) {
            appendBotMessage(`Please enter a valid sanctioned ROI percentage (0 - 60%):`, [], "worried");
            return;
          }
          session.sancRoi = numSancRoi;
          session.step = STEPS.SANC_PF;
          inputHint.textContent = "Enter sanctioned processing fee % (e.g. 2.0%, 3.0)";
          userInput.placeholder = "e.g. 2.0%, 3.0%...";
          appendBotMessage(
            `Sanctioned ROI: <strong>${session.sancRoi.toFixed(2)}% p.a.</strong><br><br>${t("askSancPf")}`,
            [
              { label: "2.0%", value: "2.0" },
              { label: "3.0%", value: "3.0", primary: true }
            ], "talking"
          );
          break;

        case STEPS.SANC_PF:
          const numSancPf = parseFloat(clean.replace(/%/g, ""));
          if (isNaN(numSancPf) || numSancPf < 0 || numSancPf > 15) {
            appendBotMessage(`Please enter a valid sanctioned Processing Fee (0 - 15%):`, [], "worried");
            return;
          }
          session.sancPf = numSancPf;
          session.step = STEPS.INCOME_FREQ;
          inputHint.textContent = "Select Monthly or Annual income";
          userInput.placeholder = "Choose Monthly or Annual...";
          appendBotMessage(
            `Sanctioned PF: <strong>${session.sancPf.toFixed(2)}%</strong>.<br><br>${t("askIncomeFreq")}`,
            [
              { label: "Monthly Income", value: "Monthly", primary: true },
              { label: "Annual Income", value: "Annual" }
            ], "talking"
          );
          break;

        case STEPS.INCOME_FREQ:
          const freq = clean.toLowerCase().includes("ann") ? "Annual" : "Monthly";
          session.incomeFreq = freq;
          session.step = STEPS.INCOME_AMOUNT;
          inputHint.textContent = `Enter ${freq.toLowerCase()} income amount`;
          userInput.placeholder = freq === "Annual" ? "e.g. 12 lakh, 12,00,000..." : "e.g. 80,000, 1 lakh...";
          appendBotMessage(
            `${t("askIncomeAmount")} <strong>${freq} Income</strong>:`,
            freq === "Annual" ? [
              { label: "₹6 Lakhs", value: "600000" },
              { label: "₹12 Lakhs", value: "1200000", primary: true },
              { label: "₹24 Lakhs", value: "2400000" }
            ] : [
              { label: "₹50,000", value: "50000" },
              { label: "₹80,000", value: "80000", primary: true },
              { label: "₹1,50,000", value: "150000" }
            ], "talking"
          );
          break;

        case STEPS.INCOME_AMOUNT:
          const parsedInc = parseNumber(clean);
          if (!parsedInc || parsedInc <= 0) {
            appendBotMessage(`Please enter a valid positive income (e.g. <em>"80,000"</em> or <em>"12 lakh"</em>):`, [], "worried");
            return;
          }
          session.monthlyIncome = session.incomeFreq === "Annual" ? parsedInc / 12.0 : parsedInc;
          session.step = STEPS.EXISTING_EMIS;
          inputHint.textContent = "Enter total existing monthly obligations (0 if none)";
          userInput.placeholder = "e.g. 20,000 or 0...";
          appendBotMessage(
            `Monthly Income: <strong>${formatINR(session.monthlyIncome)}/month</strong>. 💼<br><br>${t("askExistingEmis")}`,
            [
              { label: "0 (None)", value: "0", primary: true },
              { label: "₹10,000", value: "10000" },
              { label: "₹20,000", value: "20000" },
              { label: "₹35,000", value: "35000" }
            ], "talking"
          );
          break;

        case STEPS.EXISTING_EMIS:
          const parsedEmis = parseNumber(clean);
          if (parsedEmis === null || parsedEmis < 0) {
            appendBotMessage(`Please enter 0 or positive existing obligations:`, [{ label: "0", value: "0" }], "worried");
            return;
          }
          session.existingEmis = parsedEmis;

          // Compute Current Sanctioned Status
          session.sancEmi = calculateReducingEMI(session.sancAmount, session.sancRoi, session.sancTenure);
          const currentDtiObj = calculateDTI(session.existingEmis, session.sancEmi, session.monthlyIncome);
          session.currentDti = currentDtiObj.updatedDti;

          // Lookup Policy Matrix Benchmark
          const baseRates = lookupBaseRates(session.product, session.ticketSize, session.incomeProgram, session.propertyType, session.bureau);
          if (baseRates) {
            session.baseRoi = baseRates.baseRoi;
            session.basePf = baseRates.basePf;
          } else {
            session.baseRoi = session.sancRoi;
            session.basePf = session.sancPf;
          }

          session.step = STEPS.REQ_ROI;
          inputHint.textContent = "Enter requested ROI % p.a. (e.g. 16.5%)";
          userInput.placeholder = `Policy base is ${session.baseRoi}%, enter requested ROI...`;

          // Midway Sanctioned Status Milestone Card
          const sancCardHtml = `
            <div class="status-card">
              <div class="status-card-header blue">
                <span>${t("sancStatusTitle")}</span>
              </div>
              <div class="summary-grid">
                <div class="stat-cell">
                  <div class="stat-title">${t("sancEmiLabel")}</div>
                  <div class="stat-num" style="color:var(--accent-primary);">${formatINR(session.sancEmi)}</div>
                  <div class="stat-sub">${session.sancTenure}m @ ${session.sancRoi}%</div>
                </div>
                <div class="stat-cell">
                  <div class="stat-title">${t("currentDtiLabel")}</div>
                  <div class="stat-num" style="color:${session.currentDti > 50 ? 'var(--color-amber)' : 'var(--color-green)'};">${session.currentDti}%</div>
                  <div class="stat-sub">Income: ${formatINR(session.monthlyIncome)}/m</div>
                </div>
                <div class="stat-cell">
                  <div class="stat-title">${t("baseRoiLabel")}</div>
                  <div class="stat-num" style="color:var(--accent-secondary);">${session.baseRoi.toFixed(2)}%</div>
                  <div class="stat-sub">56-Row Matrix Policy</div>
                </div>
                <div class="stat-cell">
                  <div class="stat-title">${t("basePfLabel")}</div>
                  <div class="stat-num" style="color:var(--accent-hot);">${session.basePf.toFixed(2)}%</div>
                  <div class="stat-sub">Benchmark Fee</div>
                </div>
              </div>
            </div>`;

          appendBotMessage(
            `${sancCardHtml}<br>${t("floorWarningRoi")}<br><br>${t("askReqRoi")}`,
            [
              { label: `${session.baseRoi}% (Policy Base)`, value: String(session.baseRoi), primary: true },
              { label: `${(session.baseRoi - 1.5).toFixed(1)}% (CBO band)`, value: String(session.baseRoi - 1.5) },
              { label: `${(session.baseRoi - 3.0).toFixed(1)}% (COO band)`, value: String(session.baseRoi - 3.0) },
              { label: `14.5% (<15% CEO Floor)`, value: "14.5" }
            ], "two-legs"
          );
          break;

        case STEPS.REQ_ROI:
          const numReqRoi = parseFloat(clean.replace(/%/g, ""));
          if (isNaN(numReqRoi) || numReqRoi <= 0 || numReqRoi > 60) {
            appendBotMessage(`Please enter a valid requested ROI (0 - 60%):`, [{ label: `${session.baseRoi}%`, value: String(session.baseRoi) }], "worried");
            return;
          }
          session.reqRoi = numReqRoi;
          session.step = STEPS.REQ_PF;
          inputHint.textContent = "Enter requested PF % (e.g. 1.8%, 1.2)";
          userInput.placeholder = `Policy base is ${session.basePf}%, enter requested PF...`;
          appendBotMessage(
            `Requested ROI: <strong>${session.reqRoi.toFixed(2)}% p.a.</strong><br>${t("floorWarningPf")}<br><br>${t("askReqPf")}`,
            [
              { label: `${session.basePf}% (Full PF)`, value: String(session.basePf), primary: true },
              { label: `1.8% (CBO band)`, value: "1.8" },
              { label: `1.5% (COO band)`, value: "1.5" },
              { label: `1.2% (<1.5% CEO Floor)`, value: "1.2" }
            ], "talking"
          );
          break;

        case STEPS.REQ_PF:
          const numReqPf = parseFloat(clean.replace(/%/g, ""));
          if (isNaN(numReqPf) || numReqPf < 0 || numReqPf > 15) {
            appendBotMessage(`Please enter a valid Processing Fee (0 - 15%):`, [{ label: `${session.basePf}%`, value: String(session.basePf) }], "worried");
            return;
          }
          session.reqPf = numReqPf;
          session.step = STEPS.COMPLETED;
          inputHint.textContent = "Review results or evaluate another rate";
          userInput.placeholder = "Click 'Try different ROI/PF' or 'New case'";
          renderFinalExecutiveReport();
          break;

        case STEPS.COMPLETED:
          if (clean.toLowerCase().includes("try") || clean.toLowerCase().includes("different")) {
            reAskProposedRates();
          } else if (clean.toLowerCase().includes("new")) {
            restartSession();
          } else {
            appendBotMessage(`Would you like to test another requested rate or evaluate a new proposal?`,
              [{ label: t("btnTryRates"), icon: "✏️", primary: true }, { label: t("btnNewCase"), icon: "👤" }], "two-legs"
            );
          }
          break;
      }
    }

    /* ==========================================================================
       FINAL COMPARATIVE EXECUTIVE EVALUATION REPORT
       ========================================================================== */
    function renderFinalExecutiveReport() {
      const approval = evaluateApproval(session.baseRoi, session.reqRoi, session.basePf, session.reqPf);
      const reqEmi = calculateReducingEMI(session.sancAmount, session.reqRoi, session.sancTenure);
      const emiSavings = session.sancEmi - reqEmi;
      const baseEmi = calculateReducingEMI(session.sancAmount, session.baseRoi, session.sancTenure);

      const sancPfAmount = (session.sancAmount * session.sancPf) / 100.0;
      const reqPfAmount = (session.sancAmount * session.reqPf) / 100.0;
      const pfSavings = sancPfAmount - reqPfAmount;

      const dtiResult = calculateDTI(session.existingEmis, reqEmi, session.monthlyIncome);

      let mood = "two-legs";
      if (approval.finalApprover.level === 0) mood = "celebrating";
      else if (approval.isFloorBreached || approval.finalApprover.level === 3) mood = "worried";
      else if (approval.finalApprover.level === 1) mood = "laughing";

      let roiTag = "";
      if (session.reqRoi < CONFIG.ROI_FLOOR_PERCENT) {
        roiTag = `<span class="tag-badge ceo">Floor Breach (<15%) ➔ CEO</span>`;
      } else if (approval.roiDeviation <= 0) {
        roiTag = `<span class="tag-badge favorable">No Deviation</span>`;
      } else {
        roiTag = `<span class="tag-badge ${approval.roiApprover.tag}">-${approval.roiDeviation.toFixed(2)}% pts ➔ ${approval.roiApprover.name.replace(' Approval','')}</span>`;
      }

      let pfTag = "";
      if (session.reqPf < CONFIG.PF_FLOOR_PERCENT) {
        pfTag = `<span class="tag-badge ceo">Floor Breach (<1.5%) ➔ CEO</span>`;
      } else if (approval.pfDeviation <= 0) {
        pfTag = `<span class="tag-badge favorable">No Deviation</span>`;
      } else {
        pfTag = `<span class="tag-badge ${approval.pfApprover.tag}">-${approval.pfDeviation.toFixed(2)}% pts ➔ ${approval.pfApprover.name.replace(' Approval','')}</span>`;
      }

      let bannerTitle = "";
      if (approval.isFloorBreached) {
        bannerTitle = `🏛️ CEO Approval Required (Mandatory Floor Violation)`;
      } else if (approval.finalApprover.level === 0) {
        bannerTitle = `✅ No Approval Needed (Standard Benchmark Terms)`;
      } else {
        bannerTitle = `📑 ${approval.finalApprover.name} Required`;
      }

      const floorAlertHtml = approval.isFloorBreached ? `
        <div class="floor-badge">
          ${t("floorAlert")}: Proposed ${session.reqRoi < CONFIG.ROI_FLOOR_PERCENT ? `ROI (${session.reqRoi}% < 15%)` : ''} ${session.reqPf < CONFIG.PF_FLOOR_PERCENT ? `PF (${session.reqPf}% < 1.5%)` : ''}
        </div>` : "";

      const dtiAlertHtml = dtiResult.warning ? `
        <div class="alert-banner amber">
          <span>${t("dtiAlertTitle")}: Updated DTI of <strong>${dtiResult.updatedDti}%</strong> exceeds 50% prudent ceiling.</span>
        </div>` : "";

      const reportHtml = `
        <div class="status-card">
          <div class="status-card-header ${approval.color}">
            <span>${bannerTitle}</span>
          </div>
          <div class="status-card-body">
            ${floorAlertHtml}
            ${approval.explanation}
          </div>
          <div class="comparison-table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>${t("tableHeader")[0]}</th>
                  <th>${t("tableHeader")[1]}</th>
                  <th>${t("tableHeader")[2]}</th>
                  <th>${t("tableHeader")[3]}</th>
                  <th>${t("tableHeader")[4]}</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>ROI (% p.a.)</strong></td>
                  <td>${session.baseRoi.toFixed(2)}%</td>
                  <td>${session.sancRoi.toFixed(2)}%</td>
                  <td><strong>${session.reqRoi.toFixed(2)}%</strong></td>
                  <td>${roiTag}</td>
                </tr>
                <tr>
                  <td><strong>Processing Fee</strong></td>
                  <td>${session.basePf.toFixed(2)}%</td>
                  <td>${session.sancPf.toFixed(2)}% (${formatINR(sancPfAmount)})</td>
                  <td><strong>${session.reqPf.toFixed(2)}% (${formatINR(reqPfAmount)})</strong></td>
                  <td>${pfTag}</td>
                </tr>
                <tr>
                  <td><strong>Monthly EMI</strong></td>
                  <td>${formatINR(baseEmi)}</td>
                  <td>${formatINR(session.sancEmi)}</td>
                  <td><strong>${formatINR(reqEmi)}</strong></td>
                  <td><span class="tag-badge ${emiSavings >= 0 ? 'favorable' : 'cbo'}">${emiSavings >= 0 ? 'Saves ' + formatINR(emiSavings) + '/m' : '+ ' + formatINR(Math.abs(emiSavings))}</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="summary-grid">
            <div class="stat-cell">
              <div class="stat-title">Proposed EMI</div>
              <div class="stat-num" style="color:var(--accent-primary);">${formatINR(reqEmi)}</div>
              <div class="stat-sub">${session.sancTenure}m reducing</div>
            </div>
            <div class="stat-cell">
              <div class="stat-title">Monthly EMI Difference</div>
              <div class="stat-num" style="color:var(--color-green);">${formatINR(Math.max(0, emiSavings))}</div>
              <div class="stat-sub">${emiSavings > 0 ? 'Monthly borrower savings' : 'Same as sanctioned'}</div>
            </div>
            <div class="stat-cell">
              <div class="stat-title">PF Upfront Difference</div>
              <div class="stat-num" style="color:var(--accent-secondary);">${formatINR(Math.max(0, pfSavings))}</div>
              <div class="stat-sub">Fee discount</div>
            </div>
            <div class="stat-cell">
              <div class="stat-title">Updated DTI Ratio</div>
              <div class="stat-num" style="color:${dtiResult.warning ? 'var(--color-amber)' : 'var(--color-green)'};">${dtiResult.updatedDti}%</div>
              <div class="stat-sub">Was ${session.currentDti}%</div>
            </div>
          </div>
          ${dtiAlertHtml}
        </div>`;

      appendBotMessage(
        `${t("evalTitle")} — <strong>${escapeHtml(session.caseName)}</strong>:<br>${reportHtml}`,
        [
          { label: t("btnTryRates"), icon: "✏️", primary: true, value: "re_evaluate_rates" },
          { label: t("btnNewCase"), icon: "👤", value: "new_case" }
        ],
        mood, 450
      );
    }

    function reAskProposedRates() {
      session.step = STEPS.REQ_ROI;
      inputHint.textContent = `Enter requested ROI % p.a. (Base: ${session.baseRoi}%, Sanc: ${session.sancRoi}%)`;
      userInput.placeholder = `Benchmark is ${session.baseRoi}%, enter requested ROI...`;
      appendBotMessage(
        `Evaluating new proposed rates for <strong>${escapeHtml(session.caseName)}</strong>.<br>` +
        `Sanctioned Loan: ${formatINR(session.sancAmount)} (${session.sancTenure}m @ ${session.sancRoi}%), Base: ${session.baseRoi}% / ${session.basePf}%.<br><br>` +
        `${t("askReqRoi")}`,
        [
          { label: `${session.baseRoi}% (Base Rate)`, value: String(session.baseRoi), primary: true },
          { label: `${(session.baseRoi - 1.5).toFixed(1)}% (CBO)`, value: String(session.baseRoi - 1.5) },
          { label: `${(session.baseRoi - 3.0).toFixed(1)}% (COO)`, value: String(session.baseRoi - 3.0) },
          { label: `14.5% (<15% CEO Floor)`, value: "14.5" }
        ], "talking"
      );
    }

    const origOnChipSelected = onChipSelected;
    onChipSelected = function(val) {
      if (val === "re_evaluate_rates") {
        appendUserMessage(t("btnTryRates"));
        reAskProposedRates();
      } else if (val === "new_case" || val === "restart") {
        appendUserMessage(t("btnNewCase"));
        restartSession();
      } else {
        origOnChipSelected(val);
      }
    };

    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", () => { scrollChatToBottom(); });
    }

    // Force purge stale caches and keep service worker fresh
    const LENDY_RELEASE_BUILD = "v20261103_5";
    if (typeof window !== "undefined" && window.caches) {
      try {
        const cachedVer = localStorage.getItem("lendy_active_build");
        if (cachedVer !== LENDY_RELEASE_BUILD) {
          localStorage.setItem("lendy_active_build", LENDY_RELEASE_BUILD);
          caches.keys().then((keys) => {
            keys.forEach((key) => {
              if (key !== "lendy-pwa-v4-network-first") caches.delete(key);
            });
          });
        }
      } catch (e) {}
    }

    if ("serviceWorker" in navigator) {
      window.addEventListener("load", () => {
        navigator.serviceWorker.getRegistrations().then((registrations) => {
          for (const reg of registrations) {
            reg.update();
          }
        });
        navigator.serviceWorker.register("./sw.js?v=" + LENDY_RELEASE_BUILD).then((reg) => {
          reg.addEventListener("updatefound", () => {
            const worker = reg.installing;
            if (worker) {
              worker.addEventListener("statechange", () => {
                if (worker.state === "installed" && navigator.serviceWorker.controller) {
                  window.location.reload();
                }
              });
            }
          });
        }).catch(() => {});
      });
    }

    window.addEventListener("DOMContentLoaded", () => {
      // Restore wallpaper preference
      const savedTheme = localStorage.getItem("lendy_theme");
      if (savedTheme) {
        document.documentElement.setAttribute("data-theme", savedTheme);
        const match = WALLPAPER_THEMES.find(t => t.id === savedTheme);
        if (match) document.getElementById("themeEmoji").textContent = match.emoji;
      }
      startConversation();
      startAutonomousCatLifeCycle();
    });
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print("Generated index.html successfully with length:", len(HTML_CONTENT))
