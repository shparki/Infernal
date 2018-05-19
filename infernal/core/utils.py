from . import constants as const
import requests
import datetime
import os
import logging
import csv

import pandas as pd
import queue
import threading
import time


#eventually make available to change in pylol.cfg
DATA_PATH = os.getcwd() + '/data'
LOGS_PATH = os.getcwd() + '/logs'





class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'

class Session(object):

	def __init__ (self, api_key, endpoint='na-old'):
		self.api_key = api_key
		self.endpoint = 'na-old'
		if endpoint in const.ENDPOINTS.keys():
			self.endpoint = endpoint
		# add code here to log that endpoint not found, using default endopint

		self.uid = datetime.datetime.today().strftime('%y%m%d_%H%M%S')

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

		self.request_rate = 0.5
		self.request_throttle = 1.1


	def __str__(self):
		return 'session_{}'.format(self.uid)



	def build_url (self, url, url_params = {}):
		args = {
			'endpoint':	const.ENDPOINTS[self.endpoint],
			'url':		url
		}
		req_url = const.URLS_BASE['base'].format_map(
			default_dict(**args))
		req_url = req_url.format_map(
			default_dict(**url_params))


		return req_url

	def _request(self, url, params = {}):
		

		param_string = ''
		for key, value in params.items():
			param_string += (str(key) + '=' + str(value) + '&')
		param_string += ('api_key=' + self.api_key)
		url = url.format(params = param_string)

		self._log('Requesting...')
		self._log('URL: ' + str(url))

		req = requests.get(url)

		self._log('RESPONSE CODE: ' + str(req.status_code))
		self._log('RESPONSE: ' + str(req.json()))
		self._log('Done!')

		return req.json()

	def request(self, url, params={}):
		time.sleep(self.request_rate * self.request_throttle)
		jsn = self._request(url=url, params=params)
		return jsn




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

	def _cache(self, data):
		pass

	def _decache(self, name):
		pass





