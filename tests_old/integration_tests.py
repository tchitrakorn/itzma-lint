import testing_checks
import ast


def test_all_checks():  # integration test 1
    expected = {
        "line_number": 5,
        "offset": 0,
        "msg": "IM function names must be camel case with lowercase first letter",
    }
    errors = []
    with open("../src/tests/test_samples/test5.py") as f:
        code = f.read()
    node = ast.parse(code)
    testing_checks.LocalImportsNotAllowed.check(node, errors)
    testing_checks.UnconventionalFunctionNamesNotAllowed.check(node, errors)
    testing_checks.UnconventionalClassNamesNotAllowed.check(node, errors)
    testing_checks.UnconventionalVariableNamesNotAllowed.check(node, errors)
    result = errors[0]
    assert (
        result.line_number == expected["line_number"]
        and result.offset == expected["offset"]
        and result.msg == expected["msg"]
        and len(errors) == 2
    )


test_all_checks()
