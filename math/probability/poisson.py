#!/usr/bin/env python3
"""
Poisson distribution module
"""


class Poisson:
    """ Represents a poisson distribution """

    def __init__(self, data=None, lambtha=1.):
        """ Initializes the Poisson distribution """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """ Calculates the value of the PMF for a given number of successes """
        k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285

        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        lambtha_pow_k = self.lambtha ** k
        e_pow_minus_lambtha = e ** (-self.lambtha)

        pmf_value = (lambtha_pow_k * e_pow_minus_lambtha) / factorial

        return pmf_value

    def cdf(self, k):
        """ Calculates the value of the CDF for a given number of successes """
        k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285
        cdf_value = 0.0

        # 0-dan k-ya qədər olan bütün PMF-ləri dövrlə toplayırıq
        for i in range(k + 1):
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j

            lambtha_pow_i = self.lambtha ** i
            e_pow_minus_lambtha = e ** (-self.lambtha)

            pmf_i = (lambtha_pow_i * e_pow_minus_lambtha) / factorial
            cdf_value += pmf_i

        return cdf_value
