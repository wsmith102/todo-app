
import numpy as np

class VectorMemory:
    def __init__(self, dim=4):
        self.dim = dim
        self.vectors = []
        self.labels = []

    def add(self, vector, label=None):
        v = np.array(vector)
        self.vectors.append(v)
        self.labels.append(label)

    def search(self, query, top_k=3):
        if not self.vectors:
            return []

        q = np.array(query)
        sims = []

        for idx, v in enumerate(self.vectors):
            sim = np.dot(q, v) / (np.linalg.norm(q) * np.linalg.norm(v))
            sims.append((sim, self.labels[idx], v.tolist()))

        sims.sort(reverse=True, key=lambda x: x[0])
        return sims[:top_k]
