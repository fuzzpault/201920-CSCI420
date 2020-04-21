
'''
Name: Paul Talaga
Date: 4-15-2020
Desc: Flask Hello World

'''

from flask import Flask


# initialize Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()