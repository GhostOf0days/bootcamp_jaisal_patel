# Cleaning helpers


def fill_missing_median(df, columns):
    """Fill NA in `columns` with each column's median."""
    out = df.copy()
    for col in columns:
        out[col] = out[col].fillna(out[col].median())
    return out


def drop_missing(df, threshold=0.5):
    """Drop columns whose NA share is above `threshold`."""
    na_share = df.isna().mean()
    drop_cols = na_share[na_share > threshold].index
    return df.drop(columns=drop_cols)


def normalize_data(df, columns):
    """Min-max scale `columns` to [0, 1]."""
    out = df.copy()
    for col in columns:
        lo = out[col].min()
        hi = out[col].max()
        span = hi - lo
        if span == 0:
            out[col] = 0.0
        else:
            out[col] = (out[col] - lo) / span
    return out
