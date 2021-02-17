# API Iris Flower Dataset Classifier

This project exposes an iris flower dataset ANN model as an API. The model was built with TensorFlow/Keras and is deployed in Flask. Run the server, and enter the details for the following values:

* `sepal_length`
* `sepal_width`
* `petal_length`
* `petal_width`

The API then responds with the iris classification, which is either:

* *Iris Setosa*
* *Iris Versicolour*
* *Iris Virginica*

The API can be tested with the following CLI curl CRUD command:

* CREATE/ADD:
  * ```curl -i -H "Content-Type: application/json" -X POST -d '{"sepal_length": 2.1, "sepal_width": 5.5, "petal_length": 1.4, "petal_width": 3.2}' http://localhost:5000/api/flower```
