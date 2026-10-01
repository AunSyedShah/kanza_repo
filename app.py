from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask App!</h1>"

@app.route("/kanza")
def kanza():
    return "<h1>Hello Kanza</h1>"