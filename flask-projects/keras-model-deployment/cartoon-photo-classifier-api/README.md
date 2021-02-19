# Cartoon-Photo Classifier API

A simple Flask app that exposes the API deploying a convolutional neural network model for the [cartoon-photo classifier](https://github.com/Carla-de-Beer/tensorflow-2.x-projects/tree/master/CNN/cartoon-photo-classifier).

The model was built with TensorFlow-Keras and deployed in Flask. Run the server, open a browser window and enter the URL `http://localhost:5000/` and upload a JPEG or PNG image.

The web page then responds with a prediction and the degree of certainty.

* CREATE/ADD:
  * ```curl -i -H "Content-Type: application/json" -X POST -d '{{"imageName": "<IMAGE_NAME_EXT>", "imageBase64": "<BASE64_ENCODED_IMAGE>"}'```


<br/>
<p align="center">
  <img src="readme-images/blue_tit.jpg" width="600px"/>
  <img src="readme-images/screenshot-01.png" width="600px"/>
</p>
<p align="center">
  <img src="readme-images/bugs-bunny.jpg" width="600px"/>
  <img src="readme-images/screenshot-02.png" width="600px"/>
</p>
