# Simple Book List API

A simple book list API created with Python in Flask. The list of book titles shown are locally stored and sourced from: https://thegreatestbooks.org.

The API can be tested with the following CLI curl commands:

* GET:
  * curl -i http://localhost:5000/api/v1.0/books
  * curl -i http://localhost:5000/api/v1.0/books/1


* UPDATE/EDIT:

  * curl -i -H "Content-Type: application/json" -X PUT -d '{"read":true}' http://localhost:5000/api/v1.0/books/1


* CREATE/ADD:
  * curl -i -H "Content-Type: application/json" -X POST -d '{"title":"My new book", "author": "unknown"}' http://localhost:5000/api/v1.0/books


* DELETE:
  * curl -i -X DELETE http://localhost:5000/api/v1.0/books/1

Based on the tutorial by Miguel Grinberg:
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

</br>
<p align="center">
  <img src="images/screenShot-01.png"/>
</p>
