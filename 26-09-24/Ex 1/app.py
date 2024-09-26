from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/pessoa')
def pessoa_func():
    return render_template('pessoa.html')

@app.route('/animal')
def animal_func():
    return render_template('animal.html')

if __name__ == '__main__':
    app.run(debug=True)