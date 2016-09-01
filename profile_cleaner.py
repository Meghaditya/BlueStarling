from twython import Twython, TwythonError
from utils import fetch_twitter_credential

# GET friends/ids returns a cursored collection of 
# user ids for every user the specified user is
# following (otherwise know as their 'friends')
#
# The cursoring technique is borrowed from here -
# https://dev.twitter.com/overview/api/cursoring

def get_all_friends(twitter, screen_name_text):
	friends_list = []
	next_cursor = -1

	while True:
		if (next_cursor > 0) :
			friends = twitter.get_friends_ids(screen_name=screen_name_text, cursor=next_cursor)
		else :
			friends = twitter.get_friends_ids(screen_name=screen_name_text)

		friends_list += friends['ids']
		next_cursor = friends['next_cursor']

		if (next_cursor == 0) :
			# good old do-while
			break

	return friends_list


# For working details, please refer to the following twitter dev doc -
# https://dev.twitter.com/rest/public/timelines 

def get_all_statuses(twitter, screen_name_text):
	statuses_list = []
	max_id_val = -1
	since_id_val = -1

	while True:
		print('max_id = ' , max_id_val)
		if (max_id_val > 0) :
			statuses = twitter.get_user_timeline(screen_name=screen_name_text, max_id=max_id_val)
		else :
			statuses = twitter.get_user_timeline(screen_name=screen_name_text)
			since_id_val = statuses[0]['id']
			print('since_id = ' , since_id_val)

		print('len(statuses) : ', len(statuses))	
		if (len(statuses) == 0) :
			break

		statuses_list += statuses
		max_id_val = statuses[len(statuses)-1]['id'] - 1

	statuses = twitter.get_user_timeline(screen_name=screen_name_text, since_id=since_id_val)

	if (len(statuses) > 0):
		statuses_list += statuses	

	return statuses_list

# Currently destroying - 
#
# Statuses
# Direct Messages
# Friendships

def destroy_all_friendships(twitter, screen_name_text):
	friends_list = get_all_friends(twitter, screen_name_text)
	print('found ', len(friends_list), ' friends')
	progress_count = 0
	for friend_id in friends_list:
		if (progress_count%10 == 0) :
			print('destroyed ', progress_count, ' friendships')
		twitter.destroy_friendship(user_id=friend_id)
		progress_count += 1
	print('destroyed all')

# def destroy_all_statuses(twitter, screen_name_text):

# def destroy_all_direct_messages(twitter, screen_name_text):

# High level utility

def reset_profile(twitter, screen_name_text):
	#destroy_all_statuses(twitter, screen_name_text)
	#destroy_all_direct_messages(twitter, screen_name_text)
	destroy_all_friendships(twitter, screen_name_text)