#!/usr/bin/env python3
"""Binomial paylanmasını təmsil edən klas modulu."""


class Binomial:
    """Binomial paylanma ilə bağlı hesablamaları yerinə yetirən klas."""

    def __init__(self, data=None, n=1, p=0.5):
        """Klasın ilkin göstəricilərini təyin edir."""
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

            # Data üzərindən n və p-ni təxmin etmək (əvvəlki tapşırıqlardan)
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p_est = 1 - (variance / mean) if mean != 0 else 0.5
            n_est = round(mean / p_est) if p_est != 0 else 1
            p_est = mean / n_est if n_est != 0 else 0.5

            if n_est <= 0:
                raise ValueError("n must be a positive value")
            if p_est <= 0 or p_est >= 1:
                raise ValueError("p must be greater than 0 and less than 1")

            self.n = int(n_est)
            self.p = float(p_est)

    def _factorial(self, num):
        """Faktorial hesablayan köməkçi metod."""
        if num == 0 or num == 1:
            return 1
        res = 1
        for i in range(2, num + 1):
            res *= i
        return res

    def pmf(self, k):
        """Verilmiş uğurlu nəticə sayı (k) üçün PMF dəyərini hesablayır."""
        if not isinstance(k, (int, float)):
            return 0

        k = int(k)

        if k < 0 or k > self.n:
            return 0

        # Sətirlərin 79 simvoldan uzun olmaması üçün hissələrə bölünmüş hesablama
        n_fact = self._factorial(self.n)
        k_fact = self._factorial(k)
        n_k_fact = self._factorial(self.n - k)

        # Kombinasiya: n! / (k! * (n - k)!)
        combination = n_fact / (k_fact * n_k_fact)

        # PMF = C(n, k) * p^k * (1 - p)^(n - k)
        pmf_value = combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

        return pmf_value
