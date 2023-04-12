from typing import NamedTuple


class Flake8ASTErrorInfo(NamedTuple):
    line_number = None
    offset = None
    msg = None
    cls = None
