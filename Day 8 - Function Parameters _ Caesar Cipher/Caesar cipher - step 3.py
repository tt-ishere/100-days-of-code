from re import I


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Todo join the encrypt and decrypt funtion under a new funtion called caesar
def caesar(start_text, shift_by, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_by
            new_letter = alphabet[new_position]
            end_text += new_letter
        elif cipher_direction == "decode":
            new_position = position - shift_by
            new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"The {direction}d text is {end_text}\n")


caesar(start_text = text, shift_by = shift, cipher_direction = direction)