class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 500,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"\nWater: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def refill_ingredients(self):
        water = int(input(f"How much water(ml) would you like to add?: "))
        self.resources['water'] += water
        milk = int(input(f"How much milk(ml) would you like to add?: "))
        self.resources['milk'] += milk
        coffee = int(input(f"How much coffee(g) would you like to add?: "))
        self.resources['coffee'] += coffee

    def is_resource_sufficient(self, drink, quantity):
        can_make = True
        for item in drink.ingredients:
            drink.ingredients[item] *= quantity
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
