import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_pymongo import PyMongo
from helpers import apology, login_required
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

"""
Following code for app.config form cs50-finance
"""
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
#the location to store information about the session
app.config["SESSION_TYPE"] = "filesystem"
#enable sessions for this particular flask web application
Session(app)

MONGO_URI=os.environ['MONGO_URI']
MONGO_DBNAME=os.environ['MONGO_DBNAME']

client = MongoClient(MONGO_URI)
db= client.ms3

if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)