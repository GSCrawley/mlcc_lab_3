from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    number = data['number']
    result = number + number
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5003)