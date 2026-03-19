# =============================================
#      DIVIDEND INCOME TRACKER
# =============================================

# Portfolio Holdings with dividend rates
portfolio = {
    "XOM":  {"shares": 48.6,  "buy_price": 123.44, "annual_div": 3.96},
    "XLE":  {"shares": 12.3,  "buy_price": 56.91,  "annual_div": 2.08},
    "SCHD": {"shares": 153.14,"buy_price": 26.51,  "annual_div": 1.12},
    "VSNT": {"shares": 20.5,  "buy_price": 34.13,  "annual_div": 0.08},
    "JEDI": {"shares": 120,   "buy_price": 26.88,  "annual_div": 0.00},
    "DOW":  {"shares": 40,    "buy_price": 37.30,  "annual_div": 2.80},
    "OXY":  {"shares": 73.73, "buy_price": 54.25,  "annual_div": 0.96},
    "DHT":  {"shares": 100,   "buy_price": 17.10,  "annual_div": 0.98},
}

# Monthly dividend goal
MONTHLY_GOAL = 25.00

print("=" * 45)
print("      DIVIDEND INCOME TRACKER")
print("=" * 45)

total_annual_income = 0

for stock, data in portfolio.items():
    annual_div = data["annual_div"]

    if annual_div > 0:
        annual_income = round(annual_div * data["shares"], 2)
        quarterly_income = round(annual_income / 4, 2)
        monthly_income = round(annual_income / 12, 2)

        total_annual_income += annual_income

        print(f"\n{stock}")
        print(f"  Shares:            {data['shares']}")
        print(f"  Dividend/Share:    ${annual_div}/year")
        print(f"  Quarterly Income:  ${quarterly_income}")
        print(f"  Annual Income:     ${annual_income} 🟢")
        print("-" * 45)
    else:
        print(f"\n{stock}")
        print(f"  No dividend paid ❌")
        print("-" * 45)

# Summary
total_monthly = round(total_annual_income / 12, 2)
goal_status = "✅ ACHIEVED!" if total_monthly >= MONTHLY_GOAL else f"❌ Need ${round(MONTHLY_GOAL - total_monthly, 2)} more/month"

print(f"\nTOTAL ANNUAL DIVIDEND INCOME:  ${round(total_annual_income, 2)}")
print(f"MONTHLY AVERAGE:               ${total_monthly}")
print(f"GOAL: ${MONTHLY_GOAL}/month     {goal_status}")
print("=" * 45)
