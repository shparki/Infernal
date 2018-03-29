import RiotAPIWrapper
import Constants as const

class Tournament(object):
	version = const.VERSIONS['tournament']

	@classmethod
	def getCodes(cls, session):
		r = session._request(
			url = const.URLS_TOURN['clodes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournamentDTO(cls, session, tournament_code):
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
		r = session._request(
			url = const.URLS_TOURN['providers'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournaments(cls, session):
		r = session._request(
			url = const.URLS_TOURN('tournaments'),
			params = {
				'version': cls.version
			}
		)
		return r