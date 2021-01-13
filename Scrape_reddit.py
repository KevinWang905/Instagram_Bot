# Author: Kevin Wang
# Last Update: January 12, 2021

# Function: Scrapes subreddit of choice for 10 top posts

# Outputs: 1 excel file containing reddit post info


#################################################################################

import praw
import pandas as pd

reddit = praw.Reddit(client_id="",      # your client id
                     client_secret="",  #your client secret
                     user_agent="", #user agent name
                     username = "",     # your reddit username
                     password = "")     # your reddit password

sub = ['aww']

for s in sub:
    subreddit = reddit.subreddit(s)

    # query = ['']

    # for item in query:
    post_dict = {
        "title" : [],   #title of the post
        "score" : [],   # score of the post
        "author" : [],      # unique id of the post
        "url" : [],     #url of the post
        "comms_num": [],   #the number of comments on the post
        "created" : [],  #timestamp of the post
        "video" : [],

    }
    comments_dict = {
        "comment_id" : [],      #unique comm id
        "comment_parent_id" : [],   # comment parent id
        "comment_body" : [],   # text in comment
        "comment_link_id" : []  #link to the comment
    }
    for submission in subreddit.top('day',limit=10):
        post_dict["title"].append(submission.title)
        post_dict["score"].append(submission.score)
        post_dict["author"].append(submission.author)
        isvideo = 1
        try:
            post_dict["url"].append(submission.media['reddit_video']['fallback_url'])

        except:
            post_dict["url"].append(submission.url)
            isvideo = 0

        if isvideo == 1: post_dict["video"].append(1)
        else: post_dict["video"].append(0)
        post_dict["comms_num"].append(submission.num_comments)
        post_dict["created"].append(submission.created_utc)
        

        
    post_data = pd.DataFrame(post_dict)
    post_data.to_csv(s+"_" +"subreddit.csv")
