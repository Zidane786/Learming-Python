#Pattern Printing:-

"""
Input=Integer n
Boolean Variable =True or False
Star pattern Depend upon Integer n Consider n=5 in this case
If True :-
*
**
***
****
*****

If False:-
*****
****
***
**
*
"""
n=int(input("How many Row you want to print"))
num=int(input("Type 1 or 0"))
true_false=bool(num)


if true_false==True:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif true_false==False:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:
    print("Wrong input in Type 1 or 0")
for i in range(n,0,-1):
    print(i)