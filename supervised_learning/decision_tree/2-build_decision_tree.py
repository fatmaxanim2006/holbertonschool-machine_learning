#!/usr/bin/env python3
"""Decision Tree implementation with string representation."""


class Node:
    """Internal node of a decision tree."""

    def __init__(self, feature=None, threshold=None,
                 left_child=None, right_child=None,
                 depth=None, is_root=False):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.depth = depth
        self.is_root = is_root
        self.is_leaf = False

    def left_child_add_prefix(self, text):
        lines = text.split("\n")
        new_text = "    +---> " + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("    |    " + x) + "\n"
        return (new_text)

    def right_child_add_prefix(self, text):
        lines = text.split("\n")
        new_text = "    +---> " + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("         " + x) + "\n"
        return (new_text)

    def __str__(self):
        if self.is_root:
            header = f"root [feature={self.feature}, threshold={self.threshold}]"
        else:
            header = f"node [feature={self.feature}, threshold={self.threshold}]"

        left_str = self.left_child.__str__()
        right_str = self.right_child.__str__()

        left_lines = self.left_child_add_prefix(left_str)
        right_lines = self.right_child_add_prefix(right_str)

        return header + "\n" + left_lines + right_lines.rstrip("\n")


class Leaf:
    """Leaf node of a decision tree."""

    def __init__(self, value, depth=None):
        self.value = value
        self.depth = depth
        self.is_leaf = True

    def __str__(self):
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    """Decision Tree classifier."""

    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.root.__str__()

