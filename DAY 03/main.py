# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print(f"number {number} is even.")
# else:
#     print(f"number {number} is odd.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = weight / height ** 2

# bmi_result = ""

# if bmi <= 18.5:
#     bmi_result = "underweight"
# elif bmi > 18.5 and bmi  <= 25:
#     bmi_result = "normal weight"
# elif bmi > 25 and  bmi <= 30:
#     bmi_result = "over weight"
# elif bmi > 30 and bmi <= 35:
#     bmi_result = "obese"
# else:
#     bmi_result = "clinically obese"

# print(f"Your BMI is {'{:.2f}'.format(bmi)}, equivalent: {bmi_result}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# year = int(input("Which Year do you want to check?: "))

# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"{year} IS a Leap Year.")
#     else:
#         print(f"{year} IS NOT a Leap Year.")
# elif year % 4 == 0:
#         print(f"{year} IS a Leap Year.")
# else:
#     print(f"{year} IS NOT a Leap Year.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# print("Welcome to Python Pizza Deliveries")
# size = input("What size of pizza do you want? S, M or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25
    
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# print("Welcome to the Love Calculator!")
# my_name1 = input("Insert Name 1: ").lower()
# my_name2 = input("Insert name 2: ").lower()


# first_digit = 0
# second_digit = 0

# for n in my_name1:
#     if n == "t" or n == "r" or n == "u" or n == "e":
#         first_digit += 1
# for n in my_name2:
#     if n == "t" or n == "r" or n == "u" or n == "e":
#         first_digit += 1

# for n in my_name1:
#     if n == "l" or n == "o" or n == "v" or n == "e":
#         second_digit += 1
# for n in my_name2:
#     if n == "l" or n == "o" or n == "v" or n == "e":
#         second_digit += 1

# love_score = int(f"{first_digit}{second_digit}")

# love_score_remarks = ""

# if love_score < 10 or love_score > 90:
#     love_score_remarks = "You go together like coke and mentos."
# elif love_score >= 40 and love_score <= 50:
#     love_score_remarks = "You are alright together."

# print(f"Your Love score is {love_score}%. {love_score_remarks}")
 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

answer1 = input('You are at a cross-road. Where do you want to go? Type "left" or "right". ').lower()
if answer1  != "left":
    print("Fall into a hole. Game over.")
else:
    answer2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if answer2 != "wait":
        print("Attacked by trout. Game over.")
    else:
        answer3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
        if answer3 == "red":
            print("Burned by fire. Game over.")
        elif answer3 == "blue":
            print("Eaten by beasts. Game over.")
        elif answer3 == "yellow":
            print("You win!")
        else:
            print("Game over.")

