from openbb import obb

# Get the price of a stock
quote_data = obb.equity.price.quote(symbol="AAPL", provider="yfinance")
quote_data