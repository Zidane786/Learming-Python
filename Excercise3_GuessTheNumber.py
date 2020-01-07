"""""
Problem:-Guess the number
isme ek number diya hai jo actual(hidden} hai or fir hame kaha gaya hai ki tumhare paas n number of guessing hai or fir guess kero number
agar number jo guess kiya wo actual number se chota hai to print kero jo number guess kiya hai wo actual number se chota hai
agar wo number actual number se bada hai to print kero ki number actual number se bada hai
or agar jo number guess kiya wo actual number hai to print kero ki congratulation aapne sahi number guess kiya hai
or fir print kero ki tumhare paas itni guessing bachi hai jab guessing number galat enter kiya ho
jab hamari n number of guessing khatam ho jaye to print kero ki game over!!!
"""
number_of_guess=int(input("Enter the limit to guess:-"))
actual_number=18
i=1
while(i<=number_of_guess):
    guessing_number=int(input("Enter the guessed number:-"))
    if guessing_number<actual_number:
        print("Your guessed Number is Smaller Than Actual Number")
    elif guessing_number==actual_number:
        print('Congratulation you guess Right Number!!')
        break
    else:
        print("Your guessed Number is Bigger Than Actual Number")
    number_of_guess=number_of_guess-1
    print(number_of_guess," guessing are remaining")
    if number_of_guess==0:
        print("game over!!!")