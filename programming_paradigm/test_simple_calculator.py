import unittest

from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):

        self.assertEqual(self.calc.add(10,20),30)
        self.assertEqual(self.calc.add(-6, -2), -8)

    def test_subtraction(self):

        self.assertEqual(self.calc.subtract(10,20),-10)
        self.assertEqual(self.calc.subtract(10, 15), -5)

    def test_multiplication(self):

        self.assertEqual(self.calc.multiply(10, 20),200)
        self.assertEqual(self.calc.multiply(-6, -2), 12)

    def test_division(self):

        self.assertEqual(self.calc.divide(10, 20),0.5)
        self.assertEqual(self.calc.divide(6, 0), None)