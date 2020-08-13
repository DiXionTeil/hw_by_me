'''
Реализовать класс фигуры.
На основе фигуры реализовать класс треугольника,
        квадрата и прямоугольника с методами подсчета площади и периметра.
Методы должны возвращать значение, а не принтить (это важно)
'''
from math import sqrt


class Figures:
    def __init__(self, side_1, side_2=0):
        self.side_1 = side_1
        self.side_2 = side_2


class Triangle(Figures):
    def area(self):
        if self.side_2 != 0:
            # прямоугольный треугольник
            return (self.side_1 + self.side_2) / 2
        # равносторонний треугольник
        return round(sqrt(3) / 4 * pow(self.side_1, 2), 3)

    def perimeter(self):
        if self.side_2 != 0:
            # прямоугольный треугольник
            return round(sqrt(pow(self.side_1, 2) + pow(self.side_2, 2)) + self.side_1 + self.side_2, 3)
        # равносторонний треугольник
        return self.side_1 * 3


class Square(Figures):
    def area(self):
        if self.side_2 != 0:
            raise ValueError
        return pow(self.side_1, 2)

    def perimeter(self):
        if self.side_2 != 0:
            raise ValueError
        return self.side_1 * 4


class Rectangle(Figures):
    def area(self):
        if self.side_2 != 0:
            return self.side_1 * self.side_2
        raise ValueError

    def perimeter(self):
        if self.side_2 != 0:
            return self.side_1 * 2 + self.side_2 * 2
        raise ValueError


# ────────── * TESTING * ──────────

# триугольник
triangle1 = Triangle(5, 6)
print(triangle1.area())
print(triangle1.perimeter())
triangle2 = Triangle(8)
print(triangle2.area())
print(triangle2.perimeter())
print('─' * 10)

# квадрат
# ошибки
# square1 = Square(5, 6)
# print(square1.area())
# print(square1.perimeter())

# норм
square2 = Square(8)
print(square2.area())
print(square2.perimeter())
print('─' * 10)

# прямоугольник
# норм
rectangle1 = Rectangle(5, 6)
print(rectangle1.area())
print(rectangle1.perimeter())

# ошибки
# rectangle2 = Rectangle(8)
# print(rectangle2.area())
# print(rectangle2.perimeter())

# ─────────────────────────────────
