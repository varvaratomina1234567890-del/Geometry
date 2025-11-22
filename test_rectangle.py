import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        """Тест площади с нулевой стороной"""
        result = area(10, 0)
        self.assertEqual(result, 0)
    
    def test_area_square(self):
        """Тест площади квадрата"""
        result = area(10, 10)
        self.assertEqual(result, 100)
    
    def test_area_normal(self):
        """Тест площади обычного прямоугольника"""
        result = area(5, 7)
        self.assertEqual(result, 35)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевой стороной"""
        result = perimeter(10, 0)
        self.assertEqual(result, 20)
    
    def test_perimeter_square(self):
        """Тест периметра квадрата"""
        result = perimeter(10, 10)
        self.assertEqual(result, 40)
    
    def test_perimeter_normal(self):
        """Тест периметра обычного прямоугольника"""
        result = perimeter(5, 7)
        self.assertEqual(result, 24)
    
    def test_negative_sides(self):
        """Тест с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(-5, 10)

