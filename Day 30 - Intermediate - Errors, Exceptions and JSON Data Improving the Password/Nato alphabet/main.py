import pandas

data = pandas.read_csv("Nato alphabet/nato_alphabets.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        phonetics = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters of the alphabet please.')
        generate_phonetics()
    else:
        print(phonetics)

generate_phonetics()