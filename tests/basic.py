import os, sys
sys.path.append('..')

import pylol as pl
import pylol.riot_api_wrapper as raw

session = raw.Session('RGAPI-81d7b482-d13b-4c04-bf16-383a7e8be6a2')



def main():
	raw.Champion.getChamps(session)






def hello_world():
	rs = raw.Summoner.getSummByName(session, 'RiotSchmick')
	print(rs)

def logger_test():
	session._log('default test')
	session._log('debug test', 'debug')
	session._log('info test', 'info')
	session._log('warning test', 'warning'),
	session._log('error test', 'error'),
	session._log('critical test', 'critical'),
	session._log('unknown level test', ';laskdjf;ine')

def graphics_test1():
	graph = pl.Graphics(session)


if __name__ == '__main__':
	main()