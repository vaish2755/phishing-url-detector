import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ============================================================
# 1. LOAD PROCESSED DATA
# ============================================================

df = pd.read_csv("data/processed_data.csv")

print("Dataset loaded.")
print("Dataset shape:", df.shape)


# ============================================================
# 2. SEPARATE FEATURES AND TARGET
# ============================================================

X = df.drop("label", axis=1)
y = df["label"]

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget distribution:")
print(y.value_counts())


# ============================================================
# 3. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining set:")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\nTesting set:")
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)


# ============================================================
# 4. LOGISTIC REGRESSION
# ============================================================

print("\n" + "=" * 50)
print("Training Logistic Regression...")
print("=" * 50)

logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

logistic_model.fit(X_train, y_train)

logistic_pred = logistic_model.predict(X_test)


logistic_accuracy = accuracy_score(
    y_test,
    logistic_pred
)

logistic_precision = precision_score(
    y_test,
    logistic_pred
)

logistic_recall = recall_score(
    y_test,
    logistic_pred
)

logistic_f1 = f1_score(
    y_test,
    logistic_pred
)

logistic_cm = confusion_matrix(
    y_test,
    logistic_pred
)


print("\nLogistic Regression Results:")
print(f"Accuracy:  {logistic_accuracy:.4f}")
print(f"Precision: {logistic_precision:.4f}")
print(f"Recall:    {logistic_recall:.4f}")
print(f"F1-score:  {logistic_f1:.4f}")

print("\nConfusion Matrix:")
print(logistic_cm)


# ============================================================
# 5. RANDOM FOREST
# ============================================================

print("\n" + "=" * 50)
print("Training Random Forest...")
print("=" * 50)

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

random_forest_model.fit(X_train, y_train)

random_forest_pred = random_forest_model.predict(X_test)


random_forest_accuracy = accuracy_score(
    y_test,
    random_forest_pred
)

random_forest_precision = precision_score(
    y_test,
    random_forest_pred
)

random_forest_recall = recall_score(
    y_test,
    random_forest_pred
)

random_forest_f1 = f1_score(
    y_test,
    random_forest_pred
)

random_forest_cm = confusion_matrix(
    y_test,
    random_forest_pred
)


print("\nRandom Forest Results:")
print(f"Accuracy:  {random_forest_accuracy:.4f}")
print(f"Precision: {random_forest_precision:.4f}")
print(f"Recall:    {random_forest_recall:.4f}")
print(f"F1-score:  {random_forest_f1:.4f}")

print("\nConfusion Matrix:")
print(random_forest_cm)


# ============================================================
# 6. MODEL COMPARISON
# ============================================================

print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest"
    ],
    "Accuracy": [
        logistic_accuracy,
        random_forest_accuracy
    ],
    "Precision": [
        logistic_precision,
        random_forest_precision
    ],
    "Recall": [
        logistic_recall,
        random_forest_recall
    ],
    "F1 Score": [
        logistic_f1,
        random_forest_f1
    ]
})

print(comparison.to_string(index=False))


# ============================================================
# 7. SELECT BEST MODEL
# ============================================================

if random_forest_f1 > logistic_f1:
    best_model = random_forest_model
    best_model_name = "Random Forest"
else:
    best_model = logistic_model
    best_model_name = "Logistic Regression"


print("\nSelected model:", best_model_name)


# ============================================================
# 8. SAVE MODEL
# ============================================================

joblib.dump(best_model, "model.pkl")

print("\nBest model saved as: model.pkl")


# Save feature names
feature_names = list(X.columns)

joblib.dump(
    feature_names,
    "feature_names.pkl"
)

print("Feature names saved as: feature_names.pkl")
# ============================================================
# 9. CONFUSION MATRIX VISUALIZATION
# ============================================================

plt.figure(figsize=(7, 5))

sns.heatmap(
    confusion_matrix(y_test, random_forest_pred),
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Legitimate", "Phishing"],
    yticklabels=["Legitimate", "Phishing"]
)

plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.tight_layout()

plt.savefig("confusion_matrix.png", dpi=300)

plt.show()

print("\nConfusion matrix saved as: confusion_matrix.png")