class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
c3 = c1 + c2  # This calls the __add__ method
print(c3.real, "+ i", c3.img) 

'''When we need to do some mathematical operation
we need to use operator overloading'''