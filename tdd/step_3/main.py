from __future__ import annotations
import functools
import operator


class Euro:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def times(self, multiplier: float) -> Euro:
        return Euro(self.amount * multiplier)

    def __eq__(self, other: Euro) -> bool:
        return self.amount == other.amount


class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: float) -> Money:
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: float) -> Money:
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other: Money) -> bool:
        return self.amount == other.amount and self.currency == other.currency


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0

        for money in self.moneys:
            total += money.amount

        # total = functools.reduce(
        #     operator.add, map(lambda m: m.amount, self.moneys), 0)

        return Money(total, currency)