from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1, 
        'title': 'The Lord of the Rings - The Fellowship of the Ring',
        'author': 'J.R.R. Tolkien'
    },
    {
        'id': 2, 
        'title': 'The Lord of the Rings - The Two Towers',
        'author': 'J.R.R. Tolkien'
    },
    {
        'id': 3, 
        'title': 'The Lord of the Rings - The Return of the King',
        'author': 'J.R.R. Tolkien'
    },
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# Update book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    updated_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(updated_book)
            return jsonify(books[index])

# Create a new book
@app.route('/books', methods=['POST'])
def add_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# Delete book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
            return jsonify(books)
     
app.run(port=5000, host='localhost', debug=True)
