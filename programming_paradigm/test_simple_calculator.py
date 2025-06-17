import unittest

from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        test_addition = calc.add(10, 20)
        self.assertEqual(test_addition,30)
        self.assertEqual(calc.add(-6, -2), -8)

    def test_subtract(self):
        calc = SimpleCalculator()
        test_subtraction = calc.subtract(10, 20)
        self.assertEqual(test_subtraction,-10)
        self.assertEqual(calc.subtract(10, 15), -5)

    def test_multiply(self):
        calc = SimpleCalculator()
        test_multiply = calc.multiply(10, 20)
        self.assertEqual(test_multiply,200)
        self.assertEqual(calc.multiply(-6, -2), 12)

    def test_divide(self):
        calc = SimpleCalculator()
        test_divide = calc.divide(10, 20)
        self.assertEqual(test_divide,0.5)
        self.assertEqual(calc.divide(6, 0), None)