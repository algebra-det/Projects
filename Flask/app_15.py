# Declaring LOGIC in html file i.e. template/home1.html
# as we declared ia line 13, display=False , the LOGIC at home1.html will do the else: statement work
# We used {% (some LOGIC) %} in /template/home1.html, it defines that we are using python LOGIC here
# Try to desplay=True, then it will do the if: statement work

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])                     # not <int:name> will only work if the user input in the address is integer
def home(name):                                                                # for example, http://127.0.0.1:5000/dome/123
    session['name'] = name
    return render_template('home.html', name=name, display=False)              # Try making display=True
    # Check out template/home1.html and see how to declare some python code LOGIC in html file


if __name__=="__main__":
    app.run(debug=True)
