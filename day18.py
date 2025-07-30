#exception handling
# a=10
# # print(b) #name error aaucha 
# try:
#     print(b)

# except NameError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("Something went wrong")

# a=1
# b=2
# try:
#     print(a+d)
# except NameError as e:
#     print(e)

# #file handling

# f=open('test/hello.txt',"r")
# print(f.read())

# f=open("test/date.txt","w")
# f.write("hey")
# f.close()

# f=open("test/date.txt","a")
# f.write("\n hey") #append le last ma gayera rakhcha
# f.close()


# date="2082-03-02" #manually date rakhne
def error(e):
    f=open('test/{date}error.log',"a")
    f.write(f'\n {str(e)}')
    f.close()
    try:
        print(Hello)
    except ValueError as e:
        error(e)
    except:
       error(e)
    