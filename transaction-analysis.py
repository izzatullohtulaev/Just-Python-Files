from itertools import count

from jupyter_server import gateway
from pandas.core.groupby import groupby

TXS = [
    {"id": "T01", "amount": 100000,  "gateway": "UzCard",     "merchant_id": "UZ-0001", "status": "ok",     "customer_age": 28},
    {"id": "T02", "amount": 250000,  "gateway": "UzCard",     "merchant_id": "UZ-0001", "status": "ok",     "customer_age": 28},
    {"id": "T03", "amount": 50000,   "gateway": "UzCard",     "merchant_id": "UZ-0002", "status": "ok",     "customer_age": 35},
    {"id": "T04", "amount": 1500000, "gateway": "UzCard",     "merchant_id": "UZ-0003", "status": "failed", "customer_age": 41},
    {"id": "T05", "amount": 75000,   "gateway": "Humo",       "merchant_id": "HM-0001", "status": "ok",     "customer_age": 22},
    {"id": "T06", "amount": 200000,  "gateway": "Humo",       "merchant_id": "HM-0001", "status": "ok",     "customer_age": 22},
    {"id": "T07", "amount": 320000,  "gateway": "Humo",       "merchant_id": "HM-0002", "status": "ok",     "customer_age": 55},
    {"id": "T08", "amount": 180000,  "gateway": "Humo",       "merchant_id": "HM-0002", "status": "failed", "customer_age": 55},
    {"id": "T09", "amount": 500000,  "gateway": "Visa",       "merchant_id": "V-0001",  "status": "ok",     "customer_age": 38},
    {"id": "T10", "amount": 1200000, "gateway": "Visa",       "merchant_id": "V-0002",  "status": "ok",     "customer_age": 47},
    {"id": "T11", "amount": 800000,  "gateway": "Visa",       "merchant_id": "V-0002",  "status": "ok",     "customer_age": 47},
    {"id": "T12", "amount": 350000,  "gateway": "Visa",       "merchant_id": "V-0003",  "status": "ok",     "customer_age": 30},
    {"id": "T13", "amount": 90000,   "gateway": "Mastercard", "merchant_id": "MC-0001", "status": "ok",     "customer_age": 25},
    {"id": "T14", "amount": 450000,  "gateway": "Mastercard", "merchant_id": "MC-0002", "status": "failed", "customer_age": 60},
    {"id": "T15", "amount": 600000,  "gateway": "Mastercard", "merchant_id": "MC-0003", "status": "ok",     "customer_age": 33},
    {"id": "T16", "amount": 80000,   "gateway": "MIR",        "merchant_id": "MIR-001", "status": "ok",     "customer_age": 19},
    {"id": "T17", "amount": 150000,  "gateway": "MIR",        "merchant_id": "MIR-002", "status": "ok",     "customer_age": 41},
    {"id": "T18", "amount": 220000,  "gateway": "MIR",        "merchant_id": "MIR-002", "status": "ok",     "customer_age": 41},
    {"id": "T19", "amount": 4000000, "gateway": "UzCard",     "merchant_id": "UZ-0001", "status": "ok",     "customer_age": 28},
    {"id": "T20", "amount": 1000000, "gateway": "UzCard",     "merchant_id": "UZ-0002", "status": "ok",     "customer_age": 35},
    {"id": "T21", "amount": 65000,   "gateway": "Humo",       "merchant_id": "HM-0003", "status": "ok",     "customer_age": 49},
    {"id": "T22", "amount": 270000,  "gateway": "Visa",       "merchant_id": "V-0001",  "status": "failed", "customer_age": 38},
    {"id": "T23", "amount": 380000,  "gateway": "Visa",       "merchant_id": "V-0004",  "status": "ok",     "customer_age": 38},
    {"id": "T24", "amount": 120000,  "gateway": "Mastercard", "merchant_id": "MC-0001", "status": "ok",     "customer_age": 25},
    {"id": "T25", "amount": 700000,  "gateway": "UzCard",     "merchant_id": "UZ-0003", "status": "ok",     "customer_age": 41},
]

#1
def total_volume(txs):
    return sum(t["amount"] for t in txs if t['status'] == "ok")

#2
def top_gateway_by_volume(txs):
    import pandas as pd
    df = pd.DataFrame(txs)
    df_ok = df[df["status"] == "ok"]
    grouped_volumes = df_ok.groupby("gateway")["amount"].sum()
    return grouped_volumes.idxmax()

#3
def unique_merchants(txs):
    import pandas as pd
    df = pd.DataFrame(txs)
    return df['merchant_id'].nunique()

#4
def top_merchant_by_count(txs):
    counts = {}
    for tx in txs:
        merchant = tx["merchant_id"]
        if merchant not in counts:
            counts[merchant] = 1
        else:
            counts[merchant] += 1
    return max(counts, key=counts.get)

#5
def avg_amount_in_age_range(txs, lo, hi):
    import pandas as pd
    if not txs: return 0
    df = pd.DataFrame(txs)
    df = df[(df["customer_age"]>=lo) & (df["customer_age"]<=hi) & (df["status"]=="ok")]
    if df.empty: return 0
    return round(df["amount"].mean())

ok = TXS
print("Q1:", len(ok))
print("Q2:", total_volume(ok))
print("Q3:", top_gateway_by_volume(TXS))
print("Q4:", unique_merchants(TXS))
print("Q5:", top_merchant_by_count(TXS))
print("Q6:", avg_amount_in_age_range(TXS, 30, 50))




