from abc import ABC, abstractmethod
from typing import List


class Expression(ABC):
    @abstractmethod
    def evaluate(self, env):
        pass


class Receiver:
    pass


class Add(Expression):
    def __init__(self, a: Expression, b: Expression):
        self.a = a
        self.b = b

    def evaluate(self, env):
        return self.a.evaluate(env) + self.b.evaluate(env)

    def __eq__(self, other):
        return self.a.__eq__(self.b)

    def __str__(self):
        return f'{self.a} + {self.b}'


class Mul(Expression):
    def __init__(self, a: Expression, b: Expression):
        self.a = a
        self.b = b

    def evaluate(self, env):
        return self.a.evaluate(env) * self.b.evaluate(env)

    def __eq__(self, other):
        return self.a.__eq__(self.b)

    def __str__(self):
        return f'{self.a} * {self.b}'


class Const(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Const) and self.value == other.value

    def __str__(self):
        return str(self.value)


class Name(Expression, Receiver):
    def __init__(self, name):
        self.name = name

    def evaluate(self, env):
        return env[self.name]

    def __eq__(self, other):
        return isinstance(other, Name) and self.name == other.name

    def __str__(self):
        return f'@{self.name}'


class Assign(Expression):
    def __init__(self, a: Receiver, b: Expression):
        self.a = a
        self.b = b

    def evaluate(self, env):
        env[self.a.name] = self.b.evaluate(env)
        return env[self.a.name]

    def __eq__(self, other):
        return self.a.__eq__(other.a) and self.b.__eq__(other.b)

    def __str__(self):
        return f'{self.a} = {self.b}'


class Program:
    def __init__(self, exprs: List[Expression]):
        self.exprs = exprs

    def evaluate(self):
        env = {}
        values = []

        for expr in self.exprs:
            values.append(expr.evaluate(env))

        return values

    def __eq__(self, other):
        if not isinstance(other, Program):
            return False
        if len(self.exprs) != len(other.exprs):
            return False
        for i in range(len(self.exprs)):
            if self.exprs[i] != other.exprs[i]:
                return False

        return True
