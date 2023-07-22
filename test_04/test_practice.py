from practice import Money


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
    originalMoney = Money(4002, "KRW")
    actualMoneyAfterDivision = originalMoney.divide(4)
    expectedMoneyAfterDivision = Money(1000.5, "KRW")
    assert actualMoneyAfterDivision == expectedMoneyAfterDivision
