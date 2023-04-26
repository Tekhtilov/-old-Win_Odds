import json
import requests

url_to_players = 'https://api.opendota.com/api/proPlayers'
url_to_heroes = 'https://api.opendota.com/api/heroStats'

players_response = requests.get(url_to_players)
players_info = players_response.json()

heroes_response = requests.get(url_to_heroes)
heroes_info = heroes_response.json()



