''' Operators Precedence
    ()
    **
    /, //, %
    *
    +, -
    Bitswise shift (>>, <<)
    &, |, ^
    Comparison (==, !=, >, <, >=, <=)
'''

# Arithmatic operators
n1 = 10
n2 = 5
# addition
print(n1 + n2)

# sutraction
print(n1 - n2)

# multiplication
print(n1 * n2)

#division
print(n1 / n2)
# / operator does the operations in float 
''' To do floor(kind of like integer division in c / c++) division (//) operator is used'''

print(n1 // n2)

# modulus
print(n2 % n1)

# exponentiation
print(2 ** 5)

# Comparison operators
print(2 <= 5)

# Logical operators
expression1 = 2 > 1
expression2 = 5 < 4
print(expression1 and expression2)
print(expression1 or expression2)
print(not(expression1))
print(not(expression2))

# Identity operators(is, is not)
x = 1
y = 2
print("if x is y :", x is y)
print("if x is not y :", x is not y)

# Membership operators(in, not in)
fruits = ["apple", "banana", "cherry"]
print("if banana is present in fruits :", "banana" in fruits)
print("if mango is present in fruits :", "mango" not in fruits)

# Bitwise operators
a = 5
b = 3
print("a and b :", a & b)
print("a or b :", a | b)
print("a xor b :", a ^ b)