from .utils import Session
from . import constants as const

import pandas as pd




class League(object):
	version = const.VERSIONS['league']

	@classmethod
	def getChallengerLeague(cls, session, queue, params={}):
		session._log('Calling getChLeague...')
		url = session.build_url(
			url = const.URLS_LEAGUE['challenger'],
			url_params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		r = session.request(url, params=params)
		df = pd.DataFrame(r['entries'])

		r.pop('entries')
		data_meta = pd.Series(r)

		for key, value in data_meta.iteritems():
			df[key] = value

		return df

	@classmethod
	def getLeague(cls, session, league_id, params={}):
		session._log('Calling getLeague...')
		url = session.build_url(
			url = const.URLS_LEAGUE['by league'],
			url_params = {
				'version':			cls.version,
				'league_id':		str(league_id)
			}
		)
		r = session.request(url, params=params)
		df = pd.DataFrame(r['entries'])

		r.pop('entries')
		data_meta = pd.Series(r)

		for key, value in data_meta.iteritems():
			df[key] = value

		return df


	@classmethod
	def getMasterLeague(cls, session, queue, params={}):
		session._log('Calling getMsLeague...')
		url = session.build_url(
			url = const.URLS_LEAGUE['master'],
			url_params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		r = session.request(url, params=params)
		df = pd.DataFrame(r['entries'])

		r.pop('entries')
		data_meta = pd.Series(r)

		for key, value in data_meta.iteritems():
			df[key] = value

		return df

	@classmethod
	def getSummonerLeague(cls, session, summoner_id, params={}):
		session._log('Calling getSummLeague...')
		url = session.build_url(
			url = const.URLS_LEAGUE['by summoner'],
			url_params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		r = session.request(url, params=params)

		data_series = pd.Series(r[0])
		return data_series



