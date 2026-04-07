# test_functions.py
import unittest
import math
from unittest.mock import patch
from io import StringIO

# Import your functions
from functions import dot_product, cross_product, angle_between_vectors, vector_magnitude
from force_resultant_calculator_functions import vector_calculator_for_two_components, vector_calculator_for_three_components
from quadratic_equation_solver_function import quadratic_equation_solver
from triangle_solver import triangle_solver
from unit_converter_functions import feet, meters, pounds, kilograms, minutes, seconds, fahrenheit, celsius, kilometers_per_hour, meters_per_second


class TestEngineeringCalculator(unittest.TestCase):

    # ---------------- Vector Calculator ---------------- #
    @patch('builtins.input', side_effect=['2', '1', '2', '3', '4'])
    def test_dot_product(self, mock_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            dot_product()
            output = fake_out.getvalue()
            self.assertIn("Dot Product = 11", output)  # 1*3 + 2*4 = 11

    @patch('builtins.input', side_effect=['1', '0', '0', '0', '1', '0'])
    def test_cross_product(self, mock_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cross_product()
            output = fake_out.getvalue()
            self.assertIn("[0, 0, 1]", output)  # cross([1,0,0], [0,1,0])

    @patch('builtins.input', side_effect=['2', '1', '0', '0', '1'])
    def test_angle_between_vectors(self, mock_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            angle_between_vectors()
            output = fake_out.getvalue()
            self.assertIn("Angle = 90.00", output)  # perpendicular vectors

    @patch('builtins.input', side_effect=['2', '3', '4'])
    def test_vector_magnitude(self, mock_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            vector_magnitude()
            output = fake_out.getvalue()
            self.assertIn("Magnitude = 5.00", output)  # √(3²+4²)=5

    # ---------------- Quadratic Equation ---------------- #
    @patch('builtins.input', side_effect=['1', '-3', '2'])
    def test_quadratic_equation_solver(self, mock_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            quadratic_equation_solver()
            output = fake_out.getvalue()
            self.assertIn("x are 2.00 and 1.00", output)

    # ---------------- Triangle Solver ---------------- #
    @patch('builtins.input', side_effect=['3', '4', '5'])
    def test_triangle_solver_sss(self, mock_inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            triangle_solver()
            output = fake_out.getvalue()
            self.assertIn("Third side", output)
            self.assertIn("Area of triangle", output)

    # ---------------- Unit Converters ---------------- #
    @patch('builtins.input', side_effect=['1'])
    def test_feet(self, mock_inputs):
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                feet()
                output = fake_out.getvalue()
                self.assertIn("3.28 feet", output)

    @patch('builtins.input', side_effect=['3'])
    def test_celsius(self, mock_inputs):
        with patch('builtins.input', return_value='32'):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                celsius()
                output = fake_out.getvalue()
                self.assertIn("0.00°C", output)

    @patch('builtins.input', side_effect=['3'])
    def test_minutes(self, mock_inputs):
        with patch('builtins.input', return_value='120'):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                minutes()
                output = fake_out.getvalue()
                self.assertIn("2.00 minutes", output)


if __name__ == "__main__":
    unittest.main()