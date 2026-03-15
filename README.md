# Stock-Trader App
# My Portfolio Tracker and Covered Call Calculator

# JEDI Position
shares = 120
stock_price = 26.49
company = "Defiance Drone and Modern Warfare ETF (JEDI)"
market_open = True

# Portfolio Holdings
holdings = ["SCHD", "XOM", "JEDI", "OXY", "VSNT", "XLE", "DOW", "USAR"]

# Position Value Calculator
position_value = shares * stock_price
print("Position Value:", position_value)

# Covered Call Income Calculator
premium = 0.45
premium_income = premium * 100
print("Covered Call Income:", premium_income)

# Print All Holdings
print("My Holdings:")
for stock in holdings:
    print(stock)
