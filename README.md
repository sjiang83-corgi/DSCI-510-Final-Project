# Top 15 Playoff Scorers per 48 Minutes (2024 NBA Playoffs)

## Team Members
- Shanglin Jiang  
  Email: sjiang83@usc.edu  
  USC ID: 1967702034  


- Yufan Yao  
  Email: yufanyao@usc.edu  
  USC ID: 1450125536  




## Project Overview
This project analyzes scoring efficiency in the 2024 NBA Playoffs using points per 48 minutes as a standardized metric. 
By adjusting scoring output for playing time, the project compares players with different roles and minute allocations and highlights differences between efficiency-based and volume-based scoring.

## Data
The data were collected from Basketball-Reference and include per-game player statistics from the 2024 NBA Playoffs.  
For reproducibility, both the original scraped data and the cleaned datasets are stored locally.

- `data/raw/`: original scraped data  
- `data/processed/`: cleaned and structured data used for analysis and visualization  

## Project Structure
```text
project/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── nba_playoffs_per_game_2019.csv
│   │   ├── nba_playoffs_per_game_2020.csv
│   │   ├── nba_playoffs_per_game_2021.csv
│   │   ├── nba_playoffs_per_game_2022.csv
│   │   ├── nba_playoffs_per_game_2023.csv
│   │   └── nba_playoffs_per_game_2024.csv
│   └── processed/
│       ├── nba_playoffs_clean_2019.csv
│       ├── nba_playoffs_clean_2020.csv
│       ├── nba_playoffs_clean_2021.csv
│       ├── nba_playoffs_clean_2022.csv
│       ├── nba_playoffs_clean_2023.csv
│       ├── nba_playoffs_clean_2024.csv
│       └── nba_playoffs_clean_all_seasons.csv
├── final_project.ipynb
├── Project_proposal.pdf
├── results/
│   └── final_report.pdf
└── src/
    ├── clean_data.py
    ├── get_data.py
    ├── run_analysis.py
    ├── utils/
    └── visualize_results.py
```

## Virtual Environment Setup
python -m venv venv
source venv/bin/activate

## How to Run
1. Install the required dependencies:
   pip install -r requirements.txt
2. Run the data pipeline scripts:

   Data collection:
   python src/get_data.py

   Data cleaning:
   python src/clean_data.py

   Data analysis:
   python src/run_analysis.py

   Visualization:
   python src/visualize_results.py

3. (Optional) Open and run `final_project.ipynb` using Jupyter Notebook to reproduce visualizations.

## Dependencies
All external libraries required to run the project are listed in `requirements.txt`.
