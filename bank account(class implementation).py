#p2
(basic how debit,credit code works)

class Account:

    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    


acc1=Account(10000,9032)
print(acc1.balance,acc1.account_no)

acc1.debit(1000)
acc1.credit(5000)
acc1.debit(3500)
acc1.credit(700)
