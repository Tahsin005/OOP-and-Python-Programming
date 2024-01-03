'''Write a program to print sum from 1 to n'''
def sumofn(n):
    if n == 1:
        return 1
    return n + sumofn(n - 1)

print(sumofn(5))