# # previously using for loop
# import random
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# # LIST COMPREHENSION
# new = [n+1 for n in numbers]
# print(new)
#
# # Can use it to change string into list
# name = "Angela"
# new_name = [n.lower() for n in name]
# print(new_name)
#
# # using it with range()
# double = [n*2 for n in range(1,5)]
# print(double)
#
# # CONDITIONAL LIST COMPREHENSION
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# upper_long_names = [name.upper() for name in names if len(name) >= 5]
# print(upper_long_names)
#
# # DICT COMPREHENSION
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {name: random.randint(0,100) for name in names}
# print(students_score)
#
# passed_students = {name:score for (name, score) in students_score.items() if score >= 60}
# print(passed_students)

# LOOPING THROUGH DICTIONARIES
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# #LOOP THROUGH DATA FRAME
# for (key, value) in student_data_frame.items():
#     print(value)

# LOOP THROUGH ROWS OF A DATA FRAME
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)