#!/usr/bin/env python3
import numpy as np

# ... (Əvvəlki kodlarınızın üstündə olduğu kimi saxlayın) ...

class Node:
    # ... (init və digər metodlar) ...
    def pred(self, x):
        """Recursively predicts class for a given input x"""
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        else:
            return self.right_child.pred(x)

class Leaf:
    # ... (init və digər metodlar) ...
    def pred(self, x):
        """Returns the leaf value"""
        return self.value

class Decision_Tree:
    # ... (init və digər metodlar) ...
    def pred(self, x):
        """Calls prediction from root"""
        return self.root.pred(x)

    def update_predict(self):
        """Computes the efficient prediction function"""
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()
        
        # Effektiv proqnozlaşdırma üçün indikatorlardan istifadə edirik
        self.predict = lambda A: np.array([
            leaf.value for leaf in leaves 
            for i in range(A.shape[0]) 
            if leaf.indicator(A)[i]
        ]).reshape(A.shape[0])
