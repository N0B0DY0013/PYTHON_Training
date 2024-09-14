# fruits = ["Apple", "Pear", "Orange"]

# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         fruit = "NON-EXISTING"
        
#     print(fruit + " pie")


# make_pie(4)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         pass

# print(total_likes)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv", sep = ";")
nato_dict = {}

nato_dict = {row_data["letter"]:row_data["code"] for (index, row_data) in nato_alphabet.iterrows()}

did_not_pass = True

while did_not_pass:
    word = input(f"Please enter a word: ").upper()

    try:
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please type only letters in the English alphabet.")
    else:
        did_not_pass = False
        
print(nato_word)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

