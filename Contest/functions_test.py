import unittest
from unittest.mock import patch
from io import StringIO
import math

from force_resultant_calculator_functions import (
    validate_magnitude,
    validate_angle,
    validate_integer,
    force_collector_of_two_components,
    force_collector_of_three_components
)

from quadratic_equation_solver_function import quadratic_equation_solver
from triangle_solver import triangle_solver
from unit_converter_functions import *


class TestEngineeringCalculator(unittest.TestCase):

    # -------------------------
    # VALIDATION TESTS
    # -------------------------
    @patch("builtins.input", side_effect=["5"])
    def test_validate_magnitude(self, mock_input):
        self.assertEqual(validate_magnitude("Enter: "), 5.0)

    @patch("builtins.input", side_effect=["90"])
    def test_validate_angle(self, mock_input):
        self.assertAlmostEqual(validate_angle("Enter: "), math.pi / 2)

    @patch("builtins.input", side_effect=["3"])
    def test_validate_integer(self, mock_input):
        self.assertEqual(validate_integer("Enter: "), 3)

    # -------------------------
    # FORCE RESULTANT TESTS
    # -------------------------
    @patch("builtins.input", side_effect=["1", "10", "0"])
    def test_force_collector_of_two_components(self, mock_input):
        result = force_collector_of_two_components()
        expected = {"Force1": {"Fx": 10.0, "Fy": 0.0}}
        self.assertEqual(result, expected)

    @patch("builtins.input", side_effect=["1", "3", "4", "5"])
    def test_force_collector_of_three_components(self, mock_input):
        result = force_collector_of_three_components()
        expected = {"Force1": {"Fx": 3.0, "Fy": 4.0, "Fz": 5.0}}
        self.assertEqual(result, expected)

    # -------------------------
    # QUADRATIC TEST
    # -------------------------
    @patch("builtins.input", side_effect=["1", "-5", "6"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_quadratic_equation_solver(self, mock_stdout, mock_input):
        quadratic_equation_solver()
        self.assertIn("2.00", mock_stdout.getvalue())
        self.assertIn("3.00", mock_stdout.getvalue())

    # -------------------------
    # TRIANGLE SOLVER TEST
    # -------------------------
    @patch("builtins.input", side_effect=["3", "4", "90"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_triangle_solver(self, mock_stdout, mock_input):
        triangle_solver()
        output = mock_stdout.getvalue()
        self.assertIn("5.00", output)
        self.assertIn("6.00", output)

    # -------------------------
    # UNIT CONVERTER TESTS
    # -------------------------
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_feet(self, mock_stdout, mock_input):
        feet()
        self.assertIn("3.28", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["60"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_minutes(self, mock_stdout, mock_input):
        minutes()
        self.assertIn("1.00", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["0"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_fahrenheit(self, mock_stdout, mock_input):
        fahrenheit()
        self.assertIn("32.00", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["10"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_kilometers_per_hour(self, mock_stdout, mock_input):
        kilometers_per_hour()
        self.assertIn("36.00", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()