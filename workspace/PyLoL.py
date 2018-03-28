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

	# TODO: change versioning code, should be per-API used
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


#https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/RiotSchmick?api_key=<key>


tsesh = plSession('RGAPI-9c7f451e-0501-40ce-b76b-4a54459372da')
r = tsesh._request(const.URLS_SUMMON['by name'], params = {'summoner_name': 'RiotSchmick'})
print(r)
