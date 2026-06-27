#!/usr/bin/env python3
"""Decision Tree Implementation"""
import numpy as np


class Node:
    """Node class for Decision Tree"""
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, depth=0, is_root=False):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.depth = depth
        self.is_root = is_root
        self.is_leaf = False
        self.lower = {}
        self.upper = {}

    def update_indicator(self):
        """Computes the indicator function for the node"""
        def is_large_enough(x):
            if not self.lower:
                return np.ones(x.shape[0], dtype=bool)
            results = [np.greater(x[:, k], v) for k, v in self.lower.items()
                       if v != -np.inf]
            return np.all(results, axis=0) if results else \
                np.ones(x.shape[0], dtype=bool)

        def is_small_enough(x):
            if not self.upper:
                return np.ones(x.shape[0], dtype=bool)
            results = [np.less_equal(x[:, k], v) for k, v in self.upper.items()
                       if v != np.inf]
            return np.all(results, axis=0) if results else \
                np.ones(x.shape[0], dtype=bool)

        self.indicator = lambda x: np.all(np.array([is_large_enough(x),
                                          is_small_enough(x)]), axis=0)
        if not self.is_leaf:
            self.left_child.update_indicator()
            self.right_child.update_indicator()


class Leaf:
    """Leaf class for Decision Tree"""
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.is_leaf = True
        self.lower = {}
        self.upper = {}

    def update_indicator(self):
        """Computes the indicator function for the leaf"""
        def is_large_enough(x):
            results = [np.greater(x[:, k], v) for k, v in self.lower.items()
                       if v != -np.inf]
            return np.all(results, axis=0) if results else \
                np.ones(x.shape[0], dtype=bool)

        def is_small_enough(x):
            results = [np.less_equal(x[:, k], v) for k, v in self.upper.items()
                       if v != np.inf]
            return np.all(results, axis=0) if results else \
                np.ones(x.shape[0], dtype=bool)

        self.indicator = lambda x: np.all(np.array([is_large_enough(x),
                                          is_small_enough(x)]), axis=0)


class Decision_Tree:
    """Decision Tree class"""
    def __init__(self, root):
        self.root = root

    def update_indicator(self):
        """Updates indicator function for the whole tree"""
        self.root.update_indicator()
