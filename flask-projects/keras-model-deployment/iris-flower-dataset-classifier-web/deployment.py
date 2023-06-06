# Carla de Beer
# Created: March 2020
# A simple Flask web frontend project deploying a Keras-based model based on the iris flower multivariate data,
# in order to predict an iris category based on the input parameters provided.
# Based on the Udemy course: Complete TensorFlow 2 and Keras Deep Learning Bootcamp:
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp
# The project uses the iris flower dataset obtained from the UCI Machine Learning Repository:
# https://archive.ics.uci.edu/ml/datasets/Iris
import os

from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from tensorflow.keras.models import load_model
import numpy as np
import joblib


flower_model = load_model('model/final_iris_model.h5')
flower_scaler = joblib.load('model/iris_scaler.pkl')


def return_prediction(model, scaler, sample_json):
    # For larger data features, you should probably write a for loop
    # That builds out this array for you

    sepal_length = sample_json['sepal_length']
    sepal_width = sample_json['sepal_width']
    petal_length = sample_json['petal_length']
    petal_width = sample_json['petal_width']

    flower = [[sepal_length, sepal_width, petal_length, petal_width]]
    flower = scaler.transform(flower)

    classes = np.array(['Setosa', 'Versicolor', 'Virginica'])
    class_ind = model.predict_classes(flower)

    return classes[class_ind][0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class FlowerForm(FlaskForm):
    sepal_length = StringField('Sepal Length')
    sepal_width = StringField('Sepal Width')
    petal_length = StringField('Petal Length')
    petal_width = StringField('Petal Width')

    submit = SubmitField('Analyse')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlowerForm()

    if form.validate_on_submit():
        session['sepal_length'] = form.sepal_length.data
        session['sepal_width'] = form.sepal_width.data
        session['petal_length'] = form.petal_length.data
        session['petal_width'] = form.petal_width.data

        return redirect(url_for('prediction'))

    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():
    content = {'sepal_length': float(session['sepal_length']), 'sepal_width': float(session['sepal_width']),
               'petal_length': float(session['petal_length']), 'petal_width': float(session['petal_width'])}

    results = return_prediction(flower_model, flower_scaler, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    app.run()
