'''Implement exception handling in python by showing division operation'''
'''You can show exception - "ZeroDivisionError
input: a = 10, b = 2
output: 
    Cleanup: Division operation completed.
    5

input: a = 5, b = 0
output:
    Error: Cannot divide by zero
'''
a = int(input())
b = int(input())

try:
    result = a / b
except ZeroDivisionError:
    result = None
    print("Error: Cannot divide by zero")
finally:
    print("Division operation completed: ", result)