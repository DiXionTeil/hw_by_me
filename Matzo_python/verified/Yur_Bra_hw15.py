'''
Реализовать класс фигуры.
На основе фигуры реализовать класс треугольника,
        квадрата и прямоугольника с методами подсчета площади и периметра.
Методы должны возвращать значение, а не принтить (это важно)
'''
from math import sqrt


class Figures:
    def __init__(self, side_1):
        self.side_1 = side_1

    @property
    def side_1(self):
        return self._side_1

    @side_1.setter
    def side_1(self, s_1):
        if s_1 > 0:
            self._side_1 = s_1
        else:
            raise ValueError


class Triangle(Figures):
    def __init__(self, side_1, side_2=0):
        # self._validate_figure(side_1, side_2)
        super().__init__(side_1)
        self.side_2 = side_2

    @property
    def side_2(self):
        return self._side_2

    @side_2.setter
    def side_2(self, s_2):
        if s_2 > 0:
            self._side_2 = s_2
        elif s_2 == 0:
            self._side_2 = None
        else:
            raise ValueError

    # def _validate_figure(self, side_1, side_2):
    #     if side_1 <= 0:
    #         raise ValueError
    #     elif side_2 <= 0:
    #         raise ValueError

    def area_rectangular(self):
        return self.side_1 * self.side_2 // 2

    def area_isosceles(self):
        return round(self.side_1 * self.side_2, 2)

    def area_equilateral(self):
        return round(pow(self.side_1, 2) * sqrt(3) / 4, 2)

    def perimeter_rectangular(self):
        return round(sqrt(pow(self.side_1, 2) + pow(self.side_2, 2)) + self.side_1 + self.side_2, 2)

    def perimeter_isosceles(self):
        return round(2 * (sqrt(pow(self.side_1, 2) + pow(self.side_2, 2)) + self.side_2), 2)

    def perimeter_equilateral(self):
        return self.side_1 * 3


class Square(Figures):
    def area(self):
        return pow(self.side_1, 2)

    def perimeter(self):
        return self.side_1 * 4


class Rectangle(Figures):
    def __init__(self, side_1, side_2):
        super().__init__(side_1)
        self.side_2 = side_2

    @property
    def side_2(self):
        return self._side_2

    @side_2.setter
    def side_2(self, s_2):
        if s_2 > 0:
            self._side_2 = s_2
        else:
            raise ValueError

    def area(self):
        return self.side_1 * self.side_2

    def perimeter(self):
        return self.side_1 * 2 + self.side_2 * 2


# ────────── * TESTING * ──────────

# триугольник
triangle1 = Triangle(5, 3)
print(triangle1.area_rectangular())
print(triangle1.area_isosceles())
print(triangle1.area_equilateral())
print(triangle1.perimeter_rectangular())
print(triangle1.perimeter_isosceles())
print(triangle1.perimeter_equilateral())
print('─' * 10)

# квадрат
square2 = Square(2)
print(square2.area())
print(square2.perimeter())
print('─' * 10)

# прямоугольник
rectangle1 = Rectangle(5, 3)
print(rectangle1.area())
print(rectangle1.perimeter())

# ─────────────────────────────────
