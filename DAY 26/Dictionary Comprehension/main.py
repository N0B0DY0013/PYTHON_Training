
import random
import pandas

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {name:random.randint(1, 100) for name in names}


# passed_students = {name:score for (name, score) in student_scores.items() if score >= 60}

# print(f"Student Scores: {student_scores}")
# print(f"Passed Students: {passed_students}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# result = {word:len(word) for word in sentence.split(" ")}


# print(result)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆

# # Write your code 👇 below:
# weather_f = {day:(temperature * 1.8 + 32) for (day, temperature) in weather_c.items()}

# print(weather_f)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv", sep = ";")
print(type(nato_alphabet))
nato_dict = {}

# for (index, row_data) in nato_alphabet.iterrows():
#     nato_dict[row_data["letter"]] = row_data["code"]
nato_dict = {row_data["letter"]:row_data["code"] for (index, row_data) in nato_alphabet.iterrows()}

word = input(f"Please enter a word: ").upper()

nato_word = [nato_dict[letter] for letter in word]

print(nato_word)
