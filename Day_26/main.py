import random
import pandas as pd

# List Comprehension (syntax: new_list = [new_item for item in list])
numbers = [1, 2, 3, 4, 5]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
letters = [letter for letter in name]
print(letters)


# List Comprehension with Condition (syntax: new_list = [new_item for item in list if test])
numbers_doubled = [n*2 for n in range(1, 5) if n % 2 == 0]
print(numbers_doubled)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) <= 4]
print(short_names)


# Dictionary Comprehension creating a new dictionary (syntax: new_dict = {new_key: new_value for item in list})
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# Dictionary Comprehension Looping through dictionaries (syntax: new_dict = {new_key: new_value for (key, value) in dict.items() if test})
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Create a dataframe from a dictionary
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Looping by rows through a dataframe (syntax: for (index, row) in df.iterrows():)
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)


