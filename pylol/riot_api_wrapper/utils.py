from . import constants as const
import requests
import datetime
import os
import logging

#eventually make available to change in pylol.cfg
DATA_PATH = os.getcwd() + '/data'
LOGS_PATH = os.getcwd() + '/logs'


class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'

class Session(object):

	def __init__ (self, api_key, endpoint='na-old', req_sec = 20, req_tmin = 100):
		self.api_key = api_key
		self.endpoint = endpoint
		self.uid = datetime.datetime.today().strftime('%y%m%d_%H%M%S')
		self.req_sec = req_sec
		self.req_tmin = req_tmin

		if not os.path.exists(DATA_PATH):
			os.mkdir(DATA_PATH)


		if not os.path.exists(LOGS_PATH):
			os.mkdir(LOGS_PATH)

		self.log_file = None
		self.log_path = LOGS_PATH + '/' + self.uid + '.log'
		if not os.path.exists(self.log_path):
			self.log_file = open(self.log_path, 'w')
			self.log_file.close()


		urllib3_log = logging.getLogger('urllib3')
		urllib3_log.setLevel(logging.CRITICAL)

		logging.basicConfig(
			level = 	logging.DEBUG,
			filename = 	self.log_path,
			format = 	'[%(levelname)s] %(asctime)s : %(message)s',
			datefmt = 	'%I:%M:%S %p'
		)

		self._log('Initialized ' + str(self))






	def __str__(self):
		return 'session_{}'.format(self.uid)

	# Basic requst handler, will be split per-API afer
	def _request(self, url, params={}):
		args = {
			'endpoint': const.ENDPOINTS[self.endpoint],
			'url':		url,
			'api_key': 	self.api_key,
		}
		req_url = const.URLS_BASE['base'].format_map(
			default_dict(**args))

		req_url = req_url.format_map(
			default_dict(**params))

		self._log('Requesting...')
		self._log('URL: ' + str(req_url))

		req = requests.get(req_url)

		self._log('RESPONSE CODE: ' + str(req.status_code))
		self._log('RESPONSE: ' + str(req.json()))
		self._log('Done!')

		return req.json()

	def _log(self, message, level='debug', full=False):
		if not full:
			if len(message) > 250:
				message = message[:150] + '...'

		if level == 'info':
			logging.info(message)
		elif level == 'debug':
			logging.debug(message)
		elif level == 'warning':
			logging.warning(message)
		elif level == 'error':
			logging.error(message)
		elif level == 'critical':
			logging.critical(message)
		else:
		 	logging.error('level \'%s\' does not exist. \n\t Message: %s', str(level), str(message[:250]))











