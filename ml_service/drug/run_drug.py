import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from ml_service.drug.src.scripts.preparation import preprocessing
from ml_service.drug.src.scripts.modelling.knn import knn_model
from ml_service.drug.src.scripts.modelling.naive_bayes import nb_model
from ml_service.drug.src.scripts.modelling.tree import tree_model
from ml_service.drug.src.scripts.evaluation import evaluate

def input_data(age, gender, bp, cholesterol, na_to_k):
    gender_dict = {'F':0, 'M':1}
    bp_dict = {"HIGH": 1, "NORMAL" : 0,"LOW" : -1}
    cholesterol_dict = {'HIGH':0, 'NORMAL':1}
    result = predict_drug(age, gender_dict[gender], bp_dict[bp], cholesterol_dict[cholesterol], na_to_k)

    return result

def training_model():
    preprocessing()
    knn_best, knn_pred = knn_model()
    nb, nb_pred = nb_model()
    tree, tree_pred = tree_model()

    model = [knn_best, nb, tree]
    model_result = [knn_pred, nb_pred, tree_pred]

    best_model = evaluate(model, model_result)
    return best_model

def predict_drug(age, gender, bp, cholesterol, na_to_k):
    model = training_model()
    y_pred = model.predict([[age, gender, bp, cholesterol, na_to_k]])

    drug_dict = {0:"DrugA", 1:"DrugB", 2:"DrugC", 3:"DrugX", 4:"DrugY"}
    return drug_dict[y_pred[0]]