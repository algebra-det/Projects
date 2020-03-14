# Checking the app's Error mentioning while DEBUG is OFF
# There's an error in the /json file as it will try to get the name from the session
# but the user haven't gone to /home, so there will be error while going to /json straight from /

# TAKE A LOOK AT THE ERROR ON THE /JSON PAGE , IT WILL GET A SIMPLE TEXT SERVER ERROR WHICH WILL BE HARD TO # DEBUG
# NOT TRY CHANGING DEBUG , FROM FALSE TO TRUE , AND THEN GO TO /JSON FROM /,
# THERE WILL BE MUCH MORE EXPLANATION ABOUT THE ERROR

from flask import Flask, jsonify, session

app = Flask(__name__)

app.config['DEBUG'] = False     # Try to goto /json from / straight
app.config['SECRET_KEY'] = "Thisisasecret"

@app.route("/")
def index():
    session.pop('name', None)
    return "<h1>Hello Brother</1h>"

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/json')
def json():
    #if 'name' in session:
    mylist = [1,2,3,4]
    name = session['name']
    #else:
    #    name = 'NotinSession !'
    return jsonify({'key' : 'value', 'key2' : [1,2,3], 'name' : name})


if __name__=="__main__":
    app.run()


# YOU CAN OPEN CONSOLE TOO IN THE /JSON ERROR PAGE, BY CLCKING AT THE CONSOLE ICON AT THE
# FAR RIGHT SIDE OF THE ERROR LINES
