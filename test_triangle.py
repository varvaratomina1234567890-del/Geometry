import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        """Тест площади с нулевой высотой"""
        result = area(10, 0)
        self.assertEqual(result, 0)
    
    def test_area_normal(self):
        """Тест площади обычного треугольника"""
        result = area(6, 4)
        self.assertEqual(result, 12)
    
    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        result = perimeter(5, 5, 5)
        self.assertEqual(result, 15)
    
    def test_perimeter_normal(self):
        """Тест периметра обычного треугольника"""
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)
    
    def test_negative_sides(self):
        """Тест с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(-1, 2, 3)
    
    def test_triangle_inequality(self):
        """Тест нарушения неравенства треугольника"""
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

