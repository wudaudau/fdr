# https://code.visualstudio.com/docs/python/testing#_run-tests
from src.fdr import * # The code to test
import unittest # The test framework


class TestFdr(unittest.TestCase):

    def setUp(self) -> None:
        # example from https://stackoverflow.com/questions/25185205/calculating-adjusted-p-values-in-python
        self.p_vals = [0.0001, 0.001, 0.006, 0.03, 0.095, 0.117, 0.234, 0.552, 0.751, 0.985]
        self.p_ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.expected = [0.001, 0.005, 0.02, 0.075, 0.19, 0.195, 0.334, 0.690, 0.834, 0.985]

    def test_cal_p_vals_rank(self):
        for a, b in zip(cal_p_vals_rank(self.p_vals), self.p_ranks):
            self.assertEqual(a, b)

    def test_cal_fdr(self):
        for a, b in zip(cal_fdr(self.p_vals), self.expected):
            self.assertAlmostEqual(a, b, places=3)
