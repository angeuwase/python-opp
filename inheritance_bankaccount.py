# implement a Banking Account using the concepts of inheritance.
# Implement a basic structure of a parent class, Account, and a child class, SavingsAccount.
# Account has the following properties: title, balance
# SavingsAccount has the following properties: interestRate
# In the Account class, implement getBalance() method that returns balance.
# In the Account class, implement deposit(amount) method that adds amount to the balance. It does not return anything.
# In the Account class, implement withdrawal(amount) method that subtracts the amount from the balance. It does not return anything.
# In the SavingsAccount class, implement a interestAmount() method that returns the interest amount of the current balance. Below is the formula for calculating the interest amount:

class Account:

    def __init__(self, title=None, balance=0):
        self.__title = title
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdrawal(self, amount):
        self.__balance -= amount

class SavingsAccount(Account):

    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.getBalance()) / 100

account1 = SavingsAccount('Mark', 5000, 10)
print(account1.getBalance())                        # terminal output: 5000
account1.deposit(2000)
print(account1.getBalance())                        # terminal output: 7000
account1.withdrawal(3000)
print(account1.getBalance())                        # terminal output: 4000
print(account1.interestAmount())                    # terminal output: 400