import unittest
import Figure

# 9 Unit-тестов для нахождения площади круга и треугольника, проверка на прямоугольный треугольник
class FigureTestCase(unittest.TestCase):
    def test_square_circle_1(self):
        circle = Figure.Circle('круг 1', 2)
        self.assertEqual(circle.get_square(), 12.57)

    def test_square_circle_2(self):
        circle = Figure.Circle('круг 2', 10)
        self.assertEqual(circle.get_square(), 314.16)

    def test_square_circle_3(self):
        circle = Figure.Circle('круг 3', 8.5)
        self.assertEqual(circle.get_square(), 226.98)

    def test_square_triangle_1(self):
        triangle = Figure.Triangle('треугольник 1', 2, 2, 2)
        self.assertEqual(triangle.get_square(), 1.73)

    def test_square_triangle_2(self):
        triangle = Figure.Triangle('трейгольник 2', 10, 10, 10)
        self.assertEqual(triangle.get_square(), 43.3)

    def test_square_triangle_3(self):
        triangle = Figure.Triangle('треугольник 3', 2, 3, 4)
        self.assertEqual(triangle.get_square(), 2.9)

    def test_right_triangle_1(self):
        triangle = Figure.Triangle('треугольник 1', 2, 2, 2)
        self.assertEqual(triangle.right_triangle(), False)

    def test_right_triangle_2(self):
        triangle = Figure.Triangle('трейгольник 2', 6, 8, 10)
        self.assertEqual(triangle.right_triangle(), True)

    def test_right_triangle_3(self):
        triangle = Figure.Triangle('треугольник 3', 3, 4, 5)
        self.assertEqual(triangle.right_triangle(), True)


if __name__ == "__main__":
    unittest.main()
