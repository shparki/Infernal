from ..core import Session
from ..core import constants as const
from ..core.infernal_error import RequestError

import pandas as pd


class Champion(object):
	version = const.VERSIONS['champion']


	@classmethod
	def getChampions(cls, session, **params):
		"""Fetches all Champions
		
		Fetches information regarding all champions in League of Legends.
		Descriptions are referenced from https://developer.riotgames.com/

		Args:
		    session: (expects infernal.core.utils.Session) Session object used
		    	to query the Riot API
		    params: (expects dict) dictionary object used to refine query
		    	results from the Riot API.
		    	params recognizes the following dictionary keys & value types:
		    	- freeToPlay: (expects boolean) Optional filter param to 
		    		retrieve only free to play champions

		Returns:
		    df: pd.DataFrame object with the following columns:
		    	- rankedPlayEnabled: (boolean values) Ranked play enabled flag. 
		    	- botEnabled: (boolean values) Bot enabled flag (for custom
		    		games).
		    	- botMmEnabled: (boolean values) Bot Match Made enabled flag
		    		(for Co-op vs. AI games).
		    	- active: (boolean values) Indicates if the champion is active
		    	- freeToPlay: (boolean values): Indicates if the champion is
		    		free to play. Free to play champions are rotated
		    		periodically.
		"""
		session._log('Calling getChamps...')
		url = session.build_url(
			url = const.URLS_CHAMPION['all'],
			url_params = {
				'version':			cls.version
			}
		)

		try:
			r = session.request(url, params=params)
		except RequestError as req_err:
			print(req_err)
			session._log(str(req_err), level='error')
			return pd.DataFrame()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.DataFrame()

		data = r['champions']
		df = pd.DataFrame(data)
		df = df.set_index('id')
		df = df.sort_index()

		return df


	@classmethod
	def getChampion(cls, session, champion_id, params={}):
		session._log('calling getChamp...')
		url = session.build_url(
			url = const.URLS_CHAMPION['by champion'],
			url_params = {
				'version':			cls.version,
				'champion_id':		str(champion_id)
			}
		)
		
		try:
			r = session.request(url, params = params)
		except RequestError as req_err:
			print(req_err)
			session._log(req_err, level='error')
			return pd.Series()
		except Exception as e:
			print(e)
			session._log(e, level='error')
			return pd.Series()

		ds = pd.Series(r)
		ds = ds.rename(r['id'])
		
		return ds


