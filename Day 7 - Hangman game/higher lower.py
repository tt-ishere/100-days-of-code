from random import randint
from art import logo
from art import vs 
from game_data import data
import os

# passed in higher_lower()
opt_a = "A"
opt_b = "B"

def higher_lower(alphabet, index):
    """
    prints the higher or lower text on one line
    """    
    name = data[index]["name"]
    prof = data[index]["description"]
    country = data[index]["country"]
    print(f"Compare {alphabet}: {name}, a  {prof} from {country}.")

#generate random indexes to pick higher and lower from game data 
rand_index_a = randint(0, (len(data) - 1))
rand_index_b = randint(0, (len(data) - 1))
if rand_index_a == rand_index_b:
    rand_index_b = randint(0, len(data))

#follower count for higher & lower
a = data[rand_index_a]["follower_count"]
b = data[rand_index_b]["follower_count"]


def compare():
    is_play = False
    score = 0
    while not is_play:
        question = input("Who has more followers? 'A' or 'B': ").lower()
        if (a > b and question == a) or (b > a and question == b):
            score += 1
            os.system("cls")
            print(f"You're right! Current score: {score}")
            start()
            compare()
        else:
            print(f"Sorry, that's wrong. Your final score: {score}")
            is_play = True

def start():
    print(logo)
    higher_lower(opt_a, rand_index_a )
    print(vs)
    higher_lower(opt_b, rand_index_b)

   
start()
print(f"A: {a}")
print(f"B: {b}")
compare()

