from practice import Euro


def test_money():
    amount = Euro(10)
    double = amount.times(2)
    assert double.amount == 10
