from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/pessoa')
def pessoa_func():
    return 'pessoa'


app.run(debug=True)