

import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.withdraw(amount, f"Transfer to {other_category.name}"):
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name}".center(30, "*")
        ledger = ""
        for entry in self.ledger:
            ledger += f"{entry['description'][:23].ljust(23)}{entry['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{ledger}{total}"


if __name__ == '__main__':
    pass
