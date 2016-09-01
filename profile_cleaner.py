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
		# debug - print('max_id = ' , max_id_val)
		if (max_id_val > 0) :
			statuses = twitter.get_user_timeline(screen_name=screen_name_text, max_id=max_id_val)
		else :
			statuses = twitter.get_user_timeline(screen_name=screen_name_text)
			if (len(statuses) > 0) :
				since_id_val = statuses[0]['id']
				# debug - print('since_id = ' , since_id_val)

		# debug - print('len(statuses) : ', len(statuses))	
		if (len(statuses) == 0) :
			break

		statuses_list += statuses
		max_id_val = statuses[len(statuses)-1]['id'] - 1

	if (since_id_val != -1) :	
		statuses = twitter.get_user_timeline(screen_name=screen_name_text, since_id=since_id_val)

	if (len(statuses) > 0):
		statuses_list += statuses	

	return statuses_list


# same as above

def get_all_favorites(twitter, screen_name_text):
	favorites_list = []
	max_id_val = -1
	since_id_val = -1

	while True:
		# debug - print('max_id = ' , max_id_val)
		if (max_id_val > 0) :
			favorites = twitter.get_favorites(screen_name=screen_name_text, count=200, max_id=max_id_val)
		else :
			favorites = twitter.get_favorites(screen_name=screen_name_text, count=200)
			if (len(favorites) > 0) :
				since_id_val = favorites[0]['id']
				# debug - print('since_id = ' , since_id_val)

		# debug - print('len(favorites) : ', len(favorites))	
		if (len(favorites) == 0) :
			break

		favorites_list += favorites
		max_id_val = favorites[len(favorites)-1]['id'] - 1

	if (since_id_val != -1) :	
		favorites = twitter.get_favorites(screen_name=screen_name_text, count=200, since_id=since_id_val)

	if (len(favorites) > 0):
		favorites_list += favorites	

	return favorites_list


# Currently destroying - 
#
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


# Statuses

def destroy_all_statuses(twitter, screen_name_text):
	statuses_list = get_all_statuses(twitter, screen_name_text)
	print('found ', len(statuses_list), ' statuses')
	progress_count = 0
	for status in statuses_list:
		if (progress_count%10 == 0) :
			print('destroyed ', progress_count, ' statuses')
		twitter.destroy_status(id=status['id'])
		progress_count += 1
	print('destroyed all')


# Favorites

def destroy_all_favorites(twitter, screen_name_text):
	favorites_list = get_all_favorites(twitter, screen_name_text)
	print('found ', len(favorites_list), ' favorites')
	progress_count = 0
	for favorite in favorites_list:
		if (progress_count%10 == 0) :
			print('destroyed ', progress_count, ' favorites')
		twitter.destroy_favorite(id=favorite['id'])
		progress_count += 1
	print('destroyed all')


# High level utility

def reset_profile(twitter, screen_name_text):
	destroy_all_statuses(twitter, screen_name_text)
	destroy_all_friendships(twitter, screen_name_text)
	destroy_all_favorites(twitter, screen_name_text)