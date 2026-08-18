# Stage 06 — Data Preprocessing

Reusable cleaning functions on the sample dataset in `data/raw/`.

## Cleaning Strategy

I fill `age`, `income`, and `score` with each column's median so a few missing numbers do not resulyt in my code dropping the entire column. Median fill assumes those gaps are not systematically biased due to the MCAR or MAR described in lecture.

I drop columns whose NA share is above 0.5. This removes `extra data` which is 50% or more empty. In doing so, I assume that column is not needed for later work.

I min-max scale `age`, `income`, and `score` to [0, 1] so that the columns share a range. When I min-max scale, I assume the observed min and max are representative.

In `src/cleaning.py`, I put helper functions that I added: `fill_missing_median`, `drop_missing`, and `normalize_data`. The data that I cleaned is in `data/processed/sample_data_cleaned.csv`.
