import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        """Тест площади с нулевой стороной"""
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_area_normal(self):
        """Тест площади обычного квадрата"""
        result = area(5)
        self.assertEqual(result, 25)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевой стороной"""
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_normal(self):
        """Тест периметра обычного квадрата"""
        result = perimeter(5)
        self.assertEqual(result, 20)
    
    def test_negative_side(self):
        """Тест с отрицательной стороной"""
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-5)

if __name__ == '__main__':
    unittest.main()