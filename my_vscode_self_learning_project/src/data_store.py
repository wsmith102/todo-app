# src/data_store.py
import numpy as np

class DataStore:
    def __init__(self, n_features: int):
        self.n_features = n_features
        self.X = np.empty((0, n_features))
        self.y = np.empty((0,), dtype=int)

    def add_sample(self, features, label):
        features = np.array(features).reshape(1, -1)
        self.X = np.vstack([self.X, features])
        self.y = np.append(self.y, label)

    def get_all(self):
        return self.X, self.y
