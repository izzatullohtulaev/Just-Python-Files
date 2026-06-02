import pandas as pd

grades = pd.read_csv('DATASETS/grades.csv')
# print(grades)

# # mapping dict
# grade_to_points = {
#     'A':5,
#     'B':4,
#     'C':3
# }

# # mapping
# grades['point'] = grades['grade'].map(grade_to_points)
# print(grades)

# grades['name'] = grades['name'].map(str.title)
# print(grades)

# def upgrade_grade(grade):
#     grade = int(grade)
#     if grade == 5:
#         return grade
#     grade += 1
#     return grade
#
# grades['point'] = grades['point'].apply(upgrade_grade)
# print(grades)


# grades['point'] = grades['point'].apply(lambda x: int(x) + 1)
# print(grades)


grades['fun'] = grades.apply(lambda row: f"{row['grade']} 🔗 {row['point']}", axis=1)
print(grades)














