from .utils import Session
from . import constants as const

class ChampionMastery(object):
	version = const.VERSIONS['cmastery']

	@classmethod
	def getAllMasteries(cls, session, summoner_id):
		session._log('Calling getAllMasteries...')
		r = session._request(
			url = const.URLS_CMASTER['all'], 
			params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		return r

	@classmethod
	def getMasteryByChampion(cls, session, summoner_id, champion_id):
		session._log('Calling getMasteryByChampion...')
		r = session._request(
			url = const.URLS_CMASTER['by champion'], 
			params = {
				'version': 			cls.version, 
				'summoner_id': 		str(summoner_id),
				'champion_id': 		str(champion_id)
			}
		)
		return r

	@classmethod
	def getTotalMastery(cls, session, summoner_id):
		session._log('Calling getTotalMastery...')
		r = session._request(
			url = const.URLS_CMASTER['mastery'],
			params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		return r