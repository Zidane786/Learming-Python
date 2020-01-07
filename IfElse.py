
name=input("Enter name of nominee:-")
age=int(input("Enter age of nominee:-"))
if age>18 and age<101:
    print("HURRAY!",name,"You can drive")
elif age>7 and age<18:
    print("OOPS SORRY!",name,"You cant drive")
elif age==18:
    print("You need to wait",name,"we will think about you")
else:
    print("Invalid Age!")
zid=[12,13,14,15,16,17]
print(12 in zid)
if 12 in zid:
    print("Its in the list")
print(7 not in zid)
if 7 not in zid:
    print("Its is not in the list")