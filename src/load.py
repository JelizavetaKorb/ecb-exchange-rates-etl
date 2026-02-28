import pandas as pd


def load_data(df: pd.DataFrame, output_path: str = "exchange_rates.md") -> None:
    df.to_markdown(output_path, index=False)
