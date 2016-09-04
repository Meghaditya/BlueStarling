import time
import operator

# Get all the places with(out) the filters
#
# Params:
# Twitter - the Twython object
# country_names - the list of country names to filter with
# place_names - the list of place names to filter with

def get_places(twitter, country_names = [], place_names = []):
	
	# All the available places for trends query
	places = twitter.get_available_trends()
	places_of_interest = 0
	places_list = []

	for place in places:
		#print(place['country'])
		#print(place['country'] in country_names)	

		if ((len(country_names)>0) and \
			(place['country'] in country_names)) :
			places_of_interest += 1
			#print('Added to places ', place['name'])
			places_list.append(place)
		
		if ((len(place_names)>0) and \
			  (place['name'] in place_names)) :
			places_of_interest += 1
			#print('Added to places ', place['name'])
			places_list.append(place)
		
		if ((not country_names) and \
			(not place_names)) :
			places_of_interest += 1
			#print('Added to places ', place['name'])
			places_list.append(place)

	return places_list


# Get all the trends after finding out the places
#
# Params:
# Twitter - the Twython object
# country_names - the list of country names to filter with
# place_names - the list of place names to filter with

def get_trends_from_places(twitter, country_names = [], place_names = []):

	return get_trends(twitter, get_places(twitter, country_names, place_names))
	

# Get the trends from list of places
#
# Params:
# places_list - the list of places

def get_trends(twitter, places_list):

	trends_of_ineterest = dict([])
	places_list_len = len(places_list)
	rate_limit_counter = places_list_len

	for place in places_list:

		trends_for_place = twitter.get_place_trends(id=place['woeid'])
		rate_limit_counter -= 1
		print('Got the trends for ', place['name'])
		
		for trend in trends_for_place[0]['trends']:
		
			if trend['name'] in trends_of_ineterest:
				oldCount = trends_of_ineterest[trend['name']]
				trends_of_ineterest[trend['name']] = oldCount + 1
		
			else:
				trends_of_ineterest[trend['name']] = 1

		time.sleep(60)

	return reversed(\
		sorted(trends_of_ineterest.items(), \
			key=operator.itemgetter(1)))