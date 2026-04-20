from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


ROOT = Path(__file__).resolve().parent
INPUT_FILE = ROOT / "sp500.txt"
OUTPUT_FILE = ROOT / "results" / "sp500_plot.png"


def load_sp500_data(file_path: Path) -> pd.DataFrame:
    data = pd.read_csv(file_path, sep="\t")
    data.columns = data.columns.str.strip()

    numeric_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column].astype(str).str.replace(",", "", regex=False))

    data["Date"] = pd.to_datetime(data["Date"], format="%b %d, %Y")
    data = data.sort_values("Date").reset_index(drop=True)
    data["Period Return"] = data["Close"].pct_change()
    data["Close Difference"] = data["Close"].diff()
    return data


def make_plot(data: pd.DataFrame, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    plot_data = data.dropna(subset=["Period Return"])
    returns = plot_data["Period Return"]
    max_lags = min(40, max(1, len(returns) // 2 - 1))

    fig, axes = plt.subplots(3, 1, figsize=(12, 12), constrained_layout=True)

    axes[0].plot(plot_data["Date"], returns * 100, color="#1f4e79", linewidth=1.8)
    axes[0].axhline(0, color="black", linewidth=1, alpha=0.7)
    axes[0].set_title("S&P 500 One-Period Return")
    axes[0].set_ylabel("Percent")
    axes[0].set_xlabel("Date")
    axes[0].grid(alpha=0.3)

    plot_acf(returns, lags=max_lags, ax=axes[1])
    axes[1].set_title("Autocorrelation Function (ACF)")
    axes[1].set_xlabel("Lag")
    axes[1].set_ylabel("Correlation")
    axes[1].grid(alpha=0.3)

    plot_pacf(returns, lags=max_lags, ax=axes[2], method="ywm")
    axes[2].set_title("Partial Autocorrelation Function (PACF)")
    axes[2].set_xlabel("Lag")
    axes[2].set_ylabel("Correlation")
    axes[2].grid(alpha=0.3)

    fig.savefig(output_file, dpi=200)
    plt.close(fig)


def main() -> None:
    data = load_sp500_data(INPUT_FILE)
    make_plot(data, OUTPUT_FILE)
    print(f"Saved plot to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()