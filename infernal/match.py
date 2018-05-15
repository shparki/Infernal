from . import core

import pandas as pd



class Match(object):



	def __init__(self, game_id):
		self.game_id = game_id

		self.match = None
		self.timeline = None

		self.match_params = {
			'gameId': self.game_id,
			'seasonId': None,
			'queueId': None,
			'gameVersion': None,
			'platformId': None,
			'gameMode': None,
			'mapId': None,
			'gameType': None, 
			'gameDuration': None,
			'gameCreation': None,
			'frameInterval': None
		}
		self.teams = {}
		self.bans = {}
		self.participants = {} 
		self.participant_stats = {}
		self.participant_timelines = {}

		self.timeline = None
		self.events = {} ##
		self.participant_frames = {}



	def initialize(self, session):
		self.match = core.Match.getMatch(session, self.game_id)
		self.timeline = core.Match.getTimeline(session, self.game_id)

		self.match_params['seasonId'] = self.match['seasonId']
		self.match_params['queueId'] = self.match['queueId']
		self.match_params['gameVersion'] = self.match['gameVersion']
		self.match_params['platformId'] = self.match['platformId']
		self.match_params['gameMode'] = self.match['gameMode']
		self.match_params['mapId'] = self.match['mapId']
		self.match_params['gameType'] = self.match['gameType']
		self.match_params['gameDuration'] = self.match['gameDuration']
		self.match_params['gameCreation'] = self.match['gameCreation']
		self.match_params['frameInterval'] = self.timeline['frameInterval']
		self.match_params = pd.Series(self.match_params)


		for part in self.match['participantIdentities']:
			part_dict = part['player']
			part_dict['participant_id'] = part['participantId']
			self.participants[part_dict['participant_id']] = part_dict
		self.participants = pd.DataFrame(self.participants).transpose()
		self.particpants = self.participants.set_index('participant_id')
		
		part_2 = self.match['participants']
		for part in part_2:
			part_stats = part['stats']
			part_stats['participant_id'] = part['participantId']
			self.participant_stats[part['participantId']] = part_stats
			part.pop('stats', 0)

			part_timeline = part['timeline']
			part_timeline['participant_id'] = part['participantId']
			self.participant_timelines[part['participantId']] = part_timeline
			part.pop('timeline', 0)


		part_2 = pd.DataFrame(part_2)
		part_2 = part_2.set_index('participantId')
		self.participants = pd.concat([self.participants, part_2], axis=1)

		self.participant_stats = pd.DataFrame(self.participant_stats).transpose()
		self.participant_stats = self.participant_stats.set_index('participant_id')

		self.participant_timelines = pd.DataFrame(self.participant_timelines).transpose()
		self.participant_timelines = self.participant_timelines.set_index('participant_id')


		for team in self.match['teams']:
			self.bans[team['teamId']] = team['bans']
			team.pop('bans', 0)
			self.teams[team['teamId']] = team
		self.bans = pd.DataFrame(self.bans).transpose()
		self.teams = pd.DataFrame(self.teams).transpose()


		for frame in self.timeline['frames']:
			for event in frame['events']:
				self.events[event['timestamp']] = event
			for part_id, part_frame in frame['participantFrames'].items():
				part_frame['participant_id'] = part_id
				part_frame['timestamp'] = frame['timestamp']
				self.participant_frames[frame['timestamp']] = part_frame
		self.events = pd.DataFrame(self.events).transpose()
		self.events = self.events.set_index('timestamp')
		self.participant_frames = pd.DataFrame(self.participant_frames).transpose()
		self.participant_frames = self.participant_frames.set_index('timestamp')
