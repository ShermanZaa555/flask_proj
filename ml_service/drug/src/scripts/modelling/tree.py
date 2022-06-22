from sklearn.tree import DecisionTreeClassifier
from ml_service.drug.src.scripts.processing import tts

def tree_model():
    X_train, X_test, y_train, y_test = tts()
    tree_clf = DecisionTreeClassifier(random_state=42).fit(X_train.values, y_train)
    tree_pred = tree_predict(tree_clf, X_test.values)
    return tree_clf, tree_pred

def tree_predict(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred