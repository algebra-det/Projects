# Using Inheritance by creating a base html file i.e. in our case layout.html
# parent block(layout.html) will be declared so that everything will be same outside of the block, i.e. content of layout.html
# the blocks will be called and used from the other html files like home.html or form.html



from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/theform', methods=['POST', 'GET'])
def theform():
    if request.method == "GET":
        return render_template('form2.html')
    else:
        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('query', name=name, location=location))


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')     
    return "<h1>Hi {}, So from {}<br> You are on the query page</h1>".format(name,location)




@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Defualt'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home4.html', name=name, display=False, mylist = ['one', 'two', 'three', 'four'], listofdictionaries=[{'name' : 'Akash'}, {'name' : "Mickey"}])

if __name__=="__main__":
    app.run(debug=True)
