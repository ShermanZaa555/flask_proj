import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def tts():
    df = pd.read_csv('../flask_proj/ml_service/drug/data/processed data/drug_clean.csv')
    df_model = df.copy()
    X, y = feature_target_split(df_model)

    sm = SMOTE(random_state=42)
    X_sm, y_sm = sm.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X_sm, y_sm, random_state=0)

    return X_train, X_test, y_train, y_test

def feature_target_split(df):
    X = df.drop('Drug', axis=1)
    y = df['Drug']
    return X, y