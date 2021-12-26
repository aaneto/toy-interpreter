from .ast import Assign, Const, Name, Program
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

    def test_parse_name(self):
        self.assertEqual(parse_expr('var_name'), Name('var_name'))

    def test_parse_invalid_expr(self):
        expr = parse_expr('==')

        self.assertEqual(expr, None)

    def test_assign_whitespace(self):
        expr = parse_expr(' var = 11   ')

        self.assertEqual(expr, Assign(Name('var'), Const(11)))

    def test_parse_assign(self):
        self.assertEqual(
            parse_expr('var=100'),
            Assign(Name('var'), Const(100))
        )

    def test_small_program_without_whitespace(self):
        small_src = """age=20;300;age"""
        parsed_program = Program([
            Assign(Name('age'), Const(20)),
            Const(300),
            Name('age')
        ])

        self.assertEqual(parse(small_src), parsed_program)


if __name__ == '__main__':
    unittest.main()
