

a=[1,2,2,2,2,[1,22,23],"ishani","hello","testing",["helllo","ishani"],"world"]
def flatten_list(data):
    flat_list=[]
    for i in data:
        if isinstance(i,list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list(a))

#lamda function