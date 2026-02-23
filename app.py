from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]


def validate_book(data):
    if "title" not in data or "author" not in data:
        return False
    return True

@app.route("/api/books", methods=['GET', 'POST'])
def handle_books():
    if request.method == 'POST':
        new_book = request.get_json()
        if not validate_book(new_book):
            return jsonify({"error": "Invalid book data"}), 400

        new_id = max(book['id'] for book in books)+1
        new_book["id"] = new_id
        books.append(new_book)
        return jsonify(new_book), 201

    else:
        return jsonify(books), 200





def find_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


@app.route("/api/books/<int:id>", methods=['GET', 'PUT'])
def update_book(id):
    if request.method == 'PUT':
        book_to_update  = find_book_by_id(id)

        if book_to_update is None:
            return jsonify({"error": "Book not found"}), 404

        new_data = request.get_json()

        if not new_data or not validate_book(new_data):
            return jsonify({"error": "Invalid book data"}), 400

        book_to_update["title"] = new_data["title"]
        book_to_update["author"]= new_data["author"]

        return jsonify(book_to_update), 200

    else:
        #If GET request display book with given id
        book = find_book_by_id(id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404

        return jsonify(book), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

