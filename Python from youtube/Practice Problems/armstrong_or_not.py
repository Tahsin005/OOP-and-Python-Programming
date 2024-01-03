def isArmstrong(n, order):
    temp = n
    ans = 0
    while n > 0:
        digit = n % 10
        ans += (digit ** order)
        n //= 10
    return ans == temp
n = int(input())
length = str(n)
if isArmstrong(n, len(length)):
    print("YES")
else:
    print("NO")