'''
1. Use reddit api to retrieve data
2. store each thread data as a dictionary
3. append each thread dictionary to a list

'''
import praw
import os
# comment reading from https://praw.readthedocs.io/en/latest/tutorials/comments.html
from praw.models import MoreComments
import pandas as pd
import datetime as dt
import json
import csv
import collections
from pprint import pprint

#from app import app

'''
 
client_id=os.environ['CLIENT_ID']
client_secret=os.environ['CLIENT_SECRET']
user_agent=os.environ['USER_AGENT']
'''


reddit = praw.Reddit(client_id=os.environ['clientId'],
                     client_secret=os.environ['clientSecret'],
                     user_agent=os.environ['userAgent']
                     )


'''
reddit = praw.Reddit(client_id=clientId,
                     client_secret=clientSecret,
                     user_agent=userAgent
                     )
'''
# posts={}

posts = []

dict = {}
subreddit = reddit.subreddit('AsianBeauty')
top_subreddit = subreddit.top(limit=5)
# i=0

'''
Adding comments 
https://praw.readthedocs.io/en/latest/tutorials/comments.html
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
'''
'''
limit iterations of a loop
https://stackoverflow.com/questions/36106712/how-can-i-limit-iterations-of-a-loop-in-python
for index, item in zip(range(limit), items):
    print(index, item)
'''

limit=2
for submission in top_subreddit:
    commentsList=[]
    for index, top_level_comment in zip(range(limit), submission.comments):
        if isinstance(top_level_comment, MoreComments):
            continue
        dict={
            'body':top_level_comment.body
        }
        #print(dictt)
        commentsList.append(dict)
        #commentsList.append(top_level_comment)
      # if submission.domain == 'self.AsianBeauty':
    dict = {
        "title": submission.title,
        "score": submission.score,
        "id": submission.id,
        "url": submission.url,
        "comms_num":  submission.num_comments,
        "created": submission.created,
        "body": submission.selftext,
        "comments": commentsList
    }
    posts.append(dict)
#https://stackoverflow.com/questions/47259540/python-writing-json-file-as-list-of-dictionaries
def collect_posts():
    print('x')
    #json.dumps(posts)
    with open('app/data/posts.json', 'w+') as f:
         pprint(posts, f)
    '''
    with open('app/data/data.json', 'w') as f:
         json.dump(posts, f)
    '''
    #https://stackoverflow.com/questions/21525328/python-converting-a-list-of-dictionaries-to-json

#collect_posts()
