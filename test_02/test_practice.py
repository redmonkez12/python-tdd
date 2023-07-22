from practice import Money


def test_multiplication_in_euros():
    amount = Money(10, "EUR")
    double = amount.times(2)
    assert double.amount == 20
    assert double.currency == "EUR"


def test_multiplication_in_dollars():
    amount = Money(10, "USD")
    double = amount.times(2)
    assert double.amount == 20
    assert double.currency == "USD"
