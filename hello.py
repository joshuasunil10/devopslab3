from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''Hello, World!<br><a href="/about">About</a>'''

@app.route('/about')
def about():
    return "This is a Flask web app running in a Linux VM."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
