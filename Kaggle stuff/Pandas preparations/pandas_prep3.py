import pandas as pd

reviews = pd.read_csv("Datasets/winemag-data_first150k.csv", index_col=0)
# print(int(reviews['points'].describe()['mean']))
# print(reviews['country'].unique())
# print(reviews['country'].value_counts())

# review_points_mean = reviews['points'].mean()
# print(reviews['points'].map(lambda p: p - review_points_mean))

# print(reviews['country'].map(lambda p: p + ' - ' + reviews['region_1']))

# reviews['country_region'] = reviews.apply(lambda row: f"{row['country']} - {row['region_1']}", axis=1)
# print(reviews['country_region'])

# reviews_per_country = reviews['country'].value_counts().toS
# print(reviews_per_country)

# centered_price = reviews.apply(lambda row: reviews['price'] - reviews['price'].mean()).loc[:, 'price']
# print(centered_price)

# ratio = reviews['points'] / reviews['price']
# # print(reviews['ratio'])
# # print(reviews['ratio'].idxmax())
# print(reviews.loc[int(ratio.idxmax()), 'winery'])

# descriptor_counts = pd.Series({'fruity': reviews['description'].value_counts()})
# print(descriptor_counts)

# fruity = reviews['description'].map(lambda desc: "fruity" in desc).sum()
# tropical = reviews['description'].map(lambda desc: "tropical" in desc).sum()
#
# descriptor_counts = pd.Series([fruity, tropical], index=["fruity", "tropical"])
# print(descriptor_counts)

# # Count how many descriptions contain "tropical"
# n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
#
# # Count how many descriptions contain "fruity"
# n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
#
# # Create the Series
# descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
# print(descriptor_counts)

# star1 = reviews['points'].apply(lambda points: points < 80).sum()
# star2 = reviews['points'].apply(lambda points: 80 <= points < 95).sum()
# star3 = reviews['points'].apply(lambda points: points < 80 or reviews.loc[reviews['points']==points, 'country'] == 'Canada').sum()
# star_ratings = pd.Series([star1, star2, star3], index=['1-star', '2-star', '3-star'])

# star_ratings = reviews.apply(lambda row: 3 if row['country'] == 'Canada' or row['points'] >= 95 else (2 if row['points'] >= 85 else 1), axis=1)