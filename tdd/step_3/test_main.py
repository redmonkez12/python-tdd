from tdd.step_2.main import Euro, Money
from tdd.step_3.main import Portfolio


# Multicurrency


def test_multiplication():
    amount = Euro(5)
    double = amount.times(4)

    twenty_euro = Euro(20)

    # assert double.amount == 20
    assert double == twenty_euro


def test_multiplication_in_dollars():
    amount = Money(5, "USD")
    double = amount.times(4)

    # assert double.amount == 20
    # assert double.currency == "USD"
    twenty_dollars = Money(20, "USD")

    assert double == twenty_dollars


def test_division():
    original_money = Money(1000, "CZK")
    actual_money_after_division = original_money.divide(25)
    expected_money_after_division = Money(40, "EUR")

    assert actual_money_after_division == expected_money_after_division


def test_addition():
    five_dollars = Money(5, "USD")
    ten_dollars = Money(10, "USD")
    fifteen_dollars = Money(15, "USD")
    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_dollars)
    assert fifteen_dollars == portfolio.evaluate("USD")
