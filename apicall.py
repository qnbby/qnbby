from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-f932dfa5-4158-4b9f-b443-1c6213aa8cfd'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'miss a lot mb')
print(me)

# Return the rank status for Doublelift
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)