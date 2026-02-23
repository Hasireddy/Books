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
