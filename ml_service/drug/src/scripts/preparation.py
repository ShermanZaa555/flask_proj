import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import category_encoders as ce

def preprocessing():
    df = pd.read_csv('../flask_proj/ml_service/drug/data/raw data/drug200.csv')
    df_clean = data_cleansing(df)
    df_wrag = data_wrangling(df_clean)
    df_wrag.to_csv('../flask_proj/ml_service/drug/data/processed data/drug_clean.csv', index=False)

def data_cleansing(df):
    df_clean = df.copy()
    df_clean = edit_word(df_clean)
    df_clean = clean_outlier(df_clean)
    return df_clean

def edit_word(df):
    df['Drug'] = df['Drug'].str.replace('d','D')
    return df

def clean_outlier(df):
    df_num = [i for i in df.dtypes.index if df.dtypes[i] == 'int64' or df.dtypes[i] == 'float64']
    df_num_out = [i for i in df_num if len(find_outliers_IQR(df[i])) > 0]

    if len(df_num_out) == 0:
        return df
    else:
        for i in df_num_out:
            tenth_q = df[i].quantile(0.10)
            ninth_q = df[i].quantile(0.90)
            df[i] = np.where(df[i] < tenth_q, tenth_q, df[i])
            df[i] = np.where(df[i] > ninth_q, ninth_q, df[i])

    return df

def find_outliers_IQR(df):
  Q1 = df.quantile(0.25)
  Q3 = df.quantile(0.75)
  IQR = Q3-Q1
  outliers = df[((df < (Q1 - 1.5*IQR)) | (df > (Q3 + 1.5*IQR)))]
  return outliers

def data_wrangling(df):
    df_wrag = df.copy()
    df_str = [i for i in df_wrag.dtypes.index if df.dtypes[i] == 'object']
    df_bin = [i for i in df_str if len(df[i].unique()) == 2]

    label_encoder(df_wrag, df_bin)
    ordinal_encoding(df_wrag)
    target_encoding(df_wrag)

    return df_wrag

def label_encoder(df, df_bin):
    label_encoder = LabelEncoder()
    for i in df_bin:
        df[i] = label_encoder.fit_transform(df[i])

def ordinal_encoding(df):
    BP_Dict = {"HIGH": 1, "NORMAL" : 0,"LOW" : -1}

    df["Ordinal_BP"] = df.BP.map(BP_Dict)
    df.drop(["BP"], axis=1, inplace=True)

def target_encoding(df):
    encoder = ce.OrdinalEncoder(cols=['Drug'], mapping=[{'col':'Drug', 'mapping':{'DrugA':0, 'DrugB':1, 'DrugC':2, 'DrugX':3, 'DrugY':4}}])
    df["Drug"] = encoder.fit_transform(df["Drug"])
    df["Drug"] = df["Drug"].astype('str')