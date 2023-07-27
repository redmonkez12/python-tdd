import pytest

from PlanningPoker.planning_poker_v2 import Estimate, PlanningPoker


def test_planning_poker():
    estimates = [
        Estimate("Ted", 16),
        Estimate("Barney", 8),
        Estimate("Lily", 2),
        Estimate("Robin", 4),
    ]

    planing_poker = PlanningPoker()
    output = planing_poker.identify_extremes(estimates)
    assert output == ("Lily", "Ted")


def test_planning_poker_ascending():
    estimates = [
        Estimate("Ross", 2),
        Estimate("Phoebe", 4),
        Estimate("Monica", 8),
        Estimate("Chandler", 16),
    ]

    planing_poker = PlanningPoker()
    output = planing_poker.identify_extremes(estimates)
    assert output == ("Ross", "Chandler")


def test_planning_poker_zero_estimates():
    with pytest.raises(Exception) as e:
        planing_poker = PlanningPoker()
        planing_poker.identify_extremes([])

    assert str(e.value) == "There must be more than 1 estimate in the list"


def test_planning_poker_one_estimate():
    with pytest.raises(Exception) as e:
        planing_poker = PlanningPoker()
        planing_poker.identify_extremes([Estimate("Lilly", 10)])

        assert str(e.value) == "There must be more than 1 estimate in the list"
