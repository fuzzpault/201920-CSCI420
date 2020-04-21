
'''
Name: Paul Talaga
Date: 4-15-2020
Desc: Flask demo to add numbers from a form.

Run with 'python3 adder.py'


'''
from flask import Flask, request, render_template

# initialize Flask
app = Flask(__name__)


# If no path is provided, use this function to return the response. Ex: localhost:5000/
@app.route('/', methods=['GET'])
def index():
    if 'a' in request.args and 'b' in request.args:
       a = float(request.args.get('a') )
       b = float(request.args.get('b') )
       return "{} + {} = {}".format(a, b, a + b)
    else:
        return 'Hello World!'


#  This will get triggered if localhost:5000/pretty is accessed.
@app.route('/pretty', methods=['GET'])
def pretty():
    res = {}
    if 'a' in request.args and 'b' in request.args:
       a = float(request.args.get('a') )
       b = float(request.args.get('b') )
       res["a"] = a
       res["b"] = b
       res["result"] = a + b
    return render_template('page.html', data = res)


if __name__ == '__main__':
    # The host is optional, but if you provide 0.0.0.0 it is available 
    # to other computers, not just localhost
    app.run(host="0.0.0.0")