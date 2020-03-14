#So to overcome the app_11_1.py issue i.e.
# if the user haven't visited the /home app and get straight to the /json app than it will result an error
# we overcome this by inserting in /json that
# IF there's 'name' in session than get name , ELSE have a default name

from flask import Flask, jsonify, session

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "Thisisasecret"

@app.route("/")
def index():
    session.pop('name')
    return "<h1>Hello Brother</1h>"

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotinSession !'
    return jsonify({'key' : 'value', 'key2' : [1,2,3], 'name' : name})
    # Now try going to /json straight without going to /home/<name>
    # It will show NotinSession

if __name__=="__main__":
    app.run()
