from logic.models.hero import Hero
from logic.models.player_wl import PlayerWL
from logic.models.heroes_matchup import HeroMatchupsWR
from logic.models.player import Player
from logic.models.enemy_team import enemy_team


class HeroWinProbability:
    def __init__(self):
        self.hero = Hero(name=input("Hero name: "))
        self.hero_id = self.hero.id
        self.hero_matchup = HeroMatchupsWR(self.hero_id)
        self.player = Player(nickname=input("Enter Player's nickname: "))
        self.account_id = self.player.id
        self.player_wl = PlayerWL(account_id=self.account_id, hero_id=self.hero_id)

    def return_hero_id(self):
        return self.hero.get_hero_id()

    def return_hero_wr(self):
        return self.hero.get_hero_wr()

    def return_matchup_data(self):
        return self.hero_matchup.matchup_data

    def return_enemies_info(self):
        return self.hero_matchup.get_enemies_info()

    def return_player_id(self):
        return self.player.get_player_id()

    def return_player_wl_info(self):
        return self.player_wl.get_players_wl_info()

    def calculate_win_prob(self):
        self.win_prob = (self.return_hero_wr() / 100) * (self.return_enemies_info() / 100) * (
                self.return_player_wl_info() / 100) * 100
        rounded_win_prob = round(self.win_prob, 1)
        return rounded_win_prob
