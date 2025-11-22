import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        """Тест площади с нулевым радиусом"""
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_area_normal(self):
        """Тест площади обычного круга"""
        result = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected)
    
    def test_perimeter_zero(self):
        """Тест длины окружности с нулевым радиусом"""
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_normal(self):
        """Тест длины обычной окружности"""
        result = perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(result, expected)
    
    def test_negative_radius(self):
        """Тест с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-5)

