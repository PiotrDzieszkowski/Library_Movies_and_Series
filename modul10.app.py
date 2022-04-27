from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'