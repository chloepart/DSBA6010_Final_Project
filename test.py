"""
Logistic Regression: Predict High Performer (PerformanceRating == 4)
Dataset: IBM HR Analytics Employee Attrition & Performance (Kaggle)

Binary target:
  1 = High Performer (PerformanceRating == 4)
  0 = Not High Performer (PerformanceRating == 3)

Usage:
  1. Download WA_Fn-UseC_-HR-Employee-Attrition.csv from Kaggle
  2. Place it in the same directory as this script
  3. Run: python performance_logistic_regression.py
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    ConfusionMatrixDisplay,
)
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# ── 1. Load data ──────────────────────────────────────────────────────────────
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(f"Dataset shape: {df.shape}")
print(f"\nPerformanceRating value counts:\n{df['PerformanceRating'].value_counts()}")

# ── 2. Build binary target ────────────────────────────────────────────────────
df["HighPerformer"] = (df["PerformanceRating"] == 4).astype(int)
print(f"\nTarget distribution:\n{df['HighPerformer'].value_counts(normalize=True).round(3)}")

# ── 3. Drop columns that leak the target or are constant ──────────────────────
drop_cols = [
    "PerformanceRating",   # target source
    "DailyRate",
    "EmployeeCount",
    "EmployeeNumber",
    "JobInvolvement",
    "HourlyRate",
    "MonthlyIncome",
    "MonthlyRate",
    "PercentSalaryHike",
    "StandardHours",
    "StockOptionLevel",
]
df = df.drop(columns=drop_cols, errors="ignore")

# ── 4. Encode categorical features ───────────────────────────────────────────
cat_cols = df.select_dtypes(include="object").columns.tolist()
print(f"\nEncoding categoricals: {cat_cols}")

le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# ── 5. Train / test split ─────────────────────────────────────────────────────
X = df.drop(columns=["HighPerformer"])
y = df["HighPerformer"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ── 6. Scale features ─────────────────────────────────────────────────────────
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

# ── 7. Fit logistic regression ────────────────────────────────────────────────
model = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
model.fit(X_train_sc, y_train)

# ── 8. Evaluate ───────────────────────────────────────────────────────────────
y_pred      = model.predict(X_test_sc)
y_pred_prob = model.predict_proba(X_test_sc)[:, 1]

print("\n── Classification Report ──────────────────────────────")
print(classification_report(y_test, y_pred, target_names=["Not High (3)", "High (4)"]))

roc = roc_auc_score(y_test, y_pred_prob)
print(f"ROC-AUC: {roc:.4f}")

# ── 9. Feature importance (log-odds coefficients) ─────────────────────────────
coef_df = pd.DataFrame({
    "Feature":     X.columns,
    "Coefficient": model.coef_[0],
    "Abs":         np.abs(model.coef_[0]),
}).sort_values("Abs", ascending=False)

print("\n── Top 10 Features by |Coefficient| ──────────────────")
print(coef_df.head(10).drop(columns="Abs").to_string(index=False))

# ── 10. Plots ─────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=["Not High (3)", "High (4)"])
disp.plot(ax=axes[0], colorbar=False, cmap="Blues")
axes[0].set_title("Confusion Matrix")

# Top-15 feature coefficients
top15 = coef_df.head(15).sort_values("Coefficient")
colors = ["#e05c5c" if v < 0 else "#4a90d9" for v in top15["Coefficient"]]
axes[1].barh(top15["Feature"], top15["Coefficient"], color=colors)
axes[1].axvline(0, color="black", linewidth=0.8, linestyle="--")
axes[1].set_xlabel("Log-Odds Coefficient")
axes[1].set_title("Top 15 Feature Coefficients\n(blue = increases P(High Performer))")

plt.tight_layout()
plt.savefig("performance_lr_results.png", dpi=150, bbox_inches="tight")
print("\nPlot saved → performance_lr_results.png")
plt.show()