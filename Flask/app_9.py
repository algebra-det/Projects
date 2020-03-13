''' To redirect the user to some PAGE
    Suppose the user have to log-in and then have to be redirected to the home PAGE
'''

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World !</h1>"


@app.route('/index', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/index/<string:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def index(name):                                                             # for example, http://127.0.0.1:5000/dome/123
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)


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
        return redirect(url_for('query', name=name, location=location))
        #OR
        #name = request.form['name']
        #return redirect(url_for('index', name=name))
        #OR
        #return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)
