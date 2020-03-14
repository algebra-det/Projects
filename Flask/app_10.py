# Configurations of flask app
# Debug is a configuration,  some more are TESTING, SECRET_KEY, LOGGER_NAME
# We can define debug after the app = Flask()

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

app.config['DEBUG'] = True
# check more on : https://flask.palletsprojects.com/en/1.1.x/config/

@app.route("/")
def root():
    return "<h1>Hello Brother</1h>"

@app.route("/home", methods=["POST", "GET"], defaults={'name' : ''})
@app.route("/home/<name>", methods=["POST", "GET"])
def home(name):
    return "<h1>DEATH BED ! {}".format(name)



if __name__=="__main__":
    app.run()                   # OR here by app.run(debug=True)
