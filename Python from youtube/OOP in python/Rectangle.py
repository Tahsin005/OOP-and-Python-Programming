class Rectangle:
    def set_dimensions(self,width,height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def parameter(self):
        p = 2 * (self.width + self.height)
        return p

rec1 = Rectangle()
rec1.set_dimensions(5,10)
print(rec1.width, rec1.height)
print(rec1.calculate_area())
print(rec1.parameter())