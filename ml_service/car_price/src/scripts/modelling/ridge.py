from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from ml_service.car_price.data.io import read_csv_file
from ml_service.car_price.src.scripts.processing import tts, std_scaler

def ridge_model():
    df = read_csv_file(r'../flask_proj/ml_service/car_price/data/important data/car_price_important.csv')
    X_train, X_test, y_train, y_test = tts(df)
    X_train_scaled, X_test_scaled = std_scaler(X_train, X_test)

    param_grid = {"alpha":[0.0001, 0.001, 0.01, 0.1]}
    ridge = GridSearchCV(Ridge(), param_grid)
    ridge.fit(X_train_scaled, y_train) 

    ridge = Ridge(alpha=ridge.best_params_['alpha']).fit(X_train_scaled, y_train)
    ridge_pred = ridge_predict(ridge, X_test_scaled)

    return [ridge, ridge_pred]

def ridge_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred