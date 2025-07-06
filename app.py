from flask import Flask, request, jsonify, render_template
import json, os

app = Flask(__name__)
DATA_DIR = 'data'

# Utility functions to load and save data
def load_data(entity):
    path = f"{DATA_DIR}/{entity}.json"
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)

def save_data(entity, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(f"{DATA_DIR}/{entity}.json", "w") as f:
        json.dump(data, f, indent=2)

# Route for frontend
def home():
    return render_template('index.html')

# Unified API route for courses, students, lecturers
@app.route('/api/<entity>', methods=['GET', 'POST'])
def api(entity):
    if entity not in ['courses', 'students', 'lecturers']:
        return jsonify({'error': 'Invalid entity'}), 400

    if request.method == 'GET':
        return jsonify(load_data(entity))
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        items = load_data(entity)
        items.append(data)
        save_data(entity, items)
        return jsonify({'status': f'{entity[:-1].capitalize()} added'}), 201

if __name__ == '__main__':
    app.run(debug=True)

