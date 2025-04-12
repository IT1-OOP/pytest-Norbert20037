import unittest
import math
import pytest
from src import quadratic

class TestSolveQuadraticFormula(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(quadratic.solve_quadratic_formula(1, 2, 1), (-1.0, -1.0))
        self.assertEqual(quadratic.solve_quadratic_formula(1, -3, 2), (2.0, 1.0))

    def test_exceptions(self):
        self.assertRaises(TypeError, quadratic.solve_quadratic_formula, "1", 2, 3)
        self.assertRaises(SyntaxError, quadratic.solve_quadratic_formula, 0, 2, 3)
        self.assertRaises(NameError, quadratic.solve_quadratic_formula, 1, 5, 3)
        self.assertRaises(ValueError, quadratic.solve_quadratic_formula, 1, 2, 3)