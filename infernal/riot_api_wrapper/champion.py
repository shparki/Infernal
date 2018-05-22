from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

import pandas as pd


class Champion(object):
	version = const.VERSIONS['champion']


	@classmethod
	def getChampions(cls, session, params={}):
		session._log('Calling getChamps...')
		url = session.build_url(
			url = const.URLS_CHAMPION['all'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session.request(url, params = params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame()
		except Exception as e:
			print(e)
			return pd.DataFrame()

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
		
		try:
			r = session.request(url, params = params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		ds = pd.Series(r)
		
		return ds


