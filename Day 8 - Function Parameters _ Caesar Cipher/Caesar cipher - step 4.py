from turtle import goto
from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Todo join the encrypt and decrypt funtion under a new funtion called caesar
def caesar(start_text, shift_by, cipher_direction):
    is_done = False
    while not is_done:
        end_text = ""
        if cipher_direction == "decode":
            shift_by *= -1
        for letter in start_text:
            if letter not in alphabet:
                end_text += letter
                continue
            position = alphabet.index(letter)
            new_position = position + shift_by
            new_letter = alphabet[new_position]
            end_text += new_letter
            
        print(f"The {direction}d text is {end_text}\n")

        decision = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()  
        if decision == "yes":
           re_do()
        elif decision == "no":
            is_done = True
            print("Goodbye")
                
def re_do():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 25
    caesar(start_text = text, shift_by = shift, cipher_direction = direction)
    
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift %= 25

caesar(start_text = text, shift_by = shift, cipher_direction = direction)