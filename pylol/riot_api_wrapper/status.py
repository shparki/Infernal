from .utils import Session
from . import constants as const

# Methods to access Status API
class Status(object):
	version = const.VERSIONS['status']

	@classmethod
	def getStatus(cls, session):
		r = session._request(
			url = const.URLS_STATUS['status'],
			params = {
				'version':			cls.version
			}
		)
		return r