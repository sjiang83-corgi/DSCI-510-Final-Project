from __future__ import annotations

from typing import List
import pandas as pd
import matplotlib.pyplot as plt

from run_analysis import run_analysis, get_top_minutes_dependent, get_top_underutilized


def plot_top_scorers_single_season(df: pd.DataFrame, season: int = 2024, top_n: int = 10) -> None:
    """
    Plot top scorers for a single season using Total_PTS if available,
    otherwise fallback to PTS_per_48.
    """
    d = df[df["Season"] == season].copy()
    metric = "Total_PTS" if "Total_PTS" in d.columns else "PTS_per_48"
    d = d.dropna(subset=[metric]).sort_values(metric, ascending=False).head(top_n)

    plt.figure()
    plt.barh(d["Player"], d[metric])
    plt.gca().invert_yaxis()
    plt.xlabel(metric)
    plt.title(f"Top {top_n} Players by {metric} (Season {season})")
    plt.tight_layout()
    plt.show()


def plot_mp_vs_p48_scatter(df: pd.DataFrame, season: int = 2024) -> None:
    """
    Scatter plot of minutes played per game (MP) vs points per 48 (PTS_per_48).
    """
    d = df[df["Season"] == season].dropna(subset=["MP", "PTS_per_48"]).copy()

    plt.figure()
    plt.scatter(d["MP"], d["PTS_per_48"])
    plt.xlabel("Minutes Per Game (MP)")
    plt.ylabel("Points per 48 Minutes (PTS_per_48)")
    plt.title(f"MP vs PTS_per_48 (Season {season})")
    plt.tight_layout()
    plt.show()


def plot_top_p48_across_seasons(df: pd.DataFrame, top_n: int = 10) -> None:
    """
    Plot top PTS_per_48 performances across all seasons (player-season rows).
    """
    d = df.dropna(subset=["PTS_per_48"]).copy()
    d["PlayerSeason"] = d["Player"].astype(str) + " (" + d["Season"].astype(str) + ")"
    d = d.sort_values("PTS_per_48", ascending=False).head(top_n)

    plt.figure()
    plt.barh(d["PlayerSeason"], d["PTS_per_48"])
    plt.gca().invert_yaxis()
    plt.xlabel("PTS_per_48")
    plt.title(f"Top {top_n} PTS_per_48 Across Seasons")
    plt.tight_layout()
    plt.show()


def main(seasons: List[int]) -> None:
    """
    Run the end-to-end analysis outputs requested and generate final visualizations.
    Tables for minutes-dependent and underutilized players are computed
    across ALL selected seasons (not season-specific).
    """
    _, categorized_df = run_analysis(seasons)

    # Usage distribution
    print(categorized_df["UsageType"].value_counts())

    # Visualizations (still show example season for plots)
    plot_top_scorers_single_season(categorized_df, season=2024)
    plot_mp_vs_p48_scatter(categorized_df, season=2024)
    plot_top_p48_across_seasons(categorized_df)

    # Tables across ALL seasons
    print("\nTop minutes-dependent players (all seasons):")
    print(get_top_minutes_dependent(categorized_df).to_string(index=False))

    print("\nTop underutilized players (all seasons):")
    print(get_top_underutilized(categorized_df).to_string(index=False))


if __name__ == "__main__":
    SEASONS = [2019, 2020, 2021, 2022, 2023, 2024]
    main(SEASONS)
