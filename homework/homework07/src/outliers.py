# Outlier helpers

import pandas as pd


def detect_outliers_iqr(series, k=1.5):
    # return a boolean mask for IQR outliers, whereNA is False.
    if k <= 0:
        raise ValueError("k must be positive")
    # convert to numeric. bad values become NA.
    numeric_series = pd.to_numeric(series, errors="coerce")
    if numeric_series.dropna().empty:
        raise ValueError("series has no numeric values")
    q1 = numeric_series.quantile(0.25)
    q3 = numeric_series.quantile(0.75)
    iqr = q3 - q1
    # iqr fences.
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    mask = (numeric_series < lower) | (numeric_series > upper)
    return mask.fillna(False)


def detect_outliers_zscore(series, threshold=3.0):
    # return a boolean mask for the absolute valuye of the z-score being greater than threshold using population std. NA is False.
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    numeric_series = pd.to_numeric(series, errors="coerce")
    if numeric_series.dropna().empty:
        raise ValueError("series has no numeric values")
    mean = numeric_series.mean()
    # population std (ddof=0).
    std = numeric_series.std(ddof=0)
    if std == 0:
        return pd.Series(False, index=numeric_series.index)
    z_score = (numeric_series - mean) / std
    return (z_score.abs() > threshold).fillna(False)


def winsorize_series(series, lower=0.05, upper=0.95):
    # xclip values to the lower and upper quantiles. NA stays NA.
    if not (0 <= lower < upper <= 1):
        raise ValueError("need 0 <= lower < upper <= 1")
    numeric_series = pd.to_numeric(series, errors="coerce")
    if numeric_series.dropna().empty:
        raise ValueError("series has no numeric values")
    lower_quantile = numeric_series.quantile(lower)
    upper_quantile = numeric_series.quantile(upper)
    # clip to those quantile bounds.
    return numeric_series.clip(lower=lower_quantile, upper=upper_quantile)
