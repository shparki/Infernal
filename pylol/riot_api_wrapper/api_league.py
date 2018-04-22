from .utils import Session
from . import constants as const

import pandas as pd




class League(object):
	version = const.VERSIONS['league']

	@classmethod
	def getChallengerLeague(cls, session, queue, params={}):
		session._log('Calling getChLeague...')
		url = session._buildurl(
			url = const.URLS_LEAGUE['challenger'],
			url_params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		r = session._request(url, params=params)
		data_entries = pd.DataFrame(r['entries'])

		r.pop('entries')
		data_meta = pd.Series(r)
		return data_entries, data_meta

	@classmethod
	def getLeague(cls, session, league_id, params={}):
		session._log('Calling getLeague...')
		url = session._buildurl(
			url = const.URLS_LEAGUE['by league'],
			url_params = {
				'version':			cls.version,
				'league_id':		str(league_id)
			}
		)
		r = session._request(url, params=params)
		data_entries = pd.DataFrame(r['entries'])

		r.pop('entries')
		data_meta = pd.Series(r)
		return data_entries, data_meta


	@classmethod
	def getMasterLeague(cls, session, queue, params={}):
		session._log('Calling getMsLeague...')
		url = session._buildurl(
			url = const.URLS_LEAGUE['master'],
			url_params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		r = session._request(url, params=params)
		data_entries = pd.DataFrame(r['entries'])

		r.pop('entries')
		data_meta = pd.Series(r)
		return data_entries, data_meta

	@classmethod
	def getSummonerLeague(cls, session, summoner_id, params={}):
		session._log('Calling getSummLeague...')
		url = session._buildurl(
			url = const.URLS_LEAGUE['by summoner'],
			url_params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r[0])
		return data_series



