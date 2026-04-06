# =============================================
#   DIVIDENDS.PY — Bernie's Stock-Trader App
#   Dividend Income Tracker
#   Always Moving Forward 💪
# =============================================

from portfolio import portfolio, MONTHLY_DIVIDEND_GOAL

print("=" * 45)
print("      DIVIDEND INCOME TRACKER")
print("=" * 45)

total_annual_income = 0
paying_stocks = []
non_paying_stocks = []

for stock, data in portfolio.items():
    annual_div = data["annual_div"]

    if annual_div > 0:
        annual_income = round(annual_div * data["shares"], 2)
        quarterly_income = round(annual_income / 4, 2)
        monthly_income = round(annual_income / 12, 2)

        total_annual_income += annual_income
        paying_stocks.append(stock)

        print(f"\n{stock}")
        print(f"  Shares:            {data['shares']}")
        print(f"  Dividend/Share:    ${annual_div}/year")
        print(f"  Monthly Income:    ${monthly_income}")
        print(f"  Quarterly Income:  ${quarterly_income}")
        print(f"  Annual Income:     ${annual_income} 🟢")
        print("-" * 45)
    else:
        non_paying_stocks.append(stock)
        print(f"\n{stock}")
        print(f"  No dividend paid ❌")
        print("-" * 45)

# Summary
total_monthly = round(total_annual_income / 12, 2)
total_quarterly = round(total_annual_income / 4, 2)
goal_status = "✅ ACHIEVED!" if total_monthly >= MONTHLY_DIVIDEND_GOAL else f"❌ Need ${round(MONTHLY_DIVIDEND_GOAL - total_monthly, 2)} more/month"

print(f"\n📊 DIVIDEND SUMMARY")
print("=" * 45)
print(f"Paying Stocks:         {', '.join(paying_stocks)}")
print(f"Non Paying Stocks:     {', '.join(non_paying_stocks)}")
print(f"\nTOTAL ANNUAL INCOME:   ${round(total_annual_income, 2)}")
print(f"TOTAL QUARTERLY:       ${total_quarterly}")
print(f"MONTHLY AVERAGE:       ${total_monthly}")
print(f"GOAL: ${MONTHLY_DIVIDEND_GOAL}/month      {goal_status}")
print("=" * 45)
