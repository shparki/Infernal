from .utils import Session
from . import constants as const

class Spectator(object):
	version = const.VERSIONS['spectator']

	@classmethod
	def getActive(cls, session, summoner_id):
		session._log('Calling getActive...')
		r = session._request(
			url = const.URLS_SPECT['active'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r

	@classmethod
	def getFeatured(cls, session):
		session._log('Calling getFeatured...')
		r = session._request(
			url = const.URLS_SPECT['featured'],
			params = {
				'version':			cls.version
			}
		)
		return r