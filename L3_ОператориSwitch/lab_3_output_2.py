#Заміна оператора switch на спеціалізовані методи
class ShapeCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            self.calculate_circle_area(shape)
        elif isinstance(shape, Rectangle):
            self.calculate_rectangle_area(shape)
        elif isinstance(shape, Triangle):
            self.calculate_triangle_area(shape)
        else:
            print("Invalid shape type")

    def calculate_circle_area(self, circle):
        area = 3.14 * circle.radius * circle.radius
        print("Area of the circle:", area)

    def calculate_rectangle_area(self, rectangle):
        area = rectangle.length * rectangle.width
        print("Area of the rectangle:", area)

    def calculate_triangle_area(self, triangle):
        area = 0.5 * triangle.base * triangle.height
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

calculator = ShapeCalculator()
calculator.calculate_area(shape)
