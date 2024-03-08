import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
