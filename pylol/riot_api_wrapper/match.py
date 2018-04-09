from .utils import Session
from . import constants as const

import pandas as pd




class Match(object):
	version = const.VERSIONS['match']

	@classmethod
	def getTournamentMatchIDs(cls, session, tournament_code):
		session._log('Calling getTournMatchIDs...')
		r = sesion._request(
			url = const.URLS_MATCH['matchID by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getMatch(cls, session, match_id, params={}):
		session._log('Calling getMatch...')
		url = session._buildurl(
			url = const.URLS_MATCH['by match'],
			url_params = {
				'version':			cls.version,
				'match_id':			str(match_id)
			}
		)
		r = session._request(url, params=params)
		return r

	@classmethod
	def getMatchByTournament(cls, session, match_id, tournament_code):
		session._log('Calling getMatchByTournament...')
		r = session._request(
			url = const.URLS_MATCH['by tournament'],
			params = {
				'version':			cls.version,
				'match_id':			str(match_id),
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getMatches(cls, session, account_id, params={}):
		session._log('Calling getMatches...')
		url = session._buildurl(
			url = const.URLS_MATCH['by account'],
			url_params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		r = session._request(url, params=params)
		matches = r['matches']
		startindex = r['startIndex']
		endindex = r['endIndex']
		total = r['totalGames']

		matches_frame = pd.DataFrame(matches)
		data_series = pd.Series([matches_frame, startindex, endindex, total],
								index = ['matches', 'startIndex', 'endIndex', 'totalGames'])
		return data_series

	@classmethod
	def getRecent(cls, session, account_id, params={}):
		session._log('Calling getRecent...')
		url = session._buildurl(
			url = const.URLS_MATCH['recent by account'],
			url_params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		r = session._request(url, params=params)
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
		url = session._buildurl(
			url = const.URLS_MATCH['timeline'],
			url_params = {
				'version':			cls.version,
				'match_id':			str(match_id)
			}
		)
		r = session._request(url, params=params)
		return r


