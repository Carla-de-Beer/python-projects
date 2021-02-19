import base64
from flask import Flask, request, jsonify

import os
import glob
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the model
model = load_model('./model/simple_classifier.h5')


def return_prediction(image_json):
    result = ''

    img_name = image_json['imageName']

    img_data = base64.b64decode(image_json['imageBase64'])
    filename = img_name  # I assume you have a way of picking unique filenames
    with open('./images/' + filename, 'wb') as f:
        f.write(img_data)

    img = image.load_img('./images/' + filename, target_size=(256, 256))

    my_img_array = image.img_to_array(img)
    my_img_array = my_img_array / 255
    my_img_array = np.expand_dims(my_img_array, axis=0)

    model_path = app.root_path + '/model/simple_classifier.h5'
    image_model = tf.keras.models.load_model(model_path, custom_objects=None, compile=True)

    classes = image_model.predict(my_img_array)

    if classes[0][0] < 0.5:
        result = 'CARTOON'
        degree = round(100 - classes[0][0] * 100, 4)
    elif classes[0][0] >= 0.5:
        result = 'PHOTO'
        degree = round(classes[0][0] * 100, 4)

    app.logger.info(': ' + result)
    app.logger.info(f"Degree of certainty: {degree}%")

    return result, degree


@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'


@app.route('/api/cartoon-photo', methods=['POST'])
def predict_flower():

    [result, degree] = return_prediction(image_json=request.json)

    files = glob.glob(app.root_path + '/images/*')
    for f in files:
        os.remove(f)

    return jsonify([result, degree])


if __name__ == '__main__':
    app.run()
