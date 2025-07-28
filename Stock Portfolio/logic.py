import json
import os
import yfinance as yf
from tabulate import tabulate



class PortfolioManager:
    def __init__(self, filename="portfolio.json"):
        self.filename = filename
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except Exception as e:
                print(f"Error loading portfolio: {e}")
                return {}
        return {}

    def save_portfolio(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.portfolio, file, indent=4)
        except Exception as e:
            print(f"Error saving portfolio: {e}")

    def add_stock(self, ticker, quantity, purchase_price):
        ticker = ticker.upper()
        self.portfolio[ticker] = {
            "quantity": quantity,
            "purchase_price": purchase_price
        }
        self.save_portfolio()
        print(f"✅ Added {quantity} shares of {ticker} at ${purchase_price} per share.")

    def remove_stock(self, ticker):
        ticker = ticker.upper()
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            self.save_portfolio()
            print(f"❌ Removed {ticker} from the portfolio.")
        else:
            print(f"{ticker} not found in the portfolio.")

    def get_stock_data(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            if not data.empty:
                return data['Close'].iloc[-1]
            else:
                print(f"⚠️ Failed to fetch data for {ticker}.")
                return None
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None

    def view_portfolio(self):
        if not self.portfolio:
            print("📭 Portfolio is empty.")
            return

        table = []
        total_investment = 0
        total_current_value = 0

        for ticker, info in self.portfolio.items():
            current_price = self.get_stock_data(ticker)
            if current_price is None:
                continue

            quantity = info["quantity"]
            purchase_price = info["purchase_price"]
            current_value = quantity * current_price
            investment = quantity * purchase_price
            profit_loss = current_value - investment
            profit_loss_percent = (profit_loss / investment) * 100

            total_investment += investment
            total_current_value += current_value

            table.append([
                ticker,
                quantity,
                f"${purchase_price:.2f}",
                f"${current_price:.2f}",
                f"${current_value:.2f}",
                f"${profit_loss:.2f}",
                f"{profit_loss_percent:.2f}%"
            ])

        print(tabulate(
            table,
            headers=["Ticker", "Quantity", "Purchase Price", "Current Price", "Current Value", "Profit/Loss ($)", "Profit/Loss (%)"],
            tablefmt="grid"
        ))
        print(f"\n💰 Total Investment: ${total_investment:.2f}")
        print(f"📈 Total Current Value: ${total_current_value:.2f}")
        print(f"🧾 Overall Profit/Loss: ${total_current_value - total_investment:.2f}")


class StockResearcher:
    def get_current_price(self, ticker):
        ticker = ticker.upper()
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            return info.get('regularMarketPrice', None)
        except Exception as e:
            print(f"Error getting current price for {ticker}: {e}")
            return None

    def get_price_history(self, ticker, period="1y"):
        ticker = ticker.upper()
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)
            return hist
        except Exception as e:
            print(f"Error fetching history for {ticker}: {e}")
            return None
