from fastapi import FastAPI
from pydantic import BaseModel

from src.ai_model import SelfLearningAI
from src.vector_memory import VectorMemory
from src.background_jobs import BackgroundTrainer
from src.dashboard import router as dashboard_router
from src.database import SQLiteDB

app = FastAPI(title="Self-Learning AI Platform")

model = SelfLearningAI(n_features=4, n_classes=3)
memory = VectorMemory(dim=4)
db = SQLiteDB()

trainer = BackgroundTrainer(model, db, interval=5)
trainer.start()

app.include_router(dashboard_router)

class TeachRequest(BaseModel):
    features: list[float]
    label: int

class PredictRequest(BaseModel):
    features: list[float]

@app.post("/teach")
def teach(req: TeachRequest):
    db.insert_sample(req.features, req.label)
    memory.add(req.features, req.label)
    return {"status": "saved to SQLite and queued for training"}

@app.post("/predict")
def predict(req: PredictRequest):
    pred = model.predict(req.features)
    similar = memory.search(req.features)
    return {
        "prediction": pred,
        "similar_examples": similar
    }
