# =============================================
#   PORTFOLIO.PY — Bernie's Stock-Trader App
#   Master Holdings Data
#   Always Moving Forward 💪
# =============================================

# ROTH IRA HOLDINGS
roth_ira = {
    "SCHD": {"shares": 186.14, "buy_price": 27.08,  "annual_div": 1.12},
    "VZ":   {"shares": 100,    "buy_price": 47.13,  "annual_div": 2.66},
    "NVDA": {"shares": 12,     "buy_price": 217.64, "annual_div": 0.016},
    "CIFR": {"shares": 25,     "buy_price": 22.94,  "annual_div": 0.00},
}

# BROKERAGE HOLDINGS
brokerage = {
    "XOM":  {"shares": 28.6, "buy_price": 123.44, "annual_div": 3.96},
    "CBAS": {"shares": 5,    "buy_price": 241.00, "annual_div": 0.00},
    "WDC":  {"shares": 4,    "buy_price": 420.10, "annual_div": 0.00},
}

# TRADE HISTORY
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

# Goals
MONTHLY_DIVIDEND_GOAL = 25.00
MIN_SHARES_FOR_CALL = 100
