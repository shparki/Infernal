import requests
import traceback
import Constants as const


class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'

class Session(object):

	def __init__ (self, api_key, endpoint='na-old'):
		self.api_key = api_key
		self.endpoint = endpoint

	# Basic requst handler, will be split per-API afer
	def _request(self, url, params={}, headers={}):
		args = {
			'endpoint': 	const.ENDPOINTS[self.endpoint],
			'url':			url,
			'api_key': 		self.api_key,
		}
		req_url = const.URLS_BASE['base'].format_map(
			default_dict(**args))

		req_url = req_url.format_map(
			default_dict(**params))

		req = requests.get(req_url, headers=headers)
		return req.json()

# Methods to access Champion Mastery API
# TODO: add custom headers and organize JSON returns
# TODO: add class and method docstrings
class ChampionMastery(object):
	version = const.VERSIONS['cmastery']

	@classmethod
	def getAllMasteries(cls, session, summoner_id):
		r = session._request(
			url = const.URLS_CMASTER['all'], 
			params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		return r

	@classmethod
	def getMasterByChampion(cls, session, summoner_id, champion_id):
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
		r = session._request(
			url = const.URLS_CMASTER['mastery'],
			params = {
				'version': 			cls.version,
				'summoner_id': 		str(summoner_id)
			}
		)
		return r


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


# Methods to access League API
class League(object):
	version = const.VERSIONS['league']

	@classmethod
	def getChLeague(cls, session, queue):
		r = session._request(
			url = const.URLS_LEAGUE['challenger'],
			params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		return r

	@classmethod
	def getLeague(cls, session, league_id):
		r = session._request(
			url = const.URLS_LEAGUE['by league'],
			params = {
				'version':			cls.version,
				'league_id':		str(league_id)
			}
		)
		return r

	@classmethod
	def getMsLeague(cls, session, queue):
		r = session._request(
			url = const.URLS_LEAGUE['master'],
			params = {
				'version':			cls.version,
				'queue':			str(queue)
			}
		)
		return r

	@classmethod
	def getSummLeague(cls, session, summoner_id):
		r = session._request(
			url = const.URLS_LEAGUE['by summoner'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r


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


# Methods to access Status API
class Status(object):
	version = const.VERSIONS['status']

	@classmethod
	def getStatus(cls, session):
		r = session._request(
			url = const.URLS_STATUS['status'],
			params = {
				'version':			cls.version
			}
		)
		return r


# Methods to access Match API
class Match(object):
	version = const.VERSIONS['match']

	@classmethod
	def getTournMatchIDs(cls, session, tournament_code):
		r = sesion._request(
			url = const.URLS_MATCH['matchID by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getMatchByID(cls, session, match_id):
		r = session._request(
			url = const.URLS_MATCH['by match'],
			params = {
				'version':			cls.version,
				'match_id':			str(match_id)
			}
		)
		return r

	@classmethod
	def getMatchByTourn(cls, session, match_id, tournament_code):
		r = session._request(
			url = const.URLS_MATCH['by tournament'],
			params = {
				'version':			cls.version,
				'match_id':			str(match_id),
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getMatches(cls, session, account_id):
		r = session._request(
			url = const.URLS_MATCH['by account'],
			params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		return r

	@classmethod
	def getRecent(cls, session, account_id):
		r = session._request(
			url = const.URLS_MATCH['recent by account'],
			params = {
				'version':			cls.version,
				'account_id':		str(account_id)
			}
		)
		return r

	@classmethod
	def getTimeline(cls, session, match_id):
		r = session._request(
			url = const.URLS_MATCH['timeline'],
			params = {
				'version':			cls.version,
				'match_id':			str(match_id)
			}
		)
		return r


# Methods to access Spectator API
class Spectator(object):
	version = const.VERSIONS['spectator']

	@classmethod
	def getActive(cls, session, summoner_id):
		r = session._request(
			url = const.URLS_SPECT['active'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r

	@classmethod
	def getFeatured(cls, session):
		r = session._request(
			url = const.URLS_SPECT['featured'],
			params = {
				'version':			cls.version
			}
		)
		return r


# Methods to access Summoner API
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


# Methods to access Third Party Code API
class ThirdPartyCode(object):
	version = const.VERSIONS['tpc']

	@classmethod
	def getTPC(cls, session, summoner_id):
		r = session._request(
			url = const.URLS_TPC['by id'],
			params = {
				'version':			cls.version,
				'summoner_id':		str(summoner_id)
			}
		)
		return r


# Methods to access Tournament Stub API
class TournamentStub(object):
	version = const.VERSIONS['tstub']

	@classmethod
	def getCode(cls, session):
		r = session._request(
			url = const.URLS_TSTUB['codes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getCodesByTourn(cls, session, tournament_code):
		r = session._request(
			url = const.URLS_TSTUB['by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getProviders(cls, session, tournament_code):
		r = session._request(
			url = const.URLS_TSTUB['providers'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournaments(cls, session):
		r = session._request(
			url = const.URLS_TSTUB['tournaments'],
			params = {
				'version':			cls.version
			}
		)
		return r


# Methods to access Tournament API
class Tournament(object):
	version = const.VERSIONS['tournament']

	@classmethod
	def getCodes(cls, session):
		r = session._request(
			url = const.URLS_TOURN['clodes'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournamentDTO(cls, session, tournament_code):
		r = session._request(
			url = const.URLS_TOURN['by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getEvents(cls, session, tournament_code):
		r = session._request(
			url = const.URLS_TOURN['events by tournament'],
			params = {
				'version':			cls.version,
				'tournament_code':	str(tournament_code)
			}
		)
		return r

	@classmethod
	def getProviders(cls, session):
		r = session._request(
			url = const.URLS_TOURN['providers'],
			params = {
				'version':			cls.version
			}
		)
		return r

	@classmethod
	def getTournaments(cls, session):
		r = session._request(
			url = const.URLS_TOURN('tournaments'),
			params = {
				'version': cls.version
			}
		)
		return r








