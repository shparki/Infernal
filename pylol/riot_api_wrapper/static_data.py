from .utils import Session
from . import constants as const

import pandas as pd

# Methods to access Static Data API
# TODO: eventually add a timer to method calls here, with an option to override the timer --> will save api calls
#		turn all of these 'get---' methods into properties, where the getter either retrieves recent data or just pulls from API
class StaticData(object):
	version = const.VERSIONS['sdata']

	@classmethod
	def getChampions(cls, session, params={}):
		session._log('Calling getChamps...')
		url = session._buildurl(
			url = const.URLS_SDATA['champions'],
			url_params = {
				'version': 			cls.version
			}
		)
		r = session._request(url, params=params)

		data = r['data']
		data_frame = pd.DataFrame(data)
		return data_frame.transpose()



	@classmethod
	def getChampion(cls, session, champion_id, params={}):
		session._log('Calling getChamp...')
		url = session._buildurl(
			url = const.URLS_SDATA['by champion'],
			url_params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		r = session._request(url, params=params)
		
		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getItems(cls, session, params={}):
		session._log('Calling getItems...')
		url = session._buildurl(
			url = const.URLS_SDATA['items'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)

		data = r['data']
		data_frame = pd.DataFrame(data)
		return data_frame.transpose()

	@classmethod
	def getItem(cls, session, item_id, params={}):
		session._log('Calling getItem...')
		url = session._buildurl(
			url = const.URLS_SDATA['by item'],
			url_params = {
				'version':			cls.version,
				'item_id':			str(item_id)
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r)
		return data_series

# TODO: FIX THIS FOR ENCODING UTF-8
	@classmethod
	def getLanguageStrings(cls, session, params={}):
		session._log('Calling getLangStrings...')
		url = session._buildurl(
			url = const.URLS_SDATA['language strings'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)

		data = r['data']
		data_series = []
		for d in data:
			series = pd.Series(d)
			series.str.encode('utf-8', errors='ignore')
			data_series.append(series)
		data_frame = pd.DataFrame(data_series)
		return data_frame

# TODO: FIX THIS FOR ENCODING UTF-8
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
	def getMaps(cls, session, params={}):
		session._log('Calling getMaps...')
		url = session._buildurl(
			url = const.URLS_SDATA['maps'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)

		data = r['data']
		data_frame = pd.DataFrame(data)
		return data_frame.transpose()

	@classmethod
	def getMasteries(cls, session, params={}):
		session._log('Calling getMaps...')
		url = session._buildurl(
			url = const.URLS_SDATA['masteries'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)
		
		data = r['data']
		data_frame = pd.DataFrame(data)
		return data_frame.transpose()

	@classmethod
	def getMastery(cls, session, mastery_id, params={}):
		session._log('Calling getMastery...')
		url = session._buildurl(
			url = const.URLS_SDATA['by mastery'],
			url_params = {
				'version':			cls.version,
				'mastery_id':		str(mastery_id)
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getIcons(cls, session, params={}):
		session._log('Calling getIcons...')
		url = session._buildurl(
			url = const.URLS_SDATA['profile icons'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)
		
		data = r['data']
		data_frame = pd.DataFrame(data)
		return data_frame.transpose()

	@classmethod
	def getRealms(cls,session, params={}):
		session._log('Calling getRealms...')
		url = session._buildurl(
			url = const.URLS_SDATA['realms'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)
		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getReforgedPaths(cls, session, params={}):
		session._log('Calling getRefPaths...')
		url = session._buildurl(
			url = const.URLS_SDATA['rune paths'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)

		data_frame = pd.DataFrame(r)
		return data_frame

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
	def getSummonerSpells(cls, session, params={}):
		session._log('Calling getSumSpells...')
		url = session._buildurl(
			url = const.URLS_SDATA['summoner spells'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)

		data = r['data']
		data_frame = pd.DataFrame(data)
		return data_frame.transpose()


	@classmethod
	def getSummonerSpell(cls, session, spell_id, params={}):
		session._log('Calling getSumSpells...')
		url = session._buildurl(
			url = const.URLS_SDATA['by summoner spell'],
			url_params = {
				'version':			cls.version,
				'spell_id':			str(spell_id)
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r)
		return data_series

	@classmethod
	def getTarballLinks(cls, session, params={}):
		session._log('Calling getTarball...')
		url = session._buildurl(
			url = const.URLS_SDATA['tarball links'],
			url_params = {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)
		return r

	@classmethod
	def getVersions(cls, session, params={}):
		session._log('Calling getVersions...')
		url = session._buildurl(
			url = const.URLS_SDATA['versions'],
			url_params= {
				'version':			cls.version
			}
		)
		r = session._request(url, params=params)

		data_series = pd.Series(r)
		return data_series





