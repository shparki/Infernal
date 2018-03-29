import RiotAPIWrapper
import Constants as const

class Summoner(object):
	version = const.VERSIONS['summoner']

	@classmethod
	def getSummByAccount(cls, session, account_id):
		r = session._request(
			url = const.URLS_SUMMON['by account'],
			params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		return r

	@classmethod
	def getSummByName(cls, session, summoner_name):
		r = session._request(
			url = const.URLS_SUMMON['by name'],
			params = {
				'version':			cls.version,
				'summoner_name':	str(summoner_name)
			}
		)
		return r

	@classmethod
	def getSummByID(cls, session, summoner_id):
		r = session._request(
			url = const.URLS_SUMMON['by id'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r