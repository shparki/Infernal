import utils
from utils import const

class Match(object):
	version = const.VERSIONS['match']

	@classmethod
	def getTournMatchIDs(cls, session, tournament_code):
		r = sesion._request(
			url = const.URLS_MATCH['matchID by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getMatchByID(cls, session, match_id):
		r = session._request(
			url = const.URLS_MATCH['by match'],
			params = {
				'version':			cls.version,
				'match_id':			str(match_id)
			}
		)
		return r

	@classmethod
	def getMatchByTourn(cls, session, match_id, tournament_code):
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
	def getMatches(cls, session, account_id):
		r = session._request(
			url = const.URLS_MATCH['by account'],
			params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		return r

	@classmethod
	def getRecent(cls, session, account_id):
		r = session._request(
			url = const.URLS_MATCH['recent by account'],
			params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		return r

	@classmethod
	def getTimeline(cls, session, match_id):
		r = session._request(
			url = const.URLS_MATCH['timeline'],
			params = {
				'version':			cls.version,
				'match_id':			str(match_id)
			}
		)
		return r