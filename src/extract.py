from io import BytesIO
from zipfile import ZipFile
from typing import Tuple

import pandas as pd
import requests


DAILY_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
HIST_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"


def _download_zip(url: str) -> pd.DataFrame:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with ZipFile(BytesIO(response.content)) as zf:
        file_name = zf.namelist()[0]
        with zf.open(file_name) as file:
            df = pd.read_csv(file)

    return df


def extract_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    daily_df = _download_zip(DAILY_URL)
    historical_df = _download_zip(HIST_URL)
    return daily_df, historical_df
