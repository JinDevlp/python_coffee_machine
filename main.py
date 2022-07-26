from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"\nWhat would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        coffee_maker.refill_ingredients()
    elif choice == "owner":
        money_machine.owner()
    else:
        drink = menu.find_drink(choice)
        quantity = menu.quantity_wanted()
        if coffee_maker.is_resource_sufficient(drink, quantity) and money_machine.make_payment(drink.cost, quantity):
            coffee_maker.make_coffee(drink)
