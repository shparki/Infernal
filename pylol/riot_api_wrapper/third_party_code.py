import utils
from utils import const

class ThirdPartyCode(object):
	version = const.VERSIONS['tpc']

	@classmethod
	def getTPC(cls, session, summoner_id):
		r = session._request(
			url = const.URLS_TPC['by id'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r