import tweepy
import time
import nlp
import search 
import os
import json

consumer_key='VGI38vqe7GrHymOVoXa2velFH'
consumer_secret='Oh9l1niA18MoD5ePgMWFZNLVkeWJup9SYcHRgEEAglDh3E9CfP'
access_token='1387846848602206209-NmLNGy2HDWXTR0NuQoiJn5oDXj9x9U'
access_token_secret='hk7NqxwUObC1LOLEFrekz68fywwGjiM5W73v7gddkP4rE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

FILE_NAME = 'lastseen.txt'
output='output.json'


def read_last_seen(FILE_NAME):
	file_read=open(FILE_NAME,'r')
	last_seen_id=int(file_read.read().strip())
	file_read.close()
	return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
	file_write=open(FILE_NAME,'w')
	file_write.write(str(last_seen_id))
	file_write.close()
	return

def reply():
	mentions=api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
	for tweet in reversed(mentions):
		count=0
		for c in str(tweet.full_text):
			if c=='@':
				count=count+1
			if count>1:
				break
		if count==1:
			print(tweet.full_text)
			response=nlp.natlangpro(tweet.full_text)
			leads=search.searchTweets(response[1:])
			for x in leads:
				# api.update_status('@' + tweet.user.screen_name + " " + x,tweet.id)
				print(x)
			# store_last_seen(FILE_NAME,tweet.id)
			print("replied to " + tweet.user.screen_name)
	
while True:
	reply()
	time.sleep(5)