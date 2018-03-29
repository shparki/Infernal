import RiotAPIWrapper
import Constants as const

# Methods to access Champion API
class Champion(object):
	version = const.VERSIONS['champion']

	@classmethod
	def getChamps(cls, session):
		r = session._request(
			url = const.URLS_CHAMPION['all'],
			params = {
				'version': 			cls.version
			}
		)
		return r

	@classmethod
	def getChamp(cls, session, champion_id):
		r = sesion._request(
			url = const.URLS_CHAMPION['by champion'],
			params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		return r