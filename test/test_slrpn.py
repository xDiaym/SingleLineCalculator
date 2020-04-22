import unittest

from test.util import call


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(call('1 1 +'), 2.0)

    def test_sup(self):
        self.assertEqual(call('3 2 -'), 1.0)

    def test_mul(self):
        self.assertEqual(call('4 3 *'), 12.0)

    def test_div(self):
        self.assertEqual(call('8 4 /'), 2.0)

    def test_div_float(self):
        self.assertEqual(call('3 4 /'), 0.75)

    def test_many_ops(self):
        self.assertEqual(call('2 2 * 2 +'), 6.0)
