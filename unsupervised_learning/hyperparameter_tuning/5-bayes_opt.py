#!/usr/bin/env python3
"""Bayesian Optimization"""
import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """Performs Bayesian optimization on a noiseless 1D Gaussian process"""

    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1,
                 sigma_f=1, xsi=0.01, minimize=True):
        """
        Initialize Bayesian Optimization

        f: the black-box function to be optimized
        X_init: numpy.ndarray of shape (t, 1) - initial inputs
        Y_init: numpy.ndarray of shape (t, 1) - initial outputs
        bounds: tuple (min, max) representing the bounds of the space
        ac_samples: number of samples for acquisition analysis
        l: length parameter for the kernel
        sigma_f: standard deviation given to the output of the black-box
        xsi: exploration-exploitation factor
        minimize: bool determining whether to minimize (True) or
                  maximize (False)
        """
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        min_b, max_b = bounds
        self.X_s = np.linspace(min_b, max_b, ac_samples).reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
        Calculates the next best sample location using Expected Improvement

        Returns: X_next, EI
            X_next: numpy.ndarray of shape (1,) - next best sample point
            EI: numpy.ndarray of shape (ac_samples,) - expected improvement
                of each potential sample
        """
        mu, sigma = self.gp.predict(self.X_s)

        if self.minimize:
            Y_sample_opt = np.min(self.gp.Y)
            imp = Y_sample_opt - mu - self.xsi
        else:
            Y_sample_opt = np.max(self.gp.Y)
            imp = mu - Y_sample_opt - self.xsi

        with np.errstate(divide='warn'):
            Z = np.zeros_like(sigma)
            mask = sigma > 0
            Z[mask] = imp[mask] / sigma[mask]
            EI = np.zeros_like(sigma)
            EI[mask] = (imp[mask] * norm.cdf(Z[mask])
                        + sigma[mask] * norm.pdf(Z[mask]))

        X_next = self.X_s[np.argmax(EI)]
        return X_next, EI

    def optimize(self, iterations=100):
        """
        Optimizes the black-box function

        iterations: maximum number of iterations to perform
        If the next proposed point is one that has already been sampled,
        optimization is stopped early

        Returns: X_opt, Y_opt
            X_opt: numpy.ndarray of shape (1,) - optimal point
            Y_opt: numpy.ndarray of shape (1,) - optimal function value
        """
        for _ in range(iterations):
            X_next, _ = self.acquisition()

            if np.any(np.all(np.isclose(self.gp.X, X_next), axis=1)):
                break

            Y_next = self.f(X_next)
            self.gp.update(X_next, Y_next)

        if self.minimize:
            idx = np.argmin(self.gp.Y)
        else:
            idx = np.argmax(self.gp.Y)

        X_opt = self.gp.X[idx]
        Y_opt = self.gp.Y[idx]

        return X_opt, Y_opt
