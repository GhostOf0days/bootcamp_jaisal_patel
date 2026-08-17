# Pokemon Set Screener

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Pokemon TCG (trading card game) singles' prices on TCGPlayer move every day as more people grade new cards and more collectors join the hobby, leading to fluctuations in supply and demand. However, collectors tracking a full Pokemon set cannot easily tell which cards are unusually cheap or expensive compared to recent history when deciding what to sell or buy. Manually checking dozens of card prices is slow, and prices swing around reprints, hype, and graded-card supply.

In this project I will build a weekly screener and time-series model for the Prismatic Evolutions Pokemon set using daily market data from [TCGCSV](https://tcgcsv.com) (a TCGPlayer mirror). The pipeline will store price history per card, then use past daily prices to classify what direction should be taken for a card (buy/hold/sell) and regress on expected 7-day price change. This tool could be used for alternative investments.

## Stakeholder & User

The decision makers are active retail collectors and investors who set weekly budgets and want to know whether to buy or sell certain cards.

The people who use the output are the same as the decision makers. They are the active retail collectors and investors. They run the card screener every week to decide which Prismatic Evolutions cards to focus on.

The timing for the active retail collectors and investors deciding and using the output is weekly after TCGCSV updates (around 8 PM EST daily). They review the output before deciding what to buy, sell, or trade for the week.

## Useful Answer & Decision

The tool would be predictive and descriptive. The tool would use each card's daily price history (e.g., last 14 days) and predict whether that card should have a buy, sell, or hold rating using features like rolling returns and the price distance from the median price in the Prismatic Evolutions set. The tool could also predict the next week's percentage price change and rank cards. Metrics the tool could use are classification accuracy, a confusion matrix, and regression mean absolute error on percentage price change. The tool could output a CSV file with the card's actual price, its predicted label, and its predicted percentage price. It could also rank cards (e.g., 10 top catds). The tool would allow the decision makers to decide which Prismatic Evolutions singles to buy, hold, or sell that week.

## Assumptions & Constraints

- TCGPlayer market prices via TCGCSV are reasonable estimates of prices for Pokemon card singles unlike eBay sold alone. The reason eBay sold alone is not reliable is its prices would drastically differ based on catd condition.
- Tne tool will only monitor one set (Prismatic Evolutions) for this project. It will focus on predicting the buy, hold. or sell rating of catds, percentage changes, and card rankings.
- For active retail collectors and investors, daily prices are enough, and there is no need to capture intraday prices. This should involve a time series per card.
- There are several weeks of stored daily price data per card in order to train and backtest (TCGCSV has a data archive available from around 2024),
- The tool only uses simple models like logistic regression and/or linear regression for this project instead of techniques like deep learning.
- The TCGCSV API and data are public and allowed for this project/homework.
- Cards below a minimum price like $2 are excluded to reduce noise from bulk cards that no one would invest in due to them being common.

## Known Unknowns / Risks

- TCGCSV endpoints or file structure may change suddenly.
- Cards where people are making trades at lower frequency may show unreliable pricing data, which could hurt the model.
- Pokemon prices are not stationary and constantly change due to things like hype, reprints, and grading.
- If there's a small sample size per card, there may be overfitting and the predictions might not hold outside of the data sampled.
- Card condition may need to be accounted for in future versions since people will offer the same card at different prices depending on condition.
- Past model signals do not guarantee returns.

## Lifecycle Mapping

- Define problem framing and scoping as well as stakeholder goals → Problem Framing & Scoping (Stage 01) → This README and stakeholder memo
- Create a reproducible environment → Tooling Setup (Stage 02) → `project/` scaffold, `.env`, `src/config.py`
- Explore price data and features → Python Fundamentals (Stage 03) → Summary of statistics, rolling returns, groupby by rarity, CSV
- Ingest and accumulate daily history → Data Acquisition (Stage 04) → Timestamped raw CSV per pull from TCGCSV and scraped set metadata
- Save and reload the price dataset for every card by dates of prices → Data Storage (Stage 05) → timestamped CSV snapshots in `data/raw/`, Parquet file in `data/processed/`, check that data matches
- Train/evaluate classification and regression models → Later stages in `model/` and `notebooks/` → Buy/Hold/Sell predictions and expected percentage change output

## Repo Plan

`data/`, `src/`, `notebooks/`, `docs/`, `model/` under `project/`; update when we go over each lifecycle stage in the bootcamp (either daily or weekly). I will put my homework submissions in `homework/homeworkNumber/`.
