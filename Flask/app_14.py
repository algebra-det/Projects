# How to use variable in render_template
# We do this by defining in the /appname by stating (variable) in our case
# return render_template('home.html', name=name)
# Than defining {{ name }} in home.html

from flask import Flask, jsonify, session

app = Flask(__name__)


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name)  # Check /templates/home.html, we used {{ name }} to define the use of variable


if __name__=="__main__":
    app.run(debug=True)
