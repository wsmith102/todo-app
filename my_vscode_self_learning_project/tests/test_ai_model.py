from src.ai_model import SelfLearningAI

def test_self_learning_prediction():
    model = SelfLearningAI(n_features=4, n_classes=3)

    # Teach the model one example
    model.learn([0.1, 0.2, 0.3, 0.4], 1)

    # Predict using the same pattern
    pred = model.predict([0.1, 0.2, 0.3, 0.4])

    assert pred in [0, 1, 2]
