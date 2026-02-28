import pandas as pd

CURRENCIES = ["USD", "SEK", "GBP", "JPY"]

def transform_data(daily_df: pd.DataFrame, historical_df: pd.DataFrame) -> pd.DataFrame:
    daily_df.columns = daily_df.columns.str.strip()
    historical_df.columns = historical_df.columns.str.strip()

    date_col_daily = daily_df.columns[0]
    date_col_hist = historical_df.columns[0]
    daily_df[date_col_daily] = pd.to_datetime(daily_df[date_col_daily])
    historical_df[date_col_hist] = pd.to_datetime(historical_df[date_col_hist])

    latest_row = daily_df.iloc[0]

    available_currencies = [
        c for c in CURRENCIES
        if c in daily_df.columns and c in historical_df.columns
    ]

    if not available_currencies:
        print("Columns in daily CSV:", list(daily_df.columns))
        print("Columns in historical CSV:", list(historical_df.columns))
        raise ValueError("No matching currencies found in ECB data")

    rows = []
    for c in available_currencies:
        rate = round(float(latest_row[c]), 4)
        mean_rate = round(float(pd.to_numeric(historical_df[c], errors='coerce').mean()), 4)
        rows.append({"Currency Code": c, "Rate": rate, "Mean Historical Rate": mean_rate})

    return pd.DataFrame(rows)
