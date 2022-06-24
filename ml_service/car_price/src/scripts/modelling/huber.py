from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import GridSearchCV
from ml_service.car_price.data.io import read_csv_file
from ml_service.car_price.src.scripts.processing import tts, std_scaler

def huber_model():
    df = read_csv_file(r'../flask_proj/ml_service/car_price/data/important data/car_price_important.csv')
    X_train, X_test, y_train, y_test = tts(df)
    X_train_scaled, X_test_scaled = std_scaler(X_train, X_test)

    param_grid = {"epsilon":[1, 10, 100], "alpha":[0.0001, 0.001, 0.01, 0.1]}
    huber = GridSearchCV(HuberRegressor(max_iter=1000), param_grid)
    huber.fit(X_train_scaled, y_train) 

    huber = HuberRegressor(epsilon=huber.best_params_['epsilon'], alpha=huber.best_params_['alpha'], max_iter=1000).fit(X_train_scaled, y_train)
    huber_pred = huber_predict(huber, X_test_scaled)

    return [huber, huber_pred]

def huber_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred