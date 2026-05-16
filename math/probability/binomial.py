#!/usr/bin/env python3
"""
Binomial distribution module
"""


class Binomial:
    """ Represents a binomial distribution """

    def __init__(self, data=None, n=1, p=0.5):
        """ Initializes the Binomial distribution """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p_initial = 1 - (variance / mean)
            n_rounded = round(mean / p_initial)

            self.n = int(n_rounded)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """ Calculates the value of the PMF for a given number of successes """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        # n!, k! və (n-k)! faktoriallarının tam ədəd olaraq hesablanması
        fact_n = 1
        for i in range(1, self.n + 1):
            fact_n *= i

        fact_k = 1
        for i in range(1, k + 1):
            fact_k *= i

        fact_nk = 1
        for i in range(1, self.n - k + 1):
            fact_nk *= i

        # Tam ədəd bölməsi (//) istifadə edirik ki, dəqiqlik itməsin
        combination = fact_n // (fact_k * fact_nk)

        # PMF düsturu
        pmf_value = combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

        return float(pmf_value)
