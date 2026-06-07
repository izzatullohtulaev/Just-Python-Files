from scratch.linear_algebra import *
from scratch.statistics import mean, standard_deviation

a_to_b = distance([63, 150], [67, 160]) # 10.77
a_to_c = distance([63, 150], [70, 171]) # 22.14
b_to_c = distance([67, 160], [70, 171]) # 11.40

# print(a_to_b)
# print(a_to_c)
# print(b_to_c)

a_to_b = distance([160, 150], [170.2, 160]) # 14.28
a_to_c = distance([160, 150], [177.8, 171]) # 27.53
b_to_c = distance([170.2, 160], [177.8, 171]) # 13.37
# print('---')

# print(a_to_b)
# print(a_to_c)
# print(b_to_c)

def scale(data_matrix):
    """returns the means and standard deviations of each column"""
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix,j))
    for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix,j))
    for j in range(num_cols)]
    return means, stdevs






