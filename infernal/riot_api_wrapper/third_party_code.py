from ..core import Session
from ..core import constants as const

class ThirdPartyCode(object):
	version = const.VERSIONS['tpc']

	@classmethod
	def getThirdPartyCode(cls, session, summoner_id):
		session._log('Calling getTPC...')
		url = session._buildurl(
			url = const.URLS_TPC['by id'],
			url_params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)

		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.nan
		except Exception as e:
			print(e)
			return pd.nan
		
		return r