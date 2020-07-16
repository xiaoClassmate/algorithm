from flask import Flask, url_for, redirect, render_template, request

# Pyrebase 是 Firebase REST API 的 Python 接口
import pyrebase

# import firebase_admin
# from firebase_admin import credntials, firestore

# 設置環境參數
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)

config = {
  "apiKey": os.getenv("apiKey"),
  "authDomain": os.getenv("authDomain"),
  "databaseURL": os.getenv("databaseURL"),
  "storageBucket": os.getenv("storageBucket"),
  "serviceAccount": os.getenv("serviceAccount")
}

firebase = pyrebase.initialize_app(config)
print(config)

# # 渲染模板
# @app.route('/')
# def index():
#     return render_template('index.html')

# # 渲染模板(帶 str 參數)
# @app.route('/user/<username>')
# def user(username):
#     return render_template('index.html', templates_user = username)

# # 帶非 str 參數
# @app.route('/age/<float:age>')
# def age(age):
#     return 'I am ' + str(age) + ' years old.'

# # url_for 應用
# @app.route('/a')
# def a():
# 	return 'here is a'
# @app.route('/b')
# def b():
# 	return redirect(url_for('a'))

# # GET 與 POST
# # @app.route('/login', methods=['GET', 'POST']) 
# # def login():
# #     if request.method == 'POST': 
# #         return 'Hello ' + request.values['username'] 

# #     return "<form method='post' action='/login'><input type='text' name='username' />" \
# #             "</br>" \
# #            "<button type='submit'>Submit</button></form>"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return redirect(url_for('user', username = request.form.get('username')))
#     else:
#     	return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()    


