# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_root():
    html = '''
        <h1>GET/POST</h1>
        <a href="/test">GET</a>
        <form action="/test" method="POST">
            <input type="submit" value="POST">
        </form>
    '''
    return html


@app.route('/test', methods=['GET', 'POST'])
def hello_test():
    if request.method == 'POST':
        return '<h1 style="color: plum;">POST</h1>'
    else:
        return '<h1 style="color: skyblue;">GET</h1>'


if __name__ == '__main__':
    app.run()
