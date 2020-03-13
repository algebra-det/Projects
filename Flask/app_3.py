# ROUTE VARIABLES

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World !</h1>"

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'}) # this defaults={} is used so that if there's
@app.route('/home/<name>', methods=['POST', 'GET'])                         #  is no <name> after /home than it will take 'Default' after /home
def home(name):                                                             # try changing {'name' : 'Default'} to {'name' : ''} , than there will be nothing
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/dome', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/dome/<int:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def dome(name):                                                             # for example, http://127.0.0.1:5000/dome/123
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/rome', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/rome/<string:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def rome(name):                                                             # for example, http://127.0.0.1:5000/dome/123
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)



@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'key2' : [1,2,3]})


if __name__=="__main__":
    app.run(debug=True)
