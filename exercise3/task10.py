class BankAccount:
    def __init__(self, name: str, accountnum: float, balance: float) -> None:
        self.__name = name
        self.__account_number = accountnum
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__service_charge()
        else:
            print("Not enough money")

    def get_balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance *= 0.99

account = BankAccount("Randy Riches", "123456789", 1000)
account.withdraw(100)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())