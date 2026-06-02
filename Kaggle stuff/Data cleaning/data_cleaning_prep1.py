import pandas as pd
import numpy as np

# nfl_data = pd.read_csv('Datasets/NFL Play by Play 2009-2016 (v3).csv')
#
# # print(nfl_data.head())
#
# # np.random.seed(0)
#
# missing_values_count = nfl_data.isnull().sum()
# # print(missing_values_count.to_string())
#
# # print(nfl_data.dtypes.to_string())
#
# total_cells = nfl_data.shape[:]
# total_cells = total_cells[0]*total_cells[1]
# total_missing = missing_values_count.sum()
# missing_percentage = total_missing/total_cells*100
#
# print(nfl_data['PenalizedTeam'].isnull().sum())

sf_permits = pd.read_csv('Datasets/Building_Permits.csv') # you can download the file from https://shorturl.at/VC7U1 😊

# 1
# total_cells = sf_permits.shape[0]*sf_permits.shape[1]
# missing_cells = sf_permits.isnull().sum().sum()
# percent_missing = missing_cells/total_cells*100
# print(total_cells)
# print(missing_cells)
# print(percent_missing)

# print(sf_permits['Zipcode'].isnull().sum())


# 4
# without_missing = sf_permits.dropna()
# print(without_missing)

# # 5
# sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
# print(len(sf_permits.dtypes))
# print(len(sf_permits_with_na_dropped.iloc[0, :]))

# 6
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)








