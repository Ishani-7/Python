# def test():
#     global greet
#     greet="hello"
#     print("inside func",greet)
# test()
# print("outside func",greet)

# def test2():
#     global a
#     greet="Hello" + a
#     print("Inside the func global",greet)

# a="testing"
# test2()

#python class

'''
class Car(): #class name should start with capital
    def  car() #func name should start lower case

test=Car()

'''
# class Car(): #class vitra print chai na garne
#     no_of_wheels=4
#     no_of_seats=7

# obj = Car() #class intialize gareko
# print(obj.no_of_seats)
# print(obj.no_of_wheels)
# obj.color= "red"
# print(obj.color)

# obj1= Car()
# print(obj1.color) #yo chai garna mildaina cause obj.color vanera define garya cha, color class vitra define vako chaina

# print("-------------------------------")

# class Test():
#     a=10
#     b=100
#     def sum(self): #self chai common practice ho, aru j naam dida ni huncha
#         c=90
#         print(self.a+self.b-c) #c chai func vitra declare vako cha so aagadi self lekhna parena

# obj=Test()
# obj.sum()

# class Calc():
#     def add(self):
#         sum=self.a+self.b
#         return sum
#     def diff(self):
#         dif=self.a-self.b
#         return dif
#     def multi(self):
#         mul=self.a*self.b
#         return mul
#     def div(self):
#         divi=self.a/self.b
#         return divi
# obj=Calc()
# print(obj.add())
# print(obj.diff())
# print(obj.multi())
# print(obj.div())

# print("-------------------------------")

# class Test2():
#     def __init__(self):
#         # a="Hello world" #yesma self.a banayo vane balla calc le use garna milcha
#         self.a="Hello world" #yesma self.a banayo vane balla calc le use garna milcha
    
#     def calc(self):
#         print(f'the value of a is {self.a}') #yo class self.a bujhcha, constructor ma khojna mildaina

# obj=Test2()
# obj.calc()

# class Test2():
#     def __init__(self,*test):
#         self.test=test
    
#     def calc(self):
#         print(f'the value of a is {self.test}') 

# obj=Test2("Testing")
# obj.calc()

# class Calc():
#     def __init__(self,*args):
#          self.args=args
#     def add(self,*args):
#         sum=self.args+self.args
#         return sum
#     def diff(self,*args):
#         dif=self.args-self.args
#         return dif
#     def multi(self,*args):
#         mul=self.args*self.args
#         return mul
#     def div(self,*args):
#         divi=self.args/self.args
#         return divi
# obj=Calc()
# print(obj.add(10,100))
# print(obj.diff(10,100))
# print(obj.multi(10,100))
# print(obj.div(10,100))

class Student_Report():
    def __init__(self,*marks):
        self.marks=marks
        self.len_of_total_sub=len(marks)
    def marks_obtained(self):
        total_marks=0
        for i in self.marks:
            total_marks=total_marks+i
        return total_marks
    def percentage(self):
        perc=(self.marks_obtained()/self.len_of_total_sub)
        return perc
    def grade(self):
        perc=self.percentage()
        if perc>=80:
            grade="Distinction"
        elif perc<80 and perc>=60:
            grade="First Division"
        else:
            grade="Fail"
        return grade
    def result(self):
        total=self.marks_obtained()
        per=self.percentage()
        div=self.grade()
        result_data={
            "total":total,
            "percentage":per,
            "division":div
        }
        return result_data


obj=Student_Report(10,20,100,40,100,100)
print(obj.result())
data=obj.result()
final=f'''
Total obtain marks = {data.get('total')}
Percentage = {data.get('percentage')}
Division = {data.get('division')}
'''
print(final)