# Save and validate helpers

from datetime import datetime


def ts():
    # Timestamp for filenames.
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def save_csv(df, prefix, raw_dir, **meta):
    # Save a timestamped CSV under data/raw/.
    mid = "_".join([f"{k}-{str(v).replace(' ', '-')[:20]}" for k, v in meta.items()])
    path = raw_dir / f"{prefix}_{mid}_{ts()}.csv"
    df.to_csv(path, index=False)
    print("Saved", path)
    return path


def validate(df, required):
    # Required columns, shape, NA count.
    missing = [c for c in required if c not in df.columns]
    return {
        "missing": missing,
        "shape": df.shape,
        "na_total": int(df.isna().sum().sum()),
    }
