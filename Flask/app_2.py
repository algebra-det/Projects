from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World !</h1>"     #Any string passed will automatically be converted to HTML

#@app.route('/<name>')   # here <name> is a place-holder
#def root(name):         # have to include the place-holder i.e. name in our case, inside ()
    return "<h1>Hello {} !</h1>".format(name)   # In {} the placeholder value will be printed
# Check out by inserting into the address bar after localhost, your name or any world
#   "http://127.0.0.1:5000/Akash"


# how to use methods, to allow different methods for any url, by default its "GET"
@app.route('/home', methods=['POST', 'GET'])       #POST is used to Post request
def home():                                        # GET is used to get result for the request
    return "<h1>You are on the HOME PAGE</h1>"

@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'key2' : [1,2,3]})


if __name__=="__main__":
    app.run(debug=True)
# if there's no debug=True, than we have to CTRL+C and restart app everytime we do some changes
# i.e. we have to restart by "python app.py" to make the changes reflect
