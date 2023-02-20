numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [n ** 3 for n in numbers]
# print(squared_numbers)

# newNumbers = [n + 1 for n in numbers]
# print(newNumbers)

student = {
    'Student': ['Angela', 'James', 'Lily'],
    'Score': [56, 76, 99]
}

# for (key ,value) in student.items():
#     print(value)
    
import pandas

stu_dataframe = pandas.DataFrame(student)

# for (key ,value) in stu_dataframe.items():
#     print(key)
    
for (index, row) in stu_dataframe.iterrows():
    if row.Student == "Angela":
        print(row.Score)