# Characterizing Protein-Protein Interaction Sites from Sequence Data using Tree Ensemble Approaches


Ana Esteve Garcia, Gyula Maloveczky, Jacob M. Reaves,  Jasmine Y. Chen,   Shabnam Shajahan


---

## Overview

This project explores the use of machine learning to predict protein-protein interaction (PPI) interface residues from sequence-derived features. Interface residues play essential roles in biological functions such as signal transduction, enzymatic activity, and immune response. Given the expense and complexity of experimental identification, we apply interpretable ML models to make computational predictions.

---

## Objectives

- Compare tree-based ML models: Decision Tree, Random Forest, XGBoost
- Investigate the impact of feature window size (3, 5, 7, or 9 residues)
- Use SHAP to interpret model predictions
- Identify biologically meaningful features that distinguish interface residues

---

## Datasets
- Our primary dataset is the test subset of the on used in Stringer et al., 2022
- We also made our own subset, which included proteins potentially involved in Human-microbiome interactions according to [Zhou et al., 2022], to test if these interaction sites are different from the rest.
- Total residues: 65,150  
- Features include:
  - Evolutionary (PSSM)
  - Physicochemical (hydrophobicity, solvent accessibility)
  - Structural (secondary structure predictions)
  - Windowed features (a sliding window average of features with window sizes 3,5,7 and 9)
- Labels: Interface vs. non-interface residues  


---

## Methodology

1. **Preprocessing**
   - Categorical encoding using Eisenberg hydrophobicity scale (unique value for each amino acid)
   - Removal of redundant and metadata features
   - Addressed class imbalance using different strategies (SMOTE, SMOTE-Tomek, ADASYN, Random Undersampling)

2. **Modeling**
   - 5-fold GroupKFold cross-validation to avoid data leakage (to avoid using residues from the same protein in both the train and the test set)
   - Hyperparameter tuning with Bayesian Optimization
   - Training with tree-based models with all possible window size combinations

3. **Evaluation**
   - Primary metric: ROC-AUC
   - Model interpretation with SHAP
     
  

---

## Results

| Model                     | ROC-AUC | Precision | Recall |
|---------------------------|---------|-----------|--------|
| Random Forest (WM9)       | 0.652   | 0.193     | 0.634  |
| Random Forest (Simple + WM9) | 0.637 | 0.147    | 0.623     |



- Ensamble methods outperform simple decision tree model
- XGBoost doesn't outperform Random Forest

  
  <img width="217" alt="comparison_of_models_on_CV" src="https://github.com/user-attachments/assets/29e0f996-189d-4d4a-9172-44e63c362dae" />
- While increasing the window size typically enhanced performance, incorporating multiple window sizes yielded diminishing returns and occasionally degraded model performance.
![window](https://github.com/user-attachments/assets/453a9eb5-70d5-4efd-97ed-99f6eadf2592)

  
- Key predictive features:
  - Windowed PSSM scores
  - Hydrophobicity (inversely related to interface probability)
  - Solvent accessibility
 
- We did not find significant difference between protein interfaces involved in host-microbiome interactions and proteins that are not involved in such interactions
 
    


---

## Interpretation

- SHAP summary plots revealed windowed PSSMs, hydrophilicity, and surface accessibility as the most influential features
- Unexpectedly, hydrophobic residues were less likely to be predicted as interface residues, potentially due to the fact that they are more likely to be in the hydrophobic core.
- Nonlinear relationship between Windowed PSSM score and SHAP value

---
![shap](https://github.com/user-attachments/assets/3e333b6a-58f9-4789-8069-e5b64ba70884)
![top_4](https://github.com/user-attachments/assets/9c7b27aa-d648-40a5-9da8-b6c4f2cc1997)

## Limitations

- Possible dataset bias (e.g., inclusion of only known interaction sites)
- Simpler models underperformed compared to already established deep learning deep learning(e.g., PIPENN [Stringer et al., 2022])
- Model does not account for the sequential nature of the data explicitly (only trough engineered features)

---

## Future Work

- Apply sequential deep learning models such as CNNs, RNNs, or transformers
- Incorporate protein language model embeddings (e.g., ProtT5-XL)
- Explore experimental validation for SHAP-derived insights

---

## References
1. [Stringer et al., 2022] Stringer, B., de Ferrante, H., Abeln,
S., Heringa, J., Feenstra, K. A., and Haydarlou, R. (2022).
Pipenn: protein interface prediction from sequence with
an ensemble of neural nets. Bioinformatics, 38(8):2111–
2118.
2. [Zhou et al., 2022] Zhou, H., Beltrán, J.F. & Brito, I.L. Host-microbiome protein-protein interactions capture disease-relevant pathways. Genome Biol 23, 72 (2022).
