from .utils import Session
from . import constants as const

import pandas as pd




class ChampionMastery(object):
	version = const.VERSIONS['cmastery']

	@classmethod
	def getAllMasteries(cls, session, summoner_id, params={}):
		session._log('Calling getAllMasteries...')
		url = session._buildurl(
			url = const.URLS_CMASTERY['all'], 
			url_params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		r = session._request(url, params = params)

		data_series = []
		for d in r:
			data_series.append(pd.Series(d))
		data_frame = pd.DataFrame(data_series)
		return data_frame

	@classmethod
	def getMasteryByChampion(cls, session, summoner_id, champion_id, params={}):
		session._log('Calling getMasteryByChampion...')
		url = session._buildurl(
			url = const.URLS_CMASTERY['by champion'], 
			url_params = {
				'version': 			cls.version, 
				'summoner_id': 		str(summoner_id),
				'champion_id': 		str(champion_id)
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getTotalMastery(cls, session, summoner_id, params={}):
		session._log('Calling getTotalMastery...')
		url = session._buildurl(
			url = const.URLS_CMASTERY['mastery'],
			url_params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r, index=['total_mastery'])
		return data_series