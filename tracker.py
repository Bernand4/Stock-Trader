# =============================================
#   TRACKER.PY — Bernie's Stock-Trader App
#   Live Portfolio Tracker
#   Always Moving Forward 💪
# =============================================

import yfinance as yf
from portfolio import portfolio

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
