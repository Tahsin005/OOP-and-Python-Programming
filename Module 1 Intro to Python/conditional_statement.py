num1 = 15
num2 = 20

if num1 == num2:
    print("The numbers are equal")
    print("Python is Weird")
elif num1 > num2:
    text = f"{num1} is greater than {num2}"
    print(text)
    print("Executing the else if (elif) condition number 1")
elif num1 >= num2:
    text = f"{num1} is greater than equal to {num2}"
    print(text)
    print("Executing the else if (elif) condition number 2")
else:
    text = f"{num1} is less than {num2}"
    print(text)
    print("Executing the else condition")
    

boss = False
# if boss is True:
# if boss is not False:
# if boss != False:
if boss == False:
    print("Lunch er pore ashen")
else:
    print("Sir ekkhoni kore dibo")
    
# Nested Conditions
if boss == True:
    if num1 < 12:
        print("Boss is True and the number is less than 12")
    else:
        print("Boss is True but the valus is not less than 12")
elif boss != True:
    if num2 == 20:
        print("Boss is not True / Boss is False and the number 2 is equal to 20")