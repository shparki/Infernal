from ..core import Session
from ..core import constants as const

class Tournament(object):
	version = const.VERSIONS['tournament']

	@classmethod
	def getCodes(cls, session):
		session._log('Calling getCodes...')
		url = session.build_url(
			url = const.URLS_TOURN['clodes'],
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
	def getTournamentDTO(cls, session, tournament_code):
		session._log('Calling getTournamentDTO...')
		url = session.build_url(
			url = const.URLS_TOURN['by tournament'],
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
	def getEvents(cls, session, tournament_code):
		session._log('Calling getEvents...')
		url = session.build_url(
			url = const.URLS_TOURN['events by tournament'],
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
	def getProviders(cls, session):
		session._log('Calling getProviders...')
		url = session.build_url(
			url = const.URLS_TOURN['providers'],
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
		session._log('getTournaments...')
		url = session.build_url(
			url = const.URLS_TOURN('tournaments'),
			url_params = {
				'version': cls.version
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





