import requests
import traceback
import Constants as const


class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'

class plSession(object):

	def __init__ (self, api_key, endpoint='na-old'):
		self.api_key = api_key
		self.endpoint = endpoint

	# Basic requst handler, will be split per-API afer
	def _request(self, url, params={}):
		args = {
			'endpoint': 	const.ENDPOINTS[self.endpoint],
			'url':			url,
			'api_key': 		self.api_key,
		}
		req_url = const.URLS_BASE['base'].format_map(
			default_dict(**args))
		#print(req_url)

		params['version'] = 'v3'
		req_url = req_url.format_map(
			default_dict(**params))
		#print(req_url)

		req = requests.get(req_url)
		return req.json()

	# params can be summoner_id or champion_id
	def _cmast_request(self, params={}):
		pass



# Hello World!
# https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/RiotSchmick?api_key=<key>
tsesh = plSession('--')
r = tsesh._request(const.URLS_SUMMON['by name'], params = {'summoner_name': 'RiotSchmick'})
print(r)
#
