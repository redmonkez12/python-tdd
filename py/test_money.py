import pytest

from money import Money
from portfolio import Portfolio


def test_multiplication_in_euros():
    tenEuros = Money(10, "EUR")
    twentyEuros = Money(20, "EUR")
    assert tenEuros.times(2) == twentyEuros


def test_multiplication_in_dollars():
    amount = Money(10, "USD")
    double = amount.times(2)
    assert double.amount == 20
    assert double.currency == "USD"


def test_division():
    original_money = Money(4002, "KRW")
    actual_money_after_division = original_money.divide(4)
    expected_money_afterDivision = Money(1000.5, "KRW")
    assert actual_money_after_division == expected_money_afterDivision


def test_addition():
    five_dollars = Money(5, "USD")
    ten_dollars = Money(10, "USD")
    fifteen_dollars = Money(15, "USD")
    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_dollars)
    assert fifteen_dollars == portfolio.evaluate("USD")


def test_addition_of_dollars_and_euros():
    five_dollars = Money(5, "USD")
    ten_euros = Money(10, "EUR")
    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_euros)
    expected_value = Money(17, "USD")
    actual_value = portfolio.evaluate("USD")
    assert expected_value == actual_value


def test_addition_of_dollars_and_wons():
    one_dollar = Money(1, "USD")
    eleven_hundred_won = Money(1100, "KRW")
    portfolio = Portfolio()
    portfolio.add(one_dollar, eleven_hundred_won)
    expected_value = Money(2200, "KRW")
    actual_value = portfolio.evaluate("KRW")
    assert actual_value == expected_value


def test_addition_with_multiple_missing_exchange_rates():
    one_dollar = Money(1, "USD")
    one_euro = Money(1, "EUR")
    one_won = Money(1, "KRW")
    portfolio = Portfolio()
    portfolio.add(one_dollar, one_euro, one_won)

    with pytest.raises(Exception) as ex:
        portfolio.evaluate("Kalganid")

    assert str(ex.value) == "Missing exchange rate(s):['USD->Kalganid','EUR->Kalganid','KRW->Kalganid']"