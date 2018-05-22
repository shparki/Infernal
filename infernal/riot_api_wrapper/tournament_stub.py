from ..core import Session
from ..core import constants as const

class TournamentStub(object):
	version = const.VERSIONS['tstub']

	@classmethod
	def getCode(cls, session):
		session._log('Calling getCode...')
		url = session._buildurl(
			url = const.URLS_TSTUB['codes'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session._request(url, params=params)
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
	def getCodesByTournament(cls, session, tournament_code):
		session._log('Calling getCodesByTourn...')
		url = session._buildurl(
			url = const.URLS_TSTUB['by tournament'],
			url_params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)

		try:
			r = session._request(url, params=params)
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
	def getProviders(cls, session, tournament_code):
		session._log('Calling getProviders...')
		url = session._buildurl(
			url = const.URLS_TSTUB['providers'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session._request(url, params=params)
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
	def getTournaments(cls, session):
		session._log('Calling getTournaments...')
		url = session._buildurl(
			url = const.URLS_TSTUB['tournaments'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.nan
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.nan

		return r

		