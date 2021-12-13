from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    req = requests.get('https://cat-fact.herokuapp.com/facts')
    data = json.loads(req.content)
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    return 'Dustin is a programmer!'


if __name__ == "__main__":
    print('server is running')
    app.run(debug=True)
