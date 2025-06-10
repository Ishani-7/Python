a=1
b=11
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

print(2==2 and 1!=2)
print(3<5 or 3==2)
print(3>1 or 2==2)

greeting="Hello"
pronoun="Mr"
name="Abc"
txn_date="24 april"
acc_num=849202
amount=200
result=f"{greeting} {pronoun} {name} your transcation of {amount} on {txn_date} is successful"
print(result)

gpa=3.83
symbol_num=222
display=f"{greeting} {name},For symbol number '{symbol_num}' your overall gpa of SEE is {gpa}"
print(display)

a="hello"
print(a.upper())
print(a.lower())
print(a.title()) #aagadi ko letter capital
print(a.capitalize()) #aagadi ko letter capital
print(len(a)) #count character,space ni count huncha

b="I am a student and eat a lot of food"
print(b.count("a")) #a kati ota cha count garcha 
print(a.isdigit())  #a vitra digit cha ki chaina check garcha 
print(a.center(5))
print(a.endswith("o"))
print(a.isalpha())
print(a.isascii())
print(a.isdecimal())
print(a.isidentifier())