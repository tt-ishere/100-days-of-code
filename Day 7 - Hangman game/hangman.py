#Step 5

import random
from hangman_words import word_list


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)
#Testing code
#print(f'Pssst, the chosen word is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(*display, sep = " ")
print("\n") #creating a linebreakto make it easy on the eyes

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print("\n")

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have guessed {guess} already\n")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f'"{guess}" is not in the word \nYou have lost a life\n')
        if lives == 0:
            end_of_game = True
            print(f"Hangman word is {chosen_word}")
            print("You lose.")
            

    #Join all the elements in the list and turn it into a String.
    print(*display, sep = " ")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    
    print(stages[lives])
    print(f"Lives: {lives}\n")