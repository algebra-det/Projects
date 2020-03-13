from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World !</h1>"

@app.route('/theform')
def theform():
    return render_template("form.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1>Hello {}, from {}</h1><br>You have submitted the form succesfully</h>".format(name,location)


if __name__=="__main__":
    app.run(debug=True)


""" THE form.html :

<form method="POST" action="/process">
    <input type="text" name="name">
    <input type="text" name="location">
    <input type="submit" value="Submit">
</form>
"""
