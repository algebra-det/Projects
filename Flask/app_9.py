''' To redirect the user to some PAGE
    Suppose the user have to log-in and then have to be redirected to the home PAGE
'''

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World !</h1>"


@app.route('/theform', methods=["GET", "POST"])     # Using the form and process on the same page
def theform():

    if request.method == "GET":                           # by using action="/theform"
        return '''<form method="POST" action="/theform">
                        <input type="text" name="name">
                        <input type="text" name="location">
                        <input type="submit" value="Submit">
                    </form>'''
    else:
        #name = request.form['name']
        #location = request.form['location']
        #return "<h1>Hello {}, from {}</h1><br>You have submitted the form succesfully</h>".format(name,location)
        return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)
