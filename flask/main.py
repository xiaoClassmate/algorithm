from flask import Flask
from flask import render_template
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap=Bootstrap(app)

@app.route('/<user>')
def index(user):
    return render_template('index.html', user_template=user)

if __name__ == '__main__':
    app.debug = True
    app.run()




