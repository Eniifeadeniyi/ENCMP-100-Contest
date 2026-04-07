import unittest
from unittest.mock import patch
import math

# Import all functions from your modules
from vector_calculator import dot_product, cross_product, vector_magnitude, angle_between_vectors
from quadratic_equation_solver_function import quadratic_equation_solver
from triangle_solver2 import SSS, SSA1, SSA2
from force_resultant_calculator_functions2 import vector_calculator_for_two_components, vector_calculator_for_three_components
from unit_converter_functions import feet, meters, pounds, kilograms, minutes, seconds, fahrenheit, celsius, kilometers_per_hour, meters_per_second

# ---------------------------
# Helper functions for mocks
# ---------------------------

def mock_inputs(inputs):
    """Return a side_effect function to simulate input()."""
    def side_effect(_):
        return str(inputs.pop(0))
    return side_effect

# ---------------------------
# Unit Tests
# ---------------------------

class TestEngineeringCalculator(unittest.TestCase):

    # ---------------------------
    # Vector Calculator Tests
    # ---------------------------
    @patch("builtins.input", side_effect=mock_inputs([3, 1, 2, 3, 4, 5, 6]))
    def test_dot_product(self, mock_input):
        # Should compute dot product of v1=[1,2,3], v2=[4,5,6] -> 32
        with patch("builtins.print") as mock_print:
            dot_product()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Dot Product = 32" in p for p in printed))

    @patch("builtins.input", side_effect=mock_inputs([1,2,3,4,5,6]))
    def test_cross_product(self, mock_input):
        # v1=[1,2,3], v2=[4,5,6] -> cross product = [-3,6,-3]
        with patch("builtins.print") as mock_print:
            cross_product()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Cross Product = [-3, 6, -3]" in p for p in printed))

    @patch("builtins.input", side_effect=mock_inputs([3, 1,0,0, 0,1,0]))
    def test_vector_magnitude(self, mock_input):
        with patch("builtins.print") as mock_print:
            vector_magnitude()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Magnitude = 1.00" in p for p in printed))

    @patch("builtins.input", side_effect=mock_inputs([3, 1,0,0, 0,1,0]))
    def test_angle_between_vectors(self, mock_input):
        with patch("builtins.print") as mock_print:
            angle_between_vectors()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Angle = 90.00" in p for p in printed))

    # ---------------------------
    # Quadratic Solver Tests
    # ---------------------------
    @patch("builtins.input", side_effect=mock_inputs([1, -3, 2]))
    def test_quadratic_two_roots(self, mock_input):
        with patch("builtins.print") as mock_print:
            quadratic_equation_solver()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("x are 2.00 and 1.00" in p for p in printed))

    @patch("builtins.input", side_effect=mock_inputs([1, 2, 1]))
    def test_quadratic_one_root(self, mock_input):
        with patch("builtins.print") as mock_print:
            quadratic_equation_solver()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("one real solution: x = -1.00" in p for p in printed))

    @patch("builtins.input", side_effect=mock_inputs([1, 1, 1]))
    def test_quadratic_no_real(self, mock_input):
        with patch("builtins.print") as mock_print:
            quadratic_equation_solver()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("no real solutions" in p for p in printed))

    # ---------------------------
    # Triangle Solver Tests
    # ---------------------------
    @patch("builtins.input", side_effect=mock_inputs([3,4,5]))
    def test_SSS_triangle(self, mock_input):
        with patch("matplotlib.pyplot.show"):
            # Should run without error
            SSS()

    @patch("builtins.input", side_effect=mock_inputs([3,4,30]))
    def test_SSA1_triangle(self, mock_input):
        with patch("matplotlib.pyplot.show"):
            SSA1()

    @patch("builtins.input", side_effect=mock_inputs([3,4]))
    def test_SSA2_triangle(self, mock_input):
        with patch("matplotlib.pyplot.show"):
            SSA2()

    # ---------------------------
    # Force Resultant Calculator Tests
    # ---------------------------
    @patch("builtins.input", side_effect=mock_inputs([2, 10, 0, 20, 90]))
    def test_vector_calculator_for_two_components(self, mock_input):
        with patch("builtins.print") as mock_print, patch("matplotlib.pyplot.show"):
            vector_calculator_for_two_components()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Resultant Force:" in p for p in printed))

    @patch("builtins.input", side_effect=mock_inputs([2, 1,2,3, 4,5,6]))
    def test_vector_calculator_for_three_components(self, mock_input):
        with patch("builtins.print") as mock_print, patch("matplotlib.pyplot.show"):
            vector_calculator_for_three_components()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Resultant Force" in p for p in printed))

    # ---------------------------
    # Unit Converter Tests
    # ---------------------------
    @patch("builtins.input", side_effect=mock_inputs([1]))
    def test_feet_meters_conversion(self, mock_input):
        with patch("builtins.print") as mock_print:
            feet()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue("meters is equal to" in printed[0])

    @patch("builtins.input", side_effect=mock_inputs([3]))
    def test_minutes_seconds_conversion(self, mock_input):
        with patch("builtins.print") as mock_print:
            minutes()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue("seconds is equal to" in printed[0])

    @patch("builtins.input", side_effect=mock_inputs([100]))
    def test_temperature_conversion(self, mock_input):
        with patch("builtins.print") as mock_print:
            fahrenheit()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue("°C is equal to" in printed[0])

    @patch("builtins.input", side_effect=mock_inputs([10]))
    def test_speed_conversion(self, mock_input):
        with patch("builtins.print") as mock_print:
            kilometers_per_hour()
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue("meters per second is equal" in printed[0])

# ---------------------------
# Run the tests
# ---------------------------
if __name__ == "__main__":
    unittest.main()