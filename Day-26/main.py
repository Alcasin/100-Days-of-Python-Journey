import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict =  {row.letter:row.code for (index, row) in df.iterrows()}
user_word = input("Enter a word: ").upper()
result = [nato_dict[letter] for letter in user_word if letter in nato_dict]
print(result)

# import random
# new_list = [new_item for item in list]

# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# name = "Angela"
# new_list = [letter for letter in name]
# new_range = [n*2 for n in range(1,5)]

# new_list = [new_item for item in list if test]
# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# long_names = [name.upper() for name in names if len(name)>4]


# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passed_students = {student:score for (student, score) in students_scores.items() if score >=60}
# print(passed_students)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)


# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}










