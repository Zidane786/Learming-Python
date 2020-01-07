# BMI calculator:-
weight,height,name=int(input("Enter your weight in kg:-")),float(input("Enter your height in metre:-")),input("Enter your name:-")
bmi=weight/(height*height)
print(name," Bmi is ",bmi," Which is overweight") if bmi>25 else print(name," Bmi is ",bmi," Which is underweight")