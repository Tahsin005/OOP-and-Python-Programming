a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
# if a > b and a > c:
#     print(a, "is the greatest")
# elif b > a and b > c:
#     print(b, "is the greatest")
# else:
#     print(c, "is the greatest")



# Usign nested if-else:
if a > b:
    if a > c:
        print(a, "is the greatest number")
    else:
        print(c, "is the greatest number")
else:
    if b > c:
        print(b, "is the greatest number")
    else:
        print(c, "is the greatest number")