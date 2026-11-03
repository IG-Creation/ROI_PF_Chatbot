import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update version to v20261103_8
text = text.replace('const LENDY_RELEASE_BUILD = "v20261103_7";', 'const LENDY_RELEASE_BUILD = "v20261103_8";')

# 2. Update CSS for cat transitions
old_head_css = """.washing-face .cat-head-group {
      animation: head-tilt-wash 1.8s infinite ease-in-out;
      transform-origin: 60px 48px;
    }"""

new_head_css = """.cat-head-group {
      transform-origin: 60px 45px;
      transition: transform 0.38s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .arm-left-paw {
      transform-origin: 34px 76px;
      transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .arm-right-paw {
      transform-origin: 86px 76px;
      transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .washing-face .cat-head-group {
      animation: head-tilt-wash 1.8s infinite ease-in-out;
      transform-origin: 60px 48px;
    }"""

assert old_head_css in text, "old_head_css not found"
text = text.replace(old_head_css, new_head_css)

# 3. Replace companionSpeech and setCatVisualState and related functions
cat_funcs_old_start = text.find('function companionSpeech(')
cat_funcs_old_end = text.find('function scrollChatToBottom()')
assert cat_funcs_old_start != -1 and cat_funcs_old_end != -1, "Cat functions region not found"

cat_funcs_new = """let speechTimer = null;
    function companionSpeech(text, durationMs = 2800) {
      if (!companionBubble) return;
      if (speechTimer) clearTimeout(speechTimer);
      companionBubble.textContent = text;
      companionBubble.classList.add("active");
      speechTimer = setTimeout(() => {
        companionBubble.classList.remove("active");
      }, durationMs);
    }

    function setCatVisualState(stateName) {
      if (!robotCat) return;
      currentCatState = stateName;

      robotCat.classList.remove("washing-face", "laughing-now", "calculating-now", "worried-alert", "posture-4legs", "posture-2legs");
      if (cyberVisor) cyberVisor.style.display = "none";
      if (eyesNormalLayer) eyesNormalLayer.style.display = "block";
      if (eyesStarLayer) eyesStarLayer.style.display = "none";
      if (headGroup) headGroup.style.transform = "translate(0px, 0px) rotate(0deg)";
      if (pupilLeft) { pupilLeft.setAttribute("cx", "47"); pupilLeft.setAttribute("cy", "38"); }
      if (pupilRight) { pupilRight.setAttribute("cx", "73"); pupilRight.setAttribute("cy", "38"); }
      if (leftPawGroup) leftPawGroup.style.transform = "translate(0px, 0px) rotate(0deg)";
      if (rightPawGroup) rightPawGroup.style.transform = "translate(0px, 0px) rotate(0deg)";

      switch (stateName) {
        case "curious":
          robotCat.classList.add("posture-2legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "10"); eyeRight.setAttribute("ry", "8"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M55,51 Q60,54 65,51"); mouthLine.setAttribute("fill", "none"); }
          if (headGroup) headGroup.style.transform = "translate(-3px, 0px) rotate(7deg)";
          break;

        case "calculating":
          robotCat.classList.add("calculating-now", "posture-2legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "7"); eyeRight.setAttribute("ry", "7"); }
          if (pupilLeft && pupilRight) { pupilLeft.setAttribute("cy", "34"); pupilRight.setAttribute("cy", "34"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M54,53 L66,53"); mouthLine.setAttribute("fill", "none"); }
          break;

        case "wash-face":
          robotCat.classList.add("washing-face", "posture-2legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "3"); eyeRight.setAttribute("ry", "3"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M54,52 Q60,57 66,52"); mouthLine.setAttribute("fill", "none"); }
          break;

        case "four-legs":
          robotCat.classList.add("posture-4legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "9"); eyeRight.setAttribute("ry", "9"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M53,52 Q60,57 67,52"); mouthLine.setAttribute("fill", "none"); }
          break;

        case "laughing":
        case "joyful":
          robotCat.classList.add("laughing-now", "posture-2legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "3.5"); eyeRight.setAttribute("ry", "3.5"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M52,50 Q60,63 68,50 Z"); mouthLine.setAttribute("fill", "#0284c7"); }
          if (leftPawGroup) leftPawGroup.style.transform = "translateY(-6px) rotate(12deg)";
          if (rightPawGroup) rightPawGroup.style.transform = "translateY(-6px) rotate(-12deg)";
          break;

        case "worried-alert":
        case "worried":
          robotCat.classList.add("worried-alert", "posture-2legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "11"); eyeRight.setAttribute("ry", "11"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M53,55 Q60,49 67,55"); mouthLine.setAttribute("fill", "none"); }
          break;

        case "celebrating":
        case "excited":
          robotCat.classList.add("laughing-now", "posture-2legs");
          if (eyesNormalLayer) eyesNormalLayer.style.display = "none";
          if (eyesStarLayer) eyesStarLayer.style.display = "block";
          if (mouthLine) { mouthLine.setAttribute("d", "M51,50 Q60,65 69,50 Z"); mouthLine.setAttribute("fill", "#00f0ff"); }
          if (leftPawGroup) leftPawGroup.style.transform = "translateY(-14px) rotate(24deg)";
          if (rightPawGroup) rightPawGroup.style.transform = "translateY(-14px) rotate(-24deg)";
          break;

        case "standing-proud":
        default:
          robotCat.classList.add("posture-2legs");
          if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "10"); eyeRight.setAttribute("ry", "10"); }
          if (mouthLine) { mouthLine.setAttribute("d", "M53,52 Q60,58 67,52"); mouthLine.setAttribute("fill", "none"); }
          break;
      }
    }

    /* Live Cat reaction: Turns face towards chat message, shows emotion, then looks straight */
    function turnCatFaceToChat(reactionType, speechText) {
      if (!robotCat) return;
      if (headGroup) headGroup.style.transform = "translate(-8px, 1px) rotate(-16deg)";
      if (pupilLeft) pupilLeft.setAttribute("cx", "42");
      if (pupilRight) pupilRight.setAttribute("cx", "68");

      robotCat.classList.remove("laughing-now", "worried-alert", "calculating-now", "washing-face");

      if (reactionType === "excited" || reactionType === "celebrating") {
        robotCat.classList.add("laughing-now");
        if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "4"); eyeRight.setAttribute("ry", "4"); }
        if (mouthLine) { mouthLine.setAttribute("d", "M52,50 Q60,63 68,50 Z"); mouthLine.setAttribute("fill", "#0284c7"); }
        if (leftPawGroup) leftPawGroup.style.transform = "translateY(-12px) rotate(20deg)";
        if (rightPawGroup) rightPawGroup.style.transform = "translateY(-12px) rotate(-20deg)";
      } else if (reactionType === "worried") {
        robotCat.classList.add("worried-alert");
        if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "12"); eyeRight.setAttribute("ry", "12"); }
        if (mouthLine) { mouthLine.setAttribute("d", "M52,56 Q60,48 68,56"); mouthLine.setAttribute("fill", "none"); }
      } else if (reactionType === "joyful") {
        robotCat.classList.add("laughing-now");
        if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "3.5"); eyeRight.setAttribute("ry", "3.5"); }
        if (mouthLine) { mouthLine.setAttribute("d", "M53,51 Q60,60 67,51 Z"); mouthLine.setAttribute("fill", "#0284c7"); }
        if (rightPawGroup) rightPawGroup.style.transform = "translateY(-10px) rotate(-18deg)";
      } else if (reactionType === "thinking") {
        if (cyberVisor) cyberVisor.style.display = "block";
        if (mouthLine) { mouthLine.setAttribute("d", "M54,53 L66,53"); mouthLine.setAttribute("fill", "none"); }
      } else {
        if (eyeLeft && eyeRight) { eyeLeft.setAttribute("ry", "10"); eyeRight.setAttribute("ry", "8"); }
        if (mouthLine) { mouthLine.setAttribute("d", "M54,51 Q60,55 66,51"); mouthLine.setAttribute("fill", "none"); }
      }

      if (speechText) {
        companionSpeech(speechText, 2400);
      }
    }

    function turnCatFaceStraight() {
      if (!robotCat) return;
      if (headGroup) headGroup.style.transform = "translate(0px, 0px) rotate(0deg)";
      if (pupilLeft) pupilLeft.setAttribute("cx", "47");
      if (pupilRight) pupilRight.setAttribute("cx", "73");
      if (leftPawGroup) leftPawGroup.style.transform = "translate(0px, 0px) rotate(0deg)";
      if (rightPawGroup) rightPawGroup.style.transform = "translate(0px, 0px) rotate(0deg)";
      if (mouthLine && currentCatState !== "laughing") {
        mouthLine.setAttribute("d", "M53,52 Q60,58 67,52");
        mouthLine.setAttribute("fill", "none");
      }
    }

    function reactCatToUserResponse(step, rawValue, displayLabel) {
      let reaction = "curious";
      let remark = "";

      switch (step) {
        case STEPS.CASE_NAME:
          reaction = "excited";
          remark = `Welcome, ${rawValue}! Let's find your loan terms 🐱`;
          break;
        case STEPS.PRODUCT:
          reaction = "excited";
          remark = rawValue === "R" ? "Regular Secured Business Loan! Prime collateral 🏢" : (rawValue === "W" ? "Secured Working Capital! 🏭" : "Hypothecation Loan! 🚗");
          break;
        case STEPS.INCOME_PROGRAM:
          reaction = "joyful";
          remark = rawValue === "D" ? "Documented program gets the sharpest rates 📑" : "Assessment program selected! 🔍";
          break;
        case STEPS.PROPERTY_TYPE:
          reaction = "joyful";
          remark = rawValue === "SORP" ? "Self-occupied residential property is prime collateral 🏠" : "Commercial property registered! 🏬";
          break;
        case STEPS.BUREAU:
          if (rawValue === "G") {
            reaction = "excited";
            remark = "Score 700+ or NTC! Top-tier credit rating ⭐";
          } else {
            reaction = "worried";
            remark = "Score under 700. Checking base matrix rates ⚠️";
          }
          break;
        case STEPS.SANC_AMOUNT:
          reaction = "curious";
          const amt = parseNumber(rawValue);
          remark = amt ? `Loan amount ${formatINR(amt)} recorded! 💰` : "Loan amount noted! 💰";
          break;
        case STEPS.SANC_TENURE:
          reaction = "curious";
          const ten = parseTenureMonths(rawValue);
          remark = ten ? `${ten} months tenure locked in! ⏳` : "Tenure noted! ⏳";
          break;
        case STEPS.SANC_ROI:
        case STEPS.SANC_PF:
          reaction = "thinking";
          remark = "Sanctioned terms noted! 📈";
          break;
        case STEPS.INCOME_FREQ:
          reaction = "curious";
          remark = rawValue === "Annual" ? "Yearly income mode 📊" : "Monthly income mode 📅";
          break;
        case STEPS.INCOME_AMOUNT:
        case STEPS.EXISTING_EMIS:
          reaction = "thinking";
          remark = "Computing obligations & DTI ratio ⚖️";
          break;
        case STEPS.REQ_ROI:
          const numRoi = parseFloat(String(rawValue).replace(/%/g, ''));
          if (!isNaN(numRoi)) {
            if (numRoi < CONFIG.ROI_FLOOR_PERCENT) {
              reaction = "worried";
              remark = `Under 15% (${numRoi}%)! Mandates CEO approval 🏛️`;
            } else if (numRoi < session.baseRoi) {
              const drop = session.baseRoi - numRoi;
              reaction = drop > 2.0 ? "worried" : "thinking";
              remark = `${drop.toFixed(1)}% rate concession requested! ⚡`;
            } else {
              reaction = "excited";
              remark = "Rate meets or beats benchmark base! 🎉";
            }
          }
          break;
        case STEPS.REQ_PF:
          const numPf = parseFloat(String(rawValue).replace(/%/g, ''));
          if (!isNaN(numPf)) {
            if (numPf < CONFIG.PF_FLOOR_PERCENT) {
              reaction = "worried";
              remark = `Fee under 1.5% (${numPf}%)! Mandates CEO approval 🏛️`;
            } else {
              reaction = "thinking";
              remark = "Evaluating approval bands & final comparison... 🎯";
            }
          }
          break;
        case STEPS.COMPLETED:
          reaction = "excited";
          remark = "Let's test another combination! 🚀";
          break;
      }

      turnCatFaceToChat(reaction, remark);

      setTimeout(() => {
        turnCatFaceStraight();
      }, 950);
    }

    function startAutonomousCatLifeCycle() {
      if (autoCycleTimer) clearInterval(autoCycleTimer);
      const IDLE_VARIETY = [
        "standing-proud",
        "curious",
        "standing-proud",
        "four-legs",
        "standing-proud",
        "curious",
        "standing-proud",
        "wash-face"
      ];
      let cycleIdx = 0;
      autoCycleTimer = setInterval(() => {
        const isTyping = document.querySelector(".typing-row");
        if (!isTyping && currentCatState !== "worried-alert" && currentCatState !== "celebrating" && currentCatState !== "worried") {
          cycleIdx = (cycleIdx + 1) % IDLE_VARIETY.length;
          const nextState = IDLE_VARIETY[cycleIdx];
          setCatVisualState(nextState);
          if (nextState === "wash-face") {
            setTimeout(() => setCatVisualState("standing-proud"), 2400);
          }
        }
      }, 8000);
    }

    function catInteractedManually() {
      if (robotCat) {
        robotCat.style.transition = "transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1)";
        robotCat.style.transform = "rotateY(360deg) scale(1.15)";
        setTimeout(() => {
          robotCat.style.transition = "transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)";
          robotCat.style.transform = "rotateY(0deg) scale(1)";
        }, 600);
      }
      setCatVisualState("joyful");
      companionSpeech("Hehehe! That tickles! 🐾 Watching your loan rates closely!", 2600);
    }

    """

text = text[:cat_funcs_old_start] + cat_funcs_new + text[cat_funcs_old_end:]
print("Updated Cat visual functions")

# 4. Update appendBotCard actionTiles to support onActionTileClick
old_action_tiles_map = """let tilesHtml = "";
        if (actionTiles && actionTiles.length > 0) {
          tilesHtml = `<div class="cockpit-options-grid">` + actionTiles.map(tile => `
            <div class="action-tile-3d ${tile.primary ? 'primary-glow' : ''}" onclick="onChipSelected('${escapeHtml(tile.value)}')">
              <div class="tile-icon-3d">${tile.icon}</div>
              <div class="tile-text-group">
                <div class="tile-title">${escapeHtml(tile.title)}</div>
                <div class="tile-desc">${escapeHtml(tile.desc || '')}</div>
              </div>
            </div>
          `).join("") + `</div>`;
        }"""

new_action_tiles_map = """let tilesHtml = "";
        if (actionTiles && actionTiles.length > 0) {
          currentCardActionTiles = actionTiles;
          tilesHtml = `<div class="cockpit-options-grid">` + actionTiles.map((tile, idx) => `
            <div class="action-tile-3d ${tile.primary ? 'primary-glow' : ''}" onclick="onActionTileClick(${idx})">
              <div class="tile-icon-3d">${tile.icon}</div>
              <div class="tile-text-group">
                <div class="tile-title">${escapeHtml(tile.title)}</div>
                <div class="tile-desc">${escapeHtml(tile.desc || '')}</div>
              </div>
            </div>
          `).join("") + `</div>`;
        } else {
          currentCardActionTiles = [];
        }"""

assert old_action_tiles_map in text, "old_action_tiles_map not found"
text = text.replace(old_action_tiles_map, new_action_tiles_map)
print("Updated actionTiles mapping in appendBotCard")

# 5. Update renderChips, onChipSelected, and add resolveDisplayLabel
old_chips_block_start = text.find('function renderChips(chips) {')
old_chips_block_end = text.find('function handleStepInput(rawInput) {')
assert old_chips_block_start != -1 and old_chips_block_end != -1, "old_chips_block not found"

new_chips_block = """let currentCardActionTiles = [];
    let currentCardChips = [];

    function renderChips(chips) {
      chipsArea.innerHTML = "";
      if (!chips || chips.length === 0) {
        chipsArea.style.display = "none";
        currentCardChips = [];
        return;
      }
      currentCardChips = chips;
      chipsArea.style.display = "flex";
      chips.forEach((chip, idx) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = `action-chip ${chip.primary ? 'primary-glow' : ''}`;
        btn.innerHTML = `${chip.icon ? chip.icon + ' ' : ''}<span>${escapeHtml(chip.label)}</span>`;
        btn.onclick = () => onChipClick(idx);
        chipsArea.appendChild(btn);
      });
    }

    function onActionTileClick(idx) {
      if (!currentCardActionTiles || !currentCardActionTiles[idx]) return;
      const tile = currentCardActionTiles[idx];
      const displayLabel = `${tile.icon ? tile.icon + ' ' : ''}${tile.title}`;
      handleStepInput(tile.value, displayLabel);
    }

    function onChipClick(idx) {
      if (!currentCardChips || !currentCardChips[idx]) return;
      const chip = currentCardChips[idx];
      const displayLabel = `${chip.icon ? chip.icon + ' ' : ''}${chip.label}`;
      const val = chip.value !== undefined ? chip.value : chip.label;
      handleStepInput(val, displayLabel);
    }

    function onChipSelected(val, optLabel) {
      handleStepInput(val, optLabel || val);
    }

    function submitInput() {
      const text = userInput.value.trim();
      if (!text) return;
      handleStepInput(text, text);
      userInput.value = "";
    }

    function resolveDisplayLabel(val, label, step) {
      if (label && label !== val) return label;
      const clean = String(val).trim();

      if (clean === "re_evaluate_rates") return "✏️ Try different ROI / PF";
      if (clean === "new_case") return "👤 New customer";

      switch (step) {
        case STEPS.PRODUCT:
          if (clean === "R") return "🏢 Regular Secured Business Loan";
          if (clean === "W") return "🏭 Secured Working Capital";
          if (clean === "H") return "🚗 Hypothecation Loans";
          break;
        case STEPS.INCOME_PROGRAM:
          if (clean === "D") return "📑 Documented Income";
          if (clean === "A") return "🔍 Assessed Income";
          if (clean === "Hy") return "⚡ Hybrid Program";
          if (clean === "S") return "📋 Semi Documented";
          break;
        case STEPS.PROPERTY_TYPE:
          if (clean === "SORP") return "🏠 SORP (Self Occupied Residential)";
          if (clean === "Other") return "🏬 Other Properties";
          break;
        case STEPS.BUREAU:
          if (clean === "G") return "⭐ Bureau Score >= 700 or NTC";
          if (clean === "L") return "⚠️ Bureau Score < 700";
          break;
        case STEPS.SANC_AMOUNT:
          const pAmt = parseNumber(clean);
          if (pAmt && pAmt > 0) return `💰 ${formatINR(pAmt)}`;
          break;
        case STEPS.SANC_TENURE:
          const pTen = parseTenureMonths(clean);
          if (pTen && pTen > 0) return `⏳ ${pTen} Months (${Math.round(pTen/12)} Yrs)`;
          break;
        case STEPS.SANC_ROI:
          const pRoi = parseFloat(clean.replace(/%/g, ''));
          if (!isNaN(pRoi)) return `📈 ${pRoi.toFixed(2)}% p.a.`;
          break;
        case STEPS.SANC_PF:
          const pPf = parseFloat(clean.replace(/%/g, ''));
          if (!isNaN(pPf)) return `🏷️ ${pPf.toFixed(2)}% PF`;
          break;
        case STEPS.INCOME_FREQ:
          if (clean.toLowerCase().includes("ann")) return "📊 Yearly Earnings";
          return "📅 Monthly Earnings";
        case STEPS.INCOME_AMOUNT:
          const pInc = parseNumber(clean);
          if (pInc && pInc > 0) return `💵 ${formatINR(pInc)}${session.incomeFreq === "Annual" ? " / yr" : " / mo"}`;
          break;
        case STEPS.EXISTING_EMIS:
          const pEmi = parseNumber(clean);
          if (pEmi === 0) return "⚖️ ₹0 (No existing EMIs)";
          if (pEmi && pEmi > 0) return `⚖️ ${formatINR(pEmi)} / mo`;
          break;
        case STEPS.REQ_ROI:
          const pReqRoi = parseFloat(clean.replace(/%/g, ''));
          if (!isNaN(pReqRoi)) return `🎯 ${pReqRoi.toFixed(2)}% Requested ROI`;
          break;
        case STEPS.REQ_PF:
          const pReqPf = parseFloat(clean.replace(/%/g, ''));
          if (!isNaN(pReqPf)) return `🏷️ ${pReqPf.toFixed(2)}% Requested PF`;
          break;
      }
      return clean;
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
      inputHint.textContent = "Enter customer name or reference";
      userInput.placeholder = "e.g. Ramesh Patel, Proposal #402...";
      updateStepperUI();

      appendBotCard({
        categoryBadge: "WELCOME",
        icon3d: "👋",
        stepText: "STEP 1 OF 5",
        htmlContent: t("welcome"),
        chips: [
          { label: "Apex Enterprises", value: "Apex Enterprises", primary: true },
          { label: "Ramesh Patel", value: "Ramesh Patel" },
          { label: "Kavita Sharma", value: "Kavita Sharma" }
        ],
        catMood: "standing-proud",
        delayMs: 250
      });
    }

    function restartSession() {
      conversationToken++;
      setCatVisualState("standing-proud");
      companionSpeech("Session restarted! 🚀", 1800);
      startConversation();
    }

    /* ==========================================================================
       CONVERSATIONAL STEP HANDLER
       ========================================================================== */
    """

text = text[:old_chips_block_start] + new_chips_block + text[old_chips_block_end:]
print("Updated chips handling and display label resolution")

# 6. Update handleStepInput signature and appendUserMessage call
old_handle_input_start = text.find('function handleStepInput(rawInput) {')
old_handle_input_header = """function handleStepInput(rawInput) {
      const clean = String(rawInput).trim();
      if (!clean) return;
      appendUserMessage(clean);"""

new_handle_input_header = """function handleStepInput(rawInput, optDisplayLabel) {
      const clean = String(rawInput).trim();
      if (!clean) return;
      const userFacingText = resolveDisplayLabel(clean, optDisplayLabel, session.step);
      appendUserMessage(userFacingText);

      // Trigger live cat face turning and reaction
      reactCatToUserResponse(session.step, clean, userFacingText);"""

assert old_handle_input_header in text, "old_handle_input_header not found"
text = text.replace(old_handle_input_header, new_handle_input_header)
print("Updated handleStepInput header")

# 7. Update renderFinalExecutiveReport to set cat mood and speech
old_report_mood = """let mood = "standing-proud";
      if (approval.finalApprover.level === 0) mood = "celebrating";
      else if (approval.isFloorBreached || approval.finalApprover.level === 3) mood = "worried-alert";
      else if (approval.finalApprover.level === 1) mood = "laughing";"""

new_report_mood = """let mood = "standing-proud";
      let verdictSpeech = "";
      if (approval.finalApprover.level === 0) {
        mood = "celebrating";
        verdictSpeech = "🎉 Direct approval! Zero policy concessions needed!";
      } else if (approval.isFloorBreached || approval.finalApprover.level === 3) {
        mood = "worried-alert";
        verdictSpeech = "🏛️ CEO Approval Required (Policy Floor / Deep concession)!";
      } else if (approval.finalApprover.level === 2) {
        mood = "curious";
        verdictSpeech = "⚡ COO Approval needed for this rate concession!";
      } else if (approval.finalApprover.level === 1) {
        mood = "joyful";
        verdictSpeech = "😺 CBO Approval required — standard branch tier!";
      }
      setCatVisualState(mood);
      companionSpeech(verdictSpeech, 3600);"""

assert old_report_mood in text, "old_report_mood not found"
text = text.replace(old_report_mood, new_report_mood)
print("Updated renderFinalExecutiveReport cat mood and speech")

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Successfully generated index.html v8 (length: {len(text)})")
