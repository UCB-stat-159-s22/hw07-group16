import pandas as pd
import numpy as np
import geopandas as gpd
from shapely import wkt
from os.path import exists
import contextily as cx
import matplotlib.pyplot as plt

def aggregateAndGroup(df, groupCol, aggCol, func, reset_index = False):
	''' Group the data in df by groupCol and then aggregate the data in 
        aggCol using the function func. Func is expected to be a valid 
        function (string) that can be used to aggregate data. If groupCol
        or aggCol do not exist in the dataframe df, returns None. '''
	if groupCol not in df.columns or (aggCol is not None and aggCol not in df.columns):
		return None
	
	if aggCol is not None:
		df_change = df[[groupCol, aggCol]]
	else:
		df_change = df.copy()
	df_grouped = df_change.groupby(groupCol).agg(func)
	if func == 'size':
		return pd.DataFrame(df_grouped).reset_index().rename({0: 'Count'}, axis=1)
	if reset_index:
		return df_grouped.reset_index()
	return df_grouped

def aggregateAndGroupMultiple(df, groupCol, aggDict):
	''' Group the data in df by groupCol and then aggregate multiple
		columns of data based on the given functions in aggDict. If any of
		the given columns aren't valid for the dataframe df, return None. '''
	if type(groupCol) == str and groupCol not in df.columns:
		return None
	for col in aggDict.keys():
		if col not in df.columns:
			return None
	if type(groupCol) == str:
		all_columns = [groupCol] + list(aggDict.keys())
	else:
		all_columns = groupCol + list(aggDict.keys())
	df_columns = df[all_columns]
	df_grouped = df_columns.groupby(groupCol).agg(aggDict)
	return df_grouped.reset_index()

def open_taxi_clean_df():
	''' Opens the taxi_clean csv and taking care of mixed types and
		date parsing. '''
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

def merge_location_data(df, id_col, rename_dict = None):
	''' Add location data by joining on the id_col in df. Optionally can rename columns
		in df by providing a dictionary with the following column keys: 'the_geom', 'zone',
		and 'borough' '''
	if id_col not in df.columns:
		return 'Error: please check all columns exist in the dataframe'
	
	taxi_zones = pd.read_csv('data/taxi_zones.csv')
	taxi_zones_less = taxi_zones[['the_geom', 'LocationID', 'zone', 'borough']]
	#pickup_dict = {'the_geom':'PUGeom', 'zone': 'PUZone', 'borough': 'PUBorough'}
	#dropoff_dict = {'the_geom':'DOGeom', 'zone': 'DOZone', 'borough': 'DOBorough'}
	taxi_geom = df.merge(right=taxi_zones_less, left_on=id_col, right_on='LocationID').drop(
    'LocationID', axis=1)
	if rename_dict:
		taxi_geom = taxi_geom.rename(rename_dict, axis='columns')
	return taxi_geom

def plot_heatmap(df, geom_col, data_col, title, file, vmax=None):
	''' Plots a heatmap using data from df, with geom_col containing the
		geometry and data_col being the data ploted. The figure is given
		the provided title and saved into a file with the specified name. '''
	if geom_col not in df.columns or data_col not in df.columns:
		return 'Error: please check all columns exist in the dataframe'
	
	df_temp = df.rename({geom_col: 'geom'}, axis=1)
	df_temp['geom'] = df_temp['geom'].apply(wkt.loads)
	
	df_geo = gpd.GeoDataFrame(data=df_temp, geometry="geom", crs=3857)
	ax = df_geo.plot(column=data_col, figsize=(15, 15), legend=True, alpha=.7, vmax=vmax)
	ax.set_title(title)
	cx.add_basemap(ax, zoom=12);
	plt.savefig('figures/' + file)
