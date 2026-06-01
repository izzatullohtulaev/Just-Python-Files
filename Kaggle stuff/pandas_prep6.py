import pandas as pd

reviews = pd.read_csv("Datasets/winemag-data_first150k.csv", index_col=0)
# print(reviews.head())

# print(reviews.dtypes)

# print(reviews['price'].fillna(0).astype(int).to_string())

# prices = reviews['price'].fillna(0).astype(int)
# print(prices.sort_values(ascending=1).to_string())

# print(reviews.index.dtype)

# n_missing_prices = reviews[reviews.price.isnull()].sum
# n_missing_prices = len(reviews[reviews.price.isnull()])
# print(n_missing_prices)

reviews['region_1'] = reviews['region_1'].fillna('Unknown')
reviews_per_region = reviews.groupby('region_1').agg('count')['winery'].sort_values(ascending=False)
reviews_per_region.name = 'region_1'
print(reviews_per_region)

# print(reviews.loc[:, 'region_1'].to_string())
# print(reviews_per_region.to_string())

