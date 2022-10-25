from importlib import resources
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


choice = input("What would you like? (espresso, latte, or cappuccino): ").lower()

# while not is_off:
choice = input("What would you like? (espresso, latte, or cappuccino): ").lower()
if choice == "report":
    report = CoffeeMaker.report()
    print(report)
# elif choice == "espresso":
#     # print("Make espresso")
    
# elif choice == "latte":
#     # print("Make latte")
    
# elif choice == "cappuccino":
#     #  print("Make cappuccino")
    
# elif choice == "off":
        
