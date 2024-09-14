# FROM ACTIVITY DAY 05 ...

import random

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

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
        
    return generated_hard_password