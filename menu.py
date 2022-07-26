class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150,
                     coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0,
                     coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250,
                     milk=50, coffee=24, cost=3),
        ]

    def quantity_wanted(self):
        requested_quantity = int(input("How many would you like?: "))

        return requested_quantity
    print(quantity_wanted)

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        print("\nOwner only: (refill, report, owner)")
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None
