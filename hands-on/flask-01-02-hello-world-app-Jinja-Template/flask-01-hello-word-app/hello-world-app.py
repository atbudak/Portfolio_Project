from flask import Flask
from logging import debug

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello from Flask!!'

@app.route('/second')
def second():
    return 'Burası ikinci sayfa !!!'

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(host='0.0.0.0', port=80)