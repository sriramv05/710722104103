from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/numbers/<number_id>', methods=['GET'])
def mock_numbers(number_id):
    number_map = {
        "p": [2, 3, 5, 7, 11, 13, 17],
        "f": [0, 1, 1, 2, 3, 5, 8, 13],
        "e": [2, 4, 6, 8, 10, 12, 14],
        "o": [1, 3, 5, 7, 9, 11, 13]
    }
    numbers = number_map.get(number_id, [])
    if not numbers:
        return jsonify({"error": "Invalid ID"}), 400

    response = {
        "numbers": random.sample(numbers, min(4, len(numbers)))
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=9876)
