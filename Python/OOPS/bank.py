class Account:

    def __init__(self,acc,bal):
        self.account = acc
        self.balance = bal

    def debet(self,amount):
        self.balance += amount
        print("Your ac.no",self.account , "balance is",self.balance)

    def credit(self,amount):
        self.balance -= amount
        print("Your ac.no",self.account , "balance is",self.balance)

acc1=Account(12345,10000)
acc1.debet(1000)
acc1.credit(3000)
        