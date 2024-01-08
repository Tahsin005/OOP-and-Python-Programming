class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def deduct(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 / num2
casio = Calculator()
sum = casio.add(10,3)
sub = casio.deduct(10,3)
prod = casio.multiply(10,3)
div = casio.divide(10,3)
print(sum, sub, prod, div)