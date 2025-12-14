import pandas as pd

PROCESSED_PATH: str = "data/processed/nba_playoffs_clean_all_seasons.csv"


def analyze_basic_summary() -> pd.DataFrame:
    """
    Analyze average playoff scoring efficiency by season.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing average points per 48 minutes
        for each season.
    """
    df: pd.DataFrame = pd.read_csv(PROCESSED_PATH)

    summary: pd.DataFrame = (
        df.groupby("Season")["PTS_per_48"]
          .mean()
          .reset_index(name="Avg_PTS_per_48")
    )
    return summary


if __name__ == "__main__":
    print(analyze_basic_summary())
