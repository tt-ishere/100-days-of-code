import pandas

data = pandas.read_csv("Nato alphabet/nato_alphabets.csv")

#TODO:  1 Create a dictionary  in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO: Create a list of phonetics code words from a that the user inputs
word = input("Enter a word: ").upper()
generate_phonetics = [phonetic_dict[letter] for letter in word]
print(generate_phonetics)