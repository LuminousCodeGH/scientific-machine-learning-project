import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, roc_auc_score, precision_score, recall_score
from imblearn.over_sampling import SMOTE
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

#Performance without any oversampling/undersampling
X_train = train_data.drop(columns=['p_interface','aa_ProtPosition','uniprot_id','domain'])
y_train = train_data["p_interface"]

X_test = test_data.drop(columns=['p_interface','aa_ProtPosition','uniprot_id','domain']) 
y_test = test_data["p_interface"]
model_baseline = RandomForestClassifier(random_state=46)
model_baseline.fit(X_train, y_train)

y_prediction_baseline = model_baseline.predict(X_test)
y_prediction_probability_scores_baseline = model_baseline.predict_proba(X_test)[:, 1]

print("AUC Score:", roc_auc_score(y_test, y_prediction_probability_scores_baseline))
#AUC=0.644
print("Classification Report:\n", classification_report(y_test, y_prediction_baseline))
#precision,recall for minority class was 0
#Oversampling using SMOTE
smote = SMOTE(sampling_strategy='auto', random_state=46)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

#To check how it has resampled (oversampling minority class)
#print("Before SMOTE:", y_train_baseline.value_counts())


#Performace after oversampling
model_smote = RandomForestClassifier(random_state=46)
model_smote.fit(X_train_smote, y_train_smote)

y_prediction_smote = model_smote.predict(X_test)
y_prediction_probability_scores_smote = model_smote.predict_proba(X_test)[:, 1]

print("AUC Score:", roc_auc_score(y_test, y_prediction_probability_scores_smote))
#AUC=0.683
print("Classification Report:\n", classification_report(y_test, y_prediction_smote))
#Little improvement

#ADASYN
from imblearn.over_sampling import ADASYN
adasyn = ADASYN(sampling_strategy='auto', random_state=46)
X_train_ADASYN, y_train_ADASYN = adasyn.fit_resample(X_train, y_train)
#print("After ADASYN:", y_train_ADASYN.value_counts())
#After ADASYN: p_interface
#0    45951
#1    45384
model_oversampling_ADASYN = RandomForestClassifier(random_state=46)
model_oversampling_ADASYN.fit(X_train_ADASYN, y_train_ADASYN)

y_prediction_ADASYN = model_oversampling_ADASYN.predict(X_test)
y_prediction_probability_scores_ADASYN = model_oversampling_ADASYN.predict_proba(X_test)[:, 1]

print("AUC Score:", roc_auc_score(y_test, y_prediction_probability_scores_ADASYN))
#AUC=0.67
print("Classification Report:\n", classification_report(y_test, y_prediction_ADASYN))
#lower than smote

#TOMEK LINK & SMOTE
from imblearn.combine import SMOTETomek
smote_tomek = SMOTETomek(random_state=46)
X_train_SMOTETomek, y_train_SMOTETomek = smote_tomek.fit_resample(X_train, y_train)

model_SMOTETomek = RandomForestClassifier(random_state=46)
model_SMOTETomek.fit(X_train_SMOTETomek, y_train_SMOTETomek)

y_prediction_SMOTETomek = model_SMOTETomek.predict(X_test)
y_prediction_probability_scores_SMOTETomek = model_SMOTETomek.predict_proba(X_test)[:, 1]

print("AUC Score:", roc_auc_score(y_test, y_prediction_probability_scores_SMOTETomek))
#AUC=0.683
print("Classification Report:\n", classification_report(y_test, y_prediction_SMOTETomek))
#Similar to smote


