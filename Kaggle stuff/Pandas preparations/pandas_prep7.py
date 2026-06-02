import pandas as pd

reviews = pd.read_csv('Datasets/winemag-data_first150k.csv', index_col=0)

# print(reviews)
# reviews = reviews.rename(columns={'winery':'Vino'})

reviews = reviews.rename(index={0: 'first_row'})
print(reviews)