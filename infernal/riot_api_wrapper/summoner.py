from ..core import Session
from ..core import constants as const

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()
		
		data_series = pd.Series(r)
		data_series = data_series.rename(data_series['name'])
		
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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()

		data_series = pd.Series(r)
		data_series = data_series.rename(data_series['name'])
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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()
		
		data_series = pd.Series(r)
		data_series = data_series.rename(data_series['name'])
		return data_series

		