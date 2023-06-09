from logic.models.hero import Hero
from logic.models.heroes_matchup import HeroMatchupsWR
from logic.models.player_wl import PlayerWL
from logic.models.player import Player
from logic.models.calculate_win_prob import HeroWinProbability

wp_list = []

rad_hero_1 = HeroWinProbability()
rad_hero_1_hero_wr = rad_hero_1.return_hero_wr()
rad_hero_1_players_wl = rad_hero_1.return_player_wl_info()
rad_hero_1_hero_matchup = rad_hero_1.return_enemies_info()
rad_hero_1_win_prob = rad_hero_1.calculate_win_prob()
wp_list.append(rad_hero_1_win_prob)
print()
print(f"General win rate of {rad_hero_1.hero.name}: {rad_hero_1_hero_wr}%\n{rad_hero_1.player.nickname}'s win rate on that hero: {rad_hero_1_players_wl}%\nWin rate of {rad_hero_1.hero.name} against "
      f"enemy team: {rad_hero_1_hero_matchup}%\nHis win probability: {rad_hero_1_win_prob}")
print()

rad_hero_2 = HeroWinProbability()
rad_hero_2_hero_wr = rad_hero_2.return_hero_wr()
rad_hero_2_players_wl = rad_hero_2.return_player_wl_info()
rad_hero_2_hero_matchup = rad_hero_2.return_enemies_info()
rad_hero_2_win_prob = rad_hero_2.calculate_win_prob()
wp_list.append(rad_hero_2_win_prob)
print()
print(f"General win rate of {rad_hero_2.hero.name}: {rad_hero_2_hero_wr}%\n{rad_hero_2.player.nickname}'s win rate on that hero: {rad_hero_2_players_wl}%\nWin rate of {rad_hero_2.hero.name} against "
      f"enemy team: {rad_hero_2_hero_matchup}%\nHis win probability: {rad_hero_2_win_prob}")
print()

rad_hero_3 = HeroWinProbability()
rad_hero_3_hero_wr = rad_hero_3.return_hero_wr()
rad_hero_3_players_wl = rad_hero_3.return_player_wl_info()
rad_hero_3_hero_matchup = rad_hero_3.return_enemies_info()
rad_hero_3_win_prob = rad_hero_3.calculate_win_prob()
wp_list.append(rad_hero_3_win_prob)
print()
print(f"General win rate of {rad_hero_3.hero.name}: {rad_hero_3_hero_wr}%\n{rad_hero_3.player.nickname}'s win rate on that hero: {rad_hero_3_players_wl}%\nWin rate of {rad_hero_3.hero.name} against "
      f"enemy team: {rad_hero_3_hero_matchup}%\nHis win probability: {rad_hero_3_win_prob}")
print()

rad_hero_4 = HeroWinProbability()
rad_hero_4_hero_wr = rad_hero_4.return_hero_wr()
rad_hero_4_players_wl = rad_hero_4.return_player_wl_info()
rad_hero_4_hero_matchup = rad_hero_4.return_enemies_info()
rad_hero_4_win_prob = rad_hero_4.calculate_win_prob()
wp_list.append(rad_hero_4_win_prob)
print()
print(f"General win rate of {rad_hero_4.hero.name}: {rad_hero_4_hero_wr}%\n{rad_hero_4.player.nickname}'s win rate on that hero: {rad_hero_4_players_wl}%\nWin rate of {rad_hero_4.hero.name} against "
      f"enemy team: {rad_hero_4_hero_matchup}%\nHis win probability: {rad_hero_4_win_prob}")
print()

rad_hero_5 = HeroWinProbability()
rad_hero_5_hero_wr = rad_hero_5.return_hero_wr()
rad_hero_5_players_wl = rad_hero_5.return_player_wl_info()
rad_hero_5_hero_matchup = rad_hero_5.return_enemies_info()
rad_hero_5_win_prob = rad_hero_5.calculate_win_prob()
wp_list.append(rad_hero_5_win_prob)
print()
print(f"General win rate of {rad_hero_5.hero.name}: {rad_hero_5_hero_wr}%\n{rad_hero_5.player.nickname}'s win rate on that hero: {rad_hero_5_players_wl}%\nWin rate of {rad_hero_5.hero.name} against "
      f"enemy team: {rad_hero_5_hero_matchup}%\nHis win probability: {rad_hero_5_win_prob}")
print()
print(wp_list)

print(f'Radiants win probability = {sum(wp_list)}')
