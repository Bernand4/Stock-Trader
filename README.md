# Stock-Trader App
# My Portfolio Tracker and Covered Call Calculator
# Built: March 2026 — Always Moving Forward 💪

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

# Print Each Holding with Position Value
print("=" * 40)
print("   MY PORTFOLIO TRACKER")
print("=" * 40)

total_portfolio_value = 0

for stock, data in portfolio.items():
    position_value = round(data["shares"] * data["buy_price"], 2)
    total_portfolio_value += position_value
    print(f"{stock}")
    print(f"  Shares:         {data['shares']}")
    print(f"  Buy Price:      ${data['buy_price']}")
    print(f"  Position Value: ${position_value}")
    print("-" * 40)

print(f"TOTAL PORTFOLIO VALUE: ${round(total_portfolio_value, 2)}")
print("=" * 40)

# Covered Call Income Calculator — DHT
print("\nCOVERED CALL CALCULATOR - DHT")
print("=" * 40)
premium = 0.45
premium_income = premium * 100
print(f"Premium Per Share:   ${premium}")
print(f"Income Per Contract: ${premium_income}")
print("=" * 40)
