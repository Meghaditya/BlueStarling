import operator
from twython import TwythonError

def simple_search(twitter, topic, total=100, en_only=True):
	try:
	    search_results = twitter.search(q=topic, count=total)
	except TwythonError as e:
		print(e)

	text_set = set([])	
	search_results_dict = dict([])
	for tweet in search_results['statuses']:
		if ((not en_only) or tweet['lang'] == 'en') :
			user_name = tweet['user']['screen_name'] 
			retweet_count = tweet['retweet_count'] #if tweet['retweeted'] else 0
			favorite_count = tweet['favorite_count'] #if tweet['favorited'] else 0
			text = tweet['text']	

			if text not in text_set:
				text_set.add(text)
				# simple dictionary of object - (r_count+f_count) mapping
				# can be changed to assign proper weights to r/f
				search_results_dict[(user_name, \
					retweet_count, \
					favorite_count, \
					text)] = retweet_count+favorite_count
		else :
			print('lang is =', tweet['lang'], ' -- skipping.')

	return reversed(\
		sorted(search_results_dict.items(), \
			key=operator.itemgetter(1)))