from .utils import Session
from . import constants as const

# Methods to access Status API
class Status(object):
	version = const.VERSIONS['status']

	@classmethod
	def getStatus(cls, session, params={}):
		session._log('Calling getStatus...')
		url = session._buildurl(
			url = const.URLS_STATUS['status'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)
		return r