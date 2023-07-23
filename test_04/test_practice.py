from practice import Money, Portfolio


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
