# two_digit_number = input("Type a two digit number:")

# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = weight / height ** 2

# print("Your bmi is: " + str(int(bmi)))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#print(round(8//3,2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# age = int(input("What is your current age: "))

# diff_from_90 = 90 - age

# print(f"You have {diff_from_90 * 365} days, {diff_from_90 * 52} weeks, {diff_from_90 * 12} months left.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100
people_count = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${'{:.2f}'.format(total_bill * (1 + tip_percent) / people_count)}")