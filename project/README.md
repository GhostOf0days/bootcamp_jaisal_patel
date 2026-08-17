# Pokemon Set Screener

- Stage 01 submission: [`homework/homework01/`](../homework/homework01/) (README and [stakeholder memo](../homework/homework01/docs/stakeholder_memo.md))
- Stage 02 submission: [`homework/homework02/`](../homework/homework02/) (setup notebook and `src/config.py`)
- Stage 03 submission: [`homework/homework03/`](../homework/homework03/) (NumPy/pandas notebook and `src/utils.py`)
- Stage 04 submission: [`homework/homework04/`](../homework/homework04/) (API/scrape notebook and raw CSVs)
- Stage 05 submission: [`homework/homework05/`](../homework/homework05/) (storage notebook and README)
- Working codebase: [`project/`](.)

## Problem Statement

Weekly screener and time-series model for the **Prismatic Evolutions** Pokemon set using daily market data from [TCGCSV](https://tcgcsv.com). Stores price history per card, then classifies buy/hold/sell direction and regresses on expected 7-day % price change for alternative-investment decisions.

## Stakeholder & User

Active retail collector-investors set weekly budgets and run the screener each week to decide which Prismatic Evolutions cards to focus on. Decision makers and users are the same group. Review timing: weekly after TCGCSV updates (~8 PM EST).

## Useful Answer & Decision

Predictive and descriptive. Classification (Buy/Hold/Sell from rolling returns and set-median distance) plus regression (next-week % change). Outputs: weekly CSV with actual price, predicted label, predicted % change, and ranked top cards. Metrics: accuracy, confusion matrix, regression MAE.

## Assumptions & Constraints

- TCGCSV/TCGPlayer prices; one set; daily time series per card; simple models only
- TCGCSV archive (~2024+) for training/backtest; $2 minimum price floor
- Public API/data permitted for coursework; secrets in `.env` only

## Known Unknowns / Risks

- TCGCSV endpoint changes; thin-trade stale prices; non-stationary Pokemon market
- Overfitting on short history; condition not modeled in v1; past signals ≠ guaranteed returns

## Lifecycle Mapping

- Define problem framing and stakeholder goals → Stage 1 → README + stakeholder memo
- Create reproducible environment → Stage 2 → `project/` scaffold, `.env`, `src/config.py`
- Explore price data and features → Stage 3 → summary stats, rolling returns, groupby, CSV
- Ingest and accumulate daily history → Stage 4 → timestamped raw CSV + scraped metadata
- Save and reload card-by-date price dataset → Stage 5 → CSV in `data/raw/`, Parquet in `data/processed/`
- Train/evaluate models → later `model/` + `notebooks/` → Buy/Hold/Sell + % change outputs

## Repo Plan

`data/`, `src/`, `notebooks/`, `docs/`, `model/` under `project/`; homework in `homework/homeworkNumber/`.

## Data Storage

`data/raw/` contains my CSV files, which are easier to read (CSV is text; we can't read Parquet's binary layout as easily), while `data/processed/` contains my Parquet files that keep the same dtypes, are not human-readable, and are also smaller.

My file paths come from `.env`: `DATA_DIR_RAW=data/raw` and `DATA_DIR_PROCESSED=data/processed`.

I read and write using env variables through `src/io_utils.py`, which has `write_df` and `read_df`. My code picks CSV or Parquet from the file suffix and creates the missing folders. It also raises an error if the Parquet engine is missing.
