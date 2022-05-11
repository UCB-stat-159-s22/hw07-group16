import pandas as pd
import numpy as np
from taxitools import utils as ut
import os
from os.path import exists

def test_filter_data():
    df = ut.open_taxi_clean_df()
    df_1 = df.loc[df['passenger_count'] == 1]
    df_2 = df_1.loc[(df['fare_amount'] >= 10) & (df['fare_amount'] < 45)]
    df_3 = df_2.loc[df['total_amount'] < 100]
    df_4 = df_3.loc[df['payment_type'] == 2]
    df_5 = df_4.dropna()
    dic1 = {'passenger_count':1, 'payment_type':2}
    dic2 = {'fare_amount':[10,45], 'total_amount':['-inf',100]}
    df_auto = ut.filter_data(df, dic1, dic2)
    assert df_auto.shape == df_5.shape
    assert all(df_auto.iloc[4] == df_5.iloc[4]) == True

def test_aggregateAndGroup():
	#aggregateAndGroup(df, groupCol, aggCol, func, reset_index = False)
	df = ut.open_taxi_clean_df()
	test = ut.aggregateAndGroup(df, 'day_of_week', 'trip_duration', 'mean', True)
	assert len(test) == 7
	assert 'day_of_week' in test.columns
	assert 'trip_duration' in test.columns

def test_aggregateAndGroupMultiple():
	df = ut.open_taxi_clean_df()
	agg_dict = {'trip_duration': 'mean', 'fare_amount': 'max'}
	test = ut.aggregateAndGroupMultiple(df, 'day_of_month', agg_dict)
	assert len(columns) == 3
	assert len(test) == 31
	assert 'day_of_month' in test.columns
	assert 'trip_duration' in test.columns
	assert 'fare_amount' in test.columns
	
def test_open_taxi_clean_df():
	df = ut.open_taxi_clean_df()
	assert len(df.columns) == 25
	assert len(df) == 79970
	assert str(df_add.VendorID.dtype) == 'Int64'
	
def test_merge_location_data():
	df = ut.open_taxi_clean_df()
	test = ut.merge_location_data(df[['PULocationID']], 'PULocationID', {'the_geom':'PUGeom', 'zone': 'PUZone', 'borough': 'PUBorough'})
	assert len(test.columns) == 4
	assert 'PULocationID' in test.columns
	assert 'PUGeom' in test.columns
	assert 'PUZone' in test.columns
	assert 'PUBorough' in test.columns

def test_plot_heatmap():
	df = ut.open_taxi_clean_df()
	test = ut.aggregateAndGroup(df_add, 'PULocationID', 'fare_per_mile', 'mean', True)
	test_geom = ut.merge_location_data(test, 'PULocationID')
	ut.plot_heatmap(test_geom, 'the_geom', 'fare_per_mile', 'Test Figure', 'test_file', 70)
	assert(exists('figures/test_file.png'))
	os.remove('figures/test_file.png')