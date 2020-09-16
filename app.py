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

if __name__ == '__main__':
    app.run(debug=True)