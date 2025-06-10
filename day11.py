# #keyword argument
# print("Positional")
# def test(first,last):
#     print(first,last)

# test("ishani","sanjel")
# test("sanjel","Ishani") #last name chai ishani vayera jancha call garda

# print("Keyword")
# def test(first,last):
#     print(first,last)

# test(first="ishani",last="sanjel")
# test(last="sanjel",first="ishani") #jata rakheni last name sanjel nei bujhcha

# print("Default+keyword")
# def test(first,last="sanjel"):
#     print(first,last)

# test(first="ishani")
# test(first="ishani",last="karki")

# a=[1,2,2,"2",2,2,2,2]
# sum=0
# for i in a:
#     sum=sum+int(i)
# print(sum)

# #positional arbitary function
# def testing(*data): #yesle garda chai jati pani data pathauna payo,* rakhena vane 10 positional argument matra magcha tyo vadna badi mildaina
#     sum=0
#     for i in data:
#         if not isinstance(i,int):
#             return "parameter should be in number"
#         sum=sum+i
#     return sum

# print(testing(1,1,1,1,1,2,32,"1",1,2)) #data kei pathayena vane 0 aucha output

# def average(*data):
#     avg=0
#     sum=0
#     for i in data:
#         if isinstance(i,int):
#             sum=sum+i
#             avg=sum/len(data)
        
#     return avg

# print("The average of given number is: ",average(2,2,2,2,3))

#arbitary keyword argument
# def test4(**data):
#     print(data)

# test4(name="hello",test="testing")

# #merging two dictionaries
# def merge_dicts(**data1):
#     dicts1= data1.get('dicts1')
#     dicts2= data1.get('dicts2')
#     dicts1.update(dicts2)
#     return dicts1

# dicts1={
#     "name1":"ishani",
#     "adress":"patan"
# }
# dicts2={
#     "name2":"nikesh",
#     "age":23
# }
# print(merge_dicts(dicts1=dicts1,dicts2=dicts2))

#greeting
# def create_greeting(**info):
#     print(f"Hello {(info['name1']}, you're {info} from {info}")


# print(create_greeting(name1="ishani",age=23,address="patan"))

# def count(**num):
#     length=len(num)
#     print("Total number is",length)
# count(number=(2,1,2))

# #positional argument,arb positional,arb keyword (commonly used chai last ko 2 ta)
# def all_parameter(a,*args,**kwargs): #**kwargs pachadi a or *args rakhna mildaina
#     print(a,args,kwargs) 
# all_parameter(1,1,1,1,1,1,1,name="ishani")

#flexible calculator
def flexible_calc(*args,**kwargs):
    operation=kwargs.get('operation').lower()
    if operation=="add":
        for i in args:
            sum=0
            sum=sum+i
        return sum
    elif operation=="diff": #yo
            
            diff=diff-i
            return diff
    elif operation=="mul":
        mul=1
        for i in args:
            mul=mul*i
        return mul
    elif operation=="div": #yo
            div=div/i
            return div
    else:
            return "wrong input"

print(flexible_calc(1,2,operation="div"))