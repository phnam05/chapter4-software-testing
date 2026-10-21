# Chapter 4, section 4.6.1 (AAA pattern) and 4.6.2 (assertion methods)
import unittest
from src.calculator import add

class TestAdd(unittest.TestCase):
    def test_add_returns_correct_sum(self):
        # Arrange — set up inputs
        a = 3
        b = 5

        # Act — call the unit under test
        result = add(a, b)

        # Assert — compare actual output to expected output
        self.assertEqual(result, 8)

    def test_assertion_methods(self):
        # 4.6.2 "Equality and comparison" examples
        self.assertEqual(add(3, 5), 8)          # fails if not equal
        self.assertNotEqual(add(3, 5), 0)       # fails if equal
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)  # safe for floats
        self.assertTrue(add(1, 1) > 0)          # fails if expression is False
