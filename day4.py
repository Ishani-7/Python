# for i in "ishani":
#     print(i)

# a=[1,2,3,3,4332]
# print(type(a))
# print(a[3])
# #print(a[600]) #index out of range aaucha output ma
# print(a[-1])

# for i in ["My","name","is","Ishani"]:
#     print(i)

# for i in range(1,11,1):
#     print (i)

# print("Default increment value")
# for i in range(1,11):
#     print(i)

# print("decrement loop")
# for i in range(11,1,-1):
#     print(i)

# print("Default start value and increment value")
# for i in range(11):
#     print(i)

# a=67
# for i in range(1,11,1):
#     print(f"{a} * {i} = {a*i}")
    
# b=input("Enter a number: ") #input string ma lincha and concatenate gaarcha
# for i in range(1,11,1):
#     print(f"{b} * {i} = {b*i}")

# b=int(input("Enter a number: "))
# for i in range(1,11,1):
#     print(f"{b} * {i} = {b*i}")
    
# for i in range(1,10,1):
#     if i==4:
#         break
#     print(i)

# for i in range(1,10,1):
#     if i==4:
#         continue
#     print(i)

#isistance le chai data type ho ki haina check garcha

# a="Ishani"
# data= isinstance(a,str)
# print(data)

f=[1,2,"is","sa",3,23.4,"ishani"]
for i in f:
    if isinstance(i,str):
        continue
    print(i)
