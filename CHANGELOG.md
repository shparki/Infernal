5/21/2018: 		- Added CHANGELOG.md (FINALLY!)
				- Exception handling (did not search for bugs- testing required)
					TODO: Check for errors in exception handling for requests
					TODO: Add specific error code handling for each method
					TODO: Exception logging
				- Updated StaticData, ThirdPartCode, Tournament, TournamentStub requests to follow new format (\_buildurl then \_request)
					TODO: Update data structures for runes & rune paths (updated and old)
Questions:
	- Is there a better method to handle the brute-force way of handling RequestError in all api methods?
	- Find a way to concat \_buidurl and \_request