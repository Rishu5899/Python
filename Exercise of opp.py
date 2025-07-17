# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Bank():
    def __init__(self,balance,accountno):
     self.balance = balance
     self.accountno = accountno

    def debit (self,amount):
       self.balance -= amount
       print("Your account balance is",self.get_balance())

    def credit (self,amount):
       self.balance += amount
       print("Your account balance is ",self.get_balance())      

    def get_balance(self):
       return self.balance
s = Bank(10000,12563) 
s.debit(1000)
s.credit(2000)
s.credit(10000)
s.debit(4000)
# print(s.accountno)
# print(s.balance)
