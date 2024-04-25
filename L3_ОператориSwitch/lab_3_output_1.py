#Перетворення коду з оператором switch на поліморфізм
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of the circle:", area)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area of the rectangle:", area)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area of the triangle:", area)

# Приклад використання
shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")

if shape_type == "circle":
    radius = float(input("Enter the radius of the circle: "))
    shape = Circle(radius)
elif shape_type == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    shape = Rectangle(length, width)
elif shape_type == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    shape = Triangle(base, height)
else:
    print("Invalid shape type")

shape.calculate_area()
