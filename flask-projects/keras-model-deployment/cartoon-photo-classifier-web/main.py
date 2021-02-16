from flask import Flask, redirect, session, url_for, render_template
from flask_wtf.file import FileAllowed
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

import os
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = app.root_path + '/static/unseen/'


class UploadForm(FlaskForm):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])


def get_prediction():
    img = image.load_img(app.root_path + '/static/unseen/' + session['filename'], target_size=(256, 256))

    my_img_array = image.img_to_array(img)
    my_img_array = my_img_array / 255
    my_img_array = np.expand_dims(my_img_array, axis=0)

    model_path = app.root_path + '/model/simple_classifier.h5'
    image_model = tf.keras.models.load_model(model_path, custom_objects=None, compile=True)

    classes = image_model.predict(my_img_array)

    if classes[0][0] < 0.5:
        result = 'CARTOON'
        degree = round(100 - classes[0][0] * 100, 4)
        print(': CARTOON')
        print(f"Degree of certainty: {degree}%")
    elif classes[0][0] >= 0.5:
        result = 'PHOTO'
        degree = round(classes[0][0] * 100, 4)
        print(': PHOTO')
        print(f"Degree of certainty: {degree}%")

    return result, degree


@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    # shutil.rmtree(app.root_path + '/static/unseen/')

    if form.validate_on_submit():
        filename = secure_filename(form.upload.data.filename)
        session['filename'] = filename

        f = form.upload.data
        f.save(os.path.join(app.root_path, 'static/unseen', filename))

        return redirect(url_for('prediction'))

    return render_template('index.html', form=form)


@app.route('/prediction')
def prediction():
    [result, degree] = get_prediction()

    filename = 'static/unseen/' + session['filename']
    results = {'class': result, 'degree': degree, 'filename': filename}

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    app.run()
