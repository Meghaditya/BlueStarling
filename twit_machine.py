from random import randint
from twython import Twython, TwythonError
from time import gmtime, strftime
from search import simple_search
import time

def retweet(twitter, search_result):
	text=search_result[0][3]
	tweet_id=search_result[0][4]
	try:
		twitter.retweet(id=tweet_id)
		print('posted status - ', text)
	except TwythonError as e:
		print(e)


def follow(twitter, search_result):
	user_name=search_result[0][0]
	user_id=search_result[0][5]
	try:
		twitter.create_friendship(user_id=user_id, follow='true')
		print('following user - ', user_name)
	except TwythonError as e:
		print(e)	

def auto_tweet_dynamic_trend(twitter, trends):
	TOTAL_TRENDS = 3
	TOTAL_TWEETS = 3
	TWEET_INTERVAL_LOWER_BOUND = 15*60
	TWEET_INTERVAL_UPPER_BOUND = 20*60

	while True:
		print('Starting new iteration')
		print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
		print('-------------')
		
		i = 0
		for trend in trends:
			if (i>TOTAL_TRENDS):
				break
			i += 1
			j = 0
			search_results = simple_search(twitter, trend[0])
			for search_result in search_results:
				if (j>TOTAL_TWEETS):
					break
				j += 1
				retweet(twitter, search_result)
				follow(twitter, search_result)
				wait_time = random.randint(TWEET_INTERVAL_LOWER_BOUND, TWEET_INTERVAL_UPPER_BOUND)
				time.sleep(wait_time)
		print('-------------')