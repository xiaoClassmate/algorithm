from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/user/<username>')
def username(username):
    return 'I am ' + username

@app.route('/age/<float:age>')
def age(age):
    return 'I am ' + str(age) + ' years old.'


if __name__ == '__main__':
    app.debug = True
    app.run()

