# import requests

# names1 = {'Muhsina', 'Izzat', 'Abdulaziz'}
# names2 = {'Izzat', 'Muhsina', 'Mohinur'}
# union = names1 | names2
# intersection = names1 & names2
# difference = names1 - names2
# sym_diff = names1 ^ names2

# response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()
# dict1 = response[0]
# nominal = dict1.get("Nominal")
# ccy = dict1.get("CcyNm_UZ")
# rate = dict1.get("Rate")
# # print(f"{nominal} {ccy} = {rate} UZS")
# print(dict1.get("Country"))

# names1 = {"Izzat", "Muhsina", "Izzat", "Muhsina"}
# print(len(names1)) #prints 2

# def add(item, cart=[]):
#     cart.append(item)
#     return cart

# def add(item, cart=None):
#     if cart==None:
#         cart = []
#     cart.append(item)
#     return cart


# def find_sum(*args):
#     return sum(args)

def scan1(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

scan1(name="IZZAT", lastname="TULAYEV", IELTS="-8.5", SAT="1610")
















