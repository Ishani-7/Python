# a=[1,2,3,4,5,67,4]
# print("Before adding",len(a))


# #append
# a.append(8)
# a.append([1,2,3,4])
# print("after adding",len(a))
# print(a)

# num=[1,2,3,[1,1,2,3]]
# sum=0
# sum1=0
# i=0
# for i in num:
#     if isinstance(i,list):
#         for j in i:
#             sum=sum+j
#     else:
#         sum=sum+i
# print(sum)

##insert
# a=[1,2,2,2,3]
# a.insert(99999,"ishani") #last ma gayera rakhcha 
# a.insert(-4,"hi")
# a.insert(0,[1,2,3,4])
# print(a)

# num=[1,2,5,4]
# num.append(3)
# num.append(44)
# num.sort()
# print(num)

#extend
# a=[1,2,3,3,3,2,2]
# b=["Ishani","sanjel"]
# a.extend(b)
# b.extend(a)
# print(a,b)

# num=[1,2,2,2,2,["sudan",[1]]]
# result=[]
# for i in num:
#     if isinstance(i,list):
#         result.extend(i)
#     else:
#         result.append(i)
# print(result)

# #concatenate "+"
# a=[1,2,3,3,3,2,2]
# b=["Ishani","sanjel"]
# print(a+b)

# #del
a=[1,2,3,2,3]
# #del a #entire a nei del gardincha 
# del a[0]
# print(a)

# #remove

# a.remove("3") #error aaucha cause list ma 3 string khojcha ani vettaudaina
# a.remove(3) 
# print(a)

# #pop
# a.pop()

#clear
a.clear