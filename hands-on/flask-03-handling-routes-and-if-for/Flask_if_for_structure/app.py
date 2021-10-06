from flask import Flask, render_template

app = Flask(__name__)


@app.route('/first')
def head():
    first = 'This is first condition in Flask.'
    return render_template('index.html', message=first)


@app.route('/')
def body():
    first = ["Ahmet", "Lorenzo", "Barbara", "Angela"]
    return render_template('body.html', object=first)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
