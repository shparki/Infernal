from . import constants as const
from .infernal_error import RequestError
from .utils import default_dict

import requests
import datetime
import os
# import logging
import csv
import json

import pandas as pd
import queue
import time



class RiotAuth(requests.auth.AuthBase):
	''' Basic authenticator, extending the Requests AuthBase to be used with 
	riot header requests. Simply adds the 'X-Riot_Token' headers key with
	the definied api_key to the riot api call
	'''
	def __init__(self, api_key):
		self.api_key = api_key

	def __call__(self, r):
		r.headers['X-Riot-Token'] = self.api_key

class Session(object):

	def __init__(self, api_key, endpoint='na-old', name=None):
		
		# save the api_key associated with this session; each session should 
		# have their own api key
		self.api_key = api_key

		# build the default authenticator for the session:
		self.auth = RiotAuth(self.api_key)

		# Check if the endpoint is valid; if so then use, otherwise use the
		# default region
		self.endpoint = 'na-old'
		if endpoint in const.ENDPOINTS.keys():
			self.endpoint = endpoint

		# uid (unique-id) functions as a unique identifier for each session
		# based off the time and date of the created session
		self.uid = datetime.datetime.today().strftime('%y%m%d_%H%M%S')

		# set the name for the session; if unnamed, the session name
		# will default to the uid
		self.name = name
		if self.name is None:
			self.name = self.uid

		# set the location for the data/logs file paths; will default to 
		# /{name}/data & /{name}/logs. cwd is current working directory.
		# if directories don't exist, then create them
		cwd = str(os.getcwd())
		self.parent_dirpath = '{}/{}'.format(cwd, self.name)
		if not os.path.exists(self.parent_dirpath):
			os.mkdir(self.parent_dirpath)

		self.data_dirpath = '{}/data'.format(self.parent_dirpath, self.name)
		if not os.path.exists(self.data_dirpath):
			os.mkdir(self.data_dirpath)

		self.logs_dirpath = '{}/logs'.format(self.parent_dirpath, self.name)
		if not os.path.exists(self.logs_dirpath):
			os.mkdir(self.logs_dirpath)

		# Add logging here...

		# Rate limiting logic here
		self.request_rate = 0.5
		self.request_throttle = 0.8

	def __str__(self):
		return 'session_{} | uid: {}'.format(self.name, self.uid)


	def request(self, url, url_params, params={}):
		args = {
			'endpoint': const.ENDPOINTS[self.region],
			'url': url
		}




