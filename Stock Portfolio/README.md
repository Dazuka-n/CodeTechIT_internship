<div align="center">

<img src="https://capsule-render.vercel.app/api?type=shark&color=gradient&customColorList=20,21,22&height=220&section=header&text=Stock%20Portfolio%20Tracker&fontSize=52&fontColor=00FF88&fontAlignY=60&desc=Real-time%20investment%20dashboard%20%C2%B7%20P%26L%20%C2%B7%20Charts%20%C2%B7%20Live%20Market%20Data&descAlignY=78&descSize=16&animation=fadeIn&stroke=00FF88&strokeWidth=1" width="100%"/>

</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![yfinance](https://img.shields.io/badge/yfinance-Live_Data-6366F1?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-Styled_Plots-4ECDC4?style=for-the-badge)](https://seaborn.pydata.org)
[![Status](https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge)](.)
[![Live App](https://img.shields.io/badge/Live-stock--portfolioo.streamlit.app-FF4B4B?style=for-the-badge&logo=streamlit)](https://stock-portfolioo.streamlit.app)

</div>

---

## 📈 What It Does

**Stock Portfolio Tracker** is a personal investment dashboard that gives you a clear, real-time picture of your portfolio — what you bought, what it's worth now, and whether you're up or down.

```
Add stocks  →  fetch live prices  →  calculate P&L  →  visualize trends
```

No spreadsheets. No manual price lookups. Just your portfolio, live — in a clean web interface.

---

## ✨ Features

<div align="center">

| Feature | Description |
|---|---|
| 📥 **Add Stock** | Add a ticker + quantity + buy price to your portfolio |
| ❌ **Remove Stock** | Remove any holding with one click |
| 📊 **Portfolio Summary** | Total invested · current value · overall P&L |
| 🔍 **Stock Research** | Instant price lookup for any ticker |
| 📈 **1-Year Price Chart** | Closing price trend over the past year |
| 📉 **Volume Chart** | Trading volume trend per stock |
| 💾 **Persistent Storage** | Portfolio saved to JSON — survives app restarts |

</div>

---

## 🏗️ Architecture

```mermaid
flowchart TD
    U([👤 User]) -->|Add / Remove / Research| DB[Streamlit Dashboard\ndashboard.py]

    DB --> LG

    subgraph LG [🔧 Backend — logic.py]
        direction TB
        YF[yfinance API\nlive price fetch]
        JS[portfolio.json\nJSON persistence]
        YF --> CALC[Calculate\nInvested · Current · P&L]
        JS <--> CALC
        CALC --> HIST[1-year historical\nstock data]
    end

    HIST --> VZ

    subgraph VZ [🎨 Visualizations — visuals.py]
        direction LR
        PC[📈 Price Trend\nClosing price chart]
        VC[📉 Volume Trend\nTrading volume chart]
    end

    LG --> SUM[💰 Portfolio Summary\nmetrics display]
    VZ --> DB

    style LG fill:#0a1628,stroke:#00FF88,color:#ffffff
    style VZ fill:#0a2010,stroke:#22C55E,color:#ffffff
```

---

## 🗂️ Project Structure

```
Stock_Portfolio/
├── dashboard.py       ← Streamlit frontend — UI, layout, interactions
├── logic.py           ← Portfolio management, yfinance data, P&L calc
├── visuals.py         ← Matplotlib + Seaborn chart generators
├── portfolio.json     ← Local portfolio data store (auto-created)
├── requirements.txt
└── screenshots/
    ├── sample-screen-1.jpg
    ├── sample-screen-2.jpg
    ├── sample-screen-3.jpg
    └── sample-screen-4.jpg
```

---

## 🛠️ Tech Stack

<div align="center">

[![Python](https://skillicons.dev/icons?i=python)](https://python.org)
[![Matplotlib](https://skillicons.dev/icons?i=matplotlib)](https://matplotlib.org)

| Tool | Role |
|---|---|
| **Python** | Core language |
| **Streamlit** | Web dashboard — add/remove stocks, charts, metrics |
| **yfinance** | Live stock prices + 1-year historical OHLCV data |
| **matplotlib** | Price and volume trend charts |
| **seaborn** | Chart styling and visual polish |
| **json + os** | Local portfolio persistence across sessions |

</div>

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install streamlit yfinance matplotlib seaborn
```

### 2️⃣ Run the App

```bash
streamlit run dashboard.py
```

✅ Dashboard opens at `http://localhost:8501`

---

### Using the Dashboard

```
1. Go to "Add Stock" → enter ticker (e.g. AAPL), quantity, buy price
2. Your portfolio appears with current price + P&L calculated live
3. Click any stock → view 1-year price and volume charts
4. Use "Research" tab → look up any ticker instantly
5. Use "Remove Stock" → clean up holdings anytime
```

> **Tip:** Portfolio data is saved automatically to `portfolio.json` — your holdings persist between sessions.

---

## 📊 Screenshots

<p align="center">
  <img src="screenshots/sample-screen-1.jpg" width="700"/>
</p>
<p align="center">
  <img src="screenshots/sample-screen-2.jpg" width="700"/>
</p>
<p align="center">
  <img src="screenshots/sample-screen-3.jpg" width="700"/>
</p>
<p align="center">
  <img src="screenshots/sample-screen-4.jpg" width="700"/>
</p>

---

## 📌 Roadmap

- [ ] User authentication + multi-portfolio support
- [ ] CSV export of portfolio history
- [ ] Technical indicators — RSI, Moving Average, Bollinger Bands
- [ ] Price alerts and notifications
- [ ] Cloud deployment with persistent storage

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=shark&color=gradient&customColorList=20,21,22&height=100&section=footer&reversal=true" width="100%"/>

**Krishna** · Python Full Stack Intern · CodeTech IT Solutions

[![Live App](https://img.shields.io/badge/Try_it_Live-stock--portfolioo.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://stock-portfolioo.streamlit.app)

⭐ If this helped you, give it a star!

</div>
