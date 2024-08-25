import random

# rand_val = random.randint(0,1)

# if rand_val == 1:
#     print("Head")
# else:
#     print("Tail")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# rand_int = random.randint(0, len(names)-1)

# print(f"{names[rand_int]} is going to buy the meal today!")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# row = int(position[:1]) - 1
# column = int(position[1:]) - 1
# map[row][column] = "X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_selection = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))
print(f"{hand_selection[player_choice]} \n Computer chose:\n")

computer_choice = random.randint(0,2)
print(f"{hand_selection[computer_choice]} \n -") 

if (player_choice == 0 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1) or (player_choice == 1 and computer_choice == 0):
    print("You win!")
elif(player_choice == computer_choice):
    print("Draw.")
else:
    print("You lose!")

