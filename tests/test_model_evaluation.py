import pandas as pd
import joblib

from sklearn.metrics import accuracy_score

df = pd.read_csv("data/iris.csv")

X = df[
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
]

y = df["species"]

model = joblib.load("models/iris_model.pkl")


def test_model_accuracy():

    predictions = model.predict(X)

    accuracy = accuracy_score(
        y,
        predictions
    )

    assert accuracy >= 0.90
