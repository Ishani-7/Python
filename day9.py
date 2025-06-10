# #Dictionary:
# a={
#     "name":"Ishani",
#     "age":24
# }
# print(a["name"])
# print(a.keys())
# print(a.values())

# #print(a["ages"]) #error dekhaucha cause ages vanne key chaina
# print(a.get('ages','not found')) #chaina vane pachadi ko value dekhaucha

# #add to dict

# a["phone"]=12345 #key add garcha 

# a["age"]=23 #already vako key ma update garcha
# print(a)

# a.update({'name':"nikes","age":24,"phone":323212}) #bulk update garna chai yo use garne
# print(a)

# data={
#     'Name':"Ali",
#     "Age":23,
#     'height':6,
#     'weight':68,
#     'city':"peshwar"
# }
# print(len(data)) #lenght nikalcha

# del data # entire data delete gardincha same as list
# print(data)

# del data['Age'] #age key del gardincha
# print(data)

# data.pop('Name')
# print('pop',data)
# data.popitem()
# print("popitem",data)

# a={
#     "name":"xyz",
#     "age":23,
#     "phone":{"type":"ntc","mobile":987489203}
# }
# print(f"my phone number of {a['phone']['type']} is {a['phone']['mobile']}")

# a={
#     "name":"xyz",
#     "age":23,
#     "phone":[
#         {"type":"ntc","mobile":987489203},
#         {"type":"ncell","mobile":987203},
#         {"type":"smart","mobile":987433389203},
#     ]
# }
# phone= a['phone']
# for i in phone:
#     print(f"my phone number of {i['type']} is {i['mobile']}")


##Tuples:

#thistuple=("apple") #comma rakhena vane string bujcha
# thistuple=("apple",) 
# print(type(thistuple))

# print(len(thistuple))

# thislist=list(thistuple) #tuple to list change garne ani add garne
# print(type(thislist))
# thislist.append("Hello")
# print(tuple(thislist)) #back to tuple


##Set:

data={1,2,3,2,12,"ishani",33333,2,2,2,2} #duplicate value print hudaina,hataidincha
print(data)

data= [1,1,1,1,2,3,2] 
data_set=set(data) #set le duplicate hataucha
print(data_set)
data_list=list(data_set) 
data_list.remove(1) #duplicate hatisakesi euta 1 remove garda sabbai remove huncha
print(data_list)