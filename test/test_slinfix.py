import os
import unittest

from test.util import call


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(os.getcwd(), 'slinfix.py')

    def test_sum(self):
        self.assertEqual(call(self.path, '1 + 1'), 2.0)

    def test_sup(self):
        self.assertEqual(call(self.path, '3 - 2'), 1.0)

    def test_mul(self):
        self.assertEqual(call(self.path, '4 * 3'), 12.0)

    def test_div(self):
        self.assertEqual(call(self.path, '8 / 4'), 2.0)

    def test_div_float(self):
        self.assertEqual(call(self.path, '3 / 4'), 0.75)

    def test_many_ops(self):
        self.assertEqual(call(self.path, '2 * 2 + 2'), 6.0)
