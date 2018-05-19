from .utils import Session
from . import constants as const

import pandas as pd




class Summoner(object):
	version = const.VERSIONS['summoner']

	@classmethod
	def getSummonerByAccount(cls, session, account_id, params={}):
		session._log('Calling getSummByAccount...')
		url = session.build_url(
			url = const.URLS_SUMMON['by account'],
			url_params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		r = session.request(url, params=params)
		
		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getSummonerByName(cls, session, summoner_name, params={}):
		session._log('Calling getSummByName...')
		url = session.build_url(
			url = const.URLS_SUMMON['by name'],
			url_params = {
				'version':			cls.version,
				'summoner_name':	str(summoner_name)
			}
		)
		r = session.request(url, params=params)

		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getSummonerByID(cls, session, summoner_id, params={}):
		session._log('Calling getSummByID...')
		url = session.build_url(
			url = const.URLS_SUMMON['by id'],
			url_params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		r = session.request(url, params=params)
		
		data_series = pd.Series(r)
		return data_series