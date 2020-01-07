""""
PROBLEM:- Faulty Calculator
agar wo jo below shown calculation kere to galat answer dena hai
i.e
45*3=555
1232+234=20
56/6=212
9393-932=122
8969%2=0
isko chodke jo bhi calculation kere uska answer sahi dega calculator
"""
while(True):
    print("Type AC or ac in operator to Stop the calculator")
    operator = input("Enter the Operator:-")
    if operator=="AC" or operator=="ac":
        print("Calculator Stoped!!!")
        break
    num1 =int(input("Enter First Number:-"))
    num2 = int(input("Enter Second Number:-"))
    if (num1 == 45 and num2 == 3) and (operator == "*"):
        print("Multiplication is ",int("555"))
    elif num1 == 1232 and num2 == 234 and operator == "+":
        print("Sum is ",int("20"))
    elif num1==56 and num2==6 and operator=="/":
        print("Division is ",int("212"))
    elif num1==9393 and num2==932 and operator=="-":
        print("Subtraction is ",int("122"))
    elif num1==8969 and num2==2 and operator=="%":
        print("Remainder is ",int("0"))
    elif operator=="+":
        sum=num1+num2
        print("Sum is ",sum)
    elif operator=="/":
        div=num1/num2
        print("Division is ",div)
    elif operator=="*":
        mul=num1*num2
        print("Multiplication is ",mul)
    elif operator=="%":
        rim=num1%num2
        print("Remainder is ",rim)
    elif operator=="-":
        sub=num1-num2
        print("Subtraction is ",sub)
    else:
        print("Something went wrong check your Input again")