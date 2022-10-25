import os
from art import logo

bid_list = {}
is_done = False

def winner():
    winning_value = max(bid_list.values()) #get winning value
    winning_key = max(bid_list, key = bid_list.get) #get winning key
    print(f"The winnder is {winning_key} with a bid of bid of ${winning_value}")

# Accept bids     
while not is_done:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bid_list[name] = bid
    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system("cls") #Clear screen; hence the name blind auction 😉 
    
    #Check for the wining bid
    if decision == 'no':
        is_done = True
        os.system("cls")
        print(logo)
        winner()
        print("Thank you")
