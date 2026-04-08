import unittest
from unittest.mock import patch
from io import StringIO

from unit_converter_functions import (
    feet, meters, pounds, kilograms,
    minutes, seconds, fahrenheit, celsius,
    kilometers_per_hour, meters_per_second
)

from quadratic_equation_solver_function import quadratic_equation_solver
from vector_calculator import (
    dot_product, vector_magnitude,
    angle_between_vectors, cross_product
)
from force_resultant_calculator_functions2 import (
    validate_magnitude, validate_integer,
    validate_magnitude2,
    vector_calculator_for_two_components, vector_calculator_for_three_components,
    validate_magnitude1,validate_angle
)
from triangle_solver2 import SSS, SSA2, SSA1


class TestEngineeringCalculator(unittest.TestCase):

    # =========================
    # VALIDATION TESTS
    # =========================
    @patch('builtins.input', side_effect=['-5', 'abc', '10'])
    def test_validate_magnitude_retry(self, mock_input):
        self.assertEqual(validate_magnitude(""), -5.0)

    @patch('builtins.input', side_effect=['0', 'hello', '5'])
    def test_validate_integer_retry(self, mock_input):
        self.assertEqual(validate_integer(""), 5)
    
    @patch('builtins.input', side_effect=['-2', 'hello', '5'])
    def test_validate_magnitude1_retry(self, mock_input):
        self.assertEqual(validate_magnitude1(""), 5.0)
        
    @patch('builtins.input', side_effect=['370', 'hello', '45'])
    def test_validate_angle_retry(self, mock_input):
        self.assertEqual(validate_angle(""), 0.7853981633974483)
    
    @patch('builtins.input', side_effect=['0', 'hello', '45'])
    def test_validate_magnitude2_retry(self, mock_input):
        self.assertEqual(validate_magnitude2(""), 0)

    # =========================
    # UNIT CONVERTER TESTS
    # =========================
    @patch('builtins.input', side_effect=['10'])
    def test_meters_to_feet(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            feet()
            self.assertIn("32.81", fake_out.getvalue())

    @patch('builtins.input', side_effect=['25'])
    def test_feet_to_meters(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            meters()
            self.assertIn("7.62", fake_out.getvalue())

    @patch('builtins.input', side_effect=['50'])
    def test_kg_to_pounds(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pounds()
            self.assertIn("110.23", fake_out.getvalue())

    @patch('builtins.input', side_effect=['100'])
    def test_pounds_to_kg(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            kilograms()
            self.assertIn("45.36", fake_out.getvalue())

    @patch('builtins.input', side_effect=['120'])
    def test_seconds_to_minutes(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            minutes()
            self.assertIn("2.00", fake_out.getvalue())

    @patch('builtins.input', side_effect=['5'])
    def test_minutes_to_seconds(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            seconds()
            self.assertIn("300.00", fake_out.getvalue())

    @patch('builtins.input', side_effect=['100'])
    def test_celsius_to_fahrenheit(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            fahrenheit()
            self.assertIn("212.00", fake_out.getvalue())

    @patch('builtins.input', side_effect=['212'])
    def test_fahrenheit_to_celsius(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            celsius()
            self.assertIn("100.00", fake_out.getvalue())

    @patch('builtins.input', side_effect=['10'])
    def test_ms_to_kmh(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            kilometers_per_hour()
            self.assertIn("36.00", fake_out.getvalue())

    @patch('builtins.input', side_effect=['72'])
    def test_kmh_to_ms(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            meters_per_second()
            self.assertIn("20.00", fake_out.getvalue())

    # =========================
    # QUADRATIC TESTS
    # =========================
    @patch('builtins.input', side_effect=['1', '5', '6'])
    def test_quadratic_two_roots(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            quadratic_equation_solver()
            self.assertIn("The values of x", fake_out.getvalue())

    @patch('builtins.input', side_effect=['1', '2', '1'])
    def test_quadratic_single_root(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            quadratic_equation_solver()
            self.assertIn("one real solution", fake_out.getvalue())

    @patch('builtins.input', side_effect=['1', '1', '5'])
    def test_quadratic_no_real_roots(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            quadratic_equation_solver()
            self.assertIn("no real solutions", fake_out.getvalue())

    # =========================
    # VECTOR TESTS
    # =========================
    @patch('builtins.input', side_effect=['3', '10', '20', '30'])
    def test_vector_magnitude(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            vector_magnitude()
            self.assertIn("37.42", fake_out.getvalue())

    @patch('builtins.input', side_effect=['3', '10', '20', '30', '5', '6', '7'])
    def test_dot_product(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            dot_product()
            self.assertIn("380", fake_out.getvalue())

    @patch('builtins.input', side_effect=['2', '3', '4', '4', '3'])
    def test_angle_between_vectors(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            angle_between_vectors()
            self.assertIn("Angle", fake_out.getvalue())

    @patch('builtins.input', side_effect=['1', '0', '0', '0', '1', '0'])
    def test_cross_product(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cross_product()
            self.assertIn("[0, 0, 1]", fake_out.getvalue())

    # =========================
    # TRIANGLE TESTS
    # =========================
    @patch('builtins.input', side_effect=['3', '4', '5'])
    def test_triangle_sss(self, mock_input):
        SSS()  # should run without crashing
        
    @patch('builtins.input', side_effect=['3', '4', '60'])
    def test_triangle_ssa1(self, mock_input):
        SSA1()  # should run without crashing

    @patch('builtins.input', side_effect=['3', '4'])
    def test_triangle_ssa_right(self, mock_input):
        SSA2()  # should run without crashing

    # =========================
    # FORCE RESULTANT TESTS
    # =========================
    @patch('builtins.input', side_effect=[
        '2',
        '10', '0',
        '10', '90'
    ])
    def test_force_two_components(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            vector_calculator_for_two_components()
            self.assertIn("Magnitude", fake_out.getvalue())

    @patch('builtins.input', side_effect=[
    '3',
    '100', '200', '150',
    '50', '75', '125',
    '25', '60', '40'
    ])
    def test_force_three_components_large(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            vector_calculator_for_three_components()
            self.assertIn("Resultant Force", fake_out.getvalue())
if __name__ == "__main__":
    unittest.main()