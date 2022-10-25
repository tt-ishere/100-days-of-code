from os import system
from random import randint
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    rand_number = randint(0, len(cards) - 1)
    return rand_number


def compare(user_score, computer_score):

    print(f"Your final hand: {user_cards}, final score = {user_score}")
    print(f"Computer's first cards: {computer_cards} final score = {computer_score}\n")
        
    if user_score == 0:
        return "You have a blackjack  \nYou win 😁\n" 
        
    elif computer_score == 0:
         return "Computer has a blackjack  \nYou lose 😔\n"
        
    elif computer_score > 21:
         return "Oponenet scores over 21 /nYou win 😁\n"
     
    elif user_score > 21:
         return "Your scores are over 21 /nYou lose 😔\n"  
       
    elif user_score > computer_score:
        return "Your scores are higher \nYou win 😁\n"
    elif computer_score > user_score:
        return "Opponent scores are higher \nYou lose 😔\n"
    elif user_score == computer_score:
        return "Both scores are equal \nDraw 😐\n"

is_playing = False
while not is_playing:
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i  in range(2): 
        user_cards.append(cards[deal_card()])
        computer_cards.append(cards[deal_card()])
    while not is_game_over:
        
        def calculate_score(cards):
            score = 0
            if sum(cards) == 21 and len(cards) == 2:
                return 0
            if 11 in cards and score > 21:
                cards.remove(11)
                cards.append(1)
            score = sum(cards)
            return score

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score = {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            question = input("Type 'y' to get another card and 'n' to pass: ").lower()
            if question == 'y':
                user_cards.append(cards[deal_card()])
            else:  
                is_game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(cards[deal_card()])
        computer_score = calculate_score(computer_cards)
        
    print(compare(user_score, computer_score))

    play_again = input("Do you want to play again? If yes 'y' and no 'n': ")
    if play_again == 'y':
        system("cls")
        is_playing = False
    else:
        is_playing = True
    
    

