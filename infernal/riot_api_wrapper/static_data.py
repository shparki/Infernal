from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

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

		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		data_entries = r.pop('data')
		data_entries = pd.DataFrame(data_entries).transpose()
		data_meta = pd.Series(r)
		return data_entries, data_meta



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

		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()
		
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

		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame(), pd.Series()
		except Exception as e:
			print(e)
			return pd.DataFrame(), pd.Series()

		data_entries = r.pop('data')
		data_entries = pd.DataFrame(data_entries).transpose()
		data_meta = pd.Series(r)
		return data_entries, data_meta

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		data_series = pd.Series(r)
		return data_series


	@classmethod
	def getLanguageStrings(cls, session, params={}):
		session._log('Calling getLangStrings...')
		url = session._buildurl(
			url = const.URLS_SDATA['language strings'],
			url_params = {
				'version':			cls.version
			}
		)
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame(), pd.Series()
		except Exception as e:
			print(e)
			return pd.DataFrame(), pd.Series()

		data_entries = r.pop('data')
		data_entries = pd.Series(data_entries)
		data_meta = pd.Series(r)
		return data_entries, data_meta

	@classmethod
	def getSupportedLanguages(cls, session, params={}):
		session._log('Calling getSuppLangs...')
		url = session._buildurl(
			url = const.URLS_SDATA['supported languages'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		data = pd.Series(r)
		return data

	@classmethod
	def getMaps(cls, session, params={}):
		session._log('Calling getMaps...')
		url = session._buildurl(
			url = const.URLS_SDATA['maps'],
			url_params = {
				'version':			cls.version
			}
		)
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame(), pd.Series()
		except Exception as e:
			print(e)
			return pd.DataFrame(), pd.Series()

		images = {}
		data_entries = r.pop('data')
		for key, value in data_entries.items():
			images[key] = value['image']
			value.pop('image')
		image_frame = pd.DataFrame(images).transpose()
		image_frame = image_frame.rename(columns={
											'full': 'image_full',
											'group': 'image_group',
											'h': 'image_h',
											'sprite': 'image_sprite',
											'w': 'image_w',
											'x': 'image_x',
											'y': 'image_y'
										})
		data_entries = pd.DataFrame(data_entries).transpose()
		data_entries = pd.concat([data_entries, image_frame], axis=1)
		data_meta = pd.Series(r)
		return data_entries, data_meta

	@classmethod
	def getMasteries(cls, session, params={}):
		session._log('Calling getMaps...')
		url = session._buildurl(
			url = const.URLS_SDATA['masteries'],
			url_params = {
				'version':			cls.version
			}
		)
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame(), pd.Series()
		except Exception as e:
			print(e)
			return pd.DataFrame(), pd.Series()
		
		data_entries = r.pop('data')
		data_entries = pd.DataFrame(data_entries).transpose()
		data_meta = pd.Series(r)
		return data_entries, data_meta

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame(), pd.Series()
		except Exception as e:
			print(e)
			return pd.DataFrame(), pd.Series()
		
		images = {}
		data_entries = r.pop('data')
		for key, value in data_entries.items():
			images[key] = value['image']
			value.pop('image')
		images_frame = pd.DataFrame(images).transpose()
		images_frame = images_frame.rename(columns={
											'full': 'image_full',
											'group': 'image_group',
											'h': 'image_h',
											'sprite': 'image_sprite',
											'w': 'image_w',
											'x': 'image_x',
											'y': 'image_y'
										})
		data_entries = pd.DataFrame(data_entries).transpose()
		data_entries = pd.concat([data_entries, images_frame], axis=1)
		data_entries = data_entries.set_index('id')
		data_meta = pd.Series(r)
		return data_entries, data_meta

	@classmethod
	def getRealms(cls,session, params={}):
		session._log('Calling getRealms...')
		url = session._buildurl(
			url = const.URLS_SDATA['realms'],
			url_params = {
				'version':			cls.version
			}
		)
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		n = r['n']
		n = pd.Series(n)
		r.pop('n')
		data_series = pd.Series(r)
		data_series = pd.concat([data_series, n])
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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame()
		except Exception as e:
			print(e)
			return pd.DataFrame()

		data_frame = pd.DataFrame(r)
		return data_frame

	@classmethod
	def getReforgedPath(cls, session, path_id):
		session._log('Calling getRefPaths...')
		url = session._buildurl(
			url = const.URLS_SDATA['by rune path'],
			url_params = {
				'version':			cls.version,
				'path_id':			str(path_id)
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

	@classmethod
	def getReforgedRunes(cls, session):
		session._log('Calling getRefRunes...')
		url = session._buildurl(
			url = const.URLS_SDATA['reforged runes'],
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

	@classmethod
	def getReforgedRune(cls, session, rune_id):
		session._log('Calling getRefRunes...')
		url = session._buildurl(
			url = const.URLS_SDATA['by reforged rune'],
			url_params = {
				'version':			cls.version,
				'rune_id':			str(rune_id)
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

	@classmethod
	def getRunes(cls, session):
		session._log('Calling getRunes...')
		url = session._buildurl(
			url = const.URLS_SDATA['runes'],
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

	@classmethod
	def getRune(cls, session, rune_id):
		session._log('Calling getRune...')
		url = session._buildurl(
			url = const.URLS_SDATA['by rune'],
			url_params = {
				'version':			cls.version,
				'rune_id':			str(rune_id)
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

	@classmethod
	def getSummonerSpells(cls, session, params={}):
		session._log('Calling getSumSpells...')
		url = session._buildurl(
			url = const.URLS_SDATA['summoner spells'],
			url_params = {
				'version':			cls.version
			}
		)
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.DataFrame()
		except Exception as e:
			print(e)
			return pd.DataFrame()

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.nan
		except Exception as e:
			print(e)
			return pd.nan

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
		
		try:
			r = session._request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			return pd.Series()
		except Exception as e:
			print(e)
			return pd.Series()

		data_series = pd.Series(r)
		return data_series





