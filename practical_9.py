class Rectangle:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


a = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth: "))
r = Rectangle(b, a)
print("The area of rectangle is: ", r.area())
print("The perimeter is: ", r.perimeter())
