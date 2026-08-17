# Stakeholder Brief: Pokemon Set Screener

**Audience**: The audience are retail collectors and investors. The cadence for output/decisions made is weekly (after TCGCSV refresh around 8 PM EST). TCGCSV refreshes daily, but an average retail collector or investor is likely only need the tool once each week.

**Decsion Supported**: The decision the tool helps make is what Prismatic Evolutions singles to buy, hold, or sell during a week.

## Context

Pokemon TCG (trading card game) singles' prices on TCGPlayer move every day as more people grade new cards and more collectors join the hobby, leading to fluctuations in supply and demand. However, collectors tracking a full Pokemon set cannot easily tell which cards are unusually cheap or expensive compared to recent history when deciding what to sell or buy. Manually checking dozens of card prices is slow, and prices swing around reprints, hype, and graded-card supply. This tool stores daily price history from TCGCSV and applies time-series classification and regression to help active retail collectors and investors make Pokemon card investment decisions for the week.

## What You'll Receive (Output)

- A weekly ranked list of Prismatic Evolutions cards with a predicted decision label (buy/ hold/sell) and predicted percentage price change for that week based on every card's recent daily price history (e.g. last 14 days).
- A CSV with cards' actual prices, predicted labels, predicted percentage price change, and ranking (for the top 10 cards).
- Summary of outputs with the model type (e.g., logistic/linear regression), data source (TCGCSV/TCGPlayer), relevant output for the raw (not graded) single cards.
- Descriptive statistics (e.g., price difference from set median) alongside model outputs to comapre.

## Assumptions & Constraints

- TCGPlayer market prices via TCGCSV are reasonable estimates of prices for Pokemon card singles unlike eBay sold alone. The reason eBay sold alone is not reliable is its prices would drastically differ based on catd condition.
- Tne tool will only monitor one set (Prismatic Evolutions) for this project. It will focus on predicting the buy, hold. or sell rating of catds, percentage changes, and card rankings.
- For active retail collectors and investors, daily prices are enough, and there is no need to capture intraday prices. This should involve a time series per card.
- There are several weeks of stored daily price data per card in order to train and backtest (TCGCSV has a data archive available from around 2024),
- The tool only uses simple models like logistic regression and/or linear regression for this project instead of techniques like deep learning.
- The TCGCSV API and data are public and allowed for this project/homework.
- Cards below a minimum price like $2 are excluded to reduce noise from bulk cards that no one would invest in due to them being common.
