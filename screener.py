# =============================================
#   SCREENER.PY — Bernie's Stock-Trader App
#   Covered Call Screener
#   Always Moving Forward 💪
# =============================================

import yfinance as yf
from portfolio import portfolio, MIN_SHARES_FOR_CALL

# 10% above current price for strike suggestion
STRIKE_BUFFER = 1.10

print("=" * 45)
print("      COVERED CALL SCREENER")
print("=" * 45)

eligible = []
not_eligible = []

for stock, data in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = round(ticker.fast_info['last_price'], 2)
    shares = data["shares"]

    print(f"\n{stock}")
    print(f"  Current Price:   ${current_price}")
    print(f"  Shares Owned:    {shares}")

    if shares >= MIN_SHARES_FOR_CALL:
        suggested_strike = round(current_price * STRIKE_BUFFER, 2)
        contracts = int(shares // 100)
        est_premium = round(current_price * 0.02, 2)
        est_income = round(est_premium * 100 * contracts, 2)

        eligible.append(stock)

        print(f"  Status:           ✅ Eligible — {contracts} contract(s)")
        print(f"  Suggested Strike: ${suggested_strike}")
        print(f"  Est. Premium:     ${est_premium}")
        print(f"  Est. Income:      ${est_income}")
    else:
        shares_ne
