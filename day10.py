# #function

# def test():
#     print("hello world")

# test() #javascript ma function call aagadi garna ni milcha jun python ma mildaina function pachi matra call garne

# print("this is function call",test()) #none aucha kina ki return chaina

# def test2():
#     return "hello world"
# print("this is function call",test2())

# def test2():
#     return 1,2,"hello"
# print("this is function call",test2()) #output tuple ma aaucha default 

# def test3():
#     a=input("Enter your name:")
#     return a
# print(test3())

#positional arguments
# def user_info(a,b,c):  #argument
#     data={
#         "name":a,
#         "age":b,
#         "adress":c
#     }
#     return data
# print(user_info("ishani",25,"balaju")) #parameter


# def calc(a,b):
#     return a+b,a-b,a*b,a/b

# print("The addition,subtraction,multiplication and division of two number is: ",calc(2,3))

#default argument

def area(pie=3.14):
    formula=pie*7*7
    return formula
print("area of circle is",area()) #kei parameter chaina vane default mathi kei use garcha
print("area of circle is",area(5)) #value pathayesi tala ko value chai use garcha

def area(r,pie=3.14):  #default argument sadhai last ma aaucha 
    formula=pie*r*r
    return formula
print("area of circle default is",area(7)) 
print("area of circle non default is",area(7,33)) 

def info(a,c,b="sanjel"):
    data={
        "name":a,
        "surname":b,
        "age":c
    }
    return data

print("default surname",info("ishani",23))
print("non default surname",info("ishani",23,"karki"))