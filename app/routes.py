import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
#from flask_pymongo import PyMongo
from app.helpers import apology, login_required
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from tempfile import mkdtemp
from config import Config
from app import app
from app.get_reddit import collect_posts
from app.wiki import summary

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/wiki')
def wiki():
    s=summary()
    return render_template("wiki.html", summary=s)

@app.route('/c')
def collect():
    collect_posts()
    return "a"

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
        
if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)