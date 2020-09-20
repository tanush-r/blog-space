from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compose')
def compose():
    return render_template('compose.html')


@app.route('/popular')
def popular():
    return render_template('popular.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/discover')
def discover():
    return render_template('discover.html')


if __name__ == '__main__':
    app.run(debug=True)
