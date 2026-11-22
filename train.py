import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/iris.csv")

X = df[https://github.com/HemasuriyaK10/26z3000004_MLOPS_WEEKLY_ASSIGNMENT/pulse
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
]

y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/iris_model.pkl")

print("Model saved successfully")
