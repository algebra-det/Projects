# We wil Add /static folder in the working directory
# To add static things inside this directory, as Flask automatically
# Pick static stuff from this directory like images, css files
# We use these files by declaring
# <img src="{{ url_for('static', filename='images/jk.jpg') }}" alt="J&K">



from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, mylist = ['one', 'two', 'three', 'four'], listofdictionaries=[{'name' : 'Akash'}, {'name' : "Mickey"}])

if __name__=="__main__":
    app.run(debug=True)
