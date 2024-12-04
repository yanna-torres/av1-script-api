from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/number/<number>', methods=['GET'])
def get_number(number):
    access_number = number_exists(number)
    return jsonify({"number": number, "accessed": access_number})


def number_exists(number_to_check):
    file_path = './data/numbers.json'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Load or initialize the JSON data
    if not os.path.exists(file_path):
        data = {}
    else:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # Reset file if corrupted
                data = {}

    # Convert the number to a string for dictionary key consistency
    number_key = str(number_to_check)

    # Check if the number exists
    if number_key in data:
        # Increment 'accessed' count
        accessed_count = data[number_key]["accessed"]
        data[number_key]["accessed"] += 1
    else:
        # Initialize the number with 'accessed' = 1
        accessed_count = 0
        data[number_key] = {"accessed": 1}

    # Save the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return accessed_count

if __name__ == '__main__':
    app.run(debug=True)