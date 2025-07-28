

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

sns.set(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 14

class Visualizer:
    def __init__(self, output_dir="charts"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def plot_price_history(self, hist_df: pd.DataFrame, ticker: str, save=False):
        """
        Plot closing price history of the stock
        :param hist_df: DataFrame returned from StockResearcher.get_price_history()
        :param ticker: Stock ticker symbol (e.g., AAPL, TSLA)
        :param save: If True, saves the plot to the output_dir folder
        :return: Matplotlib figure object
        """
        if hist_df is None or hist_df.empty:
            print(f"⚠️ No data available to plot for {ticker}.")
            return None

        plt.figure()
        sns.lineplot(x=hist_df.index, y=hist_df["Close"], color="dodgerblue", linewidth=2)
        plt.title(f"{ticker.upper()} - 1 Year Closing Price History")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.tight_layout()

        if save:
            filename = os.path.join(self.output_dir, f"{ticker.upper()}_history.png")
            plt.savefig(filename)
            print(f"📈 Chart saved: {filename}")

        return plt

    def plot_volume_trend(self, hist_df: pd.DataFrame, ticker: str, save=False):
        """
        Plot trading volume trend of the stock
        """
        if hist_df is None or hist_df.empty:
            print(f"⚠️ No data available to plot for {ticker}.")
            return None

        plt.figure()
        sns.lineplot(x=hist_df.index, y=hist_df["Volume"], color="orange", linewidth=1.5)
        plt.title(f"{ticker.upper()} - 1 Year Trading Volume Trend")
        plt.xlabel("Date")
        plt.ylabel("Volume")
        plt.tight_layout()

        if save:
            filename = os.path.join(self.output_dir, f"{ticker.upper()}_volume.png")
            plt.savefig(filename)
            print(f"📊 Volume chart saved: {filename}")

        return plt
    
    def plot_stock_history(self,history_df, ticker):
     plt.figure(figsize=(10, 4))
     plt.plot(history_df.index, history_df['Close'], color='skyblue', linewidth=2)
     plt.title(f"{ticker.upper()} - 1 Year Price History", fontsize=14)
     plt.xlabel("Date")
     plt.ylabel("Close Price ($)")
     plt.grid(True)
     plt.tight_layout()
     return plt
