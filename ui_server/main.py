from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/')

def index():
        return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
        number = int(request.form['number'])
        response = requests.post('http://127.0.0.1:5001/multiply', json={'number': number})
        if response.status_code == 200:
                result = response.json()['result']
                return f"The result of {number} multiplied by itself is: {result}"
        else:
                return "Error occurred while processing the number."

@app.route('/add', methods=['POST'])
def add():
    number = int(request.form['number'])
    response = requests.post('http://127.0.0.1:5001/add', json={'number': number})
    if response.status_code == 200:
        result = response.json()['result']
        return f"The result of {number} added by itself is: {result}"
    else:
        return "Error occurred while processing the number."
if __name__ == '__main__':
        app.run(debug=True, port=5000)