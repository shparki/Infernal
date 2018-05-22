from ..core import Session
from ..core import constants as const

import pandas as pd

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.nan
		except Exception as e:
			print(e)
			return pd.nan
		
		return r