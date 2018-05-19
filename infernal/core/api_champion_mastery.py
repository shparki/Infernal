from .utils import Session
from . import constants as const

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
		r = session.request(url, params = params)

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
		r = session.request(url, params=params)

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
		r = session.request(url, params=params)

		return r