# raining = True
# if raining == True: 
#     print("Fuck, it's raining")
#     print("if else in python is weired")
# else:
#     print("Suii")

num = int(input("Enter a number : "))
# if num % 2 == 0:
if num % 2 != 0:
    print("Even")
    if num > 10:
        print("And the number is greater than 10")
    else:
        print("and the number is not greater than 10")
else:
    print("Odd")