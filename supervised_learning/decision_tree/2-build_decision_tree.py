#!/usr/bin/env python3
"""
Module to build a decision tree with pretty printing functionality
"""

import numpy as np


class Node:
    """Represents a node in a decision tree"""

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """Initializes a node"""
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Calculates the maximum depth below this node"""
        if self.left_child:
            left_depth = self.left_child.max_depth_below()
        else:
            left_depth = self.depth

        if self.right_child:
            right_depth = self.right_child.max_depth_below()
        else:
            right_depth = self.depth

        return max(left_depth, right_depth)

    def count_nodes_below(self, only_leaves=False):
        """Counts the nodes or leaves below this node"""
        left_count = 0
        right_count = 0

        if self.left_child:
            left_count = self.left_child.count_nodes_below(
                only_leaves=only_leaves)
        if self.right_child:
            right_count = self.right_child.count_nodes_below(
                only_leaves=only_leaves)

        if only_leaves:
            return left_count + right_count
        return left_count + right_count + 1

    def left_child_add_prefix(self, text):
        """Adds appropriate prefix lines for a left child"""
        lines = text.split("\n")
        new_text = "    +--->" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += "    |    " + x + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        """Adds appropriate prefix lines for a right child"""
        lines = text.split("\n")
        new_text = "    +--->" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += "         " + x + "\n"
        return new_text

    def __str__(self):
        """Returns string representation of the node and its children"""
        if self.is_root:
            out = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            out = f"node [feature={self.feature}, threshold={self.threshold}]\n"

        if self.left_child:
            out += self.left_child_add_prefix(self.left_child.__str__())
        if self.right_child:
            out += self.right_child_add_prefix(self.right_child.__str__())

        # Task 2 üçün __str__ mütləq səliqəli bitməlidir
        return out


class Leaf(Node):
    """Represents a leaf node in a decision tree"""

    def __init__(self, value, depth=None):
        """Initializes a leaf node"""
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Returns the depth of the leaf"""
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """Returns 1 since a leaf is always counted as 1"""
        return 1

    def __str__(self):
        """Returns string representation of the leaf"""
        return f"leaf [value={self.value}]"


class Decision_Tree():
    """Represents a decision tree"""

    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        """Initializes a decision tree"""
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Returns the maximum depth of the tree"""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Counts the total nodes or leaves in the tree"""
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """Returns string representation of the entire tree"""
        # Node-dan gələn son yeni sətir işarəsini silirik ki, vizuallaşdırma düzgün bitsin
        return self.r






















































cat << 'EOF' > 2-build_decision_tree.py
#!/usr/bin/env python3
"""
Module to build a decision tree with pretty printing functionality
"""

import numpy as np


class Node:
    """Represents a node in a decision tree"""

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """Initializes a node"""
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Calculates the maximum depth below this node"""
        if self.left_child:
            left_depth = self.left_child.max_depth_below()
        else:
            left_depth = self.depth

        if self.right_child:
            right_depth = self.right_child.max_depth_below()
        else:
            right_depth = self.depth

        return max(left_depth, right_depth)

    def count_nodes_below(self, only_leaves=False):
        """Counts the nodes or leaves below this node"""
        left_count = 0
        right_count = 0

        if self.left_child:
            left_count = self.left_child.count_nodes_below(
                only_leaves=only_leaves)
        if self.right_child:
            right_count = self.right_child.count_nodes_below(
                only_leaves=only_leaves)

        if only_leaves:
            return left_count + right_count
        return left_count + right_count + 1

    def left_child_add_prefix(self, text):
        """Adds appropriate prefix lines for a left child"""
        lines = text.split("\n")
        new_text = "    +--->" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += "    |    " + x + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        """Adds appropriate prefix lines for a right child"""
        lines = text.split("\n")
        new_text = "    +--->" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += "         " + x + "\n"
        return new_text

    def __str__(self):
        """Returns string representation of the node and its children"""
        if self.is_root:
            out = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            out = f"node [feature={self.feature}, threshold={self.threshold}]\n"

        if self.left_child:
            out += self.left_child_add_prefix(self.left_child.__str__())
        if self.right_child:
            out += self.right_child_add_prefix(self.right_child.__str__())

        # Task 2 üçün __str__ mütləq səliqəli bitməlidir
        return out


class Leaf(Node):
    """Represents a leaf node in a decision tree"""

    def __init__(self, value, depth=None):
        """Initializes a leaf node"""
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Returns the depth of the leaf"""
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """Returns 1 since a leaf is always counted as 1"""
        return 1

    def __str__(self):
        """Returns string representation of the leaf"""
        return f"leaf [value={self.value}]"


class Decision_Tree():
    """Represents a decision tree"""

    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        """Initializes a decision tree"""
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Returns the maximum depth of the tree"""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Counts the total nodes or leaves in the tree"""
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """Returns string representation of the entire tree"""
        # Node-dan gələn son yeni sətir işarəsini silirik ki, vizuallaşdırma düzgün bitsin
        return self.root.__str__().rstrip("\n") + "\n"
