import requests
import json
from time import gmtime, strftime, sleep

# Gets the top trends given a country name
# Handles the following errors:
# 1. Country name to code mapping doesn't exist
# 2. Country code to id mapping doesn't exist
# 3. Hawttrends returns some error

def get_top_trends(country_name):
	f_country_to_code = open('country_to_code.json', 'r')
	f_code_to_id = open('code_to_id.json', 'r') 

	country_to_code_json = json.load(f_country_to_code)
	code_to_id_json = json.load(f_code_to_id)
	trends_json = []

	if country_name.upper() not in country_to_code_json.keys():
		print('Country Code doesn\'t exist')
	else:
		country_code = country_to_code_json[country_name.upper()]
		#print('Country code = ', country_code)
		
		if country_code not in code_to_id_json.keys():
			print('Country Id doesn\'t exist')
		else:		
			country_id = code_to_id_json[country_code]
			#print('Country id = ', country_id)

			r = requests.get('http://hawttrends.appspot.com/api/terms/')
			if (r.status_code == 200):
				result_json = json.loads(r.text)
				trends_json = result_json[country_id]
			else:
				print('Hawttrends returned error')
				print('Status Code = ', r.status_code)

	return trends_json

# Gets periodic Google trends
#
# Params:
# country_name - the country for which trend to find
# time_interval - the period in seconds
#
# Prints the trends metrics

def get_periodic_google_trends(country_name, time_interval):
	old_trends = dict([])
	new_trends = dict([])
	while True:
		print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
		old_trends = new_trends
		new_trends_list = get_top_trends(country_name)
		fresh_trends = []

		for new_trend in new_trends_list:
			if new_trend in old_trends.keys():
				new_trends[new_trend] = old_trends[new_trend] + 1
				print('Search topic - ', new_trend \
					, ' - trending for - ' \
					, float((new_trends[new_trend]*time_interval)/(60*60)) \
					, ' - hours')
			else:
				fresh_trends.append(new_trend)
				new_trends[new_trend] = 0

		if(len(fresh_trends)>0):		
			print('-------------------')		
			print('New trending topics: ')		
			for trend in fresh_trends:
				print(trend)		
			print('-------------------')		

		# Sleep for an hour
		sleep(time_interval)