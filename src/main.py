from extract import extract_data
from transform import transform_data
from load import load_data


def main() -> None:
    daily_df, historical_df = extract_data()
    final_df = transform_data(daily_df, historical_df)
    load_data(final_df)


if __name__ == "__main__":
    main()
