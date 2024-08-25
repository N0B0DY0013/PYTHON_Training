import random
import art
from game_data import data

def check_result(first_list, second_list, current_score):
    if int(first_list["follower_count"]) < int(second_list["follower_count"]):
        return current_score
    else:
        print(f"You are right! Current score {current_score + 1}.")
        return current_score + 1
                
def main():
    still_correct = True
    score = 0
    selection_a = random.choice(data)
    
    while still_correct:
        print(art.logo)

        selection_b = random.choice(data)

        print(f"Compare A: {selection_a['name']}, a {selection_a['description']}, from {selection_a['country']}")

        print(art.vs)

        print(f"Against B: {selection_b['name']}, a {selection_b['description']}, from {selection_b['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if answer == "a":
            if score == check_result(selection_a, selection_b, score):
                still_correct = False
            else:
                score += 1
                selection_a = selection_b
        else:
            if score == check_result(selection_b, selection_a, score):
                still_correct = False
            else:
                score += 1
                selection_a = selection_b
    
    print(f"\nSorry, that's wrong. Final score {score}")

main()