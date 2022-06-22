from sklearn.metrics import f1_score
from ml_service.drug.src.scripts.processing import tts

def evaluate(model, model_result):
    X_train, X_test, y_train, y_test = tts()
    
    model_score = [f1_score(y_test, model_result[i], average='micro') for i in range(len(model))]
    best_model = select_best_model(model, model_score)

    return best_model

def select_best_model(model, m_score):
  maxpos = m_score.index(max(m_score))
  return model[maxpos]