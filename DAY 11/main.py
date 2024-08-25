############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score_evaluator(player_score, computer_score):
    if computer_score == 21 and player_score != 21:
        return "lose"
    elif player_score == 21 and computer_score != 21:
        return "win"
    elif player_score > 21:
        return "lose"
    elif computer_score > 21:
        return "win"
    elif computer_score > player_score:
        return "lose"
    elif player_score > computer_score:
        return "win"
    elif player_score == computer_score:
        return "draw"

def score_remarks(score_result):
    if score_result == "win":
        print("You win. 😎")
    elif score_result == "lose":
        print("You lose. 😭")
    else:
        print("Draw. 🤔")    

def show_scores(player, computer, final):
    
    if final:
        print(f"Your final hand: {player['cards']}, final score: {player['total']}")
        print(f"Computer's final hand: {computer['cards']}, final score: {computer['total']}")
    else:
        print(f"Your cards: {player['cards']}, current score: {player['total']}")
        print(f"Computer's first card: {computer['cards'][0]}")

def main():
    
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
    
    while response == "y":

        player = {}
        computer = {}
        
        player_card_list = []
        computer_card_list = []
        
        draw_again = "y"
        print(logo)
        
        # initial sets of card
        # player
        player_card_list.append(random.choice(cards))
        computer_card_list.append(random.choice(cards))
        
        while draw_again == "y":
        
            player_card_list.append(random.choice(cards))
            
            player["cards"] = player_card_list
            player["total"] = sum(player_card_list)
            
            # computer
            computer_card_list.append(random.choice(cards))
            
            computer["cards"] = computer_card_list
            computer["total"] = sum(computer_card_list)
            
            show_scores(player, computer, False)
            
            evaluated_score = score_evaluator(player["total"], computer["total"])
            
            if computer["total"] >= 21 or player["total"] >= 21:
                show_scores(player, computer, True)
                score_remarks(evaluated_score)
                draw_again = "n"
            else:
                draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
                
                if draw_again == "n":
                    show_scores(player, computer, True)
                    score_remarks(evaluated_score)
        
        response = input("Play a game of Blackjack again? Type 'y' or 'n': ") 
        

main()