import numpy as np

from ml_service.car_price.data.io import input_std_scaler
from ml_service.car_price.src.scripts.preparation import preprocessing
from ml_service.car_price.src.scripts.processing import proc
from ml_service.car_price.src.scripts.modelling.linear_regreesion import lr_model
from ml_service.car_price.src.scripts.modelling.ridge import ridge_model
from ml_service.car_price.src.scripts.modelling.ransac import ransac_model
from ml_service.car_price.src.scripts.modelling.theilsen import ts_model
from ml_service.car_price.src.scripts.modelling.huber import huber_model
from ml_service.car_price.src.scripts.modelling.svr import svr_model
from ml_service.car_price.src.scripts.evaluation import evaluate

def input_data(curbweight, highwaympg, citympg, carwidth, horsepower,
               enginesize, carlength, peakrpm, wheelbase, boreratio):

    result = predict_drug(curbweight, highwaympg, citympg, carwidth, horsepower,
                          enginesize, carlength, peakrpm, wheelbase, boreratio)

    return result

def training_model():
    preprocessing()
    proc()
    model_list = np.array([lr_model(), ridge_model(), ransac_model(), ts_model(), huber_model(), svr_model()], dtype=object)

    model = model_list[:,0]
    model_result = model_list[:,1]

    best_model = evaluate(model, model_result)
    return best_model

def predict_drug(curbweight, highwaympg, citympg, carwidth, horsepower,
                 enginesize, carlength, peakrpm, wheelbase, boreratio):

    model = training_model()
    input = [[curbweight, highwaympg, citympg, carwidth, horsepower,
              enginesize, carlength, peakrpm, wheelbase, boreratio]]

    y_pred = model.predict(input_std_scaler(input))

    return y_pred[0]