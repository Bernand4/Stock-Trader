import yfinance as yf

# Portfolio Holdings — needed in every cell that uses it
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

# =============================================
#      COVERED CALL SCREENER
# =============================================
print("=" * 45)
print("      COVERED CALL SCREENER")
print("=" * 45)

# Minimum shares needed for 1 covered call contract
MIN_SHARES = 100

# 10% above current price for strike suggestion
STRIKE_BUFFER = 1.10

for stock, data in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = round(ticker.fast_info['last_price'], 2)
    shares = data["shares"]

    print(f"\n{stock}")
    print(f"  Current Price:   ${current_price}")
    print(f"  Shares Owned:    {shares}")

    # Check if eligible for covered call
    if shares >= MIN_SHARES:
        suggested_strike = round(current_price * STRIKE_BUFFER, 2)
        contracts = int(shares // 100)

        # Estimated premium — 2% of current price as rough estimate
        est_premium = round(current_price * 0.02, 2)
        est_income = round(est_premium * 100 * contracts, 2)

        print(f"  Status:          ✅ Eligible — {contracts} contract(s)")
        print(f"  Suggested Strike: ${suggested_strike}")
        print(f"  Est. Premium:    ${est_premium}")
        print(f"  Est. Income:     ${est_income}")
    else:
        shares_needed = round(MIN_SHARES - shares, 2)
        print(f"  Status:          ❌ Need {shares_needed} more shares")

    print("-" * 45)

print("\n⚠️  Always verify premiums on Fidelity before trading.")
print("=" * 45)
