# REQUEST FROM DATA, FORM & PROCESS

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World !</h1>"


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def home(name):                                                             # for example, http://127.0.0.1:5000/dome/123
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'key2' : [1,2,3]})


@app.route('/query')
def query():        # Use this by http://localhost:5000/query?name=Akash&location=India
    name = request.args.get('name')     # to get the input from ?name=(Anything)
    location = request.args.get('location')     # to get the input from ?location=(Anything)
    return "<h1>Hi {}, So from {}<br> You are on the query page</h1>".format(name,location)

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit">
              </form>'''

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1>Hello {}, from {}</h1><br>You have submitted the form succesfully</h>".format(name,location)


if __name__=="__main__":
    app.run(debug=True)
