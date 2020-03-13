from flask import Flask, request




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
        name = request.form['name']
        location = request.form['location']
        return "<h1>Hello {}, from {}</h1><br>You have submitted the form succesfully</h>".format(name,location)


'''@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1>Hello {}, from {}</h1><br>You have submitted the form succesfully</h>".format(name,location)
'''


if __name__=="__main__":
    app.run(debug=True)
