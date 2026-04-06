# =============================================
#   TRADES.PY — Bernie's Stock-Trader App
#   Trade History Log
#   Always Moving Forward 💪
# =============================================

from portfolio import trades

print("=" * 60)
print("            TRADE HISTORY LOG")
print("=" * 60)
print(f"{'Date':<12} {'Type':<14} {'Stock':<7} {'Shares':<8} {'Price':<8} {'Total'}")
print("-" * 60)

total_bought = 0
total_sold = 0
total_premium = 0

for trade in trades:
    total = round(trade["shares"] * trade["price"], 2)
    print(f"{trade['date']:<12} {trade['type']:<14} {trade['stock']:<7} {trade['shares']:<8} ${trade['price']:<7} ${total}")

    if trade["type"] == "BUY":
        total_bought += total
    elif trade["type"] == "SELL":
        total_sold += total
    elif trade["type"] == "COVERED CALL":
        total_premium += total

print("-" * 60)

# Summary
net_cash_flow = round(total_sold + total_premium - total_bought, 2)
cash_direction = "🟢" if net_cash_flow >= 0 else "🔴"

print(f"\n📊 TRADE SUMMARY")
print("=" * 60)
print(f"TOTAL INVESTED:           ${round(total_bought, 2)}")
print(f"TOTAL SOLD:               ${round(total_sold, 2)}")
print(f"TOTAL PREMIUM COLLECTED:  ${round(total_premium, 2)}")
print
