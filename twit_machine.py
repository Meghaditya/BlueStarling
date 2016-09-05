import time
import random
from time import gmtime, strftime
from twython import Twython, TwythonError
from search import simple_search

def auto_tweet_dynamic_trend(twitter, trends):
	TOTAL_TRENDS = 3
	TOTAL_TWEETS = 5
	TWEET_INTERVAL_LOWER_BOUND = 1*60
	TWEET_INTERVAL_UPPER_BOUND = 2*60
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
				text=search_result[0][3]
				try:
					if (len(text) <= 140) :
						twitter.update_status(status=text)
						print('posted status - ', text)
					wait_time = random.randint(TWEET_INTERVAL_LOWER_BOUND, \
						TWEET_INTERVAL_UPPER_BOUND)
				except TwythonError as e:
					print(e)
				time.sleep(wait_time)
		print('-------------')