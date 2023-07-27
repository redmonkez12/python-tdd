from PlanningPoker.planning_poker import Estimate, PlanningPoker


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
