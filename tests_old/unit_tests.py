# import sys
# sys.path.append('../src')
import testing_checks
import helpers
import ast


def test_error_definition():  # unit test 0
    line_number, offset, msg, cls = 10, 2, "Testing Message", str
    error = helpers.Flake8ASTErrorInfo(line_number, offset, msg, cls)
    assert (
        error.line_number == 10
        and error.offset == 2
        and error.msg == "Testing Message"
        and error.cls == str
    )


def test_local_imports_not_allowed():  # unit test 1
    expected = {
        "line_number": 6,
        "offset": 4,
        "msg": "IM local imports are not allowed inside a function",
    }
    errors = []
    with open("../src/tests/test_samples/test1.py") as f:
        code = f.read()
    node = ast.parse(code)
    testing_checks.LocalImportsNotAllowed.check(node, errors)
    result = errors[0]
    assert (
        result.line_number == expected["line_number"]
        and result.offset == expected["offset"]
        and result.msg == expected["msg"]
    )


def test_function_name_case():  # unit test 2
    expected = {
        "line_number": 3,
        "offset": 0,
        "msg": "IM function names must be camel case with lowercase first letter",
    }
    errors = []
    with open("../src/tests/test_samples/test2.py") as f:
        code = f.read()
    node = ast.parse(code)
    testing_checks.UnconventionalFunctionNamesNotAllowed.check(node, errors)
    result = errors[0]
    assert (
        result.line_number == expected["line_number"]
        and result.offset == expected["offset"]
        and result.msg == expected["msg"]
    )


def test_class_name_case():  # unit test 3
    expected = {
        "line_number": 3,
        "offset": 0,
        "msg": "IM class names must be camel case with uppercase first letter",
    }
    errors = []
    with open("../src/tests/test_samples/test3.py") as f:
        code = f.read()
    node = ast.parse(code)
    testing_checks.UnconventionalClassNamesNotAllowed.check(node, errors)
    result = errors[0]
    assert (
        result.line_number == expected["line_number"]
        and result.offset == expected["offset"]
        and result.msg == expected["msg"]
    )


def test_variable_name_plurality():  # unit test 4
    expected = {
        "line_number": 3,
        "offset": 0,
        "msg": "IM variable names must be plural if they are assigned to a list",
    }
    errors = []
    with open("../src/tests/test_samples/test4.py") as f:
        code = f.read()
    node = ast.parse(code)
    testing_checks.UnconventionalVariableNamesNotAllowed.check(node, errors)
    result = errors[0]
    assert (
        result.line_number == expected["line_number"]
        and result.offset == expected["offset"]
        and result.msg == expected["msg"]
    )


test_error_definition()
test_local_imports_not_allowed()
test_function_name_case()
test_class_name_case()
test_variable_name_plurality()
