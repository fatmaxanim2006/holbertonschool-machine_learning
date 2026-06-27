def update_indicator(self):
        """Computes the indicator function for the node"""
        def is_large_enough(x):
            if not self.lower:
                return np.ones(x.shape[0], dtype=bool)
            # Hər bir feature üçün lower bound-dan böyük olmasını yoxlayır
            results = [np.greater(x[:, key], val) for key, val in self.lower.items() if val != -np.inf]
            if not results:
                return np.ones(x.shape[0], dtype=bool)
            return np.all(results, axis=0)

        def is_small_enough(x):
            if not self.upper:
                return np.ones(x.shape[0], dtype=bool)
            # Hər bir feature üçün upper bound-dan kiçik və ya bərabər olmasını yoxlayır
            results = [np.less_equal(x[:, key], val) for key, val in self.upper.items() if val != np.inf]
            if not results:
                return np.ones(x.shape[0], dtype=bool)
            return np.all(results, axis=0)

        self.indicator = lambda x: np.all(np.array([is_large_enough(x), is_small_enough(x)]), axis=0)

        # Uşaqlar üçün də rekursiv olaraq çağırırıq
        if not self.is_leaf:
            self.left_child.update_indicator()
            self.right_child.update_indicator()
