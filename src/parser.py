import re
from .ast import Assign, Program, Const, Expression, Name

# Must be X.Y or .Y since an integer will be caught if this is only X
float_re = re.compile(r'\d?(?:\.\d+)')
name_re = re.compile(r'[a-zA-Z_]+')


def parse(text: str) -> Program:
    """
    Parse a program into a AST.

    Example:
    x = 10 * 2;
    y = x + 10;
    5 + 20
    """
    return Program([
        parse_expr(expr)
        for expr in text.split(';')
        if parse_expr(expr) is not None]
    )


def parse_expr(text: str) -> Expression:
    text = text.strip(' \t\n\r')

    if is_assign(text):
        return parse_assign(text)
    elif is_integer(text):
        return Const(int(text))
    elif is_float(text):
        return Const(float(text))
    elif is_name(text):
        return Name(text)


def is_name(text: str) -> Name:
    return name_re.match(text)


def is_integer(text: str) -> bool:
    for ch in text:
        if not ch.isdigit():
            return False

    return True


def is_float(text: str) -> float:
    return float_re.match(text)


def is_assign(text: str) -> bool:
    return '=' in text and len(text.split('=')) == 2


def parse_assign(text: str) -> Assign:
    a, b = text.split('=')
    return Assign(parse_expr(a), parse_expr(b))
