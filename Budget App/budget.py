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

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to %s" % category.name)
            category.deposit(amount, "Transfer from %s" % self.name)
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = "{0}".center(30, "*").format(self.name)
        items = "\n".join(
            [
                "{0:<23}{1:>7.2f}".format(item["description"][:23], item["amount"])
                for item in self.ledger
            ]
        )
        total = "Total: {:.2f}".format(self.get_balance())
        return "{0}\n{1}{2}".format(title, items, total)


def create_spend_chart(categories):
    spent_percentages = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += item["amount"]
        spent_percentages.append(int(abs(spent / category.get_balance()) * 100))

    max_percentage = max(spent_percentages)
    chart = "Percentage spent by category\n"
    for i in range(max_percentage, -10, -10):
        chart += "{:>3}|".format(i)
        for percentage in spent_percentages:
            if percentage >= i:
                chart += " o"
            else:
                chart += "  "
        chart += "\n"

    chart += "    "
    for i in range(len(categories)):
        chart += "----"
    chart += "\n"
    chart += "     "

    for category in categories:
        chart += "{}  ".format(category.name[0])
    chart += "\n"
    chart += "     "
    for category in categories:
        chart += "{}  ".format(category.name[1])
    chart += "\n"

    if len(categories[0].name) > 2:
        chart += "     "
        for category in categories:
            chart += "{}  ".format(category.name[2])
        chart += "\n"

    return chart


if __name__ == "__main__":
    pass
