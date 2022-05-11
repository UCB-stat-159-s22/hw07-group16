# Analysis of Taxi Trip Data in NYC
This repository contains all the data and notebooks for data cleaning and analysis needed to obtain the conclusions made regarding taxi trips in NYC.

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

## Makefile
The following are available make commands:
- `env`: Creates the environment and configures it by activating it and installing ipykernel into it
- `remove-env`: Removes the configured environment
- `data/taxi_clean.csv`: Create the cleaned taxi_tripdata.csv
- `clean`: Remove all figures from the /figures and /tables directory
- `all`: Create all figures and tables from the notebooks
