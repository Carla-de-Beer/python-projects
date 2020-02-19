"""
Carla de Beer
Created: September 2019
Simple book list API created with Python in Flask.
Based on the tutorial by Miguel Grinberg:
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
"""

from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
from idna import unicode
import book_list

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", books=book_list.books)


@app.route('/api/v1.0/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in book_list.books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': book_list.books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'description': request.json.get('description', ''),
        'date': request.json.get('date', ''),
        'read': False
    }
    book_list.books.append(book)
    return jsonify({'book': book}), 201


@app.route('/api/v1.0/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in book_list.books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'author' in request.json and type(request.json['author']) is not unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'date' in request.json and type(request.json['date']) is not unicode:
        abort(400)
    if 'read' in request.json and type(request.json['read']) is not bool:
        abort(400)
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['description'] = request.json.get('description', book[0]['description'])
    book[0]['date'] = request.json.get('date', book[0]['date'])
    book[0]['read'] = request.json.get('read', book[0]['read'])
    return jsonify({'book': book[0]})


@app.route('/api/v1.0/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in book_list.books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    book_list.books.remove(book[0])
    return jsonify({'result': True})


@app.route('/api/v1.0/books', methods=['GET'])
def get_books():
    return jsonify({'books': [make_public_book(book) for book in book_list.books]})


def make_public_book(book):
    new_book = {}
    for field in book:
        if field == 'id':
            new_book['uri'] = url_for('get_book', book_id=book['id'], _external=True)
        else:
            new_book[field] = book[field]
    return new_book


if __name__ == '__main__':
    app.run(debug=True)
