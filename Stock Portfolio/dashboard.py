import streamlit as st
from logic import PortfolioManager, StockResearcher
from visuals import Visualizer

pm = PortfolioManager()
sr = StockResearcher()
viz = Visualizer()

st.set_page_config(page_title="📈 Stock Portfolio Dashboard", layout="wide")
st.title("📊 Stock Portfolio Dashboard")

# --- SIDEBAR MENU ---
menu = st.sidebar.selectbox("📂 Menu", ["View Portfolio", "Add Stock", "Remove Stock", "Stock Research"])

# --- VIEW PORTFOLIO ---
if menu == "View Portfolio":
    st.header("📁 Your Portfolio")
    if not pm.portfolio:
        st.info("Your portfolio is empty. Add stocks from the sidebar.")
    else:
        data = pm.view_portfolio()

        holdings = data["holdings"]
        total_investment = data["total_investment"]
        total_current_value = data["total_current_value"]
        overall_profit_loss = data["overall_profit_loss"]

        st.subheader("📊 Holdings Summary")
        st.dataframe(holdings)

        st.markdown("---")
        st.metric("💰 Total Investment", f"${total_investment}")
        st.metric("📈 Total Current Value", f"${total_current_value}")
        st.metric("🧾 Overall Profit/Loss", f"${overall_profit_loss}")


# --- ADD STOCK ---
elif menu == "Add Stock":
    st.header("➕ Add New Stock")
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)").upper()
    quantity = st.number_input("Quantity", min_value=1)
    purchase_price = st.number_input("Purchase Price per Share ($)", min_value=0.01, format="%.2f")
    if st.button("Add Stock"):
        if ticker and quantity > 0 and purchase_price > 0:
            pm.add_stock(ticker, quantity, purchase_price)
            st.success(f"{quantity} shares of {ticker} added at ${purchase_price} each.")
        else:
            st.error("Please enter valid data.")

# --- REMOVE STOCK ---
elif menu == "Remove Stock":
    st.header("❌ Remove Stock")
    if not pm.portfolio:
        st.info("Portfolio is empty.")
    else:
        ticker = st.selectbox("Select a stock to remove", list(pm.portfolio.keys()))
        if st.button("Remove"):
            pm.remove_stock(ticker)
            st.success(f"{ticker} removed from portfolio.")

# --- STOCK RESEARCH ---
elif menu == "Stock Research":
    st.header("🔍 Research a Stock")
    ticker = st.text_input("Enter Stock Ticker to Research").upper()
    if ticker:
        price = sr.get_current_price(ticker)
        if price:
            st.metric("Current Price", f"${price:.2f}")
            history = sr.get_price_history(ticker)
            if history is not None and not history.empty:
                st.subheader("📈 1-Year Price Chart")
                fig = viz.plot_stock_history(history, ticker)
                st.pyplot(fig)
            else:
                st.warning("No price history available.")
        else:
            st.error("Could not fetch current price.")
