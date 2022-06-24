import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocessing():
    df = pd.read_csv('../flask_proj/ml_service/car_price/data/raw data/CarPrice.csv')
    df_clean = data_cleansing(df)
    df_wrag = data_wrangling(df_clean)
    df_wrag.to_csv('../flask_proj/ml_service/car_price/data/processed data/car_price_clean.csv', index=False)

def data_cleansing(df):
    df_clean = df.copy()
    df_clean.drop(['car_ID', 'CarName'], axis=1, inplace = True)
    df_clean = clean_outlier(df_clean)
    return df_clean

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
    df_category = [i for i in df_str if len(df[i].unique()) > 2]

    label_encoder(df_wrag, df_bin)
    df_wrag = one_hot_encoder(df_wrag, df_category)
    return df_wrag

def label_encoder(df, df_bin):
    label_encoder = LabelEncoder()
    for i in df_bin:
        df[i] = label_encoder.fit_transform(df[i])

def one_hot_encoder(df, df_cag):
    df = pd.get_dummies(df, columns=df_cag)
    return df