from . import constants as const
from .infernal_error import RequestError
from .utils import default_dict

import requests
import datetime
import os
import logging
import csv

import pandas as pd
import queue
import threading
import time


class Session(object):

	def __init__ (self, api_key, endpoint='na-old', name=''):
		
		# Save api_key
		self.api_key = api_key

		# Check if the endpoint is valid; if not default to 'na-old'
		self.endpoint = 'na-old'
		if endpoint in const.ENDPOINTS.keys():
			self.endpoint = endpoint
			self._log('Endpoint {} not found; using default endpoing \'na-old\''.format(endpoint))

		# uid functions as a unique identifier for each session and the names for logging files
		self.uid = datetime.datetime.today().strftime('%y%m%d_%H%M%S')

		# Create data & logs folders if they do not exist- created at the location of the script
		self.data_dpath = os.getcwd() + '/data'
		self.logs_dpath = os.getcwd() + '/logs'

		if not os.path.exists(self.data_dpath):
			os.mkdir(self.data_dpath)

		if not os.path.exists(self.logs_dpath):
			os.mkdir(self.logs_dpath)

		# Instantiate logger file
		self.log_file = None
		self.log_path = self.logs_dpath + '/' + self.uid + '.log'
		if not os.path.exists(self.log_path):
			self.log_file = open(self.log_path, 'w')
			self.log_file.close()

		# Disable requests logging
		urllib3_log = logging.getLogger('urllib3')
		urllib3_log.setLevel(logging.CRITICAL)

		# Initialize logging & format
		logging.basicConfig(
			level = 	logging.DEBUG,
			filename = 	self.log_path,
			format = 	'[%(levelname)s] %(asctime)s : %(message)s',
			datefmt = 	'%I:%M:%S %p'
		)

		self._log('Initialized ' + str(self))

		# Rate limiting logic here
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

		return req

	def request(self, url, params={}):
		time.sleep(self.request_rate * self.request_throttle)

		req = self._request(url=url, params=params)

		if req.status_code >= 400:
			raise RequestError(str(req.status_code))

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

	def _cache(self, data):
		pass

	def _decache(self, name):
		pass

