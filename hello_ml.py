import numpy as np

class PERCEPTRON:

    def __init__(self, eta=0.01, n_itr=10):
        pass

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    
    # fit the training data
    def fit(self, X, y):

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_itr):
            pass

        pass