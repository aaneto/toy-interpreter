from .ast import Const
from .parser import parse, parse_expr
import unittest


class TestParser(unittest.TestCase):

    def test_parse_number(self):
        self.assertEqual(parse_expr("100"), Const(100))

    def test_parse_float(self):
        self.assertEqual(parse_expr("2.3"), Const(2.3))
        self.assertEqual(parse_expr("0.3"), Const(0.3))
        self.assertEqual(parse_expr(".5"), Const(0.5))

    def test_parse_invalid_number(self):
        self.assertEqual(parse_expr("0."), None)


if __name__ == '__main__':
    unittest.main()
