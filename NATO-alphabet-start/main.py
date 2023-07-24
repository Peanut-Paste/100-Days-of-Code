# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # #Looping through dictionaries:
# student_list = student_dict["student"]
# score_list = student_dict["score"]
#
# print(student_list)
# print(score_list)
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas

nato_alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpha_dict = {row.letter: row.code for (index, row) in nato_alpha_data.iterrows()}

def generate_phonetic():
    userinput = input("Input please: ").upper()
    try:
        input_list = [nato_alpha_dict[letter] for letter in userinput]
    except KeyError:
        print("Please only enter alphabet")
        generate_phonetic()
    else:
        print(input_list)

generate_phonetic()