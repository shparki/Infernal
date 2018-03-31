import os, sys
sys.path.append('..')

import pylol as pl
import pylol.riot_api_wrapper as raw

session = raw.Session('RGAPI-81d7b482-d13b-4c04-bf16-383a7e8be6a2')



def main():
	hello_world()


def hello_world():
	rs = raw.Summoner.getSummByName(session, 'RiotSchmick')
	print(rs)


if __name__ == '__main__':
	main()