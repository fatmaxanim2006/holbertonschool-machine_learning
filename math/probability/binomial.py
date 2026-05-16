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

            # Mean (ortalama) hesablanması
            mean = sum(data) / len(data)

            # Variance (dispersiya) hesablanması
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            # p və n-in ilkin təmini
            p_initial = 1 - (variance / mean)
            n_rounded = round(mean / p_initial)

            # n tam ədədə çevrilir, p isə n üzərindən yenidən dəqiqləşdirilir
            self.n = int(n_rounded)
            self.p = float(mean / self.n)
