from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html',number1 = 20, number2 = 40)



if __name__ == '__name__':
    app.run(debug=True, port=2000)