def isArmstrong(n, order):
    temp = n
    ans = 0
    while n > 0:
        digit = n % 10
        ans += (digit ** order)
        n //= 10
    return ans == temp

# user input

low = int(input("Enter the lower limit : "))
upp = int(input("Enter the upper limit : "))

for num in range(low, upp + 1):
    if isArmstrong(num, len(str(num))):
        print(num)