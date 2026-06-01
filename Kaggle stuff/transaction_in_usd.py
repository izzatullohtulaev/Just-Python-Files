import pandas as pd

transactions = pd.read_csv('Datasets/transactions.csv', index_col=0)
# print(transactions.head())

print(transactions.dtypes)