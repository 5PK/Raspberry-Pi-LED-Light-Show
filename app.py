# FLASK_APP=hello.py flask run

from flask import Flask, render_template
import os
# Load the env variables
if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")