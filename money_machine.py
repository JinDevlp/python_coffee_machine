class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.owner_collect = 0

    def report(self):
        """Prints the current profit"""
        print(f"\nMoney inside machine: {self.CURRENCY}{self.profit}")
        print(f"Money transferred: {self.CURRENCY}{self.owner_collect}")

    def owner(self):
        owner_option = input(
            f"Hello boss. Total collected is: {self.CURRENCY}{self.profit}. What would you like to do? 'collect money'? ")
        if owner_option == 'collect money':
            amount = int(input("How much would you like to take out? "))
            self.owner_collect += amount
            print(f"{self.CURRENCY}{amount} transferred to your account")
            self.profit -= amount
        else:
            print(f"Total collected is: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(
                input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost, quantity):
        """Returns True when payment is accepted, or False if insufficient."""
        cost *= quantity
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
