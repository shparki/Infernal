import RiotAPIWrapper
import Constants as const

class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'

class Session(object):

	def __init__ (self, api_key, endpoint='na-old'):
		self.api_key = api_key
		self.endpoint = endpoint

	# Basic requst handler, will be split per-API afer
	def _request(self, url, params={}, headers={}):
		args = {
			'endpoint': 	const.ENDPOINTS[self.endpoint],
			'url':			url,
			'api_key': 		self.api_key,
		}
		req_url = const.URLS_BASE['base'].format_map(
			default_dict(**args))

		req_url = req_url.format_map(
			default_dict(**params))

		req = requests.get(req_url, headers=headers)
		return req.json()