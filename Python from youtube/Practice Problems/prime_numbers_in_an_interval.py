def isPrime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
            break
    return True

low = int(input("Enter the lower limit : "))
upp = int(input("Enter the upper limit : "))

for num in range(low, upp + 1):
    if num > 1:
        if isPrime(num):
            print(num)