from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the index page'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/raise_exception')
def raise_exception():
    raise Exception("test")


if __name__ == '__main__':
    app.run(debug=True)
