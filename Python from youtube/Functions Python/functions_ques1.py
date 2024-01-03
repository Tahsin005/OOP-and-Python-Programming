'''Write a python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument'''

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n - 1) * n

n = int(input())
fact = factorial(n)
print("Factorial of", n, "is :", fact)