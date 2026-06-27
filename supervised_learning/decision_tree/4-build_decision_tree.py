#!/usr/bin/env python3
import numpy as np

# ... (Əvvəlki metodlarınız burada qalmalıdır) ...

class Node:
    # ... (init və digər metodlar) ...

    def update_bounds_below(self):
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -1 * np.inf}

        for child in [self.left_child, self.right_child]:
            # Sol uşaq üçün (kiçik bərabərdir threshold)
            if child == self.left_child:
                child.lower = self.lower.copy()
                child.upper = self.upper.copy()
                child.upper[self.feature] = min(child.upper.get(self.feature, np.inf), self.threshold)
            
            # Sağ uşaq üçün (böyükdür threshold)
            else:
                child.lower = self.lower.copy()
                child.upper = self.upper.copy()
                child.lower[self.feature] = max(child.lower.get(self.feature, -np.inf), self.threshold)

        for child in [self.left_child, self.right_child]:
            child.update_bounds_below()

class Leaf:
    # ... (init və digər metodlar) ...

    def update_bounds_below(self):
        pass

class Decision_Tree:
    # ... (init və digər metodlar) ...

    def update_bounds(self):
        self.root.update_bounds_below()
