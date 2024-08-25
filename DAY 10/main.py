
# def format_name(first_name, last_name):
#     return f"{first_name} {last_name}".title()

# print(format_name(input("What is your first name?: "), 
#                   input("What is your last name?: ")))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# def is_leap(year):
#   """A function that checks whether the submitted year is a Leap Year or not."""
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):

#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return 0
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    keep_going = True
    is_repeated = False
    result = 0

    while keep_going:
        
        if is_repeated:
            num1 = result
        
        operation_symbol = input("Pick an operation: ")

        if ["+", "-", "*", "/"].count(operation_symbol) > 0:
            
            num2 = float(input("What's the second number?: "))
            
            result = operations[operation_symbol](num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {result}")
        
        if input(f"Type 'y' to continue calculating  with {result}, or type 'n' to start a new calculation.: ").lower() == "n":
            calculate()
        else:
            if is_repeated == False:
                is_repeated = True
                
calculate()