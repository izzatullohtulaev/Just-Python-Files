import pandas as pd

reviews = pd.read_csv("Datasets/winemag-data_first150k.csv", index_col=0)

# print(reviews['country'].value_counts())
# print(reviews.groupby("price").price.count()[reviews.groupby("price").price.count().idxmax()])
# print(reviews.groupby('points').price.mean())
# print(reviews.groupby('winery').apply(lambda df: df['country'].iloc[-1]))
# print(reviews.groupby('winery').apply(lambda df: df['price'].mean()))
# print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))
# juanico_wines = reviews.loc[(reviews['country'] == 'Uruguay') & (reviews['province'] == 'Juanico')]
# juanico = reviews.loc[(reviews['country']=='Uruguay') & (reviews['province']=='Juanico'), ['country', 'province', 'winery', 'points', 'price']]
# print(juanico)

# countries_reviewed = reviews.groupby(['country', 'province'])['description'].agg([len]).to_string()
# print(countries_reviewed.index)


# countries_reviewed = reviews.groupby(['country', 'province'])['description'].agg(['count'])
# countries_reviewed = countries_reviewed.sort_values(by='count', ascending=False)
# print(countries_reviewed.to_string())

# authors_reviews = reviews.groupby("taster_twitter_handle")['description'].agg(['count'])
# reviews_written = authors_reviews.sort_values('count', ascending=False)
# reviews_written = pd.Series([reviews_written['count']])
# print(reviews_written.get(['count']))

# reviews_written = reviews.groupby("winery")['description'].agg('count')
# print(reviews_written)

# best_rating_per_price = reviews.groupby("price")['points'].max()
# print(type(best_rating_per_price))

# price_extremes = reviews.groupby('variety')['price'].agg(['min', 'max'])
# print(price_extremes)
# print(type(price_extremes))

# sorted_varieties = reviews.groupby('variety')['price'].agg(['min', 'max']).sort_values(by=['min', 'max'], ascending=False)
# print(sorted_varieties)

# reviewer_mean_ratings = reviews.groupby('variety')['points'].agg('mean')
# print(reviewer_mean_ratings)

# country_variety_counts = reviews.groupby(['country', 'variety'])['winery'].agg('count').sort_values(ascending=False)
# print(country_variety_counts)

# print(reviews['winery'].nunique())