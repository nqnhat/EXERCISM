from threading import RLock

class BankAccount(object):

    myRLock = RLock()
    
    def __init__(self):
        self.balance = None

    def get_balance(self):
        with self.myRLock:
            if self.balance is None:
                raise ValueError("Account is deactived")
            return self.balance

    def open(self):
        with self.myRLock:
            self.balance = 0

    def deposit(self, amount):
        with self.myRLock:
            if self.balance is None:
                raise ValueError("Account is deactived")

            if amount < 0:
                  raise ValueError("Cannot make negative deposits")
            self.balance = self.balance + amount
            

    def withdraw(self, amount):
        with self.myRLock:
            if self.balance is None:
                    raise ValueError("Account is deactived")
            if amount < 0:
                    raise ValueError("Cannot make negative withdrawls")
            elif amount > self.balance:
                    raise ValueError("Cannot make withdraw exeeding balance")
            self.balance = self.balance - amount
                                 

    def close(self):
        with self.myRLock:
            self.balance = None
