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
from app import app

'''
 
client_id=os.environ['CLIENT_ID']
client_secret=os.environ['CLIENT_SECRET']
user_agent=os.environ['USER_AGENT']

reddit = praw.Reddit(client_id,
                     client_secret,
                     user_agent
                     )
'''
reddit = praw.Reddit(client_id=os.environ['clientId'],
                     client_secret=os.environ['clientSecret'],
                     user_agent=os.environ['userAgent']
                     )
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
    for index, top_level_comment in zip(range(limit), submission.comments):
        if isinstance(top_level_comment, MoreComments):
            continue
        #print(top_level_comment.body)
      # if submission.domain == 'self.AsianBeauty':
    dict = {
        "title": submission.title,
        "score": submission.score,
        "id": submission.id,
        "url": submission.url,
        "comms_num":  submission.num_comments,
        "created": submission.created,
        "body": submission.selftext
    }

    posts.append(dict)

def collect_posts():
    with open('app/data/data.json', 'w') as f:
         json.dump(posts, f)


