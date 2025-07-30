#multiple inheritance
# class A:
#     def __init__(self,name):
#         self.acc_name=name

# class B:
#     def birthday_msg(self):
#         display=f'Happy Birthday {self.acc_name}'
#         return display
#     def loan_recovery_msg(self):
#         outp=input("Do you want to recover your loan of : ")
#         return outp
#     def success_msg(self,amount):
#         return "Loan recovered succesfully" 

# class C(B,A):
#     pass

# obj=C("ishani")
# # print(obj.birthday_msg())
# print(obj.loan_recovery_msg())
# print(obj.success_msg(11))
 
#POLYMORPHISM
class Dog():
    def speak(self):
        return "barks"
class Cat():
    def speak(self):
        return "meow"
class Human():
    def speak(self):
        return "speaks"  
dog_obj=Dog()
cat_obj=Cat()
human_obj=Human()
for i in [dog_obj,cat_obj,human_obj]:
    print(i.speak())


class Payment():
    def pay(self,amount):
        raise NotImplementedError("this is required for each class")
    
class Esewa(Payment):
    def test(self):
        print("i am test")
    def pay(self,amount):
        return f'Pay {amount} from esewa'
    
class Khalti(Payment):
    def points(self):
        return "points"
    def pay(self,amount):
        return f'Pay {amount} from khalti'

esewa_obj=Esewa()
khalti_obj=Khalti()

for i in [esewa_obj,khalti_obj]:
    print(i.pay(22))