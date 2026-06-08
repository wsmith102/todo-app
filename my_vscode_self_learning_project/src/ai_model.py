import numpy as np
from sklearn.linear_model import SGDClassifier

class SelfLearningAI:
    def __init__(self, n_features=4, n_classes=3):
        self.n_features = n_features
        self.n_classes = n_classes
        self.model = SGDClassifier(loss="log_loss")
        self.initialized = False

    def _init_model(self, X, y):
        classes = np.arange(self.n_classes)
        self.model.partial_fit(X, y, classes=classes)
        self.initialized = True

    def learn(self, features, label):
        X = np.array(features).reshape(1, -1)
        y = np.array([label])

        if not self.initialized:
            self._init_model(X, y)
        else:
            self.model.partial_fit(X, y)

    def predict(self, features):
        X = np.array(features).reshape(1, -1)
        return int(self.model.predict(X)[0])
