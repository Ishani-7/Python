#while loop

# i=10
# while(i<=10):
#     print("Testing")
#     i=i+1

# while True:
#     print(1)
#     break

# #multiplication using while loop
# a=int(input("enter a number: "))
# i=1
# while(i<=10):
#     print(f'{a} * {i} = {a*i}')
#     i=i+1

# i=1
# while(i<=10):
#     if i==4:
#         break
#     print("Hi",i)
#     i=i+1
# print("--------------")
# j=1
# while(j<=10):
#     print("Hi",j)
#     if j==7:
#         continue
#     j=j+1

# a=[1,"Test",True,2,3,4,4,5,1,2,"Hello","HI"]
# b=len(a)
# i=0
# while(i<=b-1):
#     if isinstance(a[i],int):
#         if isinstance(a[i],bool):
#             i=i+1
#             continue
#         if a[i]==5:
#             break
#         print(a[i])
#         i=i+1
#     else:
#         i=i+1
#         continue

n=100
inp=0
while(True):
    inp=int(input("Enter a number:"))
    if inp==n:
        print("You won")
        break
    else:
        print("You Lost")
