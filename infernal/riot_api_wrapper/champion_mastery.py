from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

import pandas as pd




class ChampionMastery(object):
	version = const.VERSIONS['cmastery']

	@classmethod
	def getAllMasteries(cls, session, summoner_id, params={}):
		session._log('Calling getAllMasteries...')
		url = session.build_url(
			url = const.URLS_CMASTERY['all'], 
			url_params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)

		try:
			r = session.request(url, params = params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.DataFrame()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.DataFrame()

		df = pd.DataFrame(r)
		df.lastPlayTime = df.lastPlayTime.astype('datetime64[ms]')
		df = df.set_index('championId')
		df = df.sort_index()

		return df

	@classmethod
	def getMasteryByChampion(cls, session, summoner_id, champion_id, params={}):
		session._log('Calling getMasteryByChampion...')
		url = session.build_url(
			url = const.URLS_CMASTERY['by champion'], 
			url_params = {
				'version': 			cls.version, 
				'summoner_id': 		str(summoner_id),
				'champion_id': 		str(champion_id)
			}
		)

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()

		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getTotalMastery(cls, session, summoner_id, params={}):
		session._log('Calling getTotalMastery...')
		url = session.build_url(
			url = const.URLS_CMASTERY['mastery'],
			url_params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		
		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.nan
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.nan

		return r



