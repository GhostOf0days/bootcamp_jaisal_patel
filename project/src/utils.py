# Pokemon Set Screener data helpers

from datetime import datetime


def get_summary_stats(df):
    # Return describe() for numeric columns.
    print(f"[{datetime.now()}] Function 'get_summary_stats' called.")
    return df.select_dtypes(include="number").describe()


def add_rolling_return(df, price_col="market_price", window=7):
    # Rolling % change per card.
    out = df.sort_values(["card_name", "date"]).copy()
    out["rolling_return"] = (
        out.groupby("card_name", group_keys=False)[price_col]
        .pct_change(periods=window)
        .mul(100)
        .round(2)
    )
    return out
