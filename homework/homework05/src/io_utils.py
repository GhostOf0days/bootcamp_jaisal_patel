# Save and load helpers

from pathlib import Path

import pandas as pd


def detect_format(path):
    # Route by file suffix.
    suffix = str(path).lower()
    if suffix.endswith(".csv"):
        return "csv"
    if suffix.endswith(".parquet") or suffix.endswith(".pq") or suffix.endswith(".parq"):
        return "parquet"
    raise ValueError("Unsupported format: " + str(path))


def write_df(df, path):
    # Save CSV or Parquet.
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fmt = detect_format(path)
    if fmt == "csv":
        df.to_csv(path, index=False)
    else:
        try:
            df.to_parquet(path)
        except Exception as error:
            raise RuntimeError("Parquet engine not available. Install pyarrow or fastparquet.") from error
    return path


def read_df(path):
    # Load CSV or Parquet.
    path = Path(path)
    fmt = detect_format(path)
    if fmt == "csv":
        preview = pd.read_csv(path, nrows=0)
        if "date" in preview.columns:
            return pd.read_csv(path, parse_dates=["date"])
        return pd.read_csv(path)
    try:
        return pd.read_parquet(path)
    except Exception as error:
        raise RuntimeError("Parquet engine not available. Install pyarrow or fastparquet.") from error


def validate_loaded(original, reloaded, cols=("date", "ticker", "price")):
    # Shape, columns, dtypes.
    checks = {
        "shape_equal": original.shape == reloaded.shape,
        "cols_present": all(c in reloaded.columns for c in cols),
    }
    if "price" in reloaded.columns:
        checks["price_is_numeric"] = pd.api.types.is_numeric_dtype(reloaded["price"])
    if "date" in reloaded.columns:
        checks["date_is_datetime"] = pd.api.types.is_datetime64_any_dtype(reloaded["date"])
    return checks
