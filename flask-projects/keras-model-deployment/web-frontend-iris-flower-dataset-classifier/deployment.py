# Carla de Beer
# Created: March 2020
# A simple Flask web frontend project deploying a Keras-based model based on the iris flower multivariate data,
# to predict an iris category based on the input parameters provided.
# Based on the Udemy course: Complete TensorFlow 2 and Keras Deep Learning Bootcamp:
# https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp
# The project uses the iris flower dataset obtained from the UCI Machine Learning Repository:
# https://archive.ics.uci.edu/ml/datasets/Iris

from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from tensorflow.keras.models import load_model
import joblib

flower_model = load_model("model/final_iris_model.h5")
flower_scaler = joblib.load("model/iris_scaler.pkl")


def return_prediction(model, scaler, sample_json):
    # For larger data features, you should probably write a for loop
    # That builds out this array for you

    s_len = sample_json["sepal_length"]
    s_wid = sample_json["sepal_width"]
    p_len = sample_json["petal_length"]
    p_wid = sample_json["petal_width"]

    flower = [[s_len, s_wid, p_len, p_wid]]
    flower = scaler.transform(flower)

    classes = np.array(["setosa", "versicolor", "virginica"])
    class_ind = model.predict_classes(flower)

    return classes[class_ind][0]


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


class FlowerForm(FlaskForm):
    sepal_length = StringField("Sepal Length")
    sepal_width = StringField("Sepal Width")
    pet_length = StringField("Petal Length")
    pet_width = StringField("Petal Width")

    submit = SubmitField("Analyze")


@app.route("/", methods=["GET", "POST"])
def index():
    form = FlowerForm()

    if form.validate_on_submit():
        session["sepal_length"] = form.sepal_length.data
        session["sepal_width"] = form.sepal_width.data
        session["pet_length"] = form.pet_length.data
        session["pet_width"] = form.pet_width.data

        return redirect(url_for("prediction"))

    return render_template("home.html", form=form)


flower_model = load_model("final_iris_model.h5")
flower_scaler = joblib.load("iris_scaler.pkl")


@app.route("/prediction")
def prediction():
    content = {}

    content["sepal_length"] = float(session["sepal_length"])
    content["sepal_width"] = float(session["sepal_width"])
    content["petal_length"] = float(session["pet_length"])
    content["petal_width"] = float(session["pet_width"])

    results = return_prediction(flower_model, flower_scaler, content)

    return render_template("prediction.html", results=results)


if __name__ == "__main__":
    app.run()
