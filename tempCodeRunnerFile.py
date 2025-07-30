num=[1,2,3,[1,1,2,3]]
sum=0
sum1=0
i=0
for i in num:
    if isinstance(i,list):
        for j in i:
            sum=sum+j
    else:
        sum=sum+i
print(sum)
