import sys
from API_requests import heroes_info
import requests

sys.path.insert(1, '../API_requests.py')


class Hero:
    def __init__(self, name):
        self.name = name
        self.id = self.get_hero_id()

    def get_hero_id(self):
        for heroname in heroes_info:
            if self.name == heroname['localized_name']:
                hero_id = heroname['id']
                return hero_id

    def get_hero_wr(self):
        for hero in heroes_info:
            if self.name == hero['localized_name']:
                heroWR = (hero['pro_win'] * 100) / hero['pro_pick']
                return int(heroWR)
