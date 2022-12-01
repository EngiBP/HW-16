#Напишите код для описания геометрической фигуры.
#Создайте класс «прямоугольник» с помощью метода init(). На выходе в консоли вам необходимо получить площадь данной фигуры.

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'
    def get_area(self):
        return self.width * self.height

rect_1 = Rectangle(5, 10, 50, 100)
rect_2 = Rectangle(10, 20, 40, 200)

print(rect_1, rect_1.get_area())
print(rect_2, rect_2.get_area())