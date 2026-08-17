# Summary stats helper

from datetime import datetime


def get_summary_stats(df):
    # Return describe() for numeric columns.
    print(f"[{datetime.now()}] Function 'get_summary_stats' called.")
    return df.select_dtypes(include="number").describe()
