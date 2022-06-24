from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from ml_service.car_price.data.io import read_csv_file
from ml_service.car_price.src.scripts.processing import tts, std_scaler

def svr_model():
    df = read_csv_file(r'../flask_proj/ml_service/car_price/data/important data/car_price_important.csv')
    X_train, X_test, y_train, y_test = tts(df)
    X_train_scaled, X_test_scaled = std_scaler(X_train, X_test)

    param_grid = {"C":[1, 10, 100], "gamma":[0.0001, 0.001, 0.01, 0.1]}
    svr = GridSearchCV(SVR(), param_grid)
    svr.fit(X_train_scaled, y_train) 

    svr = SVR(C=svr.best_params_['C'], gamma=svr.best_params_['gamma'], max_iter=1000).fit(X_train_scaled, y_train)
    svr_pred = svr_predict(svr, X_test_scaled)

    return [svr, svr_pred]

def svr_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred