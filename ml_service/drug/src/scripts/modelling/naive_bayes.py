from sklearn.naive_bayes import GaussianNB
from ml_service.drug.src.scripts.processing import tts

def nb_model():
    X_train, X_test, y_train, y_test = tts()

    nb = GaussianNB().fit(X_train, y_train)
    nb_pred = nb_predict(nb, X_test)
    return nb, nb_pred

def nb_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred