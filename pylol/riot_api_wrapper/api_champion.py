from .utils import Session
from . import constants as const

import pandas as pd




class Champion(object):
	version = const.VERSIONS['champion']


	@classmethod
	def getChampions(cls, session, params={}):
		session._log('Calling getChamps...')
		url = session._buildurl(
			url = const.URLS_CHAMPION['all'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params = params)

		data = r['champions']
		data_series = []
		for d in data:
			data_series.append(pd.Series(d))
		data_frame = pd.DataFrame(data_series)
		return data_frame


	@classmethod
	def getChampion(cls, session, champion_id, params={}):
		session._log('calling getChamp...')
		url = session._buildurl(
			url = const.URLS_CHAMPION['by champion'],
			url_params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		r = session._request(url, params = params)

		data_series = pd.Series(r)
		return data_series