from .utils import Session
from . import constants as const

class Tournament(object):
	version = const.VERSIONS['tournament']

	@classmethod
	def getCodes(cls, session):
		session._log('Calling getCodes...')
		r = session._request(
			url = const.URLS_TOURN['clodes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournamentDTO(cls, session, tournament_code):
		session._log('Calling getTournamentDTO...')
		r = session._request(
			url = const.URLS_TOURN['by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getEvents(cls, session, tournament_code):
		session._log('Calling getEvents...')
		r = session._request(
			url = const.URLS_TOURN['events by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getProviders(cls, session):
		session._log('Calling getProviders...')
		r = session._request(
			url = const.URLS_TOURN['providers'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournaments(cls, session):
		session._log('getTournaments...')
		r = session._request(
			url = const.URLS_TOURN('tournaments'),
			params = {
				'version': cls.version
			}
		)
		return r