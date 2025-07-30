import mysql.connector
connector=mysql.connector.connect(
    host='localhost',
    user='root',
    # port=3306 #port change garya chaina vane na rakhda vayo
)
#create
print(connector)
cursor=connector.cursor()
# cursor.execute(".........................")
# connector.commit()

#delete
cursor.execute("Delete from `student` where name= 'hello world'")
connector.commit()

#select
cursor.execute("select * from `student`")
result=cursor.fetchall()
print(result)

"""
C:create
R:read
U:update
D:Delete
"""
#lambda function
def data(a,b): #using function
    return a+b
print(data(1,2))

x=lambda a,b : a+b
print(x,(1,2))

test=[]
for i in range(1,10):
    test.append(i)

#same but using one line

data=[i for i in range(1,10)]
print(test)
print(data)

#os library
import os
os.remove("test.pt") #remove gardincha