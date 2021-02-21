# Cartoon-Classifier Classifier Web

A simple Flask web frontend deploying a convolutional neural network model for the [cartoon-photo classifier](https://github.com/Carla-de-Beer/tensorflow-2.x-projects/tree/master/CNN/cartoon-photo-classifier). The API uses the simpler of the two models because, even though its acuuracy is a bit lower than that of the model trained with transfer learning, its size is significantly smaller.

The model was built with TensorFlow-Keras and deployed in Flask. Run the server, open a browser window and enter the URL `http://localhost:5000/` and upload a JPEG or PNG image.

The web page then responds with a prediction and a degree of certainty expressed as a percentage.

### Screen Views
<br/>
<p align="center">
  <img src="images/screenshot-01.png" width="650px"/>
  <img src="images/screenshot-02.png" width="650px"/>
  <img src="images/screenshot-03.png" width="650px"/>
</p>
