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



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
