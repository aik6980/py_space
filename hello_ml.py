import numpy as np
import pandas as pd

class PERCEPTRON:

    def __init__(self, eta=0.01, n_itr=10):
        self.eta = eta
        self.n_itr = n_itr

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    
    # fit the training data
    def fit(self, X, y):

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_itr):
            errors = 0
            for xi, target in zip(X,y)
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update!=0)

            self.errors_.append(errors)
