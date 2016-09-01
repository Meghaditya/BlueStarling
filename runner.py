from utils import custom_prompt
from utils import fetch_twitter_credential
from twython import Twython
from simple_retweet import simple_iterative_retweet
from profile_cleaner import get_all_statuses

(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = fetch_twitter_credential()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mode_text = 'Enter mode :\n' + \
			'1. Simple Iterative Retweet.\n' + \
			'2. Clean Profile\n' + \
			'Your Choice : '

mode = int(custom_prompt(mode_text))

if mode == 1:
	topic = custom_prompt('Enter the topic : ')
	simple_iterative_retweet(twitter, topic)
elif mode == 2:
	screen_name = custom_prompt('Enter screen name : ')
	statuses = get_all_statuses(twitter, screen_name)
	print(len(statuses))
else:
	print('wrong input')