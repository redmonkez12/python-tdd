import pytest

from calculator import Calculator


@pytest.fixture()
def calculator_fixture():
    calculator = Calculator()
    return calculator


#
# def test_multiplication(calculator_fixture: Calculator):
#     # calculator = Calculator()
#
#     # output = calculator.multiply(2, 5)
#     output = calculator_fixture.multiply(2, 5)
#     assert output == 10
#
#
# def test_multiplication_negative_and_positive_number():
#     calculator = Calculator()
#
#     output = calculator.multiply(-3, 5)
#     assert output == -15


# @pytest.mark.parametrize(["a", "b"],
#     [
#         (7, -6),
#         (5, 3),
#         (12, -3),
#         (-1, -2),
#         (5.6, 2.1),
#     ]
# )
def test_addition(a: float, b: float) -> None:
    calculator = Calculator()

    output = calculator.add(a, b)
    assert output == a + b

#
# def test_addition_negative_and_positive_number():
#     calculator = Calculator()
#
#     output = calculator.add(7, -6)
#     assert output == 1


# def test_subtraction():
#     calculator = Calculator()
#
#     output = calculator.sub(5, 3)
#     assert output == 2
#
#
# def test_subtraction_two_negative_numbers():
#     calculator = Calculator()
#
#     output = calculator.sub(-2, -3)
#     assert output == 1
#
#
# def test_subtraction_negative_and_positive():
#     calculator = Calculator()
#
#     output = calculator.sub(-1, 1)
#     assert output == -2
#
#     # output = calculator.sub(1, -1)
#     # assert output == 2
