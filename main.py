from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
nescafe = CoffeeMaker()
money = MoneyMachine()

is_on = True
possible_choices = ["off", "report", "espresso", "latte", "cappuccino"]

while is_on:
    choice = ""
    while choice not in possible_choices:
        choice = input(f"What would you like? ({menu.get_items()[:-1]}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        nescafe.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if nescafe.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                nescafe.make_coffee(drink)
