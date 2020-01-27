import os
from tempfile import mkdtemp
from flask_session import Session

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MONGO_URI=os.environ['MONGO_URI']
    MONGO_DBNAME=os.environ['MONGO_DBNAME']

    SESSION_FILE_DIR = mkdtemp()
    SESSION_PERMANENT = False
    #the location to store information about the session
    SESSION_TYPE = "filesystem"
'''
    clientId=os.environ['CLIENT_ID']
    clientSecret=os.environ['CLIENT_SECRET']
    userAgent=os.environ['USER_AGENT']
    '''