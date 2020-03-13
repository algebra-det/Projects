# USING JSONIFY(for online ) , JSON(for .json files)

from flask import Flask, jsonify, request
import json

with open("values.json", "r+") as file:     # To process json file in processjsonfile()
    data = json.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World !</h1>"


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def index(name):                                                             # for example, http://127.0.0.1:5000/dome/123
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


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()           # to get data from online json formats or links
    name = data['name']                 # that's why POST is used to get the data from any link
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'result' : 'Success', 'name' : name , 'location' : location, 'randomkeylist' : randomlist})




@app.route('/processjsonfile', methods=['GET'])     # GET as we are using a .json file from line
def processjsonfile():                              # i.e. from line 4
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    return ({'result' : 'Success', 'name' : name , 'location' : location, 'randomkeylist' : randomlist})

"""JSONIFY is used to obtain data from online json type content
    while JSON is used to obtain data from a .json file in the directory

    JSONIFY is therefore rich and usable and that's why we use POST with this to get data from online
    JSON is not used here that much because we need seldomly be needing data from local .json file"""

if __name__=="__main__":
    app.run(debug=True)
