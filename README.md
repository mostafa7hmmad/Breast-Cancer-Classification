# Breast-Cancer-Classification
![Breast](A.jpg)
## Overview
This project uses a machine learning model to predict whether a breast tumor is malignant or benign based on various physical characteristics of the tumor cells. The goal is to assist in early diagnosis and treatment planning for breast cancer patients.

---

## Dataset Description

The dataset contains features extracted from digitized images of breast mass biopsies. Each feature represents a physical measurement of the tumor cells.

### Features
- **Mean measurements**:
  - `x.radius_mean`
  - `x.texture_mean`
  - `x.perimeter_mean`
  - `x.area_mean`

- **Standard error (SE) measurements**:
  - `x.perimeter_se`
  - `x.area_se`
  - `x.compactness_se`
  - `x.concavity_se`
  - `x.concave_pts_se`
  - `x.fractal_dim_se`

- **Worst (maximum) measurements**:
  - `x.radius_worst`
  - `x.texture_worst`
  - `x.perimeter_worst`
  - `x.area_worst`
  - `x.smoothness_worst`
  - `x.compactness_worst`
  - `x.concavity_worst`
  - `x.concave_pts_worst`
  - `x.symmetry_worst`
  - `x.fractal_dim_worst`

### Target Variable
- `y`: Tumor classification (0 = Benign, 1 = Malignant)

---

## Model Development

### Model Used
- Random Forest Classifier

### Hyperparameter Tuning
Grid Search with 5-fold cross-validation was used to identify the best hyperparameters:
- `max_depth`: None
- `max_features`: `'sqrt'`
- `min_samples_leaf`: 2
- `min_samples_split`: 5
- `n_estimators`: 50

### Performance Metrics

#### Test Set Accuracy
- **94.52%**

#### Confusion Matrix
```
[[50  2]
 [ 2 19]]
```
- True Positives: 50
- True Negatives: 19
- False Positives: 2
- False Negatives: 2

#### Classification Report
```
               Precision    Recall  F1-score   Support

    Benign (0)       0.96      0.96      0.96        52
 Malignant (1)       0.90      0.90      0.90        21

    Accuracy                           0.95        73
   Macro avg       0.93      0.93      0.93        73
Weighted avg       0.95      0.95      0.95        73
```

#### Cross-Validation Accuracy
- Individual Fold Scores: [0.9041, 0.8889, 0.9444, 0.9583, 0.9583]
- Mean Cross-validation Accuracy: **93.08%**

---

## Insights

- The Random Forest Classifier demonstrates excellent predictive power, achieving an accuracy of 94.52% on the test set.
- The model's high precision and recall values indicate its reliability in identifying both benign and malignant tumors.

### Recommendations
1. Perform feature importance analysis to identify the most influential features for prediction.
2. Explore alternative models (e.g., ensemble methods or neural networks) for comparison.
3. Use interpretability tools (e.g., SHAP or LIME) to explain predictions for individual patients.

