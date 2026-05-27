import numpy as np

"""INTRODUCTION TO NUMPY______________________________________________"""

# print(np.__all__)

# array = np.array([1, 2, 3, 4])
# print(array)
# array *= 2
# print(array)

# array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F']],
#                   [['G', 'H', 'I'], ['J', 'K', 'L']],
#                   [['M', 'N', 'O'], ['P', 'Q', 'R']]])
# print(array)
# print(array.ndim)
# print(array.shape)
# print(array[2, 1, 1])
# word = array[0, 0, 0]+array[1, 0, 1]+array[1, 0, 1]
# print(word)


"""SLICING_____________________________________________________________"""

# array = np.array([[1, 2, 3, 4], 
#                   [5, 6, 7, 8], 
#                   [9, 10, 11, 12], 
#                   [13, 14, 15, 16]])
# print(array[0:4])
# print(array[0:4:2])
# print(array[::-2])
# print(array[0:3, 0])

"""EXERCISE_____________________________________________________________"""

# radii = np.array([1, 2, 3])
# areas = np.pi * radii ** 2
# for area in areas:
#     print(area)

"""INTERACTIONS BETWEEN ARRAY ELEMENTS___________________________________"""

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([2, 6, 9])

# summ = arr1 + arr2
# subt = arr1 - arr2
# mult = arr1 * arr2
# divd = arr1 / arr2
# powr = arr1 ** arr2

# print(summ)
# print(subt)
# print(mult)
# print(divd)
# print(powr)

"""RANDOM RANGE_________________________________________________________"""

# rng = np.random.default_rng()

# fruits = np.array(['😊', '👍', '🎉', '✔', '😆', '😎', '🤣', '🎁', '😘'])
# fruits = rng.choice(fruits, size=[4, 4])

# print(fruits)

"""ARITHMETIC COMPARISON OPERATORS______________________________________"""

# scores = np.array([32, 78, 56, 87, 46, 88, 99, 100, 12])

# scores[scores < 40] = 0
# print(scores)

"""BROADCASTING__________________________________________________________"""

# # 1ST EXAMPLE
# array1 = np.array([[1, 2, 3, 4], 
#                    [12, 54, 67, 86],
#                    [3, 2, 3, 4], 
#                    [4, 2, 3, 4]])
# array2 = np.array([[1], [2], [3], [4]])
# print("Initial arrays:")
# print(array1)
# print()
# print(array2)
# print()
# print("Shapes:")
# print(array1.shape)
# print(array2.shape)
# print("RESULT AFTER (+):")
# print(array1 + array2)

# # 2ND EXAMPLE
# array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
# array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])

# print("First array:")
# print(array1)
# print()
# print("Second array:")
# print(array2)
# print()
# print("Shapes:")
# print(array1.shape)
# print(array2.shape)
# print()
# print("RESULT AFTER (*):")
# print(array1 * array2)

"""AGGREGATE FUNCTIONS__________________________________________________"""

# array = np.array([[1, 2, 3, 4, 5],
#                   [6, 7, 8, 9, 10]])

# print(np.sum(array))
# print(np.sum(array, axis=0))
# print(np.sum(array, axis=1))
# print(np.max(array))
# print(np.min(array))
# print(np.argmin(array))
# print(np.argmax(array))

"""FILTERING_____________________________________________________________"""

# ages = np.array([[16, 20, 17, 49, 19, 67, 56, 86, 32],
#                  [47, 26, 84, 19, 73, 43, 25, 48, 35]])
#
# teens = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages<65)]
# olds = ages[ages >= 65]
#
# print("Teenager ages: "+str(teens))
# print("Adult ages: "+str(adults))
# print("Old people ages: "+str(olds))

















