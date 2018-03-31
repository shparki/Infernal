from .utils import Session
from . import constants as const

# Methods to access Static Data API
# TODO: eventually add a timer to method calls here, with an option to override the timer --> will save api calls
#		turn all of these 'get---' methods into properties, where the getter either retrieves recent data or just pulls from API
class StaticData(object):
	version = const.VERSIONS['sdata']

	@classmethod
	def getChamps(cls, session):
		r = session._request(
			url = const.URLS_SDATA['champions'],
			params = {
				'version': 			cls.version
			}
		)
		return r

	@classmethod
	def getChamp(cls, session, champion_id):
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
		r = session._request(
			url = const.URLS_SDATA['items'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getItem(cls, session, item_id):
		r = session._request(
			url = const.URLS_SDATA['by item'],
			params = {
				'version':			cls.version,
				'item_id':			str(item_id)
			}
		)
		return r

	@classmethod
	def getLangStrings(cls, sesion):
		r = session._request(
			url = const.URLS_SDATA['langauge strings'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getSuppLangs(cls, session):
		r = session._request(
			url = const.URLS_SDATA['supported langauges'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getMaps(cls, session):
		r = session._request(
			url = const.URLS_SDATA['maps'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getMasteries(cls, session):
		r = session._request(
			url = const.URLS_SDATA['masteries'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getMastery(cls, session, mastery_id):
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
		r = session._request(
			url = const.URLS_SDATA['profile icons'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRealms(cls,session):
		r = session._request(
			url = const.URLS_SDATA['realms'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRefPaths(cls, session):
		r = session._request(
			url = const.URLS_SDATA['rune paths'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRefPath(cls, session, path_id):
		r = session._request(
			url = const.URLS_SDATA['by rune path'],
			params = {
				'version':			cls.version,
				'path_id':			str(path_id)
			}
		)
		return r

	@classmethod
	def getRefRunes(cls, session):
		r = session._request(
			url = const.URLS_SDATA['reforged runes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRefRune(cls, session, rune_id):
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
		r = session._request(
			url = const.URLS_SDATA['runes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getRune(cls, session, rune_id):
		r = session._request(
			url = const.URLS_SDATA['by rune'],
			params = {
				'version':			cls.version,
				'rune_id':			str(rune_id)
			}
		)
		return r

	@classmethod
	def getSumSpells(cls, session):
		r = session._request(
			url = const.URLS_SDATA['summoner spells'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getSumSpell(cls, session, spell_id):
		r = session._request(
			url = const.URLS_SDATA['by summoner spell'],
			params = {
				'version':			cls.version,
				'spell_id':			str(spell_id)
			}
		)
		return r

	@classmethod
	def getTarball(cls, session):
		r = session._request(
			url = const.URLS_SDATA['tarball links'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getVersions(cls, session):
		r = session._request(
			url = const.URLS_SDATA['versions'],
			params= {
				'version':			cls.version
			}
		)
		return r