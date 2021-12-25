import re
from .ast import Program, Const, Expression

# Must be X.Y or .Y since an integer will be caught if this is only X
float_re = re.compile(r'\d?(?:\.\d+)')


def parse(text: str) -> Program:
    """
    Parse a program into a AST.

    Example:
    x = 10 * 2;
    y = x + 10;
    5 + 20
    """
    return Program([parse_expr(expr) for expr in text.split(';') if parse_expr(expr) is not None])


def parse_expr(text: str) -> Expression:
    if is_integer(text):
        return Const(int(text))
    elif is_float(text):
        return Const(float(text))


def is_integer(text: str) -> bool:
    for ch in text:
        if not ch.isdigit():
            return False

    return True


def is_float(text: str) -> float:
    return float_re.match(text)
