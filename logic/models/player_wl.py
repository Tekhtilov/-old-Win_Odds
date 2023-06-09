import requests
from logic.models.player import Player
from logic.models.hero import Hero
import json


class PlayerWL(Hero, Player):
    def __init__(self, account_id, hero_id):
        self.account_id = account_id
        self.hero_id = hero_id

    def get_players_wl_info(self):
        url_to_players_wl = f"https://api.opendota.com/api/players/{self.account_id}/wl"
        params = {'hero_id': self.hero_id, 'date': 360, 'lobby_type': 1, 'game_mode': 2}
        players_wl_response = requests.get(url_to_players_wl, params=params)
        self.players_wl_data = players_wl_response.json()

    # def get_players_wl(self):
        heroes_wins = self.players_wl_data['win']
        heroes_losses = self.players_wl_data['lose']
        if heroes_losses == 0 and heroes_wins == 0:
            heroes_winrate = 0
        else:
            heroes_winrate = int(heroes_wins / (heroes_wins + heroes_losses) * 100)
        return heroes_winrate
