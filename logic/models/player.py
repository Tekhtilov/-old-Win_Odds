import sys
from API_requests import players_info

sys.path.insert(1, '../API_requests.py')


class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.id = self.get_player_id()

    def get_player_id(self):
        for playernickname in players_info:
            if self.nickname == playernickname['name']:
                player_account_id = playernickname['account_id']
                return player_account_id
