from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

# 渲染模板
@app.route('/')
def index():
    return render_template('index.html')

# 渲染模板(帶 str 參數)
@app.route('/user/<username>')
def username(username):
    return render_template('index.html', templates_user = username)

# 帶非 str 參數
@app.route('/age/<float:age>')
def age(age):
    return 'I am ' + str(age) + ' years old.'

# url_for 應用
@app.route('/a')
def a():
	return 'here is a'
@app.route('/b')
def b():
	return redirect(url_for('a'))

# GET 與 POST
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'Hello ' + request.values['username']
	else:
		return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()    


