height = int(input("Enter your height in m: "))
age = int(input("How old are you?\n"))
bill = 0

if height >= 120:
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Teenager tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55: #free for people aged 45 - 55
        print("Enjoy your free ride, this one is on us!")
    else:
        print("Adult tickets are $12")
        bill = 12
        
    want_photos =input("Do you want a photo taken? Y or No: ")
    if want_photos == "Y" or "y":
        # Add $3 to bill
        bill += 3
    print(f"Your final bill is {bill}")
        
else:
    print("Sorry, you can't ride with us due to safety purposes!")  