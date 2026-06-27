def fit_node(self, node):
        """Recursively builds the tree"""
        node.feature, node.threshold = self.split_criterion(node)

        # Hər bir fərdin seçilmiş feature-a görə threshold-dan 
        # böyük və ya kiçik olmasını yoxlayırıq
        cond = (self.explanatory[:, node.feature] > node.threshold)
        left_population = node.sub_population & cond
        right_population = node.sub_population & ~cond

        # Yarpaq olma şərtləri: min_pop, max_depth və ya təmiz (homojen) class
        def is_leaf(pop):
            if np.sum(pop) < self.min_pop or node.depth >= self.max_depth:
                return True
            return len(np.unique(self.target[pop])) <= 1

        is_left_leaf = is_leaf(left_population)
        is_right_leaf = is_leaf(right_population)

        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def get_leaf_child(self, node, sub_population):
        """Creates a leaf child node"""
        # Ən çox rast gəlinən (most represented) sinfi tapırıq
        values, counts = np.unique(self.target[sub_population], return_counts=True)
        value = values[np.argmax(counts)]
        leaf_child = Leaf(value)
        leaf_child.depth = node.depth + 1
        leaf_child.sub_population = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """Creates a node child"""
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def accuracy(self, test_explanatory, test_target):
        """Calculates accuracy on test data"""
        return np.sum(np.equal(self.predict(test_explanatory), test_target)) / test_target.size
