# Analysis of Taxi Trip Data in NYC

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw07-group16/HEAD?labpath=main.ipynb )

This repository contains all the data and notebooks for data cleaning and analysis needed to obtain the conclusions made regarding taxi trips in NYC. Traveling by taxi is one of the most popular modes of transportation in NYC, with over 80,000 trips in the month of July 2021 alone, according to the provided dataset. Because of this, we wanted to analyze some of this data to get a better understanding of fares and other aspects of taxi trips within NYC. The main notebook contains a summary of all our findings regarding fares vs. different metrics of time, tip analysis, a tip prediciton model, and fares and trips vs. location of taxi zones.

## Data
The data used in this analysis can be found at the following links:
- https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc
- https://data.cityofnewyork.us/Transportation/NYC-Taxi-Zones/d3c5-ddgc

taxi_clean.csv contains additional columns from the taxi_tripdata.csv:
- `day_of_week`: Day of the week the trip took place, with 0=Monday and 6=Sunday
- `day_of_month`: Day of the month the trip took place
- `hour_of_day`: Hour of the day the trip started
- `trip_duration`: Duration of the entire trip in seconds
- `total_without_tip`: Total cost of the trip not including tip
- `fare_per_mile`: Dollar cost of the trip per mile (not including tip cost)

For more information regarding the columns in the taxi trips dataset see: https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

## Installation
To run the code in this repo, either use the provided Binder link (which will set up the environment necessary for analysis), or clone this git repository and do the following:
1. Configure the environment by running `make env` and activate this environment by running `conda activate hw7env`. Doing this will also install the taxitools package.
2. If you'd like to manually install or uninstall the taxitools package, run `pip install .` and `pip uninstall taxitools` respectively in the root directory of this repo.
3. Execute notebooks manually or run `make all` to run all the notebooks (excluding the taxi_clean.ipynb data cleaning notebook). Running `make clean` will clean all the figures and tables produced by the notebooks. 

**Note:** while there isn't a required order of execution for the analysis notebooks, all the figures from the analysis notebooks should exist before attempting to manually execute main.ipynb (All figures currently exist, but may be removed by calling `make clean`).

## Makefile
The following are available make commands:
- `env`: Creates the environment and configures it by activating it and installing ipykernel into it
- `remove-env`: Removes the configured environment
- `data/taxi_clean.csv`: Create the cleaned taxi_tripdata.csv
- `clean`: Remove all figures from the /figures and /tables directory
- `all`: Create all figures and tables from the notebooks

## Testing
To run tests in the taxitools package, follow these steps:
1. Ensure that the proper environment is setup by running `make env`. If an old version of the environment is currently setup, or you would like to reconfigure the environment, run `conda activate` on a different environment and run `make remove-env` first.
2. After running `conda activate hw7env`, run `conda install -c anaconda pytest`.
3. If the taxitools package is not yet installed, manually run `pip install .` inside of the root directory (hw07-group16).
4. Run `pytest taxitools`.
