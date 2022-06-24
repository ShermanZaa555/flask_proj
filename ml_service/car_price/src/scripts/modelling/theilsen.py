from sklearn.linear_model import TheilSenRegressor
from ml_service.car_price.data.io import read_csv_file
from ml_service.car_price.src.scripts.processing import tts, std_scaler

def ts_model():
    df = read_csv_file(r'../flask_proj/ml_service/car_price/data/important data/car_price_important.csv')
    X_train, X_test, y_train, y_test = tts(df)
    X_train_scaled, X_test_scaled = std_scaler(X_train, X_test)

    ts = TheilSenRegressor().fit(X_train_scaled, y_train)
    ts_pred = ts_predict(ts, X_test_scaled)

    return [ts, ts_pred]

def ts_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred