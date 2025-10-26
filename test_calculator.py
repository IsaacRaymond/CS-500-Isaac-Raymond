import unittest
from calculator import calculator, display_menu

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-5, -5), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-2, 3), -6)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, -1), -5)

    def test_division_by_zero(self):
        self.assertEqual(divide(10, 0), "Error: Division by zero is not allowed.")


if __name__ == "__main__":
    unittest.main()