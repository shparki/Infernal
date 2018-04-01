from .utils import Session
from . import constants as const

class League(object):
	version = const.VERSIONS['league']

	@classmethod
	def getChLeague(cls, session, queue):
		session._log('Calling getChLeague...')
		r = session._request(
			url = const.URLS_LEAGUE['challenger'],
			params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		return r

	@classmethod
	def getLeague(cls, session, league_id):
		session._log('Calling getLeague...')
		r = session._request(
			url = const.URLS_LEAGUE['by league'],
			params = {
				'version':			cls.version,
				'league_id':		str(league_id)
			}
		)
		return r

	@classmethod
	def getMsLeague(cls, session, queue):
		session._log('Calling getMsLeague...')
		r = session._request(
			url = const.URLS_LEAGUE['master'],
			params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		return r

	@classmethod
	def getSummLeague(cls, session, summoner_id):
		session._log('Calling getSummLeague...')
		r = session._request(
			url = const.URLS_LEAGUE['by summoner'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r