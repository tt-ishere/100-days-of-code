#Step 2

import random

word = ["book", "ghana", "accra", "weija", "kodjonya", "krobo", "baby"]
chosen_word = random.choice(word)

#Testing code
print(f"Chosen word is {chosen_word}")

#Todo1 - Create a list called display
#Replace every letter of chosen word with "_" and display it.

display = []
word_lenght = len(chosen_word)
for letter in chosen_word:
    display.append("_")
print(*display, sep = " ")
guess = input("Guess a letter in the chosen word: ").lower()

#Todo2 Loop through each letter in chosen_word
#If letter at a position matches "guess", then reveal the letter
#at that position in display list

for position in range(word_lenght):
    if chosen_word[position] == guess:
        display[position] = guess
    else:
        display[position] = "_"

#Todo3 - Print the guessed letter if available in chosen_word the right
#position and the unguessed words ie."_" at their position

print(*display, sep = " ")
