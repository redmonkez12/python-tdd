from tdd.step_1.main import Euro


def test_multiplication():
    amount = Euro(5)
    double = amount.times(4)

    assert double.amount == 20
