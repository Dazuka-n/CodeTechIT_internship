

from logic import StockResearcher
from visuals import Visualizer

# Example stock
ticker = "TSLA"

# Initialize components
researcher = StockResearcher()
visualizer = Visualizer()

# Get 1 year price history
hist_df = researcher.get_price_history(ticker)

# Plot and save charts
if hist_df is not None:
    visualizer.plot_price_history(hist_df, ticker, save=True)
    visualizer.plot_volume_trend(hist_df, ticker, save=True)
