import threading
import time
import numpy as np

class BackgroundTrainer:
    def __init__(self, model, db, interval=5):
        self.model = model
        self.db = db
        self.interval = interval
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self.loop, daemon=True)
            thread.start()

    def loop(self):
        while self.running:
            X, y = self.db.load_all()
            if len(y) > 0:
                X = np.array(X)
                y = np.array(y)
                self.model.learn(X, y)
            time.sleep(self.interval)
