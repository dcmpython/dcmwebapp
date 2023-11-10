# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is Dylan\'s first web app on Heroku!'

