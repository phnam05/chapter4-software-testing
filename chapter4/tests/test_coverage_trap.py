# Chapter 4, section 4.6.3 "Limitations of coverage"
# This test raises coverage but asserts nothing, so it can never fail.
import unittest
from src.calculator import add

class TestCoverageTrap(unittest.TestCase):
    def test_coverage_trap(self):
        add(3, 5)   # no assertion
