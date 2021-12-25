import unittest
from .ast import Const, Add, Name, Mul, Assign, Program


class TestAST(unittest.TestCase):

    def test_add(self):
        val = Add(Const(10), Const(12))
        self.assertEqual(val.evaluate({}), 22)

    def test_const(self):
        val = Const(111)
        self.assertEqual(111, val.evaluate({}))

    def test_name(self):
        var = Name('x')
        self.assertEqual(var.evaluate({'x': 10}), 10)

    def test_mul(self):
        val = Mul(Const(2), Const(10))
        self.assertEqual(val.evaluate({}), 20)

    def test_assignment(self):
        env = {}

        Assign(Name('x'), Const(100)).evaluate(env)
        self.assertEqual(100, Name('x').evaluate(env))

    def test_program(self):
        exprs = [
            Assign(Name('x'), Add(Const(1), Const(2))),
            Assign(Name('y'), Mul(Name('x'), Const(10))),
            Add(Name('x'), Name('y'))
        ]

        vals = Program(exprs).evaluate()

        self.assertEqual(vals, [
            3,
            30,
            33
        ])


if __name__ == '__main__':
    unittest.main()
