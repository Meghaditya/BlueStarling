import time
from twython import Twython, TwythonError
from utils import fetch_twitter_credential

# A simple method to iteratively post tweets by searching with a given topic.
#
# topic - the search query for finding tweets
# iteration - the number of times the cycle would go on
# en_only - should retweet tweets in english
# time_delay - the time delay between each re-tweet

def simple_iterative_retweet(topic, iteration=5, en_only=True, time_delay=1):
	(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = fetch_twitter_credential()
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	
	try:
	    search_results = twitter.search(q=topic, count=iteration)
	except TwythonError as e:
		print(e)

	for tweet in search_results['statuses']:
		if ((not en_only) or tweet['lang'] == 'en') :
			print('posted tweet from = ', tweet['user']['screen_name'])
			twitter.retweet(id=tweet['id'])
			time.sleep(time_delay)
		else :
			print('lang is =', tweet['lang'], ' -- skipping.')