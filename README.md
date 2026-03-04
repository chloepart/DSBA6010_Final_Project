# DSBA6010 Final Project
## LLM-Based Privacy Attacks on Employee Data

---

## AI CONTEXT BLOCK
> This section is written for AI tools (e.g., Claude, GitHub Copilot) to quickly understand the project goals, structure, and conventions before assisting with code or analysis.

**What this project does:**
This project demonstrates that employee data shared publicly — even after applying Differential Privacy (DP) — remains vulnerable to modern LLM-based inference attacks. We privatize a real HR dataset at multiple privacy budgets (epsilon levels) and then attack it using Membership Inference and Attribute Inference techniques.

**Primary goal:** Show that increasing epsilon (weaker privacy) improves model utility but increases attack success rate, and that even low-epsilon (stronger privacy) settings may not fully protect against modern inference attacks.

**Target variable:** `Attrition` (binary: Yes/No) — whether an employee left the company.

**Sensitive attributes of interest for inference attacks:** `MonthlyIncome`, `Age`, `Gender`, `JobSatisfaction`, `PerformanceRating`

**Privacy mechanism used:** Differential Privacy via the `diffprivlib` library (IBM's DP library, scikit-learn compatible). Logistic Regression is the primary model throughout for consistency and DP compatibility.

**Epsilon levels tested:** ε = 0.1 (strong privacy), ε = 1.0 (moderate), ε = 10.0 (weak), plus a no-privacy baseline.

**Attack types:**
- *Membership Inference:* Can an attacker determine whether a specific record was in the training set?
- *Attribute Inference:* Can an attacker recover sensitive attribute values from the privatized dataset?

**Key metric:** ROC-AUC is the primary evaluation metric across both utility and attack success, enabling apples-to-apples comparison across epsilon levels.

**Notebook file:** `DSBA6010_Final_Project.ipynb`  
**Dataset file:** `WA_Fn-UseC_-HR-Employee-Attrition.csv` (not committed to repo — see setup)  
**Language/environment:** Python 3, pip, Jupyter Notebook / VS Code

---

## Project Overview

Sharing employee data — even in anonymized form — has become increasingly dangerous as LLMs enable inference attacks that were not feasible just a few years ago. This project demonstrates that risk concretely by:

1. **Privatizing** the IBM HR dataset using Differential Privacy at several ε levels
2. **Assessing utility** by measuring model accuracy after privatization
3. **Attacking** the privatized data using Membership Inference and Attribute Inference attacks

---

## Dataset

**IBM HR Analytics Employee Attrition & Performance**  
Source: [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
1,470 employee records with 35 features including age, income, job satisfaction, department, and attrition label.

Three constant-value columns are dropped during preprocessing: `EmployeeCount`, `Over18`, `StandardHours`.  
All categorical columns are label-encoded. Features are standardized with `StandardScaler` before model training.  
Train/test split: 80/20, stratified on `Attrition`.

To use the dataset, either:
- Download manually from Kaggle and place `WA_Fn-UseC_-HR-Employee-Attrition.csv` in the project root, or
- Use the Kaggle API (see setup instructions below)

---

## Notebook Structure

| Section | Description | Status |
|---|---|---|
| 0. Dependencies | Install required packages | ✅ Complete |
| 1. Setup & Data Loading | Load IBM HR dataset via Kaggle API or manual download | ✅ Complete |
| 2. EDA | Explore attrition distribution, feature distributions, correlations | ✅ Complete |
| 3. Preprocessing | Encode categoricals, train/test split, feature scaling | ✅ Complete |
| 4. Baseline Model | Logistic Regression on original data (accuracy ceiling) | ✅ Complete |
| 5. Differential Privacy | Apply DP at ε = 0.1, 1.0, 10.0 using `diffprivlib` | 🔲 Pending |
| 6. Utility Assessment | Compare model accuracy/AUC across epsilon levels | 🔲 Pending |
| 7. Membership Inference Attack | Can an attacker determine if a record was in the training set? | 🔲 Pending |
| 8. Attribute Inference Attack | Can an attacker recover sensitive attributes from the privatized data? | 🔲 Pending |

---

## Setup

```bash
# Clone the repo
git clone https://github.com/chloepart/DSBA6010_Final_Project.git
cd DSBA6010_Final_Project

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn diffprivlib kaggle

# (Optional) Configure Kaggle API
# Download kaggle.json from https://www.kaggle.com/settings -> API -> Create New Token
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

Then open `DSBA6010_Final_Project.ipynb` in VS Code or Jupyter and run cells top to bottom.

---

## Project Timeline

| Milestone | Due Date | Status |
|---|---|---|
| Research phase + presentation on Liu et al. 2025 | March 20, 2025 | 🔲 Pending |
| Data loading, privatization, utility assessment | March 30, 2025 | 🔲 Pending |
| Membership Inference + Attribute Inference attacks | April 9, 2025 | 🔲 Pending |

---

## Key References

- Liu, Y., et al. (2025). Evaluating LLM-based personal information extraction and countermeasures. *USENIX Security '25*.
- Staab, R., et al. (2024). Beyond memorization: Violating privacy via inference with large language models. *ICLR 2024*.
- Jayaraman, B., & Evans, D. (2022). Are attribute inference attacks just imputation? *CCS '22*.
- Kandpal, N., et al. (2024). User inference attacks on large language models. *EMNLP 2024*.
- Cirillo, S., et al. (2025). Augmenting anonymized data with AI. *arXiv:2504.03778*.
- Yan, D., et al. (2025). Stop tracking me! Proactive defense against attribute inference attacks in LLMs. *arXiv:2602.11528*.
- IBM. (2015). IBM HR analytics employee attrition & performance [Dataset]. Kaggle.

---

## Course

DSBA 6010 — University of North Carolina at Charlotte
