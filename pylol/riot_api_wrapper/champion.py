from .utils import Session
from . import constants as const

# Methods to access Champion API
class Champion(object):
	version = const.VERSIONS['champion']


	@classmethod
	def getChampions(cls, session):
		session._log('Calling getChamps...')
		r = session._request(
			url = const.URLS_CHAMPION['all'],
			params = {
				'version': 			cls.version
			}
		)
		return r

	@classmethod
	def getChampion(cls, session, champion_id):
		session._log('calling getChamp...')
		r = sesion._request(
			url = const.URLS_CHAMPION['by champion'],
			params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		return r