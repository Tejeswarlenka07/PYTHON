class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


s = Square(10)

print("THE AREA OF THE SQUARE = ", s.area())
print("THE PERIMETER OF THE SQUARE = ", s.perimeter())
