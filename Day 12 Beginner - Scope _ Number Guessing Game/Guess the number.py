from random import randint
from art import logo

guessed_number = randint(1, 100)
easy = 10
hard = 5

def guess(level_number):
    is_easy = False
    while not is_easy:
        user_guess = int(input("Make a guess: "))
        level_number -= 1
        if user_guess > guessed_number:
            print("Too high \nGuess again")
            print(f"You have {level_number} attempts remaing to guess the number")
        if guessed_number > user_guess:
            print("Too low \nGuess again")
            print(f"You have {level_number} attempts remaing to guess the number")
        if user_guess == guessed_number:
            print(f"You got it right!")
            print(f"I was thinking of {guessed_number}")
            is_easy = True
        if level_number == 0:
            print("Game over")
            print(f"I was thinking of {guessed_number}")
            is_easy = True

# Prompt users to type the right levels 
def try_again():
    if difficulty == 'easy':
        print(f"You have 10 attempts remaining to guess")
        guess(easy)
    elif difficulty == 'hard':
        print(f"You have 5 attempts remaining to guess")
        guess(hard)

print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")


# Let player chose difficulty level 
difficulty = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    print(f"You have 10 attempts remaining to guess")
    guess(easy)
elif difficulty == 'hard':
    print(f"You have 5 attempts remaining to guess")
    guess(hard)
else:
    print("UNKNOWN GAME LEVEL\nTRY AGAIN")
    difficulty = input("Choose difficulty level. Type 'easy' or 'hard': ")
    try_again()
