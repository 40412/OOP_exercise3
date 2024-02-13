# File: task3.py
# Author: Jasmin Fränti
# Description: Task 3 of exercise 3 
# Class LunchCard that has a balance and methods to modify the balance

class LunchCard:

    def __init__(self, balance: float):
        self.balance = balance

    def eat_ordinary(self):

        if self.balance - 2.95 >= 0:
            self.balance -= 2.95
        else: 
            print("Not enough money! Get a job!!")

    def eat_luxury(self):

        if self.balance - 5.90 >= 0:
            self.balance -= 5.90
        else:
            print("Not enough money! Get a job!!")

    def deposit_money(self, amount):

        if amount < 0:
            raise ValueError("Cannot deposit negative values")
        else:
            self.balance += amount

    def __str__(self):
        return f"The balance is {self.balance} euros"
    
my_card = LunchCard(50)
print(my_card)

my_card.eat_luxury()
print(my_card)

my_card.eat_ordinary()
print(my_card)

my_card.deposit_money(20)
print(my_card)

my_card.deposit_money(0)
print(my_card)