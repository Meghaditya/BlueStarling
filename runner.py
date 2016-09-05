import time
import random
from time import gmtime, strftime
from utils import custom_prompt
from utils import fetch_twitter_credential
from twython import Twython
from simple_retweet import simple_iterative_retweet
from profile_cleaner import reset_profile
from trends import get_trends_from_places
from search import simple_search
from twit_machine import auto_tweet_dynamic_trend

(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = fetch_twitter_credential()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mode_text = 'Enter mode :\n' + \
			'1. Simple Iterative Retweet.\n' + \
			'2. Clean Profile\n' + \
			'3. Get Hourly Trends in India\n' + \
			'4. Get 100 tweets about topic\n' + \
			'5. Start Dynamic Trend TwitMachine\n' + \
			'Your Choice : '

mode = int(custom_prompt(mode_text))

if mode == 1:
	topic = custom_prompt('Enter the topic : ')
	simple_iterative_retweet(twitter, topic)
elif mode == 2:
	screen_name = custom_prompt('Enter screen name : ')
	reset_profile(twitter, screen_name)
elif mode == 3:
	while True:
		print('Getting Hourly trend in India')
		print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
		print('-------------')
		trends = get_trends_from_places(twitter, ['India'], [])
		for trend in trends:
			print(trend)
		print('-------------')
		time.sleep(60*60)
elif mode == 4:
	topic = custom_prompt('Enter the topic : ')
	search_results = simple_search(twitter, topic)
	for result in search_results:
		print(result)
elif mode == 5:
	auto_tweet_dynamic_trend(twitter, \
		get_trends_from_places(twitter, ['Singapore'], []))
else:
	print('wrong input')