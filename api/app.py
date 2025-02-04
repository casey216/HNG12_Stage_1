from flask import Flask, request, jsonify
from utils import is_armstrong, is_prime, is_perfect, digit_sum, get_fun_fact
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Handle CORS

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Input Validation
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)

    # Determine Properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    # Fetch Fun Fact
    fun_fact = get_fun_fact(number)

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
