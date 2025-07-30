#inheritance
# class A(): #parent class
#     a=10
#     b=11

# class B(A): #child class
#     c=111
#     d=77

# obj= B()
# print(obj.a)
# print(obj.d)

# class Sum():
#     def __init__(self):
#         a=100
#         b=100
#         print("I am parent")
#     def total(self):
#         s=self.a+self.b
#         return s
# class Avg(Sum):
#     def __init__(self,length):
#         print("I am child")
#         self.length=length
#         Sum.__init__(self) #manually parent ko constructor call garna
#         super().__init__() #arko option to call parent's constructor
#     def average(self):
#         result=(self.total())/self.length
#         return result
# obj=Avg(2)
# print(obj.average())

class Account():
    def __init__(self,name):
            self.name=name
class BankAccount(Account):
    def __init__(self,name):
        self.name=name
        self.balance=0.0
        Account.__init__(self,name)
    def positive(self,amount):
        if amount<0:
            return True
        return False
    def deposit(self,amount):
        if self.positive(amount):
            return "Amount should be positive"
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        if self.balance<=0:
            return "insufficient balance"
        else:
            self.balance=self.balance-amount
        return self.balance
    def balances(self):
        output={
            "acc name":self.name,
            "current balance":self.balance
        }
        return output
    
obj=BankAccount("Ishani")
print(obj.deposit(-700))
print(obj.withdraw(500))
print(obj.balances())