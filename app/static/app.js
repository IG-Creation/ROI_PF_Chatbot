// Frontend Application Script

const chatHistory = document.getElementById("chatHistory");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const sessionId = "session_" + Math.random().toString(36).substring(2, 9);

function scrollToBottom() {
  chatHistory.scrollTop = chatHistory.scrollHeight;
}

function appendUserMessage(text) {
  const wrapper = document.createElement("div");
  wrapper.className = "message-wrapper user";
  wrapper.innerHTML = `
    <div class="avatar">👤</div>
    <div class="message-bubble">${escapeHtml(text)}</div>
  `;
  chatHistory.appendChild(wrapper);
  scrollToBottom();
}

function appendTypingIndicator() {
  const wrapper = document.createElement("div");
  wrapper.className = "message-wrapper typing";
  wrapper.id = "typingIndicator";
  wrapper.innerHTML = `
    <div class="avatar bot">🤖</div>
    <div class="message-bubble">
      <div class="typing-dots">
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
      </div>
    </div>
  `;
  chatHistory.appendChild(wrapper);
  scrollToBottom();
}

function removeTypingIndicator() {
  const indicator = document.getElementById("typingIndicator");
  if (indicator) {
    indicator.remove();
  }
}

function appendBotMessage(markdownText, data = null) {
  removeTypingIndicator();
  const wrapper = document.createElement("div");
  wrapper.className = "message-wrapper";

  // Parse markdown
  let parsedContent = "";
  if (window.marked) {
    parsedContent = marked.parse(markdownText);
  } else {
    parsedContent = markdownText.replace(/\n/g, "<br>");
  }

  const chartId = "chart_" + Math.random().toString(36).substring(2, 9);
  let chartHtml = "";

  // If data has scenarios for simulation, append a canvas
  if (data && data.scenarios && Array.isArray(data.scenarios)) {
    chartHtml = `
      <div class="chart-container-box">
        <canvas id="${chartId}"></canvas>
      </div>
    `;
  }

  wrapper.innerHTML = `
    <div class="avatar bot">🤖</div>
    <div class="message-bubble">
      ${parsedContent}
      ${chartHtml}
    </div>
  `;
  chatHistory.appendChild(wrapper);

  // Render chart if data is present
  if (data && data.scenarios && Array.isArray(data.scenarios) && window.Chart) {
    setTimeout(() => {
      renderScenarioChart(chartId, data.scenarios);
    }, 50);
  }

  scrollToBottom();
}

function renderScenarioChart(canvasId, scenarios) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;

  const labels = scenarios.map((s) => s.label);
  const profits = scenarios.map((s) => s.net_profit);
  const revenues = scenarios.map((s) => s.revenue);

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Net Profit ($)",
          data: profits,
          backgroundColor: profits.map((p) =>
            p >= 0 ? "rgba(59, 130, 246, 0.85)" : "rgba(239, 68, 68, 0.85)"
          ),
          borderRadius: 4,
        },
        {
          label: "Gross Revenue ($)",
          data: revenues,
          backgroundColor: "rgba(148, 163, 184, 0.35)",
          borderRadius: 4,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: { color: "#94a3b8" },
        },
      },
      scales: {
        x: {
          ticks: { color: "#94a3b8" },
          grid: { color: "rgba(255, 255, 255, 0.05)" },
        },
        y: {
          ticks: { color: "#94a3b8" },
          grid: { color: "rgba(255, 255, 255, 0.05)" },
        },
      },
    },
  });
}

async function sendMessage() {
  const text = userInput.value.trim();
  if (!text) return;

  appendUserMessage(text);
  userInput.value = "";
  sendBtn.disabled = true;
  appendTypingIndicator();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, session_id: sessionId }),
    });

    if (!res.ok) {
      throw new Error(`HTTP ${res.status}: ${res.statusText}`);
    }

    const json = await res.json();
    appendBotMessage(json.message, json.data);
  } catch (err) {
    appendBotMessage(`⚠️ **Communication error:** ${err.message}`);
  } finally {
    sendBtn.disabled = false;
    userInput.focus();
  }
}

function sendPreset(query) {
  userInput.value = query;
  sendMessage();
}

function clearChat() {
  chatHistory.innerHTML = `
    <div class="message-wrapper">
      <div class="avatar bot">🤖</div>
      <div class="message-bubble">
        <h3>Conversation reset.</h3>
        <p>Ask a question or select any preset to start analyzing your managed pricing or ROI.</p>
      </div>
    </div>
  `;
}

async function uploadCatalog(input) {
  if (!input.files || input.files.length === 0) return;
  const file = input.files[0];

  appendUserMessage(`Uploaded catalog: ${file.name}`);
  appendTypingIndicator();

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch("/api/upload/catalog", {
      method: "POST",
      body: formData,
    });

    if (!res.ok) {
      throw new Error(`Upload error: ${res.statusText}`);
    }

    const data = await res.json();
    let rowsHtml = data.products
      .map(
        (p) =>
          `| ${p.product} | $${p.unit_cost.toFixed(2)} | $${p.selling_price.toFixed(
            2
          )} | ${p.units} | ${p.pricing_factor}x | ${p.gross_margin_percent}% | $${p.total_profit.toFixed(
            2
          )} | ${p.roi_percent}% |`
      )
      .join("\n");

    const report = `### 📊 Bulk Catalog Pricing Analysis

Processed **${data.count} items** from \`${file.name}\`:

| Metric | Portfolio Total |
| :--- | :--- |
| **Total Revenue** | **$${data.total_revenue.toLocaleString()}** |
| **Total Production Cost** | **$${data.total_cost.toLocaleString()}** |
| **Portfolio Net Profit** | **$${data.total_profit.toLocaleString()}** |
| **Portfolio ROI** | **+${data.portfolio_roi_percent}%** |
| **Portfolio Pricing Factor (PF)** | **${data.portfolio_pricing_factor}x** |

#### Product Breakdown:
| Product | Unit Cost | Price | Units | PF | Margin | Profit | ROI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
${rowsHtml}
`;
    appendBotMessage(report);
  } catch (err) {
    appendBotMessage(`⚠️ Failed to parse catalog: ${err.message}`);
  } finally {
    input.value = "";
  }
}

function escapeHtml(string) {
  const entityMap = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  };
  return String(string).replace(/[&<>"']/g, function (s) {
    return entityMap[s];
  });
}
