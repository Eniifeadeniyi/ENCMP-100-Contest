import unittest
from functions import *

class TestForEngineeringCalculatorFunctions(unittest.TestCase):
    def testThatForceCollectorOnlyTakesValidInput():
        actual = forceCollector("5,4")
        expected = []
        self.assertEqual(actual,expected)