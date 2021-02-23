import requests
import json
import os
import random

import praw


reddit = praw.Reddit(client_id=os.environ["PRAW_CLIENT_ID"],
                     client_secret=os.environ["PRAW_CLIENT_SECRET"],
                     user_agent="thoughtful_showerthoughts_reader:v1.0 by /u/riesz_representation",
                     username="riesz_representation"
                    )


with open("submissions.json") as f:
    current_submissions = json.load(f)


def get_cowsay_message(msg):
    url = "http://cowsay.morecode.org/say"
    params = {
        "message": msg,
        "format": "text"
    }
    r = requests.get(url, params=params)
    return r.text

def fetch_showerthoughts():
    subreddit = reddit.subreddit("showerthoughts")
    submissions = []
    for submission in subreddit.hot(limit=200):
        submissions.append(submission.title)

    with open("submissions.json", "w") as f:
        json.dump(submissions, f, indent=2)

def get_random_showerthought_from_file():
    return random.choice(current_submissions)