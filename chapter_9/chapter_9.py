''' Страница упражнения - 280 '''

# 2
from flask import Flask, render_template, request

app = Flask(__name__)

# 3
@app.route('/')
def home():
    # return "It's alive!"

    # 5
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')

    return render_template('home.html', **kwargs)

app.run(port=5000, host='localhost')

# 4
#home.html
