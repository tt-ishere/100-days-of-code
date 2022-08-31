import random
#Todo1 - create a list of random words

word = ["book", "ghana", "accra", "weija", "kodjonya", "krobo", "baby"]

#Todo2 - randomly choose a word from word list and assign it to chosen_word

chosen_index = random.randint(0, len(word) -1) #-1 to avoid out of range error since random uses both endpoints
chosen_word = word[chosen_index]

#Todo3 - Ask user to guess a letter a letter and assign it to "guess". Make "guess" lower case.

guess = input("Guess a letter in the chosen word: ").lower()

#Todo3 - Check if the guesed letter is present in the chosen word

print("Chosen word is " ,chosen_word)
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

