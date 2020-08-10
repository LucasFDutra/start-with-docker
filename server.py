from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello'


os.environ['FLASK_ENV'] = "development"
app.run()
