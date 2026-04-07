# =============================================
#   DASHBOARD.PY — Bernie's Stock-Trader App
#   Full Trading Dashboard
#   Always Moving Forward 💪
# =============================================

import yfinance as yf
from datetime import datetime
from portfolio import portfolio, trades, MONTHLY_DIVIDEND_GOAL, MIN_SHARES_FOR_CALL

# =============================================
# SETUP
# =============================================
now = datetime.now().strftime("%A %B %d, %Y — %I:%M %p")

total_portfolio_value = 0
total_gain_loss = 0
total_annual_dividends = 0
total_premium = 0
big_gainers = []
watching = []
eligible_calls = []

UP_THRESHOLD = 10
DOWN_THRESHOLD = -5
STRIKE_BUFFER = 1.10

# =============================================
# PULL LIVE DATA
# =============================================
live_data = {}
for stock, data in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = round(ticker.fast_info['last_price'], 2)
    position_value = round(data["shares"] * current_price, 2)
    gain_loss = round((current_price - data["buy_price"]) * data["shares"], 2)
    pct_change = round(((current_price - data["buy_price"]) / data["buy_price"]) * 100, 2)

    total_portfolio_value += position_value
    total_gain_loss += gain_loss

    # Dividends
    annual_div = data.get("annual_div", 0)
    annual_income = round(annual_div * data["shares"], 2)
    total_annual_dividends += annual_income

    # Alerts
    if pct_change >= UP_THRESHOLD:
        big_gainers.append(f"{stock} +{pct_change}%")
    elif pct_change <= DOWN_THRESHOLD:
        watching.append(f"{stock} {pct_change}%")

    # Covered call eligibility
    if data["shares"] >= MIN_SHARES_FOR_CALL:
        contracts = int(data["shares"] // 100)
        suggested_strike = round(current_price * STRIKE_BUFFER, 2)
        est_premium = round(current_price * 0.02 * 100 * contracts, 2)
        eligible_calls.append(f"{stock} — {contracts} contract(s) | Strike ~${suggested_strike} | Est. ${est_premium}")

    live_data[stock] = {
        "current_price": current_price,
        "position_value": position_value,
        "gain_loss": gain_loss,
        "pct_change": pct_change,
        "annual_income": annual_income
    }

# Trade summary
total_bought = sum(t["shares"] * t["price"] for t in trades if t["type"] == "BUY")
total_sold = sum(t["shares"] * t["price"] for t in trades if t["type"] == "SELL")
total_premium = sum(t["shares"] * t["price"] for t in trades if t["type"] == "COVERED CALL")
net_cash_flow = round(total_sold + total_premium - total_bought, 2)

# Monthly dividends
total_monthly_div = round(total_annual_dividends / 12, 2)
div_goal_status = "✅ ACHIEVED" if total_monthly_div >= MONTHLY_DIVIDEND_GOAL else f"❌ Need ${round(MONTHLY_DIVIDEND_GOAL - total_monthly_div, 2)} more"

# =============================================
# PRINT DASHBOARD
# =============================================
print("=" * 55)
print("       BERNIE'S TRADING DASHBOARD")
print(f"       {now}")
print("=" * 55)

# Portfolio Summary
gain_direction = "🟢" if total_gain_loss >= 0 else "🔴"
print(f"\n💰 PORTFOLIO VALUE:      ${round(total_portfolio_value, 2)}")
print(f"📈 TOTAL GAIN/LOSS:      {gain_direction} ${round(total_gain_loss, 2)}")
print(f"💵 MONTHLY DIVIDENDS:    ${total_monthly_div} {div_goal_status}")
print(f"🎯 PREMIUM COLLECTED:    ${round(total_premium, 2)}")
cash_direction = "🟢" if net_cash_flow >= 0 else "🔴"
print(f"💳 NET CASH FLOW:        {cash_direction} ${net_cash_flow}")

# Alerts
print(f"\n{'=' * 55}")
print("🚨 PRICE ALERTS")
print("-" * 55)
if big_gainers:
    print(f"🚀 Big Gainers:  {', '.join(big_gainers)}")
if watching:
    print(f"⚠️  Watch List:   {', '.join(watching)}")
if not big_gainers and not watching:
    print("✅ All positions within normal range")

# Covered Call Opportunities
print(f"\n{'=' * 55}")
print("📋 COVERED CALL OPPORTUNITIES")
print("-" * 55)
for call in eligible_calls:
    print(f"  ✅ {call}")

# Individual Positions
print(f"\n{'=' * 55}")
print("📊 INDIVIDUAL POSITIONS")
print("-" * 55)
for stock, d in live_data.items():
    direction = "🟢" if d["gain_loss"] >= 0 else "🔴"
    print(f"\n  {stock}")
    print(f"    Current Price:  ${d['current_price']}")
    print(f"    Position Value: ${d['position_value']}")
    print(f"    Gain/Loss:      {direction} ${d['gain_loss']} ({d['pct_change']}%)")
    if d["annual_income"] > 0:
        print(f"    Annual Div:     ${d['annual_income']} 💵")

# Trade History
print(f"\n{'=' * 55}")
print("📝 RECENT TRADES")
print("-" * 55)
for trade in trades[-5:]:
    total = round(trade["shares"] * trade["price"], 2)
    print(f"  {trade['date']} | {trade['type']:<14} | {trade['stock']} | ${total}")

print(f"\n{'=' * 55}")
print("       Always Moving Forward 💪")
print("=" * 55)
