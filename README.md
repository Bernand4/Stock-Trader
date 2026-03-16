import yfinance as yf

# Portfolio Holdings with Share Count and Buy Price
portfolio = {
    "XOM":  {"shares": 48.6,  "buy_price": 123.44},
    "XLE":  {"shares": 12.3,  "buy_price": 56.91},
    "SCHD": {"shares": 153.14,"buy_price": 26.51},
    "VSNT": {"shares": 20.5,  "buy_price": 34.13},
    "JEDI": {"shares": 120,   "buy_price": 26.88},
    "DOW":  {"shares": 40,    "buy_price": 37.30},
    "OXY":  {"shares": 73.73, "buy_price": 54.25},
    "DHT":  {"shares": 100,   "buy_price": 17.10},
}

# Print Portfolio Header
print("=" * 45)
print("      BERNIE'S PORTFOLIO TRACKER")
print("=" * 45)

total_portfolio_value = 0
total_gain_loss = 0

for stock, data in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = round(ticker.fast_info['last_price'], 2)
    position_value = round(data["shares"] * current_price, 2)
    gain_loss = round((current_price - data["buy_price"]) * data["shares"], 2)
    percent_change = round(((current_price - data["buy_price"]) / data["buy_price"]) * 100, 2)
    
    total_portfolio_value += position_value
    total_gain_loss += gain_loss

    # Green arrow for gain, red for loss
    direction = "🟢" if gain_loss >= 0 else "🔴"

    print(f"\n{stock}")
    print(f"  Shares:          {data['shares']}")
    print(f"  Buy Price:       ${data['buy_price']}")
    print(f"  Current Price:   ${current_price}")
    print(f"  Position Value:  ${position_value}")
    print(f"  Gain/Loss:       {direction} ${gain_loss} ({percent_change}%)")
    print("-" * 45)

print(f"\nTOTAL PORTFOLIO VALUE: ${round(total_portfolio_value, 2)}")
print(f"TOTAL GAIN/LOSS:       {'🟢' if total_gain_loss >= 0 else '🔴'} ${round(total_gain_loss, 2)}")
print("=" * 45)
