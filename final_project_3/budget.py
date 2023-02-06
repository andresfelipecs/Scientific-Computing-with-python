

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
        items = "\n".join([f"{item['description'][:23].ljust(23)}{item['amount']:>7.2f}" for item in self.ledger])
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}{total}"
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
        chart += f"{i:>3}|"
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
        chart += f"{category.name[0]}  "
    chart += "\n"
    chart += "     "
    for category in categories:
        chart += f"{category.name[1]}  "
    chart += "\n"
    
    if len(categories[0].name) > 2:
        chart += "     "
        for category in categories:
            chart += f"{category.name[2]}  "
        chart += "\n"
    
    return chart
    
if __name__ == '__main__':
    pass
