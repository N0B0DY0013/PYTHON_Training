import math
from art import logo
# #Write your code below this line 👇
# def paint_calc(height, width, cover):
#     print(f"You'll need {math.ceil((height * width) / cover)} can/s of paint.")


# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# #Write your code below this line 👇

# def prime_checker(number):

#     if number > 0:
#         divisible_count  = 0
        
#         for i in range(number):
#             if number % (i + 1) == 0:
#                 divisible_count += 1    

#         if divisible_count > 2:
#             print("It's not a prime number.")
#         else:
#             print("It's a prime number")


# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    
    new_text = ""
    
    for letter in text:
        
        index = 0

        if alphabet.count(letter) > 0:
            if alphabet.index(letter) >= shift:
                index = alphabet.index(letter) - shift
            else:
                index = len(alphabet) - shift + alphabet.index(letter)
            
            new_text += alphabet[index]
    
    print(f"The encoded text is {new_text}")

def decrypt(text, shift):
    
    new_text = ""
    
    for letter in text:
        
        index = 0
        
        if alphabet.count(letter) > 0:
            index =  alphabet.index(letter) - ((len(alphabet)) - shift)
            new_text += alphabet[index]
    
    print(f"The decoded text is {new_text}")
    
def main():
    
    print(logo)
    
    answer = "yes"
    
    while answer == "yes":
        
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
        if ["encode", "decode"].count(direction) > 0:
            
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            
            if direction == "encode":
                encrypt(text=text, shift=shift)
            elif direction == "decode":
                decrypt(text=text, shift=shift)
            
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

main()