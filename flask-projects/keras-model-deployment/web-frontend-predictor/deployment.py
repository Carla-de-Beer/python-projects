# Carla de Beer
# Created: March 2020
# A simple Flask web frontend project deploying a Keras-based model based on the iris flower multivariate data, 
# to predict an iris category based on the input parameters provided.
# Based on the Udemy course: Complete TensorFlow 2 and Keras Deep Learning Bootcamp:
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp
# The project uses the iris flower dataset obtained from the UCI Machine Learning Repository:
# https://archive.ics.uci.edu/ml/datasets/Iris

from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib

flower_model = load_model('model/final_iris_model.h5')
flower_scaler = joblib.load('model/iris_scaler.pkl')


def return_prediction(model, scaler, sample_json):
    sepal_length = sample_json['sepal_length']
    sepal_width = sample_json['sepal_width']
    petal_length = sample_json['petal_length']
    petal_width = sample_json['petal_width']

    flower = [[sepal_length, sepal_width, petal_length, petal_width]]
    flower = scaler.transform(flower)

    classes = np.array(['setosa', 'versicolor', 'virginica'])
    class_index = model.predict_classes(flower)

    return classes[class_index[0]]


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Flower Predictor App is Running</h1>'


@app.route('/api/flower', request=['POST'])
def flower_prediction():
    return jsonify(return_prediction(model, scaler, request.json))


if __name__ == '__main__':
    app.run()
