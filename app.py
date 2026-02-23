import logging
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

books = [
    {"id": 1, "title": "The Great Adventure 1", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "Mystery of the Night 2", "author": "George Orwell"},
    {"id": 3, "title": "Future World 3", "author": "John Smith"},
    {"id": 4, "title": "Lost in Time 4", "author": "Mary Johnson"},
    {"id": 5, "title": "Hidden Secrets 5", "author": "Alex Brown"},
    {"id": 6, "title": "Journey Beyond 6", "author": "Sophie Taylor"},
    {"id": 7, "title": "Echoes of the Past 7", "author": "Robert Davis"},
    {"id": 8, "title": "The Last Empire 8", "author": "Jane Wilson"},
    {"id": 9, "title": "Shadows of Destiny 9", "author": "Alice Clark"},
    {"id": 10, "title": "Dreams of Tomorrow 10", "author": "William Miller"},
    {"id": 11, "title": "The Great Adventure 11", "author": "Mary Smith"},
    {"id": 12, "title": "Mystery of the Night 12", "author": "Alex Johnson"},
    {"id": 13, "title": "Future World 13", "author": "Sophie Brown"},
    {"id": 14, "title": "Lost in Time 14", "author": "Robert Taylor"},
    {"id": 15, "title": "Hidden Secrets 15", "author": "Jane Davis"},
    {"id": 16, "title": "Journey Beyond 16", "author": "Alice Wilson"},
    {"id": 17, "title": "Echoes of the Past 17", "author": "William Clark"},
    {"id": 18, "title": "The Last Empire 18", "author": "F. Scott Miller"},
    {"id": 19, "title": "Shadows of Destiny 19", "author": "George Smith"},
    {"id": 20, "title": "Dreams of Tomorrow 20", "author": "John Johnson"},
    {"id": 21, "title": "The Great Adventure 21", "author": "Mary Brown"},
    {"id": 22, "title": "Mystery of the Night 22", "author": "Alex Taylor"},
    {"id": 23, "title": "Future World 23", "author": "Sophie Davis"},
    {"id": 24, "title": "Lost in Time 24", "author": "Robert Wilson"},
    {"id": 25, "title": "Hidden Secrets 25", "author": "Jane Clark"},
    {"id": 26, "title": "Journey Beyond 26", "author": "Alice Miller"},
    {"id": 27, "title": "Echoes of the Past 27", "author": "William Fitzgerald"},
    {"id": 28, "title": "The Last Empire 28", "author": "F. Scott Brown"},
    {"id": 29, "title": "Shadows of Destiny 29", "author": "George Taylor"},
    {"id": 30, "title": "Dreams of Tomorrow 30", "author": "John Davis"},
    {"id": 31, "title": "The Great Adventure 31", "author": "Mary Wilson"},
    {"id": 32, "title": "Mystery of the Night 32", "author": "Alex Clark"},
    {"id": 33, "title": "Future World 33", "author": "Sophie Miller"},
    {"id": 34, "title": "Lost in Time 34", "author": "Robert Fitzgerald"},
    {"id": 35, "title": "Hidden Secrets 35", "author": "Jane Brown"},
    {"id": 36, "title": "Journey Beyond 36", "author": "Alice Taylor"},
    {"id": 37, "title": "Echoes of the Past 37", "author": "William Davis"},
    {"id": 38, "title": "The Last Empire 38", "author": "F. Scott Wilson"},
    {"id": 39, "title": "Shadows of Destiny 39", "author": "George Clark"},
    {"id": 40, "title": "Dreams of Tomorrow 40", "author": "John Miller"},
    {"id": 41, "title": "The Great Adventure 41", "author": "Mary Fitzgerald"},
    {"id": 42, "title": "Mystery of the Night 42", "author": "Alex Smith"},
    {"id": 43, "title": "Future World 43", "author": "Sophie Johnson"},
    {"id": 44, "title": "Lost in Time 44", "author": "Robert Brown"},
    {"id": 45, "title": "Hidden Secrets 45", "author": "Jane Taylor"},
    {"id": 46, "title": "Journey Beyond 46", "author": "Alice Davis"},
    {"id": 47, "title": "Echoes of the Past 47", "author": "William Wilson"},
    {"id": 48, "title": "The Last Empire 48", "author": "F. Scott Clark"},
    {"id": 49, "title": "Shadows of Destiny 49", "author": "George Miller"},
    {"id": 50, "title": "Dreams of Tomorrow 50", "author": "John Fitzgerald"},
    {"id": 51, "title": "The Great Adventure 51", "author": "Mary Smith"},
    {"id": 52, "title": "Mystery of the Night 52", "author": "Alex Johnson"},
    {"id": 53, "title": "Future World 53", "author": "Sophie Brown"},
    {"id": 54, "title": "Lost in Time 54", "author": "Robert Taylor"},
    {"id": 55, "title": "Hidden Secrets 55", "author": "Jane Davis"},
    {"id": 56, "title": "Journey Beyond 56", "author": "Alice Wilson"},
    {"id": 57, "title": "Echoes of the Past 57", "author": "William Clark"},
    {"id": 58, "title": "The Last Empire 58", "author": "F. Scott Miller"},
    {"id": 59, "title": "Shadows of Destiny 59", "author": "George Smith"},
    {"id": 60, "title": "Dreams of Tomorrow 60", "author": "John Johnson"},
    {"id": 61, "title": "The Great Adventure 61", "author": "Mary Brown"},
    {"id": 62, "title": "Mystery of the Night 62", "author": "Alex Taylor"},
    {"id": 63, "title": "Future World 63", "author": "Sophie Davis"},
    {"id": 64, "title": "Lost in Time 64", "author": "Robert Wilson"},
    {"id": 65, "title": "Hidden Secrets 65", "author": "Jane Clark"},
    {"id": 66, "title": "Journey Beyond 66", "author": "Alice Miller"},
    {"id": 67, "title": "Echoes of the Past 67", "author": "William Fitzgerald"},
    {"id": 68, "title": "The Last Empire 68", "author": "F. Scott Brown"},
    {"id": 69, "title": "Shadows of Destiny 69", "author": "George Taylor"},
    {"id": 70, "title": "Dreams of Tomorrow 70", "author": "John Davis"},
    {"id": 71, "title": "The Great Adventure 71", "author": "Mary Wilson"},
    {"id": 72, "title": "Mystery of the Night 72", "author": "Alex Clark"},
    {"id": 73, "title": "Future World 73", "author": "Sophie Miller"},
    {"id": 74, "title": "Lost in Time 74", "author": "Robert Fitzgerald"},
    {"id": 75, "title": "Hidden Secrets 75", "author": "Jane Brown"},
    {"id": 76, "title": "Journey Beyond 76", "author": "Alice Taylor"},
    {"id": 77, "title": "Echoes of the Past 77", "author": "William Davis"},
    {"id": 78, "title": "The Last Empire 78", "author": "F. Scott Wilson"},
    {"id": 79, "title": "Shadows of Destiny 79", "author": "George Clark"},
    {"id": 80, "title": "Dreams of Tomorrow 80", "author": "John Miller"},
    {"id": 81, "title": "The Great Adventure 81", "author": "Mary Fitzgerald"},
    {"id": 82, "title": "Mystery of the Night 82", "author": "Alex Smith"},
    {"id": 83, "title": "Future World 83", "author": "Sophie Johnson"},
    {"id": 84, "title": "Lost in Time 84", "author": "Robert Brown"},
    {"id": 85, "title": "Hidden Secrets 85", "author": "Jane Taylor"},
    {"id": 86, "title": "Journey Beyond 86", "author": "Alice Davis"},
    {"id": 87, "title": "Echoes of the Past 87", "author": "William Wilson"},
    {"id": 88, "title": "The Last Empire 88", "author": "F. Scott Clark"},
    {"id": 89, "title": "Shadows of Destiny 89", "author": "George Miller"},
    {"id": 90, "title": "Dreams of Tomorrow 90", "author": "John Fitzgerald"},
    {"id": 91, "title": "The Great Adventure 91", "author": "Mary Smith"},
    {"id": 92, "title": "Mystery of the Night 92", "author": "Alex Johnson"},
    {"id": 93, "title": "Future World 93", "author": "Sophie Brown"},
    {"id": 94, "title": "Lost in Time 94", "author": "Robert Taylor"},
    {"id": 95, "title": "Hidden Secrets 95", "author": "Jane Davis"},
    {"id": 96, "title": "Journey Beyond 96", "author": "Alice Wilson"},
    {"id": 97, "title": "Echoes of the Past 97", "author": "William Clark"},
    {"id": 98, "title": "The Last Empire 98", "author": "F. Scott Miller"},
    {"id": 99, "title": "Shadows of Destiny 99", "author": "George Smith"},
    {"id": 100, "title": "Dreams of Tomorrow 100", "author": "John Johnson"}
]


def validate_book(data):
    if "title" not in data or "author" not in data:
        return False
    return True



@app.route("/api/books", methods=['GET', 'POST'])
@limiter.limit("10/minute")
def handle_books():
    if request.method == 'POST':
        app.logger.info('POST request received for /api/books')
        new_book = request.get_json()
        if not validate_book(new_book):
            return jsonify({"error": "Invalid book data"}), 400

        new_id = max(book['id'] for book in books)+1
        new_book["id"] = new_id
        books.append(new_book)
        return jsonify(new_book), 201

    else:
        #https://commandrisk-geminilittle-5000.codio.io/api/books?page=2&limit=10

        app.logger.info('GET request received for /api/books')
        author = request.args.get('author')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        start_index = (page - 1) * limit
        end_index = start_index + limit

        if author:
            filtered_books = [book for book in books if book['author'] == author]
            return jsonify(filtered_books)

        paginated_books = books[start_index:end_index]

        return jsonify(paginated_books)



def find_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


@app.route("/api/books/<int:id>", methods=['GET', 'PUT'])
def update_book(id):
    app.logger.info('PUT request received for /api/books')

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



@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
  app.logger.info('DELETE request received for /api/books')
  book_to_delete = find_book_by_id(id)

  if not book_to_delete:
    return jsonify({"error": "Book not found"}), 404

  books.remove(book_to_delete)

  return jsonify(book_to_delete), 200



# ----- Global error handlers -----
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

