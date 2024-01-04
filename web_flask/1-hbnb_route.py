#!/usr/bin/python3
"""another script that starts a web flask aplication"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(debug=True)
