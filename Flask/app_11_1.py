# Using COOKIES to make a SESSION
# Suppose you have logged in the website, so we have to pass your information to every url
# So that the page know that it's this user
# Hence cookies comes into play, the site(or URLs) will get the data from the cookies stored
# We do this by using SECRET_KEY in config to make the cookies private

from flask import Flask, jsonify, session

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "Thisisasecret"      # WITHOUT THIS SECRET KEY, NO ONE CAN CHANGE THE CONTENT OF THE COOKIES
# Suppose if any malicios person get his hands on the cookie file, he can see the content of the cookies and change it's content
# but with secret_key , he can't change the content, So never put any sensetive content inside the cookie

@app.route("/")
def index():
    return "<h1>Hello Brother</1h>"

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name      # Assigning the name in the session
    # by using the above syntax we can use this name anywhere in the code by retrieving it from the sesssion
    return "<h1>Hello {}, You are on the HOME PAGE</h1>".format(name)

@app.route('/json')
def json():
    name = session['name']      # retrieving the name from the session and assigning it to variable name
    return jsonify({'key' : 'value', 'key2' : [1,2,3], 'name' : name})
    # now check the /json app you will see the name which we used in /home/<akash> app

# There's one issue here i.e. if the user haven't visited the /home app then /json will return an error
# For example, if the user goto /index than straight to /json there will be error
# To overcome this issue see app_11_2.py

if __name__=="__main__":
    app.run()
