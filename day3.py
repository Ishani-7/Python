'''
if(1==2):
    print("I am true")
    print("I am true")
elif(1==1):
    print("I am True")
else:
    print("I am false")

'''
'''
GPA=3.8
Highest=4.0
if(GPA<Highest):
    print("Your position is second")
elif(GPA==Highest):
    print("Both are in same position")
else:
    print("Your position is first")
'''
'''
Percentage=35
if(Percentage>=0 and Percentage<=100):
    if(Percentage>=80 and Percentage<=100) :
        print("Your percentage is distinction")
    elif(Percentage<=80 and Percentage>=60) :
        print("Your percentage is first division")
    elif(Percentage>=60 and Percentage>=50) :
        print("Your percentage is second division")
    elif(Percentage<=50 and Percentage>=45) :
        print("Your percentage is third division")
    else:
        print("You didn't pass the exam")
else:
    print("invalid percentage")

'''

Percentage=input("Enter your percentage: ")
if(Percentage.isdigit()==True):
    if(int(Percentage)>=0 and int(Percentage)<=100):
        if(int(Percentage)>=80 and int(Percentage)<=100) :
            print("Your percentage is distinction")
        elif(int(Percentage)<=80 and int(Percentage)>=60) :
            print("Your percentage is first division")
        elif(int(Percentage)>=60 and int(Percentage)>=50) :
            print("Your percentage is second division")
        elif(int(Percentage)<=50 and int(Percentage)>=45) :
            print("Your percentage is third division")
        else:
            print("You didn't pass the exam")
    else:
            print("invalid percentage")
else:
     print("Invalid")

'''
data=input("Enter your value:")
print("Data is",type(data))

a=45
print("data is",type(a))
b=float(a)
print("data is",type(b))
'''

#result="m" if gender =="M" else "F" #single line if condition




