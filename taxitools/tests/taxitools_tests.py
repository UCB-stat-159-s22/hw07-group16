import pandas as pd
import numpy as np
from taxitools import utils as ut
from os.path import exists

def filter_data_test():
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

