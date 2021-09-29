from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello from Flask!!'

@app.route('/second')
def second():
    return 'Burası ikinci sayfa !!!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)