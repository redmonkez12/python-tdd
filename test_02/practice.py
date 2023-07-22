from __future__ import annotations


class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: float) -> Money:
        return Money(self.amount * multiplier, self.currency)
