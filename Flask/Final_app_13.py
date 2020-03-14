from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)

app.config['SECRET_KEY'] = "Thisisasecret"


@app.route('/')
def index():
    session.pop('name', None)
    return "<h1>Hello World !</h1>"


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def home(name):                                                                # for example, http://127.0.0.1:5000/dome/123
    session['name'] = name
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = "NotinSession"
    return jsonify({'key' : 'value', 'key2' : [1,2,3], 'name' : name})


@app.route('/query')
def query():        # Use this by http://localhost:5000/query?name=Akash&location=India
    name = request.args.get('name')     # to get the input from ?name=(Anything)
    location = request.args.get('location')     # to get the input from ?location=(Anything)
    return "<h1>Hi {}, So from {}<br> You are on the query page</h1>".format(name,location)



@app.route('/theform', methods=["GET", "POST"])     # Using the form and process on the same page
def theform():

    if request.method == "GET":                           # by using action="/theform"
        return '''<form method="POST" action="/theform">
                        <input type="text" name="name">
                        <input type="text" name="location">
                        <input type="submit" value="Submit">
                    </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('query', name=name, location=location))     # As query takes name and location so we have to pass them here,
        #OR                                                                 # these will be automatically passed to the query?name=&location=
        #name = request.form['name']
        #location = request.form['location']
        #return redirect(url_for('home'))
        #OR
        #name = request.form['name']
        #return redirect(url_for('index', name=name))




'''@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1>Hello {}, from {}</h1><br>You have submitted the form succesfully</h>".format(name,location)
'''

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()           # to get data from online json formats or links
    name = data['name']                 # that's why POST is used to get the data from any link
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'result' : 'Success', 'name' : name , 'location' : location, 'randomkeylist' : randomlist})



if __name__=="__main__":
    app.run(debug=True)
