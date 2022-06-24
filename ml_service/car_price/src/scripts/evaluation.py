from math import sqrt
from sklearn.metrics import mean_squared_error
from ml_service.car_price.data.io import read_csv_file
from ml_service.car_price.src.scripts.processing import tts

def evaluate(model, model_result):
    df = read_csv_file('../flask_proj/ml_service/car_price/data/important data/car_price_important.csv')
    X_train, X_test, y_train, y_test = tts(df)
    
    model_score = []
    for i in range(len(model_result)):
      model_score.append(sqrt(mean_squared_error(y_test, model_result[i])))
    
    best_model = select_best_model(model, model_score)

    return best_model

def select_best_model(model, m_score):
  maxpos = m_score.index(min(m_score))
  return model[maxpos]