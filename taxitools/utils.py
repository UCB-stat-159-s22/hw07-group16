import pandas as pd
import numpy as np
from os.path import exists

def aggregateAndGroup(df, groupCol, aggCol, func):
	''' Group the data in df by groupCol and then aggregate the data in 
		aggCol using the function func. Func is expected to be a valid 
		function (string) that can be used to aggregate data. If groupCol
		or aggCol do not exist in the dataframe df, returns None. '''
	
	if groupCol not in df.columns or aggCol not in df.columns:
		return None
	
	df_two_cols = df[[groupCol, aggCol]]
	df_grouped = df_two_cols.groupby(groupCol).agg(func)
	return df_grouped

def open_taxi_clean_df():
	err_msg = 'If cleaned dataset does not yet exist in the repo, run make data/taxi_clean.csv to produce the cleaned data.'
	assert exists('data/taxi_clean.csv'), err_msg
	dtypes = {'VendorID': 'Int64', 'store_and_fwd_flag': 'str', 'RatecodeID': 'Int64', 'passenger_count': 'Int64', 'payment_type': 'Int64', 'trip_type': 'Int64'}
	parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
	df = pd.read_csv('data/taxi_clean.csv', dtype=dtypes, parse_dates=parse_dates)
	return df