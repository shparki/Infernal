from .utils import Session
from . import constants as const

# Methods to access Static Data API
# TODO: eventually add a timer to method calls here, with an option to override the timer --> will save api calls
#		turn all of these 'get---' methods into properties, where the getter either retrieves recent data or just pulls from API
class StaticData(object):
	version = const.VERSIONS['sdata']

	@classmethod
	def getChampions(cls, session):
		session._log('Calling getChamps...')
		r = session._request(
			url = const.URLS_SDATA['champions'],
			params = {
				'version': 			cls.version
			}
		)
		return r

	@classmethod
	def getChampion(cls, session, champion_id):
		session._log('Calling getChamp...')
		r = session._request(
			url = const.URLS_SDATA['by champion'],
			params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		return r

	@classmethod
	def getItems(cls, session):
		session._log('Calling getItems...')
		r = session._request(
			url = const.URLS_SDATA['items'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getItem(cls, session, item_id):
		session._log('Calling getItem...')
		r = session._request(
			url = const.URLS_SDATA['by item'],
			params = {
				'version':			cls.version,
				'item_id':			str(item_id)
			}
		)
		return r

	@classmethod
	def getLanguageStrings(cls, sesion):
		session._log('Calling getLangStrings...')
		r = session._request(
			url = const.URLS_SDATA['langauge strings'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getSupportedLanguages(cls, session):
		session._log('Calling getSuppLangs...')
		r = session._request(
			url = const.URLS_SDATA['supported langauges'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getMaps(cls, session):
		session._log('Calling getMaps...')
		r = session._request(
			url = const.URLS_SDATA['maps'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getMasteries(cls, session):
		session._log('Calling getMaps...')
		r = session._request(
			url = const.URLS_SDATA['masteries'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getMastery(cls, session, mastery_id):
		session._log('Calling getMastery...')
		r = session._request(
			url = const.URLS_SDATA['by mastery'],
			params = {
				'version':			cls.version,
				'mastery_id':		str(mastery_id)
			}
		)
		return r

	@classmethod
	def getIcons(cls, session):
		session._log('Calling getIcons...')
		r = session._request(
			url = const.URLS_SDATA['profile icons'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRealms(cls,session):
		session._log('Calling getRealms...')
		r = session._request(
			url = const.URLS_SDATA['realms'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getReforgedPaths(cls, session):
		session._log('Calling getRefPaths...')
		r = session._request(
			url = const.URLS_SDATA['rune paths'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getReforgedPath(cls, session, path_id):
		session._log('Calling getRefPaths...')
		r = session._request(
			url = const.URLS_SDATA['by rune path'],
			params = {
				'version':			cls.version,
				'path_id':			str(path_id)
			}
		)
		return r

	@classmethod
	def getReforgedRunes(cls, session):
		session._log('Calling getRefRunes...')
		r = session._request(
			url = const.URLS_SDATA['reforged runes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getReforgedRune(cls, session, rune_id):
		session._log('Calling getRefRunes...')
		r = session._request(
			url = const.URLS_SDATA['by reforged rune'],
			params = {
				'version':			cls.version,
				'rune_id':			str(rune_id)
			}
		)
		return r

	@classmethod
	def getRunes(cls, session):
		session._log('Calling getRunes...')
		r = session._request(
			url = const.URLS_SDATA['runes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRune(cls, session, rune_id):
		session._log('Calling getRune...')
		r = session._request(
			url = const.URLS_SDATA['by rune'],
			params = {
				'version':			cls.version,
				'rune_id':			str(rune_id)
			}
		)
		return r

	@classmethod
	def getSummonerSpells(cls, session):
		session._log('Calling getSumSpells...')
		r = session._request(
			url = const.URLS_SDATA['summoner spells'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getSummonerSpell(cls, session, spell_id):
		session._log('Calling getSumSpells...')
		r = session._request(
			url = const.URLS_SDATA['by summoner spell'],
			params = {
				'version':			cls.version,
				'spell_id':			str(spell_id)
			}
		)
		return r

	@classmethod
	def getTarballLinks(cls, session):
		session._log('Calling getTarball...')
		r = session._request(
			url = const.URLS_SDATA['tarball links'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getVersions(cls, session):
		session._log('Calling getVersions...')
		r = session._request(
			url = const.URLS_SDATA['versions'],
			params= {
				'version':			cls.version
			}
		)
		return r