# Passing more stuff to the html file i.e. /templates/home2.html
# Here we are passing mylist & listofdictionaries to the home2.html
# To use them in the html file itself in the LOGIC declaration
# Checkout the /templates/home2.html for further knowledge


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, mylist = ['one', 'two', 'three', 'four'], listofdictionaries=[{'name' : 'Akash'}, {'name' : "Mickey"}])

if __name__=="__main__":
    app.run(debug=True)
