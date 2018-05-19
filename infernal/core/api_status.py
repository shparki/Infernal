from .utils import Session
from . import constants as const

# Methods to access Status API
class Status(object):
	version = const.VERSIONS['status']

	@classmethod
	def getStatus(cls, session, params={}):
		session._log('Calling getStatus...')
		url = session.build_url(
			url = const.URLS_STATUS['status'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session.request(url, params=params)
		return r