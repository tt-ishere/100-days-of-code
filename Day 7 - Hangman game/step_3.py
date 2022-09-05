#Step 3

import random

word = ["book", "ghana", "accra", "weija", "kodjonya", "krobo", "baby"]
chosen_word = random.choice(word)
end_of_game = False

#Testing code
print(f"Chosen word is {chosen_word}")

display = []
word_lenght = len(chosen_word)
for letter in chosen_word:
    display.append("_")
#print(*display, sep = " ")

#Todo1 - use while loop to allow user to guess again till
#all the blanks been filled then user has won

#guess = input("Guess a letter in the chosen word: ").lower()

#Check guessed letter
while "_" in display:
    #print(*display, sep = " ")
    guess = input("Guess a letter in the chosen word: ").lower()
    
    for position in range(word_lenght):
        if chosen_word[position] == guess:
            display[position] = guess

    print(*display, sep = " ")

    print("You won!")
        