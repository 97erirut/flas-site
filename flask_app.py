<<<<<<< HEAD
"""author: Erik Ruthström, 2015"""

#importera flask
from flask import Flask, render_template
import sqlite3 as lite

#
DATABASE = "flask-sited/database/testdb.db"
DEBUG = True
SECRET_KEY = "11223345"
USERNAME = "admin"
PASSWORD = "default"

#skapa flask-appen
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def startpage():
    return render_template("index.html")

if (__name__== "__main__"):
    app.run()
=======
"""Author: Erik Ruthström, 2015"""

#import flask
from flask import Flask, render_template

#create flask-app
app = Flask(__name__)

@app.route('/')
@app.route('/startpage/')
def startpage():
    """..."""
    return render_template("startpage.html")

if (__name__ == "__main__"):
    app.run()
>>>>>>> origin/master
