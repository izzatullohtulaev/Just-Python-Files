# Transaction Date                  str
# No Of Withdrawals               int64
# No Of XYZ Card Withdrawals      int64
# No Of Other Card Withdrawals    int64
# Total amount Withdrawn          int64
# Amount withdrawn XYZ Card       int64
# Amount withdrawn Other Card     int64
# Weekday                           str
# Festival Religion                 str
# Working Day                       str
# Holiday Sequence                  str

import pandas as pd

transactions = pd.read_csv('Datasets/transactions.csv', index_col=0)
# print(transactions.count())

# print(transactions.dtypes)
# print(transactions.iloc[0:3, 4])
# print("\nThe column changed!\n")
# transactions['Total amount Withdrawn'] *= 0.0214
# print(transactions.iloc[0:3, 4])

# print(transactions.iloc[:, 4])
# print("\nThe column changed!\n")

transactions = transactions.astype({'Total amount Withdrawn': 'float64', 'Amount withdrawn XYZ Card': 'float64', 'Amount withdrawn Other Card': 'float64'})

for i in range(0, int(transactions.count()['Transaction Date'])):
    if '2011' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0214
        transactions.iloc[i, 5] *= 0.0214
        transactions.iloc[i, 6] *= 0.0214
    elif '2012' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0187
        transactions.iloc[i, 5] *= 0.0187
        transactions.iloc[i, 6] *= 0.0187
    elif '2013' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0177
        transactions.iloc[i, 5] *= 0.0177
        transactions.iloc[i, 6] *= 0.0177
    elif '2014' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0160
        transactions.iloc[i, 5] *= 0.0160
        transactions.iloc[i, 6] *= 0.0160
    elif '2015' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0159
        transactions.iloc[i, 5] *= 0.0159
        transactions.iloc[i, 6] *= 0.0159
    elif '2016' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0149
        transactions.iloc[i, 5] *= 0.0149
        transactions.iloc[i, 6] *= 0.0149
    elif '2017' in transactions.iloc[i, 0]:
        transactions.iloc[i, 4] *= 0.0154
        transactions.iloc[i, 5] *= 0.0154
        transactions.iloc[i, 6] *= 0.0154

print(transactions.iloc[:, 4])

# transactions.to_csv('Datasets/transactions_in_usd.csv')