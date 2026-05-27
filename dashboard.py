# =============================================
#   BERNIE'S TRADING DASHBOARD
#   Two Account View — Roth IRA + Brokerage
#   Always Moving Forward 💪
# =============================================

import yfinance as yf
from datetime import datetime

# =============================================
# ROTH IRA HOLDINGS
# =============================================
roth_ira = {
    "SCHD": {"shares": 186.14, "buy_price": 27.08,  "annual_div": 1.12},
    "VZ":   {"shares": 100,    "buy_price": 47.13,  "annual_div": 2.66},
    "NVDA": {"shares": 12,     "buy_price": 217.64, "annual_div": 0.016},
    "CIFR": {"shares": 25,     "buy_price": 22.94,  "annual_div": 0.00},
}

# =============================================
# BROKERAGE HOLDINGS
# =============================================
brokerage = {
    "XOM":  {"shares": 28.6, "buy_price": 123.44, "annual_div": 3.96},
    "CBAS": {"shares": 5,    "buy_price": 241.00, "annual_div": 0.00},
    "WDC":  {"shares": 4,    "buy_price": 420.10, "annual_div": 0.00},
}

# =============================================
# TRADE HISTORY
# =============================================
trades = [
    {"date": "2026-03-16", "type": "BUY",  "stock": "DHT",  "shares": 100,   "price": 17.10,  "account": "Roth IRA"},
    {"date": "2026-03-16", "type": "SELL", "stock": "USAR", "shares": 60,    "price": 20.01,  "account": "Roth IRA"},
    {"date": "2026-04-09", "type": "SELL", "stock": "OXY",  "shares": 73.73, "price": 57.02,  "account": "Roth IRA"},
    {"date": "2026-04-09", "type": "SELL", "stock": "XOM",  "shares": 20,    "price": 151.15, "account": "Roth IRA"},
    {"date": "2026-04-09", "type": "BUY",  "stock": "DOW",  "shares": 40,    "price": 37.77,  "account": "Roth IRA"},
    {"date": "2026-04-17", "type": "BUY",  "stock": "VSNT", "shares": 25,    "price": 41.20,  "account": "Brokerage"},
    {"date": "2026-04-20", "type": "BUY",  "stock": "SCHD", "shares": 33,    "price": 30.84,  "account": "Roth IRA"},
    {"date": "2026-04-29", "type": "BUY",  "stock": "WDC",  "shares": 4,     "price": 420.10, "account": "Brokerage"},
    {"date": "2026-05-07", "type": "BUY",  "stock": "POET", "shares": 50,    "price": 15.19,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "BUY",  "stock": "POET", "shares": 50,    "price": 8.10,   "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "POET", "shares": 50,    "price": 8.28,   "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "POET", "shares": 50,    "price": 9.18,   "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "DHT",  "shares": 100,   "price": 18.87,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "DOW",  "shares": 80,    "price": 37.55,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "JEDI", "shares": 120,   "price": 28.13,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "JEDI", "shares": 0.003, "price": 28.24,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "SELL", "stock": "XLE",  "shares": 12.3,  "price": 57.51,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "BUY",  "stock": "VZ",   "shares": 100,   "price": 47.13,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "BUY",  "stock": "INOD", "shares": 10,    "price": 82.21,  "account": "Roth IRA"},
    {"date": "2026-05-07", "type": "BUY",  "stock": "INOD", "shares": 10,    "price": 95.65,  "account": "Roth IRA"},
    {"date": "2026-05-11", "type": "BUY",  "stock": "AAOI", "shares": 8,     "price": 166.80, "account": "Roth IRA"},
    {"date": "2026-05-11", "type": "SELL", "stock": "AAOI", "shares": 8,     "price": 163.82, "account": "Roth IRA"},
    {"date": "2026-05-12", "type": "SELL", "stock": "VSNT", "shares": 45.5,  "price": 39.83,  "account": "Brokerage"},
    {"date": "2026-05-13", "type": "SELL", "stock": "INOD", "shares": 20,    "price": 102.93, "account": "Roth IRA"},
    {"date": "2026-05-20", "type": "BUY",  "stock": "NVDA", "shares": 6,     "price": 211.27, "account": "Roth IRA"},
    {"date": "2026-05-21", "type": "SELL", "stock": "AXTI", "shares": 20,    "price": 120.35, "account": "Roth IRA"},
    {"date": "2026-05-26", "type": "BUY",  "stock": "CBAS", "shares": 5,     "price": 241.00, "account": "Brokerage"},
    {"date": "2026-05-27", "type": "BUY",  "stock": "NVDA", "shares": 6,     "price": 224.00, "account": "Roth IRA"},
    {"date": "2026-05-27", "type": "BUY",  "stock": "CIFR", "shares": 25,    "price": 22.94,  "account": "Roth IRA"},
]

MONTHLY_DIVIDEND_GOAL = 25.00
MIN_SHARES_FOR_CALL = 100
UP_THRESHOLD = 10
DOWN_THRESHOLD = -5
STRIKE_BUFFER = 1.10

# =============================================
# FUNCTION TO PROCESS AN ACCOUNT
# =============================================
def process_account(account_name, holdings):
    total_value = 0
    total_gain = 0
    total_divs = 0
    big_gainers = []
    watching = []
    eligible_calls = []

    print("=" * 55)
    print("   " + account_name.upper())
    print("=" * 55)

    for stock, data in holdings.items():
        ticker = yf.Ticker(stock)
        try:
            info = ticker.info
            current_price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            current_price = round(float(current_price), 2)
        except:
            current_price = data["buy_price"]

        position_value = round(data["shares"] * current_price, 2)
        gain_loss = round((current_price - data["buy_price"]) * data["shares"], 2)
        pct_change = round(((current_price - data["buy_price"]) / data["buy_price"]) * 100, 2)
        annual_income = round(data["annual_div"] * data["shares"], 2)

        total_value += position_value
        total_gain += gain_loss
        total_divs += annual_income

        direction = "🟢" if gain_loss >= 0 else "🔴"

        if pct_change >= UP_THRESHOLD:
            big_gainers.append(stock + " +" + str(pct_change) + "%")
        elif pct_change <= DOWN_THRESHOLD:
            watching.append(stock + " " + str(pct_change) + "%")

        if data["shares"] >= MIN_SHARES_FOR_CALL:
            contracts = int(data["shares"] // 100)
            suggested_strike = round(current_price * STRIKE_BUFFER, 2)
            est_premium = round(current_price * 0.02 * 100 * contracts, 2)
            eligible_calls.append(stock + " - " + str(contracts) + " contract(s) | Strike ~$" + str(suggested_strike) + " | Est. $" + str(est_premium))

        print("\n  " + stock)
        print("    Shares:         " + str(data['shares']))
        print("    Buy Price:      $" + str(data['buy_price']))
        print("    Current Price:  $" + str(current_price))
        print("    Position Value: $" + str(position_value))
        print("    Gain/Loss:      " + direction + " $" + str(gain_loss) + " (" + str(pct_change) + "%)")
        if annual_income > 0:
            print("    Annual Div:     $" + str(annual_income))
        print("-" * 55)

    total_monthly_div = round(total_divs / 12, 2)
    gain_direction = "🟢" if total_gain >= 0 else "🔴"

    print("\n  ACCOUNT SUMMARY")
    print("  Total Value:      $" + str(round(total_value, 2)))
    print("  Total Gain/Loss:  " + gain_direction + " $" + str(round(total_gain, 2)))
    print("  Monthly Divs:     $" + str(total_monthly_div))

    if eligible_calls:
        print("\n  COVERED CALL OPPORTUNITIES")
        for call in eligible_calls:
            print("  ✅ " + call)

    if big_gainers:
        print("\n  🚀 Big Gainers: " + ", ".join(big_gainers))
    if watching:
        print("\n  ⚠️  Watch List:  " + ", ".join(watching))

    return total_value, total_gain, total_divs

# =============================================
# TRADE JOURNAL
# =============================================
def print_trade_journal():
    print("\n" + "=" * 55)
    print("   TRADE JOURNAL — ALL TRANSACTIONS")
    print("=" * 55)

    total_bought = 0
    total_sold = 0

    for trade in trades:
        total = round(trade["shares"] * trade["price"], 2)
        print("  " + trade['date'] + " | " + trade['type'] + " | " + trade['stock'] + " | " + str(trade['shares']) + " shares | $" + str(trade['price']) + " | $" + str(total) + " | " + trade['account'])

        if trade["type"] == "BUY":
            total_bought += total
        elif trade["type"] == "SELL":
            total_sold += total

    net = round(total_sold - total_bought, 2)
    direction = "🟢" if net >= 0 else "🔴"

    print("\n  JOURNAL SUMMARY")
    print("  Total Bought:     $" + str(round(total_bought, 2)))
    print("  Total Sold:       $" + str(round(total_sold, 2)))
    print("  Net Cash Flow:    " + direction + " $" + str(net))

    print("\n  📝 JOURNAL NOTE — AAOI May 11 2026")
    print("  Panic sold 8 shares at $163.82 — bought at $166.80")
    print("  Loss: -$23.84 — Stock has since recovered.")
    print("  Lesson: Stick to the plan. No panic selling.")

# =============================================
# RUN DASHBOARD
# =============================================
now = datetime.now().strftime("%A %B %d, %Y - %I:%M %p")

print("=" * 55)
print("      BERNIE'S TRADING DASHBOARD")
print("      " + now)
print("=" * 55)

roth_value, roth_gain, roth_divs = process_account("ROTH IRA", roth_ira)
print("\n")
brokerage_value, brokerage_gain, brokerage_divs = process_account("Individual TOD Brokerage", brokerage)

total_value = round(roth_value + brokerage_value, 2)
total_gain = round(roth_gain + brokerage_gain, 2)
total_monthly_divs = round((roth_divs + brokerage_divs) / 12, 2)
div_goal = "✅ ACHIEVED" if total_monthly_divs >= MONTHLY_DIVIDEND_GOAL else "❌ Need $" + str(round(MONTHLY_DIVIDEND_GOAL - total_monthly_divs, 2)) + " more"
gain_direction = "🟢" if total_gain >= 0 else "🔴"

print("\n" + "=" * 55)
print("   GRAND TOTAL — ALL ACCOUNTS")
print("=" * 55)
print("  Total Portfolio Value: $" + str(total_value))
print("  Total Gain/Loss:       " + gain_direction + " $" + str(total_gain))
print("  Monthly Dividends:     $" + str(total_monthly_divs) + " " + div_goal)

print_trade_journal()

print("\n" + "=" * 55)
print("      Always Moving Forward 💪")
print("=" * 55)
