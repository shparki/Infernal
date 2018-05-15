from .utils import Session
from . import constants as const

import pandas as pd



class Spectator(object):
	version = const.VERSIONS['spectator']

	@classmethod
	def getActive(cls, session, summoner_id, params={}):
		session._log('Calling getActive...')
		url = session._buildurl(
			url = const.URLS_SPECT['active'],
			url_params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		r = session._request(url, params=params)
		return r

	@classmethod
	def getFeatured(cls, session, params={}):
		session._log('Calling getFeatured...')
		url = session._buildurl(
			url = const.URLS_SPECT['featured'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)
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
