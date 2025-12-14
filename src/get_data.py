import os
from typing import List
import pandas as pd

RAW_DIR: str = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)


def fetch_playoff_per_game(season: int) -> pd.DataFrame:
    """
    Parameters
    ----------
    season : int
        NBA season year (e.g., 2023 for the 2022–23 playoffs).

    Returns
    -------
    pd.DataFrame
        Raw per-game playoff statistics for the given season.
    """
    url: str = f"https://www.basketball-reference.com/playoffs/NBA_{season}_per_game.html"
    print(f"Fetching data for season {season}...")

    tables: List[pd.DataFrame] = pd.read_html(url)
    df: pd.DataFrame = tables[0]

    raw_path: str = os.path.join(
        RAW_DIR, f"nba_playoffs_per_game_{season}_raw.csv"
    )
    df.to_csv(raw_path, index=False)

    df["Season"] = season
    return df


def download_all_seasons(seasons: List[int]) -> None:
    """
    Parameters
    ----------
    seasons : List[int]
        A list of NBA season years.
    """
    for season in seasons:
        fetch_playoff_per_game(season)


if __name__ == "__main__":
    SEASONS: List[int] = [2019, 2020, 2021, 2022, 2023, 2024]
    download_all_seasons(SEASONS)
