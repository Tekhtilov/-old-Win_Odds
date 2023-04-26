import sys
import requests
import json
from API_requests import heroes_info
from logic.models.enemy_team import enemy_team

sys.path.insert(1, '../API_requests.py')


class HeroMatchupsWR:
    def __init__(self, id):
        self.id = id
        hero_id = id
        url_to_hero_matchups = f'https://api.opendota.com/api/heroes/{hero_id}/matchups'
        params_hero_matchups = {'date': 365}
        matchup_response = requests.get(url_to_hero_matchups, params=params_hero_matchups)
        self.matchup_data = matchup_response.json()

    def get_enemies_info(self):
        self.heroes_dict = {}
        for hero in heroes_info:
            if hero['localized_name'] in enemy_team.enemy_team_list:
                self.heroes_dict[hero['id']] = hero['localized_name']

        hero_matchupWR_list = []
        for matchup in self.matchup_data:
            if matchup['hero_id'] in self.heroes_dict:
                matchupWR = int((matchup['wins'] * 100) / matchup['games_played'])
                hero_matchupWR_list.append(matchupWR)
        sum_list = sum(hero_matchupWR_list)
        hero_matchup_wr = sum_list / 5

        return hero_matchup_wr
