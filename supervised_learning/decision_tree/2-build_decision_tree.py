#!/usr/bin/env python3

class Node:
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_root = is_root
        self.depth = depth
        self.is_leaf = False

    def left_child_add_prefix(self, text):
        lines = text.split("\n")
        new_text = "+--->" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("|    " + x) + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        lines = text.split("\n")
        new_text = "+--->" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("     " + x) + "\n"
        return new_text

    def __str__(self):
        if self.is_root:
            res = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            res = f"node [feature={self.feature}, threshold={self.threshold}]\n"
        
        # Sol ve sağ çocukların string temsillerini al ve önek ekle
        res += self.left_child_add_prefix(str(self.left_child))
        res += self.right_child_add_prefix(str(self.right_child))
        
        return res.rstrip()

class Leaf:
    def __init__(self, value, depth=None):
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def __str__(self):
        return f"-> leaf [value={self.value}]"

class Decision_Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.root.__str__()
