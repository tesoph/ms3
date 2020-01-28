from flask import Flask
from config import Config
from pymongo import MongoClient
from flask_session import Session

#Creates the app object as an instance of class Flask
#__name__is a Python predefined variable which is set to the name of the module in which it is used.
app = Flask(__name__)
#'config' = config.py, Config is actual class
app.config.from_object(Config)
#enable sessions for this particular flask web application
Session(app)

#client = MongoClient(Config.MONGO_URI)
#db= client.users

#routes module is imported at the bottom.
#Workaround to circular imports
#(routes needs to import app which is defined above)
#from app import routes
from app import routes
'''
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
    }
'''
