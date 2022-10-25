from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
is_off = False


def make_drink():
    # menu.get_items()
    drink = menu.find_drink(choice)
    is_ingredients_enough = coffeemaker.is_resource_sufficient(drink)
    is_payment_successful = money.make_payment(drink.cost)
    if is_ingredients_enough and is_payment_successful:
        coffeemaker.make_coffee(drink)


while not is_off:
    choice = input("What would you like? (espresso, latte, or cappuccino): ").lower()
    if choice == "report":
        coffeemaker.report()
        money.report()
    elif choice == "espresso":
        make_drink()
    elif choice == "latte":
        # print("Make latte") 
        make_drink()
    elif choice == "cappuccino":
        #  print("Make cappuccino")
        make_drink()
    elif choice == "off":
        is_off = True
