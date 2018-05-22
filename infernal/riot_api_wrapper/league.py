from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

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

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame()
		except Exception as e:
			print(e)
			return pd.DataFrame()


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

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()


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

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame()
		except Exception as e:
			print(e)
			return pd.DataFrame()

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

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		data_series = pd.Series(r[0])
		return data_series



