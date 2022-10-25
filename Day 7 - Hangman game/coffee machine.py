MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}



# TODO 4 CHECK IF TRANSACTIONS IS SUCCESSFULL


# TODO 1 PRINT REPORT
def report():
    for k,v in resources.items():
        if k == "water":
           print(*[f"{k}: {v} ml"], sep = "\n") 
        elif k == "milk":
            print(*[f"{k}: {v} ml"], sep = "\n")
        elif k == "coffee":
            print(*[f"{k}: {v} g"], sep = "\n")  
        elif k == "money":
            print(*[f"{k}: $ {v}"], sep = "\n") 

# TODO 2 CHECK IF RESOURCES IS SUFFICIENT
def is_sufficient(item):
    for k,v in MENU[item]["ingredients"].items():
        if k == "water" and resources["water"] < v:
            print(f"Sorry, there is not enough {k}")
        elif k == "milk" and resources["milk"] < v:
            print(f"Sorry, there is not enough {k}")
        elif k == "coffee" and resources["coffee"] < v:
             print(f"Sorry, there is not enough {k}")


def make_it(item):
    # TODO 3 PROCESS COINS
    print("Please insert your coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    
    total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
    # TODO 4 CHECK IF TRANSACTIONS IS SUCCESSFULL
    if MENU[item]["cost"] <= total_coins:
        change = total_coins - MENU[item]["cost"]
        r_change = round(change, 2)
        print(f"Here is {r_change} in change ")
        resources["money"] += MENU[item]["cost"]
        
        # TODO 5 MAKE COFFEE
        for k,v in MENU[item]["ingredients"].items():
            if k == "water":
                resources["water"] - v
            elif k == "milk":
                resources["milk"] - v
            elif k == "coffee":
                resources["coffee"] - v
        print(f"Here is your {item} ☕ enjoy")
    else:
        print("Sorry that's not enough money. Money refunded.")
        

            
is_off = False
while not is_off:
    prompt = input("What would you like? (espresso, latte, or cappuccino): ").lower()
    if prompt == "report":
        report()
    elif prompt == "espresso":
        # print("Make espresso")
        is_sufficient(prompt)
        make_it(prompt)
    elif prompt == "latte":
        # print("Make latte")
        is_sufficient(prompt)
        make_it(prompt)
    elif prompt == "cappuccino":
        #  print("Make cappuccino")
        is_sufficient(prompt)
        make_it(prompt)
    elif prompt == "off":
        is_off = True