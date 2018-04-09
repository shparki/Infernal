# General Constants
VERSIONS = {
    'cmastery':                 'v3',
    'champion':                 'v3',
    'league':                   'v3',
    'sdata':                    'v3',
    'status':                   'v3',
    'match':                    'v3',
    'spectator':                'v3',
    'summoner':                 'v3',
    'tpc':                      'v3',
    'tstub':                    'v3',
    'tournament':               'v3'
}

RESPONSE_CODES = {
    '400':                      'Bad request',
    '401':                      'Unauthorized',
    '403':                      'Forbidden',
    '404':                      'Not found',
    '405':                      'Method not allowed',
    '415':                      'Unsupported media type',
    '422':                      'Player exists, but hasn\'t played since match history collection began',
    '429':                      'Rate limit exceeded',
    '500':                      'Internal server error',
    '502':                      'Bad gateway',
    '503':                      'Service unavailable',
    '504':                      'Gateway timeout'
}

ENDPOINTS = {
    # Regional Endpoints
    'br':                       'br1.api.riotgames.com',
    'eune':                     'eun1.api.riotgames.com',
    'euw':                      'euw1.api.riotgames.com',
    'jp':                       'jp1.api.riotgames.com',
    'kr':                       'kr.api.riotgames.com',
    'lan':                      'la1.api.riotgames.com',
    'las':                      'la2.api.riotgames.com',
    'na':                       'na.api.riotgames.com',
    'na-old':                   'na1.api.riotgames.com',
    'oce':                      'oc1.api.riotgames.com',
    'tr':                       'tr1.api.riotgames.com',
    'ru':                       'ru.api.riotgames.com',
    'pbe':                      'pbe1.api.riotgames.com',

    # Regional Proxies
    'americas':                 'americas.api.riotgames.com',
    'europe':                   'europe.api.riotgames.com',
    'asia':                     'asia.api.riotgames.com'
}


# URLS; Convention: all urls start in '/' but do not end in one
URLS_BASE = {
    # Main base for all URLs
    'base':                     'https://{endpoint}{url}?{params}',

    # Primary midpoints for all sub-apis
    'cmastery':                 '/lol/champion-mastery/{version}',
    'champion':                 '/lol/platform/{version}',
    'league':                   '/lol/league/{version}',
    'sdata':                    '/lol/static-data/{version}',
    'status':                   '/lol/status/{version}',
    'match':                    '/lol/match/{version}',
    'spectator':                '/lol/spectator/{version}',
    'summoner':                 '/lol/summoner/{version}',
    'tpc':                      '/lol/platform/{version}',
    'tstub':                    '/lol/tournament-stub/{version}',
    'tournament':               '/lol/tournament/{version}'
}

URLS_CMASTERY = {
    # Get all champion mastery entities sorted by number of champion points descending.
    'all':                      URLS_BASE['cmastery'] + '/champion-masteries/by-summoner/{summoner_id}',

    # Get a champion mastery by player ID and champion ID.
    'by champion':              URLS_BASE['cmastery'] + '/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}',

    # Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
    'mastery':                  URLS_BASE['cmastery'] + '/scores/by-summoner/{summoner_id}'
}

URLS_CHAMPION = {
    # Retrieve all champions.
    'all':                      URLS_BASE['champion'] + '/champions',

    # Retrieve champion by ID.
    'by champion':              URLS_BASE['champion'] + '/champions/{champion_id}'
}

URLS_LEAGUE = {
    # Get the challenger league for given queue.
    'challenger':               URLS_BASE['league'] + '/challengerleagues/by-queue/{queue}',

    # Get league with given ID, including inactive entries.
    'by league':                URLS_BASE['league'] +  '/leagues/{league_id}',

    #Get the master league for given queue.
    'master':                   URLS_BASE['league'] + '/masterleagues/by-queue/{queue}',

    # Get league positions in all queues for a given summoner ID.
    'by summoner':              URLS_BASE['league'] + '/positions/by-summoner/{summoner_id}' 
}

URLS_SDATA = {
    # Retrieves champion list.
    'champions':                URLS_BASE['sdata'] + '/champions/',

    # Retrieves champion by ID.
    'by champion':              URLS_BASE['sdata'] + '/champions/{champion_id}',

    # Retrieves item list.
    'items':                    URLS_BASE['sdata'] + '/items',

    # Retrieves item by ID.
    'by item':                  URLS_BASE['sdata'] + '/items/{item_id}',

    # Retrieve language strings data.
    'language strings':         URLS_BASE['sdata'] + '/language-strings',

    # Retrieve supported langauges data.
    'supported languages':      URLS_BASE['sdata'] + '/languages',

    # Retrieve map data.
    'maps':                     URLS_BASE['sdata'] + '/maps',

    # Retrieve mastery list.
    'masteries':                URLS_BASE['sdata'] + '/masteries',

    # Retrieve mastery item by ID.
    'by mastery':               URLS_BASE['sdata'] + '/masteries/{mastery_id}',

    # Retrieve profile icons.
    'profile icons':            URLS_BASE['sdata'] + '/profile-icons',

    # Retrieve realm data.
    'realms':                   URLS_BASE['sdata'] + '/realms',

    # Retrieves reforged rune path list.
    'rune paths':               URLS_BASE['sdata'] + '/reforged-rune-paths',

    # Retrieves reforged rune path by ID.
    'by rune path':             URLS_BASE['sdata'] + '/reforged-rune-paths/{path_id}',

    # Retrieves reforged rune list.
    'reforged runes':           URLS_BASE['sdata'] + '/reforged-runes',

    # Retrieves reforged rune by ID.
    'by reforged rune':         URLS_BASE['sdata'] + 'r/eforged-runes/{rune_id}',

    # Retrieves rune list.
    'runes':                    URLS_BASE['sdata'] + '/runes',

    # Retrieves rune by ID.
    'by rune':                  URLS_BASE['sdata'] + '/runes/{rune_id}',

    # Retrieves summoner spell list.
    'summoner spells':          URLS_BASE['sdata'] + '/summoner-spells',

    # Retrieves summoner spell by ID.
    'by summoner spell':        URLS_BASE['sdata'] + '/summoner-spells/{spell_id}',

    # Retrieves full tarball link
    'tarball links':            URLS_BASE['sdata'] + '/tarball-links',

    # Retrieves version data
    'versions':                 URLS_BASE['sdata'] + '/versions'
}

URLS_STATUS = {
    # Get League of Legends status for the given shard.
    'status':                   URLS_BASE['status'] + '/shard-data'
}

URLS_MATCH = {
    # Get match IDs by tournament code.
    'matchID by tournament':    URLS_BASE['match'] + '/matches/by-tournament-code/{tournament_code}/ids',

    #Get match by match ID.
    'by match':                 URLS_BASE['match'] + '/matches/{match_id}',

    #Get match by match ID and tournament code.
    'by tournament':            URLS_BASE['match'] + '/matches/{match_id}/by-tournament-code/{tournament_code}',

    # Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any.
    'by account':               URLS_BASE['match'] + '/matchlists/by-account/{account_id}',

    # Get matchlist for last 20 matches played on given account ID and platform ID.
    'recent by account':        URLS_BASE['match'] + '/matchlists/by-account/{account_id}/recent',

    # Get match timeline by match ID.
    'timeline':                 URLS_BASE['match'] + '/timelines/by-match/{match_id}'
}

URLS_SPECT = {
    # Get current game information for the given summoner ID.
    'active':                   URLS_BASE['spectator'] + '/active-games/by-summoner/{summoner_id}',

    # Get list of featured games.
    'featured':                 URLS_BASE['spectator'] + '/featured-games'
}

URLS_SUMMON = {
    # Get a summoner by account ID.
    'by account':               URLS_BASE['summoner'] + '/summoners/by-account/{account_id}',

    # Get a summoner by summoner name.
    'by name':                  URLS_BASE['summoner'] + '/summoners/by-name/{summoner_name}',

    # Get a summoner by summoner ID.
    'by id':                    URLS_BASE['summoner'] + '/summoners/{summoner_id}'
}

URLS_TPC = {
    # Get third party code for a given summoner ID. (?)
    'by id':                    URLS_BASE['tpc'] + '/third-party-code/by-summoner/{summoner_id}'
}

URLS_TSTUB = {
    # Create a mock tournament code for the give tournament.
    'codes':                    URLS_BASE['tstub'] + '/codes',

    # Gets a mock list of lobby events by tournament code.
    'by tournament':            URLS_BASE['tstub'] + '/lobby-events/by-code/{tournament_code}',

    # Creates a mock tournament provider and returns its ID.
    'providers':                URLS_BASE['tstub'] + '/providers',

    # Creates a mock tournament and returns its ID.
    'tournaments':              URLS_BASE['tstub'] + '/tournaments'
}

URLS_TOURN = {
    # Create tournament code for the given tournament.
    'codes':                    URLS_BASE['tournament'] + '/codes',

    # Update the pick type, map, spectator type, or allowed summoners for a code. / Returns the tournament code DTO associated with a tournament code string.
    'by tournament':            URLS_BASE['tournament'] + '/codes/{tournament_code}',

    # Gets a list of lobby events by tournament code.
    'events by tournament':     URLS_BASE['tournament'] + '/lobby-events/by-code/{tournament_code}',

    # Creates a tournament provider and returns its ID.
    'providers':                URLS_BASE['tournament'] + '/providers',

    # Creates a tournament and returns its ID.
    'tournaments':              URLS_BASE['tournament'] + '/tournaments'
}


# Game Constants NEED TO FINISH THIS, JUST TOO MANY FOR RIGHT NOW
SEASONS = {
    '0':                        'Preseason 3',
    '1':                        'Season 3',
    '2':                        'Preseason 2014',
    '3':                        'Season 2014',
    '4':                        'Preseason 2015',
    '5':                        'Season 2015',
    '6':                        'Preseason 2016',
    '7':                        'Season 2016',
    '8':                        'Preseason 2017',
    '9':                        'Season 2017',
    '10':                       'Preseason 2018',
    '11':                       'Season 2018'
}

MATCH_QUEUES = {
    '0':                        'Custom;',
    '72':                       'Howling Abyss; 1v1 Snowdown Showdown games',
    '73':                       'Howling Abyss; 2v2 Snowdown Showdown games',
    '75':                       'Summoner\'s Rift; 6v6 Hexakill games',
    '76':                       'Summoner\'s Rift; Ultra Rapid Fire games',
    '78':                       'Howling Abyss; One For All: Mirror Mode games',
    '83':                       'Summoner\'s Rift Co-op vs AI Ultra Rapid Fire games',
    '98':                       'Twisted Treeline; 6v6 Hexakill games',
    '100':                      'Butcher\'s Bridge; 5v5 ARAM games',
    '310':                      'Summoner\'s Rift; Nemesis games',
    '313':                      'Summoner\'s Rift; Black Market Brawlers games',
    '317':                      'Crystal Scar; Definitely Not Dominion games',
    '325':                      'Summoner\'s Rift; All Random games',
    '400':                      'Summoner\'s Rift; 5v5 Draft Pick games',
    '420':                      'Summoner\'s Rift; 5v5 Ranked Solo games',
    '430':                      'Summoner\'s Rift; 5v5 Blink Pick games',
    '440':                      'Summoner\'s Rift; 5v5 Ranked Flex games',
    '450':                      'Howling Abyss; 5v5 ARAM games',
    '460':                      'Twisted Treeline; 3v3 Blink Pick games',
    '470':                      'Twisted Treeline; 3v3 Ranked Flex games',
    '600':                      'Summoner\'s Rift; Blood Hunt Assassin games',
    '610':                      'Cosmic ruins; Dark Star: Singularity games',
    '800':                      'Twisted Treeline; Co-op vs. AI Intermediate Bot games',
    '810':                      'Twisted Treeline; Co-op vs. AI Intro Bot games',
    '820':                      'Twisted Treeline; Co-op vs. AI Beginner Bot games',
    '830':                      'Summoner\'s Rift; Co-op vs. AI Intro Bot games',
    '840':                      'Summoner\'s Rift; Co-op vs. AI Beginner Bot games',
    '850':                      'Summoner\'s Rift; Co-op vs. AI Intermediate Bot games',
    '900':                      'Summoner\'s Rift; ARURF games',
    '910':                      'Crystal Scar; Ascension games',
    '920':                      'Howling Abyss; Legend of the Poro King games',
    '940':                      'Summoner\'s Rift; Nexus Siege games',
    '950':                      'Summoner\'s Rift; Doom Bots Voting games',
    '960':                      'Summoner\'s Rift; Doom Bots Standard games',
    '980':                      'Valoran City Park; Star Guardian Invasion: Normal games',
    '990':                      'Valoran City Park; Star Guardian Invasion: Onslaught games',
    '1000':                     'Overcharge; PROJECT: Hunters games',
    '1010':                     'Summoner\'s Rift; Snow ARURF games',
    '1020':                     'Summoner\'s Rift; One for All games'
}






