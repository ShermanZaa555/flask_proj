import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from ml_service.car_price.data.io import read_csv_file

def proc():
    df_model = read_csv_file('../flask_proj/ml_service/car_price/data/processed data/car_price_clean.csv')
    df_im = df_model[feature_importance(df_model)]
    df_im = df_im.assign(price=df_model['price'])
    df_im.to_csv('../flask_proj/ml_service/car_price/data/important data/car_price_important.csv', index=False)

def tts(df):
    X, y = feature_target_split(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test

def feature_importance(df):
    X_train, X_test, y_train, y_test = tts(df)
    X_train_scaled, X_test_scaled = std_scaler(X_train, X_test)
    forest = RandomForestRegressor(oob_score=True, random_state=42).fit(X_train_scaled, y_train)
    feat_importances = pd.Series(forest.feature_importances_, index=X_train.columns).sort_values()
    importances = feat_importances.sort_values(ascending=False)[:10]
    return importances.index

def feature_target_split(df):
    X = df.drop('price', axis=1)
    y = df['price']
    return X, y

def std_scaler(x_train, x_test):
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    return x_train_scaled, x_test_scaled
