# =============================================
#   SCREENER.PY — Bernie's Stock-Trader App
#   Expanded Stock Screener
#   Always Moving Forward 💪
# =============================================

import yfinance as yf
from portfolio import portfolio, MIN_SHARES_FOR_CALL

# =============================================
# WATCHLIST — holdings + candidates to screen
# =============================================
WATCHLIST = [
    # Energy
    "XOM", "CVX", "COP", "OXY", "SLB", "PSX", "VLO", "MPC",
    # Dividend stalwarts
    "T", "VZ", "MO", "PM", "KO", "PEP", "JNJ", "IBM",
    # Industrials / chemicals
    "DOW", "LYB", "EMN",
    # Shipping / tankers
    "DHT", "FRO", "STNG",
    # ETFs
    "SCHD", "XLE", "JEPI", "DIVO",
    # Already own (ensure they appear)
    "VSNT", "JEDI",
]

# =============================================
# FILTER THRESHOLDS
# =============================================
MIN_YIELD      = 2.0    # minimum dividend yield %
MAX_PE         = 25.0   # max P/E (skip overvalued)
MAX_FROM_52W_LOW = 40.0 # max % above 52-week low (momentum gate)
MIN_PRICE      = 5.0    # skip micro-caps / penny stocks
STRIKE_BUFFER  = 1.10   # covered call strike = price * this

# =============================================
# SCORING WEIGHTS  (must sum to 100)
# =============================================
YIELD_WEIGHT    = 40   # dividend income priority
VALUE_WEIGHT    = 30   # P/E value
MOMENTUM_WEIGHT = 30   # proximity to 52-week low (lower = better entry)


def score_stock(div_yield, pe, pct_from_low):
    """Return 0-100 composite score. Higher is better."""

    # Yield score: 0% → 0 pts, 8%+ → 40 pts (cap at 8%)
    yield_score = min(div_yield / 8.0, 1.0) * YIELD_WEIGHT

    # Value score: P/E 0 → 30 pts, P/E 25 → 0 pts (linear)
    if pe is None or pe <= 0:
        value_score = 0
    else:
        value_score = max(0, (1 - pe / MAX_PE)) * VALUE_WEIGHT

    # Momentum score: 0% above low → 30 pts, 40%+ → 0 pts (linear)
    momentum_score = max(0, (1 - pct_from_low / MAX_FROM_52W_LOW)) * MOMENTUM_WEIGHT

    return round(yield_score + value_score + momentum_score, 1)


# =============================================
# FETCH + EVALUATE
# =============================================
owned = set(portfolio.keys())
results = []
skipped = []

print("=" * 55)
print("       STOCK SCREENER — Fetching data...")
print("=" * 55)

for symbol in dict.fromkeys(WATCHLIST):  # deduplicate, preserve order
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        price      = info.get("currentPrice") or info.get("regularMarketPrice")
        low_52w    = info.get("fiftyTwoWeekLow")
        high_52w   = info.get("fiftyTwoWeekHigh")
        pe         = info.get("trailingPE")
        div_yield  = (info.get("dividendYield") or 0) * 100  # convert to %
        name       = info.get("shortName", symbol)

        if not price or not low_52w:
            skipped.append((symbol, "missing price data"))
            continue

        if price < MIN_PRICE:
            skipped.append((symbol, f"price ${price} below minimum"))
            continue

        pct_from_low = round(((price - low_52w) / low_52w) * 100, 1)

        # Apply hard filters
        reasons = []
        if div_yield < MIN_YIELD:
            reasons.append(f"yield {div_yield:.1f}% < {MIN_YIELD}%")
        if pe and pe > MAX_PE:
            reasons.append(f"P/E {pe:.1f} > {MAX_PE}")
        if pct_from_low > MAX_FROM_52W_LOW:
            reasons.append(f"{pct_from_low}% above 52w low")

        is_owned   = symbol in owned
        shares     = portfolio.get(symbol, {}).get("shares", 0)
        call_ready = shares >= MIN_SHARES_FOR_CALL
        contracts  = int(shares // 100) if call_ready else 0
        est_strike = round(price * STRIKE_BUFFER, 2) if call_ready else None
        est_income = round(price * 0.02 * 100 * contracts, 2) if call_ready else 0

        composite = score_stock(div_yield, pe, pct_from_low)

        results.append({
            "symbol":       symbol,
            "name":         name,
            "price":        round(price, 2),
            "yield":        round(div_yield, 2),
            "pe":           round(pe, 1) if pe else None,
            "pct_from_low": pct_from_low,
            "score":        composite,
            "passed":       len(reasons) == 0,
            "reasons":      reasons,
            "is_owned":     is_owned,
            "call_ready":   call_ready,
            "contracts":    contracts,
            "est_strike":   est_strike,
            "est_income":   est_income,
        })

    except Exception as e:
        skipped.append((symbol, str(e)))

# =============================================
# SORT & SPLIT
# =============================================
passed   = [r for r in results if r["passed"]]
filtered = [r for r in results if not r["passed"]]

passed.sort(key=lambda r: r["score"], reverse=True)

new_buys  = [r for r in passed if not r["is_owned"]]
holdings  = [r for r in passed if r["is_owned"]]

# Also include owned stocks that didn't pass — still actionable
owned_filtered = [r for r in filtered if r["is_owned"]]

# =============================================
# OUTPUT
# =============================================
print()
print("=" * 55)
print("  NEW BUY CANDIDATES  (ranked by score)")
print("=" * 55)
if new_buys:
    for r in new_buys:
        pe_str = f"{r['pe']}" if r["pe"] else "N/A"
        print(f"\n  {r['symbol']:<6}  {r['name']}")
        print(f"    Score:        {r['score']}/100")
        print(f"    Price:        ${r['price']}")
        print(f"    Yield:        {r['yield']}%")
        print(f"    P/E:          {pe_str}")
        print(f"    vs 52w Low:   +{r['pct_from_low']}%")
else:
    print("\n  No new candidates passed all filters today.")

print()
print("=" * 55)
print("  CURRENT HOLDINGS — ACTION NEEDED")
print("=" * 55)
all_holdings_shown = holdings + owned_filtered
all_holdings_shown.sort(key=lambda r: r["score"], reverse=True)

if all_holdings_shown:
    for r in all_holdings_shown:
        pe_str     = f"{r['pe']}" if r["pe"] else "N/A"
        status_tag = "✅ PASSES FILTERS" if r["passed"] else f"⚠️  {', '.join(r['reasons'])}"
        print(f"\n  {r['symbol']:<6}  Score: {r['score']}/100  |  {status_tag}")
        print(f"    Price:        ${r['price']}")
        print(f"    Yield:        {r['yield']}%")
        print(f"    P/E:          {pe_str}")
        print(f"    vs 52w Low:   +{r['pct_from_low']}%")
        if r["call_ready"]:
            print(f"    Covered Call: {r['contracts']} contract(s) | Strike ~${r['est_strike']} | Est. ${r['est_income']}")
        else:
            shares_needed = MIN_SHARES_FOR_CALL - portfolio.get(r["symbol"], {}).get("shares", 0)
            print(f"    Covered Call: Need {shares_needed:.0f} more shares for eligibility")
else:
    print("\n  No holdings data available.")

print()
print("=" * 55)
print("  FILTERED OUT")
print("=" * 55)
non_owned_filtered = [r for r in filtered if not r["is_owned"]]
if non_owned_filtered or skipped:
    for r in non_owned_filtered:
        print(f"  {r['symbol']:<6}  ${r['price']}  — {', '.join(r['reasons'])}")
    for sym, reason in skipped:
        print(f"  {sym:<6}  skipped — {reason}")
else:
    print("  None.")

print()
print("=" * 55)
print("       Always Moving Forward 💪")
print("=" * 55)
