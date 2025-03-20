from flask import Flask, jsonify, request
import requests
from utils import is_prime, is_fibonacci, is_even, is_odd

app = Flask(__name__)
WINDOW_SIZE = 10
window = []
TEST_SERVER_URL = "http://localhost:9876/numbers"

@app.route('/numbers/<number_id>', methods=['GET'])
def get_numbers(number_id):
    global window
    valid_ids = {"p", "f", "e", "o"}
    if number_id not in valid_ids:
        return jsonify({'error': 'Invalid ID. Use p, f, e, or o.'}), 400

    try:
        response = requests.get(f"{TEST_SERVER_URL}/{number_id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch data: {str(e)}'}), 500

    new_numbers = response.json().get("numbers", [])
    window_prev = window.copy()
    window.extend(new_numbers)
    window = window[-WINDOW_SIZE:]
    avg = sum(window) / len(window) if window else 0
    result = {
        "numbers": new_numbers,
        "windowPrevState": window_prev,
        "windowCurrState": window,
        "avg": avg
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
