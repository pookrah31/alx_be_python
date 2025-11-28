import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    # Addition tests
    def test_add(self):
        self.assertAlmostEqual(self.calculator.add(2, 3), 5)
        self.assertAlmostEqual(self.calculator.add(-1, 1), 0)
        self.assertAlmostEqual(self.calculator.add(-1, -1), -2)
        self.assertAlmostEqual(self.calculator.add(0, 0), 0)
        self.assertAlmostEqual(self.calculator.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calculator.add(-2.5, 2.5), 0.0)
        self.assertAlmostEqual(self.calculator.add(1e10, 1e10), 2e10)
        self.assertAlmostEqual(self.calculator.add(1e-10, 1e-10), 2e-10)

    # Subtraction tests
    def test_subtract(self):
        self.assertAlmostEqual(self.calculator.subtract(5, 3), 2)
        self.assertAlmostEqual(self.calculator.subtract(-1, 1), -2)
        self.assertAlmostEqual(self.calculator.subtract(-1, -1), 0)
        self.assertAlmostEqual(self.calculator.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calculator.subtract(3.5, 2.5), 1.0)
        self.assertAlmostEqual(self.calculator.subtract(-2.5, -2.5), 0.0)
        self.assertAlmostEqual(self.calculator.subtract(1e10, 5e9), 5e9)
        self.assertAlmostEqual(self.calculator.subtract(1e-10, 5e-11), 5e-11)

    # Multiplication tests
    def test_multiply(self):
        self.assertAlmostEqual(self.calculator.multiply(2, 3), 6)
        self.assertAlmostEqual(self.calculator.multiply(-1, 1), -1)
        self.assertAlmostEqual(self.calculator.multiply(-1, -1), 1)
        self.assertAlmostEqual(self.calculator.multiply(0, 5), 0)
        self.assertAlmostEqual(self.calculator.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calculator.multiply(-2.5, 2), -5.0)
        self.assertAlmostEqual(self.calculator.multiply(1e5, 1e5), 1e10)
        self.assertAlmostEqual(self.calculator.multiply(1e-5, 1e-5), 1e-10)

    # Division tests
    def test_divide(self):
        self.assertAlmostEqual(self.calculator.divide(6, 3), 2)
        self.assertAlmostEqual(self.calculator.divide(-6, 2), -3)
        self.assertAlmostEqual(self.calculator.divide(-6, -2), 3)
        self.assertAlmostEqual(self.calculator.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calculator.divide(-7.5, 2.5), -3.0)
        self.assertAlmostEqual(self.calculator.divide(1e10, 1e5), 1e5)
        self.assertAlmostEqual(self.calculator.divide(1e-10, 1e-5), 1e-5)

    # Division by zero tests (check for None)
    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.divide(10, 0))
        self.assertIsNone(self.calculator.divide(-10, 0))
        self.assertIsNone(self.calculator.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
