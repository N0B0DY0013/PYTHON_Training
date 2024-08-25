
import random

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# total_height = 0

# for height in student_heights:
#     total_height+=height
    
# print(f"Average height is: {round(total_height / len(student_heights))}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score

# print(f"The highest score in the class is: {highest_score}.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# total_even = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         total_even += number
        
# print(f"Total of all even numbers from 1 - 100 is: {total_even}.")
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")  
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)  

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_length = nr_letters + nr_symbols + nr_numbers


generated_password = ""
random_char = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for n in range(0, total_length):
    if n + 1 <= nr_letters:
        random_char = letters[random.randint(0,len(letters)-1)]
    elif n + 1 <= (nr_letters + nr_symbols):
        random_char = symbols[random.randint(0,len(symbols)-1)]
    else:
        random_char = numbers[random.randint(0,len(numbers)-1)]

    generated_password = generated_password + random_char

print(f"Your easy-level generated password is: {generated_password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

generated_hard_password = ""
placed_position = []
for n in range(0, total_length):
    random_position = random.randint(1, total_length)
    while placed_position.count(random_position) > 0:
        random_position = random.randint(1, total_length)
        
    placed_position.append(random_position)
    generated_hard_password = generated_hard_password + generated_password[random_position - 1]
    
print(f"Your hard-level generated password is: {generated_hard_password}")