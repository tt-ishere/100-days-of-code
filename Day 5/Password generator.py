import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Pypassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))

num_symbols = int(input("How many symbols would you like in your password?\n"))

num_numbers = int(input("How many numbers would you like in your password?\n"))

#generating random leters from letter list
len_letters = len(letters) #size of letters list
password = [] #to hold the random letters

for i in range(0, num_letters):
    rand_letters = random.randint(0, len_letters -1) #-1 because range includes both
    password.extend(letters[rand_letters])
    
# print(letter_password)

#generating random symbols from symbols list
len_symbols = len(symbols) 

for i in range(0, num_symbols):
    rand_symbols = random.randint(0, len_symbols - 1) 
    password.extend(symbols[rand_symbols])
    
# print(sym_password)

#generating random numbers from number list
len_numbers = len(numbers)

for i in range(0, num_numbers):
    rand_numbers = random.randint(0, len_numbers - 1) 
    password.extend(numbers[rand_numbers])

#randomizing password list so that it is in no order
random.shuffle(password)
print(*password, sep="")