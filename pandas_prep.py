import pandas as pd

"""SERIES_______________________________________________________________________"""

# # EXAMPLE 1
# data = [100, 102, 104, 200, 202]
# series = pd.Series(data, index=["a", "b", "c", "d", "e"])
# # print(series)
# # series.loc["c"] = 200
# print(series)
# # print(series.iloc[4])
# print(series[series > 104])

# # EXAMPLE 2
# calories = {"Day 1":1750, "Day 2": 2100, "Day 3": 1700}
# series = pd.Series(calories)
#
# series.loc["Day 3"] += 500
#
# print(series[series < 2000])

# # EXAMPLE 3
# class Dinasour:
#     def __init__(self, df=None):
#         self.df = df
#
# Bulbasaur = Dinasour()
# Ivysaur = Dinasour()
# Venusaur = Dinasour()
# Charmander = Dinasour()
# Charmeleon = Dinasour()
# Charizard = Dinasour()
# dinosaours = [Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard]
# series = pd.Series(dinosaours)
#
# print(series)

"""DATAFRAMES___________________________________________________________________"""

# data = {"Name":["Spongebob", "Patrick", "Squidward"],
#         "Age":[30, 35, 50]
# }
#
# df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
#
# df["Job"] = ["Cook", "N/A", "Cashier"] # adds a new column
#
# new_row = pd.DataFrame([{"Name":"Sandy", "Age":28, "Job":"Engineer"}], index=["Employee 4"]) # adds a new row
# df = pd.concat([df, new_row])
#
# print(df)

"""IMPORTING_____________________________________________________________________"""

# df = pd.read_csv("data.csv")
# print(df.to_string())

# import requests
#
# url = "https://cbu.uz/upload/open_data/0002/4-009-0002_uz.json"
# data = requests.get(url).json()
# del data[-1]
# df = pd.DataFrame(data)
# print(df.to_string())

# data_file = "cbu_data.csv"
# df.to_csv(data_file, index=False)

"""SELECTION____________________________________________________________________"""

# df = pd.read_csv("data.csv", index_col="Name")
# # print(df["Height"])
#
# pokemon = input("Enter Pokemon Name: ")
# pokemon = pokemon.title()
#
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")

"""FILTERING____________________________________________________________________"""

# df = pd.read_csv("data.csv")
# tall_pokemons = df[df["Height"] >= 2]
# heavy_pokemons = df[(df["Weight"] > 100) & df["Height"] >= 1]
#
# # print(tall_pokemons.loc[:, ["Name", "Height"]])
# print(heavy_pokemons.loc[:, ["Name","Height", "Weight"]])
# # print(df.iloc[0:6, 2])

"""AGGREGATION___________________________________________________________________"""

# df = pd.read_csv("data.csv")
# group = df.groupby("Type1")
#
# print(group["Height"].sum())
# print(df.mean(numeric_only=True))
# print(df["Name"].count(numeric_only=True))

"""DATA CLEANING________________________________________________________________"""

df = pd.read_csv("data.csv")

# # removing unwanted columns
# df = df.drop(columns=["Legendary", "Type2"])

# # handling the missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2" : "None"})

# # fix inconsistent data
# df["Type1"] = df["Type1"].replace({"Grass":"GRASS"})

# # standardize text
# df["Name"] = df["Name"].str.lower()

# # fixed data types
# df["Legendary"] = df["Legendary"].astype(bool)
# print(df.to_string(index=False))