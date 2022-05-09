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

def filter_data(df, filter_specif, filter_range):
    ''' Filter df and remove null values. filter_specif and filter_range are dictionaries. 
        The keys are the column names in both dictionaries. 
        The values in filter_specif are what the values in the column should equal to
        The values in filter_range are 2 element lists. The first is the min range, and second is a max range
        If you want one sided filters, i.e. x >= 8, pass in [8, 'inf'], or ['-inf', 8] for x < 8
        If you only need specific values, pass in None for filter_range variable and vice versa'''
    
    if filter_specif is not None:
        for col in filter_specif:
            df = df.loc[df[col] == filter_specif[col]]
    if filter_range is not None:
        for col in filter_range:
            if filter_range[col][0] == '-inf':
                df = df.loc[df[col] < filter_range[col][1]]
            if filter_range[col][1] == 'inf':
                df = df.loc[df[col] >= filter_range[col][0]]
            if (filter_range[col][0] != '-inf') and (filter_range[col][1] != 'inf'):
                df = df.loc[(df[col] >= filter_range[col][0]) & (df[col] < filter_range[col][1])]
    df = df.dropna()
    return df