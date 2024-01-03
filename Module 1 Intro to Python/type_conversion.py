# num = 21
# print(type(num))

# string_representation_of_num = str(num)
# name = (str)(num)
# print(type(string_representation_of_num))
# print(type(name))


# Difference between float and decimal
from decimal import Decimal, getcontext
float1 = 0.1
float2 = 0.2 
result_float = float1 + float2


getcontext().prec = 10

decimal_number1 = Decimal("0.1")
decimal_number2 = Decimal("0.2")

result_decimal = decimal_number1 + decimal_number2

print("Result in float", result_float)
print("Result in decimal", result_decimal)