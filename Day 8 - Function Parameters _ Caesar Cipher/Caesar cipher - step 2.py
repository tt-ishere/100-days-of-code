from re import I


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_by):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_by
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

#Todo create a function called decrypt that takes 'text' and 'shift'
# as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount 
    # and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #cipher_text = "hello"
    #print output: "The encoded text is hello"



def decrypt(cipher_text, shift_by):
    deciphered_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_by
        deciphered_letter = alphabet[new_position]
        deciphered_text += deciphered_letter
    print(f"The decoded text is {deciphered_text}\n")
   

if direction == "encode":
    encrypt(plain_text = text, shift_by = shift)
else:
    decrypt(cipher_text = text, shift_by = shift)

 

