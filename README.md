# Week 12 Demo: Time Series Analysis & Forecasting

Interactive Jupyter notebook walking through stationarity, ACF/PACF, ADF testing, AR model fitting, and 12-month forecasting using real REIT return data.

## How to Run

```bash
# From the Week 12 folder root
pip install -r requirements.txt
jupyter notebook time_series_demo.ipynb
```

Run cells top-to-bottom. Each section builds on the previous one.

## Notebook Sections

| Section | Topic | Figure |
|:--------|:------|:-------|
| 1 | Setup and Data Loading | — |
| 2 | What Is a Time Series? | `fig01_returns_history.png` |
| 3 | Stationarity — The Core Concept | `fig02_returns_vs_price_index.png`, `fig03_stationarity_examples.png` |
| 4 | Autocorrelation Functions (ACF and PACF) | `fig04_acf_pacf_returns.png` |
| 5 | The Augmented Dickey-Fuller (ADF) Test | — |
| 6 | AR Model Selection and Estimation | — |
| 7 | Residual Diagnostics | `fig05_residual_diagnostics.png` |
| 8 | 12-Month Forecast | `fig06_forecast.png` |
| 9 | What Can We Actually Forecast? | — |
| 10 | Factor ACF Comparison (REIT vs. Momentum) | `fig07_acf_comparison.png` |
| 11 | Summary and Key Takeaways | — |

## Data

- **File:** `data/factors_master_long_only.csv`
- **Primary series:** `vwtret` — REIT value-weighted monthly return (Dec 1986–Jan 2026, 456 obs)
- **Source:** CRSP/Compustat via WRDS

## Figures

All 7 figures are saved as individual PNGs in this folder. They are also used in `Week-12-Slides.pptx`.

| File | Description |
|:-----|:------------|
| `fig01_returns_history.png` | Full history of REIT monthly returns |
| `fig02_returns_vs_price_index.png` | Price level vs. returns — why we use returns |
| `fig03_stationarity_examples.png` | 2×2 grid: stationary vs. non-stationary series |
| `fig04_acf_pacf_returns.png` | ACF and PACF diagnostic plots for `vwtret` |
| `fig05_residual_diagnostics.png` | Residual checks after AR model fit |
| `fig06_forecast.png` | 12-month AR forecast with widening confidence intervals |
| `fig07_acf_comparison.png` | ACF comparison: REIT returns vs. momentum factor |
