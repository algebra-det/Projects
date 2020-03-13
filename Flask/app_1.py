from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World !</h1>"     #Any string passed will automatically be converted to HTML

@app.route('/<name>')   # here <name> is a place-holder
def root(name):         # have to include the place-holder i.e. name in our case, inside ()
    return "<h1>Hello {} !</h1>".format(name)   # In {} the placeholder value will be printed
# Check out by inserting into the address bar after localhost, your name or any world
#   "http://127.0.0.1:5000/Akash"

@app.route('/home')
def home():
    return "<h1>You are on the HOME PAGE</h1>"

if __name__=="__main__":
    app.run(debug=True)
