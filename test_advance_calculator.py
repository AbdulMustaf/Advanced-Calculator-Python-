import unittest
from advanced_calculator import AdvanceCalculator

class TestAdvanceCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = AdvanceCalculator()

    # Test Basic Operations
    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 7), 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(15, 3), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 3), 8)

    # Test Factorial
    def test_factorial(self):
        self.assertEqual(self.calculator.factorial(5), 120)
        self.assertEqual(self.calculator.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.calculator.factorial(-3)

    # Test Prime Check
    def test_is_prime(self):
        self.assertTrue(self.calculator.is_prime(7))
        self.assertFalse(self.calculator.is_prime(4))
        self.assertFalse(self.calculator.is_prime(1))

    # Test Trigonometric Functions
    def test_sine(self):
        self.assertAlmostEqual(self.calculator.sine(30), 0.5, places=2)

    def test_cosine(self):
        self.assertAlmostEqual(self.calculator.cosine(60), 0.5, places=2)

    def test_tangent(self):
        self.assertAlmostEqual(self.calculator.tangent(45), 1.0, places=2)

    # Test Logarithms
    def test_logarithm(self):
        self.assertAlmostEqual(self.calculator.logarithm(100, 10), 2, places=2)
        with self.assertRaises(ValueError):
            self.calculator.logarithm(-10, 10)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(self.calculator.natural_logarithm(2.71828), 1, places=2)
        with self.assertRaises(ValueError):
            self.calculator.natural_logarithm(0)

    # Test Exponential
    def test_exponential(self):
        self.assertAlmostEqual(self.calculator.exponential(1), 2.71828, places=2)

    # Test Memory Operations
    def test_memory_operations(self):
        self.calculator.store_memory(10)
        self.assertEqual(self.calculator.recall_memory(), 10)
        self.calculator.clear_memory()
        self.assertEqual(self.calculator.recall_memory(), 0.0)

    # Test History
    def test_history(self):
        self.calculator.evaluate_expression("2 + 3")
        self.assertEqual(self.calculator.show_history(), "2 + 3 = 5")
        self.calculator.undo_last_operation()
        self.assertEqual(self.calculator.show_history(), "No history available.")

if __name__ == "__main__":
    unittest.main()
