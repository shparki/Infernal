from ..core import Session
from ..core import constants as const

class ThirdPartyCode(object):
	version = const.VERSIONS['tpc']

	@classmethod
	def getThirdPartyCode(cls, session, summoner_id):
		session._log('Calling getTPC...')
		url = session.build_url(
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
			session._log(req_err, level='error')
			return pd.nan
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.nan
		
		return r