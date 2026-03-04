# DSBA6010 Final Project
## LLM-Based Privacy Attacks on Employee Data

This project investigates the privacy risks of sharing employee data in the age of Large Language Models (LLMs). Using the IBM HR Analytics dataset, we apply Differential Privacy at multiple epsilon levels and then evaluate how well modern inference attacks can recover sensitive information from the privatized data.

---

## Project Overview

Sharing employee data — even in anonymized form — has become increasingly dangerous as LLMs enable new classes of inference attacks that were not feasible just a few years ago. This project demonstrates that risk concretely by:

1. **Privatizing** the IBM HR dataset using Differential Privacy (DP) at several epsilon (ε) levels
2. **Assessing utility** by measuring model accuracy after privatization
3. **Attacking** the privatized data using Membership Inference and Attribute Inference attacks

---

## Dataset

**IBM HR Analytics Employee Attrition & Performance**  
Source: [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
1,470 employee records with 35 features including age, income, job satisfaction, department, and attrition label.

To use the dataset, either:
- Download manually from Kaggle and place `WA_Fn-UseC_-HR-Employee-Attrition.csv` in the project root, or
- Use the Kaggle API (see setup instructions below)

---

## Notebook Structure

| Section | Description |
|---|---|
| 0. Dependencies | Install required packages |
| 1. Setup & Data Loading | Load IBM HR dataset via Kaggle API or manual download |
| 2. EDA | Explore attrition distribution, feature distributions, correlations |
| 3. Preprocessing | Encode categoricals, train/test split, feature scaling |
| 4. Baseline Model | Logistic Regression on original data (accuracy ceiling) |
| 5. Differential Privacy | Apply DP at ε = 0.1, 1.0, 10.0 using `diffprivlib` |
| 6. Utility Assessment | Compare model accuracy/AUC across epsilon levels |
| 7. Membership Inference Attack | Can an attacker determine if a record was in the training set? |
| 8. Attribute Inference Attack | Can an attacker recover sensitive attributes from the privatized data? |

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
