# =============================================
#   ALERTS.PY — Bernie's Stock-Trader App
#   Price Alert System
#   Always Moving Forward 💪
# =============================================

import yfinance as yf
from portfolio import portfolio

# Alert thresholds
UP_THRESHOLD = 10      # Alert if up 10% or more
DOWN_THRESHOLD = -5    # Alert if down 5% or more

print("=" * 50)
print("           PRICE ALERTS")
print("=" * 50)

big_gainers = []
watching = []
steady = []

for stock, data in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = round(ticker.fast_info['last_price'], 2)
    buy_price = data["buy_price"]
    pct_change = round(((current_price - buy_price) / buy_price) * 100, 2)

    print(f"\n{stock}")
    print(f"  Buy Price:     ${buy_price}")
    print(f"  Current Price: ${current_price}")
    print(f"  Change:        {'+' if pct_change >= 0 else ''}{pct_change}%")

    if pct_change >= UP_THRESHOLD:
        alert = f"🚀 UP {pct_change}% — Consider Covered Call or Taking Profits"
        big_gainers.append(stock)
    elif pct_change <= DOWN_THRESHOLD:
        alert = f"⚠️  DOWN {pct_change}% — Watch Closely"
        watching.append(stock)
    elif pct_change > 0:
        alert = f"🟢 UP {pct_change}% — Holding Steady"
        steady.append(stock)
    else:
        alert = f"🔴 DOWN {pct_change}% — Monitor Position"
        watching.append(stock)

    print(f"  Alert:         {alert}")
    print("-" * 50)

# Summary
print(f"\n📊 ALERT SUMMARY")
print("=" * 50)
if big_gainers:
    print(f"🚀 Big Gainers:  {', '.join(big_gainers)}")
if watching:
    print(f"⚠️  Watch List:   {', '.join(watching)}")
if steady:
    print(f"🟢 Holding Steady: {', '.join(steady)}")
if not big_gainers and not watching:
    print("✅ All positions within normal range")
print("=" * 50)
