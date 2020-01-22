import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
a=os.environ.get('MONGO_DBNAME')
b=os.environ.get('MONGO_URI')
print(f'hi, {a}')
print(f'hi, {b}')
c=os.environ['MONGO_URI']
print(c)

mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'Hello World a...again'


if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
    