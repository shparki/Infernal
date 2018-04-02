from .utils import Session
from . import constants as const

class Summoner(object):
	version = const.VERSIONS['summoner']

	@classmethod
	def getSummonerByAccount(cls, session, account_id):
		session._log('Calling getSummByAccount...')
		r = session._request(
			url = const.URLS_SUMMON['by account'],
			params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		return r

	@classmethod
	def getSummonerByName(cls, session, summoner_name):
		session._log('Calling getSummByName...')
		r = session._request(
			url = const.URLS_SUMMON['by name'],
			params = {
				'version':			cls.version,
				'summoner_name':	str(summoner_name)
			}
		)
		return r

	@classmethod
	def getSummonerByID(cls, session, summoner_id):
		session._log('Calling getSummByID...')
		r = session._request(
			url = const.URLS_SUMMON['by id'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r