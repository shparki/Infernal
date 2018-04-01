from .utils import Session
from . import constants as const

class TournamentStub(object):
	version = const.VERSIONS['tstub']

	@classmethod
	def getCode(cls, session):
		session._log('Calling getCode...')
		r = session._request(
			url = const.URLS_TSTUB['codes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getCodesByTourn(cls, session, tournament_code):
		session._log('Calling getCodesByTourn...')
		r = session._request(
			url = const.URLS_TSTUB['by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getProviders(cls, session, tournament_code):
		session._log('Calling getProviders...')
		r = session._request(
			url = const.URLS_TSTUB['providers'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournaments(cls, session):
		session._log('Calling getTournaments...')
		r = session._request(
			url = const.URLS_TSTUB['tournaments'],
			params = {
				'version':			cls.version
			}
		)
		return r