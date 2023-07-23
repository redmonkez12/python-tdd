import functools
import operator

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0.0
        failures = []

        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)

        if len(failures) == 0:
            return Money(total, currency)

        failureMessage = ",".join(str(f) for f in failures)
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")

    def __convert(self, money: Money, currency: str) -> float:
        exchanges_rates = {'EUR->USD': 1.2, 'USD->KRW': 1100}
        # exchanges_rates = {}

        if money.currency == currency:
            return money.amount

        key = money.currency + "->" + currency
        return money.amount * exchanges_rates[key]


# one_dollar = Money(1, "USD")
# one_euro = Money(1, "EUR")
# one_won = Money(1, "KRW")
# portfolio = Portfolio()
# portfolio.add(one_dollar, one_euro, one_won)
# portfolio.evaluate("Kalganid")