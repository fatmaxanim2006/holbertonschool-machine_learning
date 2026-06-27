#!/usr/bin/env python3
"""Decision Tree Implementation"""


def left_child_add_prefix(text):
    """Adds prefix for left child"""
    lines = text.split("\n")
    new_text = "    +---> " + lines[0] + "\n"
    for x in lines[1:]:
        if x:
            new_text += "      " + x + "\n"
    return new_text


def right_child_add_prefix(text):
    """Adds prefix for right child"""
    lines = text.split("\n")
    new_text = "    +---> " + lines[0] + "\n"
    for x in lines[1:]:
        if x:
            new_text += "      " + x + "\n"
    return new_text


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

    def __str__(self):
        if self.is_root:
            res = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            res = f"node [feature={self.feature}, threshold={self.threshold}]\n"
        res += left_child_add_prefix(self.left_child.__str__())
        res += right_child_add_prefix(self.right_child.__str__())
        return res


class Leaf:
    """Leaf class for Decision Tree"""
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.is_leaf = True

    def __str__(self):
        return f"leaf [value={self.value}]"


class Decision_Tree:
    """Decision Tree class"""
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return self.root.__str__()
