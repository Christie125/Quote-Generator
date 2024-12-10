from flask import Flask, render_template, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enabled CORS for all routes

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/quote')
def quote():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    if response.status_code == 200:
        quote = response.json()[0]
        return jsonify({
            'quote': quote['q'],
            'author': quote['a']
        })
    else:
        return jsonify ({'error': 'Failed to fetch quote'})

if __name__ == '__main__':
    app.debug = True
    app.run()
