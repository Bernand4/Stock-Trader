# =============================================
#   PORTFOLIO.PY — Bernie's Stock-Trader App
#   Master Holdings Data
#   Always Moving Forward 💪
# =============================================

portfolio = {
    "XOM":  {
        "shares": 48.6,
        "buy_price": 123.44,
        "annual_div": 3.96
    },
    "XLE":  {
        "shares": 12.3,
        "buy_price": 56.91,
        "annual_div": 2.08
    },
    "SCHD": {
        "shares": 153.14,
        "buy_price": 26.51,
        "annual_div": 1.12
    },
    "VSNT": {
        "shares": 20.5,
        "buy_price": 34.13,
        "annual_div": 0.08
    },
    "JEDI": {
        "shares": 120,
        "buy_price": 26.88,
        "annual_div": 0.00
    },
    "DOW":  {
        "shares": 40,
        "buy_price": 37.30,
        "annual_div": 2.80
    },
    "OXY":  {
        "shares": 73.73,
        "buy_price": 54.25,
        "annual_div": 0.96
    },
    "DHT":  {
        "shares": 100,
        "buy_price": 17.10,
        "annual_div": 0.98
    },
}

# Trade History
trades = [
    {"date": "2026-03-16", "type": "BUY",          "stock": "DHT",  "shares": 100, "price": 17.10},
    {"date": "2026-03-16", "type": "SELL",         "stock": "USAR", "shares": 60,  "price": 20.01},
    {"date": "2026-03-16", "type": "COVERED CALL", "stock": "DHT",  "shares": 100, "price": 0.75},
]

# Goals
MONTHLY_DIVIDEND_GOAL = 25.00
MIN_SHARES_FOR_CALL = 100
