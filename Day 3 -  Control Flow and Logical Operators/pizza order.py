print("WELCOME TO PYTHON PIZZAS!!! \nMake your Pizza order here!!!")
print("use caps only!")

bill = 0
# Taking user inputs 
size = input("What size of pizza do you want? L, M, or S: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra chesse? Y or N: " )

# multiple if statements to proces the bill 
# It's not compulsory to add an "else" line
if size == "L":
    bill += 25.00 #bill will auto update
if size == "M":
    bill += 20.00
if size == "S":
    bill += 15.00
    
if add_pepperoni == "Y" and size == "S":
    bill += 2.00
if add_pepperoni == "Y" and (size == "L" or "M"):
    bill += 3.00

if extra_cheese == "Y":
    bill += 1.00
    
print(f"Your final bill is ${bill}")