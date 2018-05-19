from .utils import Session
from . import constants as const

import pandas as pd


class Champion(object):
	version = const.VERSIONS['champion']


	@classmethod
	def getChampions(cls, session, params={}, meta=False):
		session._log('Calling getChamps...')
		url = session.build_url(
			url = const.URLS_CHAMPION['all'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session.request(url, params = params)

		data = r['champions']
		df = pd.DataFrame(data)
		df = df.set_index('id')
		df = df.sort_index()

		return df


	@classmethod
	def getChampion(cls, session, champion_id, params={}):
		session._log('calling getChamp...')
		url = session.build_url(
			url = const.URLS_CHAMPION['by champion'],
			url_params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		r = session.request(url, params = params)

		ds = pd.Series(r)
		
		return ds


