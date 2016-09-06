# the heart
from twython import Twython

# utilities
from utils import custom_prompt
from utils import fetch_twitter_credential

# a simple one
from simple_retweet import simple_iterative_retweet

# a useful one
from profile_cleaner import reset_profile

# a key one
from twitter_trends import get_trends_from_places
from twitter_trends import get_hourly_twitter_trends

# an important one
from search import simple_search

# another key one
from twit_machine import retweet
from twit_machine import follow
from twit_machine import auto_tweet_dynamic_trend

# an experimental one
from google_trends import get_hourly_google_trends

# Initialize Twython with twitter credentials
# common code used by all path
(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = fetch_twitter_credential()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# C-style Switch block - deja vu!
mode_text = 'Enter mode :\n' + \
			'1. Simple Iterative Retweet.\n' + \
			'2. Clean Profile\n' + \
			'3. Get Hourly Twitter Trends in Any Country\n' + \
			'4. Get 100 tweets about topic\n' + \
			'5. Start Dynamic Trend TwitMachine\n' + \
			'6. Start Google Trend TwitMachine\n' + \
			'7. Test simple retweet and follow\n' + \
			'Your Choice : '

mode = int(custom_prompt(mode_text))

# Switch blocks implemented using if-else
# all vars inside cases are suffixed with
# mode number

# Simple Iterative Retweet
if mode == 1:
	topic_1 = custom_prompt('Enter the topic : ')
	simple_iterative_retweet(twitter, topic_1)

# Clean Profile
elif mode == 2:
	screen_name_2 = custom_prompt('Enter screen name : ')
	reset_profile(twitter, screen_name_2)

# Get Hourly Twitter Trends in Any Country
elif mode == 3:
	c_name_3 = custom_prompt('Enter country name : ')
	get_hourly_twitter_trends(twitter, c_name_3)
	
# Get 100 tweets about topic	
elif mode == 4:
	topic_4 = custom_prompt('Enter the topic : ')
	search_results = simple_search(twitter, topic_4)
	for result in search_results:
		print(result)

# Start Dynamic Trend TwitMachine
elif mode == 5:
	c_name_5 = custom_prompt('Enter country name:')
	auto_tweet_dynamic_trend(twitter, \
		get_trends_from_places(twitter, [c_name_5], []))

# Get Hourly Google Trends in Any Country
elif mode == 6:
	c_name_6 = custom_prompt('Enter country name: ')
	get_hourly_google_trends(c_name_6)

# Test simple retweet and follow
elif mode == 7:
	search_topic_7 = custom_prompt('Enter search topic: ')
	search_results_7 = simple_search(twitter, search_topic_7, 1)
	for s_7 in search_results_7:
		follow(twitter, s_7)
		retweet(twitter, s_7)

# error
else:
	print('wrong input')