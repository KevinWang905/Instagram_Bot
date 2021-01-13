# Author: Kevin Wang
# Last Update: January 12, 2021

# Function: Takes output of scrape_reddit and downloads videos

# Outputs: 4 mp4, 1 csv: username list


#################################################################################

import urllib.request
import pandas as pd
raw = pd.read_csv('aww.csv')


videos = raw[raw['video']==1].copy()
videos.reset_index(inplace = True)
videos['author'] = videos.apply(lambda x: '/u/'+x['author'], axis = 1)

names = videos[['author']]

names.to_csv('names.csv')


for i in range(0,4):
	url = videos['url'][i]
	print(url)
	urllib.request.urlretrieve(url, '/Users/kevin wang/Desktop/Reddit_Insta/{:d}.mp4'.format(i))