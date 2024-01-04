#!/usr/bin/python3
"""script that starts a web flask application"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello HBNB!"
