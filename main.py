from flask import Flask, render_template, url_for, redirect, request, send_from_directory
from flask_socketio import SocketIO, send, emit
from flask_bootstrap import Bootstrap
from datetime import timedelta
from templates.industriousWoman import run_algo
import string
import random
import os

bootstrap = Bootstrap()

app = Flask(__name__ ,
            template_folder='templates',
            static_folder='static',
            static_url_path='')

app.config['SECRET_KEY'] = 'secret!'
app.send_file_max_age_default = timedelta(seconds=1)
socketio = SocketIO(app)

# render_template 將會找尋 html 檔案傳送給使用者

# 遊客頁面
@app.route("/guest")
def guest():
	return render_template("guest.html")

# 首頁
@app.route("/index")
def index():
	return render_template("index.html")

# 註冊頁面
@app.route("/reg")
def reg():
	return render_template("reg.html")

# 登入頁面
@app.route("/sign")
def sign():
	return render_template("sign.html")

# 替所有服務器隨機產生字串
@socketio.on('getToken')
def getToken():
	emit("receiveToken","".join(random.choice(string.ascii_letters) for x in range(5)).replace(" ",""))

# 獲取 myToken 後給 industoriousWoman.py 區別 goods.json
@socketio.on('uid')
def uid(myToken):
	paintStack.append(myToken)
	print(myToken)

# 按下計算的 button 後運行演算法
@app.route('/result')
def my_link():
	strs = run_algo()
	return render_template('index.html', string_variable=strs)
	
if __name__ == "__main__":
	charList = []
	for i in range(0, 200):
		charList.append(chr(i))
	paintStack = []
	socketio.run(app, host = '127.0.0.1', port = 5000, debug=True)