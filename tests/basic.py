import os, sys
sys.path.append('..')

import pylol as pl
import pylol.riot_api_wrapper as raw

session = raw.Session('RGAPI-81d7b482-d13b-4c04-bf16-383a7e8be6a2')



def main():
	# champion_test()
	champion_mastery_test()
	# summoner_test()




def hello_world():
	rs = raw.Summoner.getSummonerByName(session, 'RiotSchmick')
	print(rs)

def logger_test():
	session._log('default test')
	session._log('debug test', 'debug')
	session._log('info test', 'info')
	session._log('warning test', 'warning'),
	session._log('error test', 'error'),
	session._log('critical test', 'critical'),
	session._log('unknown level test', ';laskdjf;ine')


def champion_test():
	r = raw.Champion.getChampions(session)
	print(r)

	r = raw.Champion.getChampion(session, 266)
	print(r)

# TODO: Fix getMasteryByChampion to take status code into account for unplayed champions
def champion_mastery_test():
	r = raw.ChampionMastery.getAllMasteries(session, 26770285)
	print(r)

	r = raw.ChampionMastery.getMasteryByChampion(session, 26770285, 1)
	print(r)

	r = raw.ChampionMastery.getTotalMastery(session, 26770285)
	print(r)

def summoner_test():
	r = raw.Summoner.getSummonerByName(session, 'Shparki')
	print(r)

	r = raw.Summoner.getSummonerByAccount(session, 41513544)
	print(r)

	r = raw.Summoner.getSummonerByID(session, 26770285)
	print(r)


if __name__ == '__main__':
	main()