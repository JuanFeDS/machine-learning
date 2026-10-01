import pandas as pd
import numpy as np

import joblib

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def predict():
    X_test = np.array([6.452020054,6.261979694,1.070622325,1.402182937,0.595027924,0.477487415,0.149014473,0.046668742,2.616068125])

    predict = model.predict(X_test.reshape(1, -1))
    return jsonify({'Prediction':list(predict)})


if __name__ == '__main__':
    model = joblib.load('models/model.pkl')

    app.run(port=5500)