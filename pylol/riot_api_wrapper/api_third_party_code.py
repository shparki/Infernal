from .utils import Session
from . import constants as const

class ThirdPartyCode(object):
	version = const.VERSIONS['tpc']

	@classmethod
	def getThirdPartyCode(cls, session, summoner_id):
		session._log('Calling getTPC...')
		r = session._request(
			url = const.URLS_TPC['by id'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r