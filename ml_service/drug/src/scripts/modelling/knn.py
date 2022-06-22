import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from ml_service.drug.src.scripts.processing import tts

def knn_model():
    X_train, X_test, y_train, y_test = tts()

    param_grid = {"n_neighbors":np.arange(1,16)}
    knn_grid = GridSearchCV(KNeighborsClassifier(), param_grid)
    knn_grid.fit(X_train, y_train)

    knn_best = KNeighborsClassifier(n_neighbors=knn_grid.best_params_['n_neighbors']).fit(X_train, y_train)
    knn_pred = knn_predict(knn_best, X_test)

    return knn_best, knn_pred

def knn_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred