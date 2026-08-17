# Stage 05 — Data Storage

Env-driven paths, CSV in `data/raw/`, Parquet in `data/processed/`.

## Data Storage

`data/raw/` contains my CSV files, which are easier to read (CSV is text; we can't read Parquet's binary layout as easily), while `data/processed/` contains my Parquet files that keep the same dtypes, are not human-readable, and are also smaller.

My file paths come from `.env`: `DATA_DIR_RAW=data/raw` and `DATA_DIR_PROCESSED=data/processed`.

I read and write using env variables through `src/io_utils.py`, which has `write_df` and `read_df`. My code picks CSV or Parquet from the file suffix and creates the missing folders. It also raises an error if the Parquet engine is missing.
