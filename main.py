from flask import Flask

def make_bold(function):
    def wrapper_function():
       return f"<b> {function()} </b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def underline(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function
app = Flask(__name__)

@app.route("/")
@make_bold
@make_italic
@underline
def hello_world():
    return "Hello, Flask!"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"