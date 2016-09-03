import time
from time import gmtime, strftime
from utils import custom_prompt
from utils import fetch_twitter_credential
from twython import Twython
from simple_retweet import simple_iterative_retweet
from profile_cleaner import destroy_all_favorites
from trends import get_trends_from_places

(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = fetch_twitter_credential()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mode_text = 'Enter mode :\n' + \
			'1. Simple Iterative Retweet.\n' + \
			'2. Clean Profile\n' + \
			'3. Get Hourly Trends in India\n' + \
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
else:
	print('wrong input')