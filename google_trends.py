import requests
import json
from time import gmtime, strftime, sleep

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


def get_timely_google_trends(country_name, time_interval):
	while True:
		print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
		# Get and print trends
		print(get_top_trends(country_name))
		# Sleep for an hour
		sleep(time_interval)