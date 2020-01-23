import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_pymongo import PyMongo
from helpers import apology, login_required
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
a=os.environ.get('MONGO_DBNAME')
b=os.environ.get('MONGO_URI')
print(f'hi, {a}')
print(f'hi, {b}')
c=os.environ['MONGO_URI']
print(c)
'''
from cs50
'''
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
#the location to store information about the session
app.config["SESSION_TYPE"] = "filesystem"
#enable sessions for this particular flask web application
Session(app)

MONGO_URI=os.environ['MONGO_URI']
MONGO_DBNAME=os.environ['MONGO_DBNAME']

#mongo = PyMongo(app)

client = MongoClient(MONGO_URI)
db= client.ms3

@app.route("/")
#@login_required
def index():
    """index page"""
    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # check password confirmation
        if not request.form.get('password') == request.form.get('confirmation'):
            return apology("passwords don't match", 403)
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        
        user=request.form.to_dict()
        alreadyExists = db.users.find_one({"username": user['username']})

     
        del user['confirmation']
        plain = request.form.get("password")
        user['password'] = generate_password_hash(plain, method='pbkdf2:sha256', salt_length=8)

        if alreadyExists:
            return apology("Username already exists", 400)
        if not alreadyExists:
            db.users.insert_one(user)
     

        # log user in
        '''
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                        username=request.form.get("username"))'''
        #db.users.find_one({"username": session['user']})
        # Remember which user has logged in
        #session["user_id"] = rows[0]["id"]
        session['user_id'] = (db.users.find_one({"username": user['username']}))['_id']
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


'''
login() adapted from c50 finance
'''
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        '''
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))'''
        user = db.users.find_one({"username": request.form.get("username")})

        # Ensure username exists and password is correct
        if not user or not check_password_hash(user['password'], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session['user_id'] = (db.users.find_one({"username": user['username']}))['_id']
       #session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
    