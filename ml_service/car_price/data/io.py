import pandas as pd
from sklearn.preprocessing import StandardScaler

def read_csv_file(path):
    df = pd.read_csv(path)
    df_copy = df.copy()
    return df_copy

def input_std_scaler(input):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(input)
    return x_scaled