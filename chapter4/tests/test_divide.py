# Chapter 4, section 4.6.2 (assertRaises / assertRaisesRegex)
# and 4.6.3 (one test per branch for 100% branch coverage)
import unittest
from src.calculator import divide

class TestDivide(unittest.TestCase):
    def test_divide_raises_on_zero(self):
        # Arrange
        a = 10
        b = 0

        # Act + Assert — the exception is the expected output
        with self.assertRaises(ValueError):
            divide(a, b)

    def test_divide_raises_correct_message(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5.0)   # exercises the normal branch

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)                       # exercises the guard branch
