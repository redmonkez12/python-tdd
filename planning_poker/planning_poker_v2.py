class Estimate:
    def __init__(self, developer: str, estimate: float):
        self.developer = developer
        self.estimate = estimate


class PlanningPoker:
    def __init__(self):
        self.estimates: list[Estimate] = []

    def identify_extremes(self, estimates: list[Estimate]) -> tuple[str, str]:
        if len(estimates) <= 1:
            raise Exception("There must be more than 1 estimate in the list")

        low_estimate = None
        high_estimate = None

        for estimate in estimates:
            if high_estimate is None or estimate.estimate > high_estimate.estimate:
                high_estimate = estimate

            if low_estimate is None or estimate.estimate < low_estimate.estimate:
                low_estimate = estimate

        return low_estimate.developer, high_estimate.developer