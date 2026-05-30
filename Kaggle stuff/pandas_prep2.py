import pandas as pd
# games = pd.read_csv("Datasets/games.csv", index_col="winner")
# pd.set_option('display.max_rows', 5)
# print(games['black_id'][5])
# print(games.iloc[0, 6])
# print(games.iloc[-1:])
# print(games.iloc[0:10])
# games.set_index('winner', inplace=True)
# print(games.head())

reviews = pd.read_csv("Datasets/winemag-data_first150k.csv", index_col=0)
# print(reviews.loc[(reviews['country'] == 'Italy') | (reviews['country'] == 'France'), ['country', 'points', 'winery']].to_string())
# print(reviews.loc[reviews['price'].isnull(), ['country', 'price', 'winery']].to_string())
desc = reviews.iloc[:, ['description']]