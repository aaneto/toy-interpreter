import re
from .ast import Add, Assign, Program, Const, Expression, Name, Mul

# Must be X.Y or .Y since an integer will be caught if this is only X
float_re = re.compile(r'\d?(?:\.\d+)')
name_re = re.compile(r'[a-zA-Z_]+')


class ParseError(BaseException):
    def __init__(self, *args):
        super().__init__(*args)


def parse(text: str) -> Program:
    """
    Parse a program into a AST.

    Example:
    x = 10 * 2;
    y = x + 10;
    5 + 20
    """
    if text is None or len(text) == 0:
        return []

    exprs = []
    for line in text.split(';'):
        filtered_line = remove_whitespace(line)
        expr = parse_expr(filtered_line)
        if expr is not None:
            exprs.append(expr)

    return Program(exprs)


def remove_whitespace(text: str) -> str:
    return text.strip(' \t\n\r')


def parse_expr(text: str) -> Expression:
    if len(text) == 0:
        return None
    elif is_assign(text):
        return parse_assign(text)
    elif is_add(text):
        return parse_add(text)
    elif is_mul(text):
        return parse_mul(text)
    elif is_integer(text):
        return Const(int(text))
    elif is_float(text):
        return Const(float(text))
    elif is_name(text):
        return Name(text)
    else:
        raise ParseError(f'Cannot parse expression: {text}')


def is_add(text: str) -> bool:
    return "+" in text


def parse_add(text: str) -> Add:
    idx = text.index('+')
    left = parse_expr(remove_whitespace(text[:idx]))
    right = parse_expr(remove_whitespace(text[idx + 1:]))

    return Add(left, right)

def is_mul(text: str) -> bool:
    return "*" in text


def parse_mul(text: str) -> Mul:
    idx = text.index('*')
    left = parse_expr(remove_whitespace(text[:idx]))
    right = parse_expr(remove_whitespace(text[idx + 1:]))

    return Mul(left, right)


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
    return Assign(
        parse_expr(remove_whitespace(a)),
        parse_expr(remove_whitespace(b))
    )
