from math import pi, sqrt


# Класс родитель для фигур
class Figure:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_square(self):
        pass


# Класс круг
class Circle(Figure):
    def __init__(self, name, R):
        super().__init__(name=name)
        self.radius = R

    def get_radius(self):
        return self.radius

    # Поиск площади - S = Pi*R^2
    def get_square(self):
        return round(pi * self.radius ** 2, 2)


# Класс треугольник
class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name=name)
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def get_sides(self):
        return self.side_a, self.side_b, self.side_c

    # Поиск площади - Формула Герона
    def get_square(self):
        semi_perim = (self.side_a + self.side_b + self.side_c) / 2
        return round(
            sqrt(semi_perim * (semi_perim - self.side_a) * (semi_perim - self.side_b) * (semi_perim - self.side_c)), 2)

    # Проверка на прямоугольный треугольник
    def right_triangle(self):
        sides = [self.side_a, self.side_b, self.side_c]
        hypoten = max(sides)
        sides.remove(hypoten)
        return hypoten ** 2 == sides[0] ** 2 + sides[1] ** 2
