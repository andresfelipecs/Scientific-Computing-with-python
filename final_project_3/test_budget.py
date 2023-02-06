# test_budget.py 

import pytest
from .budget import Category
"""
Code Analysis:
- The class Category is used to track deposits and withdrawals from a given account. 
- The __init__ method initializes the class with a name and an empty ledger. 
- The deposit method adds an entry to the ledger with the amount and description of the deposit. 
- The withdraw method checks if there are enough funds to withdraw the given amount and adds an entry to the ledger with the amount and description of the withdrawal. 
- The get_balance method calculates the balance of the account by summing up all entries in the ledger. 
- The transfer method withdraws the given amount from the current account and deposits it into the other account. 
- The check_funds method checks if there are enough funds in the account to withdraw the given amount. 
- The __str__ method returns a string representation of the account with the name, entries in the ledger, and the total balance.
"""

"""
Test Plan:
- test_init(): tests that the class is initialized correctly with the given name and an empty ledger
- test_deposit(): tests that the deposit method adds an entry to the ledger with the correct amount and description
- test_withdraw(): tests that the withdraw method checks if there are enough funds to withdraw the given amount and adds an entry to the ledger with the correct amount and description
- test_get_balance(): tests that the get_balance method calculates the balance of the account correctly by summing up all entries in the ledger
- test_transfer(): tests that the transfer method withdraws the given amount from the current account and deposits it into the other account
- test_check_funds(): tests that the check_funds method checks if there are enough funds in the account to withdraw the given amount
"""

class TestCategory:

    def setup_method(self):
        self.cat1 = Category("Cat1")
        self.cat2 = Category("Cat2")

    def test_init(self):
        assert self.cat1.name == "Cat1"
        assert self.cat1.ledger == []

    def test_deposit(self):
        self.cat1.deposit(100, "Test Deposit")
        assert self.cat1.ledger[0]["amount"] == 100
        assert self.cat1.ledger[0]["description"] == "Test Deposit"

    def test_withdraw(self):
        self.cat1.deposit(100)
        self.cat1.withdraw(50, "Test Withdraw")
        assert self.cat1.ledger[1]["amount"] == -50
        assert self.cat1.ledger[1]["description"] == "Test Withdraw"

    def test_get_balance(self):
        self.cat1.deposit(100)
        self.cat1.withdraw(50)
        assert self.cat1.get_balance() == 50

    def test_transfer(self):
        self.cat1.deposit(100)
        self.cat1.transfer(50, self.cat2)
        assert self.cat1.get_balance() == 50
        assert self.cat2.get_balance() == 50

    def test_check_funds(self):
        self.cat1.deposit(100)
        assert self.cat1.check_funds(50) == True