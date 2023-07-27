class Estimate:
    def __init__(self, developer: str, estimate: float):
        self.developer = developer
        self.estimate = estimate


class PlanningPoker:
    def __init__(self):
        self.estimates: list[Estimate] = []

    def identify_extremes(self, estimates: list[Estimate]) -> tuple[str, str]:
        low_estimate = None
        high_estimate = None

        for estimate in estimates:
            if high_estimate is None or estimate.estimate > high_estimate.estimate:
                high_estimate = estimate

            if low_estimate is None or estimate.estimate < low_estimate.estimate:
                low_estimate = estimate

        return low_estimate.developer, high_estimate.developer


# estimates = [
#     Estimate("Ted", 16),
#     Estimate("Barney", 8),
#     Estimate("Lily", 2),
#     Estimate("Robin", 4),
# ]

if __name__ == "__main__":
    estimates = [
        Estimate("Ross", 2),
        Estimate("Phoebe", 4),
        Estimate("Monica", 8),
        Estimate("Chandler", 16),
    ]

    planing_poker = PlanningPoker()
    result = planing_poker.identify_extremes(estimates)
    print(result)
