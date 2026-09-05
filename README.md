# Analyse_Ventes_JV

A data analysis project exploring video game sales data across regions, genres, and years, using the "Video Game Sales" dataset from Kaggle (16,500+ games). Built as a learning exercise in data cleaning and aggregation with pandas.

## Data Source

This project uses the [Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales) 
dataset from Kaggle, licensed under CC0 (Public Domain). The data can be freely 
used, modified, and redistributed without restriction.

## Analyses

The script performs the following analyses:

- **Top 10 best-selling games** — ranked by global sales
- **Sales by genre** — total global sales aggregated per genre
- **Sales by year** — evolution of global sales over time
- **Sales by region and genre** — comparison of NA/EU/JP sales across genres

## Known Data Limitations

- The dataset appears to stop being reliably updated after 2016. The number of 
  games recorded drops sharply from 2016 onward (e.g. 344 games in 2016 vs. 
  only 3 in 2017), which causes the apparent decline in total sales for recent 
  years in the `sales_by_year` analysis. This should be read as incomplete 
  data collection, not an actual market decline.
- Some rows have missing `Publisher` values, replaced with `"Unknown"`.
- Some rows have missing `Year` values, left as `NaN` and automatically 
  excluded from year-based aggregations.

## Installation

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
4. Install dependencies: `pip install -r requirements.txt`

## Usage

Run the script: python main.py


Results are saved as CSV files in the `output/` folder.

## Tests

Run the test suite with: pytest
