import pickle

# filename = 'talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     talabalar = file.readlines()

talaba1 = {'ism':'Aziz', 'familya':'Lazizov', 'tyil':2009, 'kurs':1}
talaba2 = {'ism':'Ahmad', 'familya':'Shakarov', 'tyil':2008, 'kurs':2}
with open('text', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)
    
with open('text', 'rb') as fayl:
    print(pickle.load(fayl))
    talaba = pickle.load(fayl)
print(talaba)