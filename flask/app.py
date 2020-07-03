from flask import Flask, url_for, redirect, render_template

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

@app.route('/a')
def a():
	return 'here is a'

@app.route('/b')
def b():
	return redirect(url_for('a'))

if __name__ == '__main__':
    app.debug = True
    app.run()

