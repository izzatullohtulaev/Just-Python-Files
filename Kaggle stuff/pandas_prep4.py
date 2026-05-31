import pandas as pd

reviews = pd.read_csv("Datasets/winemag-data_first150k.csv", index_col=0)
print(reviews['winery'].value_counts().idxmax())