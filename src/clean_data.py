import os
from typing import List
import pandas as pd

RAW_DIR: str = "data/raw"
PROCESSED_DIR: str = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)


def clean_playoff_stats(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning steps include:
    - Removing repeated header rows
    - Converting numeric columns
    - Removing players with zero minutes
    - Computing total points and points per 48 minutes

    Parameters
    ----------
    raw_df : pd.DataFrame
        Raw playoff per-game statistics.

    Returns
    -------
    pd.DataFrame
        Cleaned playoff statistics with derived metrics.
    """
    df: pd.DataFrame = raw_df.copy()

    if "Rk" in df.columns:
        df = df[df["Rk"] != "Rk"]

    df = df[~df["Player"].isna()].copy()

    for col in ["G", "MP", "PTS"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df[df["MP"] > 0].copy()

    df["Total_PTS"] = df["PTS"] * df["G"]
    df["PTS_per_48"] = df["PTS"] * (48.0 / df["MP"])

    keep_cols: List[str] = [
        "Season", "Player", "Tm",
        "G", "MP", "PTS", "Total_PTS", "PTS_per_48"
    ]
    keep_cols = [c for c in keep_cols if c in df.columns]

    return df[keep_cols].reset_index(drop=True)


def clean_all_seasons(seasons: List[int]) -> None:
    """
    Parameters
    ----------
    seasons : List[int]
        A list of NBA season years.
    """
    all_cleaned: List[pd.DataFrame] = []

    for season in seasons:
        raw_path: str = os.path.join(
            RAW_DIR, f"nba_playoffs_per_game_{season}_raw.csv"
        )
        raw_df: pd.DataFrame = pd.read_csv(raw_path)

        clean_df: pd.DataFrame = clean_playoff_stats(raw_df)

        processed_path: str = os.path.join(
            PROCESSED_DIR, f"nba_playoffs_clean_{season}.csv"
        )
        clean_df.to_csv(processed_path, index=False)

        all_cleaned.append(clean_df)

    combined: pd.DataFrame = pd.concat(all_cleaned, ignore_index=True)
    combined.to_csv(
        os.path.join(PROCESSED_DIR, "nba_playoffs_clean_all_seasons.csv"),
        index=False
    )


if __name__ == "__main__":
    SEASONS: List[int] = [2019, 2020, 2021, 2022, 2023, 2024]
    clean_all_seasons(SEASONS)
