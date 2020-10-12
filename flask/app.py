from flask import Flask, url_for, redirect, render_template, request
from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.send_file_max_age_default = timedelta(seconds=1)

@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/register.html')
def register():
	return render_template('register.html')

@app.route('/login.html')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.debug = True
	app.run()    


