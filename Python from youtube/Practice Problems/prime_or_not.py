n = int(input())
flag = True
if n == 1:
    print("Not prime")
elif n > 1:
    for i in range(2, n, 1):
        if n % i == 0:
            flag = False
            break
    if flag == True:
        print("Prime")
    else:
        print("Not prime")
else:
    print("Enter a positive integer")