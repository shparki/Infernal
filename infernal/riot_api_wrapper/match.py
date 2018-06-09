from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

import pandas as pd




class Match(object):
	version = const.VERSIONS['match']

	@classmethod
	def getTournamentMatchIDs(cls, session, tournament_code, params={}):
		session._log('Calling getTournMatchIDs...')
		url = sesion.build_url(
			url = const.URLS_MATCH['matchID by tournament'],
			url_params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
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
	def getMatch(cls, session, match_id, params={}):
		session._log('Calling getMatch...')
		url = session.build_url(
			url = const.URLS_MATCH['by match'],
			url_params = {
				'version':			cls.version,
				'match_id':			str(match_id)
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
	def getMatchByTournament(cls, session, match_id, tournament_code, params={}):
		session._log('Calling getMatchByTournament...')
		url = session.build_url(
			url = const.URLS_MATCH['by tournament'],
			url_params = {
				'version':			cls.version,
				'match_id':			str(match_id),
				'tournament_code':	str(tournament_code)
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
	def getMatches(cls, session, account_id, params={}, meta=False):
		session._log('Calling getMatches...')
		url = session.build_url(
			url = const.URLS_MATCH['by account'],
			url_params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()


		matches = r['matches']
		startindex = r['startIndex']
		endindex = r['endIndex']
		total = r['totalGames']

		matches_frame = pd.DataFrame(matches)
		meta_series = pd.Series([startindex, endindex, total], 
			index=['startIndex', 'endIndex', 'totalGames'])

		if meta:
			return matches_frame, meta_series
		else:
			return matches_frame

	@classmethod
	def getRecent(cls, session, account_id, params={}):
		session._log('Calling getRecent...')
		url = session.build_url(
			url = const.URLS_MATCH['recent by account'],
			url_params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()


		matches = r['matches']
		startindex = r['startIndex']
		endindex = r['endIndex']
		total = r['totalGames']

		matches_frame = pd.DataFrame(matches)
		data_series = pd.Series([matches_frame, startindex, endindex, total],
								index = ['matches', 'startIndex', 'endIndex', 'totalGames'])
		return data_series



	@classmethod
	def getTimeline(cls, session, match_id, params={}):
		session._log('Calling getTimeline...')
		url = session.build_url(
			url = const.URLS_MATCH['timeline'],
			url_params = {
				'version':			cls.version,
				'match_id':			str(match_id)
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


