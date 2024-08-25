import random
from hangman_art import logo, stages
import hangman_word


word_list = hangman_word.word_list
guessed_letters = []
incorrect_count = 0
unguessed_letter_count = 0

def show_guessed_letters():
    
    guessed_word = ""
    
    if len(guessed_letters) > 0:
        for letter in  guessed_letters:
            guessed_word += letter[1] + " "
            
    print("\n"+guessed_word)
        
def evaluate_guessed_letter(inserted_letter):
    
    matched_letter = 0
    
    global unguessed_letter_count
    unguessed_letter_count = 0
    
    for letter in  guessed_letters:
        if inserted_letter == letter[0] and letter[1] == "_":
            letter[1] = letter[0]
            matched_letter += 1
        
        if letter[1] == "_":
            unguessed_letter_count += 1
         
    if matched_letter == 0:
        global incorrect_count
        incorrect_count += 1
        
        print (f"Letter does not match. You have {7-incorrect_count} tries left.")
        print(stages[7-incorrect_count])

def main():
    
    global incorrect_count
    incorrect_count = 0
    
    word_to_guess = random.choice(word_list)

    print(word_to_guess)

    for letter in word_to_guess:
        guessed_letters.append([letter, "_"])
        global unguessed_letter_count
        unguessed_letter_count = unguessed_letter_count + 1
    
    print(logo)
      
    while incorrect_count < 7 and unguessed_letter_count > 0:
        show_guessed_letters()
        guessed_letter = input("Guess a letter: ").lower()
        
        evaluate_guessed_letter(guessed_letter)
    
    if unguessed_letter_count == 0:
        show_guessed_letters()
        print("You win!")    
    
    if incorrect_count >= 7:
        print("\nYou Lose!")    

    
main()