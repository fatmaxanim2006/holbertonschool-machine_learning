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

    def update_bounds_below(self):
        """Recursively computes bounds for each node"""
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -np.inf}

        for child in [self.left_child, self.right_child]:
            child.lower = self.lower.copy()
            child.upper = self.upper.copy()
            if child == self.left_child:
                child.upper[self.feature] = min(child.upper.get(self.feature, np.inf), self.threshold)
            else:
                child.lower[self.feature] = max(child.lower.get(self.feature, -np.inf), self.threshold)
            
            child.update_bounds_below()


class Leaf:
    """Leaf class for Decision Tree"""
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.is_leaf = True
        self.lower = {}
        self.upper = {}

    def update_bounds_below(self):
        """Leaves do not have children, just pass"""
        pass


class Decision_Tree:
    """Decision Tree class"""
    def __init__(self, root):
        self.root = root

    def update_bounds(self):
        """Updates bounds for all nodes starting from root"""
        self.root.lower = {0: -np.inf}
        self.root.upper = {0: np.inf}
        self.root.update_bounds_below()

    def get_leaves(self):
        """Returns all leaves in the tree"""
        return self.get_leaves_recursively(self.root)

    def get_leaves_recursively(self, node):
        """Helper to get leaves"""
        if node.is_leaf:
            return [node]
        return self.get_leaves_recursively(node.left_child) + \
               self.get_leaves_recursively(node.right_child)
