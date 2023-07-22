from __future__ import annotations


class Euro:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Euro:
        return Euro(self.amount * multiplier)
