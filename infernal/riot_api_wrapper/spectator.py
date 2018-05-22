from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

import pandas as pd



class Spectator(object):
	version = const.VERSIONS['spectator']

	@classmethod
	def getActive(cls, session, summoner_id, params={}):
		session._log('Calling getActive...')
		url = session.build_url(
			url = const.URLS_SPECT['active'],
			url_params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
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

	@classmethod
	def getFeatured(cls, session, params={}):
		session._log('Calling getFeatured...')
		url = session.build_url(
			url = const.URLS_SPECT['featured'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.DataFrame()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.DataFrame()

		game_list = r.pop('gameList')
		data_meta = pd.Series(r)

		for parti in game_list:
			parti['bannedChampions'] = pd.Series(parti['bannedChampions'])
			parti['observers'] = pd.Series(parti['observers'])
			parti['participants'] = pd.DataFrame(parti['participants'])
		data_entries = pd.DataFrame(game_list)

		for key, value in data_meta.iteritems():
			data_entries[key] = value

		return data_entries
