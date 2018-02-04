import json
import bs4
import requests
import urllib.request
from pprint import pprint
import urllib.request
#
# passing_players = {}
#
#
# def schedule_url(year, stype, week):
#     """
#     Returns the NFL.com XML schedule URL. `year` should be an
#     integer, `stype` should be one of the strings `PRE`, `REG` or
#     `POST`, and `gsis_week` should be a value in the range
#     `[0, 17]`.
#     """
#     xmlurl = 'http://www.nfl.com/ajax/scorestrip?'
#     if stype == 'POST':
#         week += 17
#         if week == 21:  # NFL.com you so silly
#             week += 1
#     url = '%sseason=%d&seasonType=%s&week=%d' % (xmlurl, year, stype, week)
#     get_game_id(url)
#
#
# def get_game_id(file_path):
#     """Returns the game ID for each unique game."""
#     handler = requests.get(file_path)
#     soup = bs4.BeautifulSoup(handler.text, "lxml")
#
#     # Get game id from nfl.com
#     for message in soup.find_all('g'):
#         msg_attrs = dict(message.attrs)
#         game_id = msg_attrs['eid']
#         get_game_data(game_id)
#
#
# def get_game_data(game_id):
#     """Return the unique game ID."""
#     json_url = 'http://www.nfl.com/liveupdate/game-center/'
#     url = '%s%s/%s_gtd.json' % (json_url, game_id, game_id)
#     resp = urllib.request.urlopen(url)
#     get_players(resp, game_id)
#
#
# def get_players(resp, game_id):
#     """Collect the passing players for the game."""
#     data = json.loads(resp.read().decode())
#     passing_stats = {**data[game_id]['away']['stats']['passing'],
#                      **data[game_id]['home']['stats']['passing']}
#
#     for name, item in passing_stats.items():
#         passing_players[name] = item['name']
#
#     filename = 'passing_players.txt'
#     save_players(filename)
#
#
# def save_players(filename):
#     """Save the player dictionary to a new file"""
#     players = {'players': passing_players}
#
#     with open(filename, 'w') as file:
#         file.write(json.dumps(players))
#
#
# def player_loop(start_year, end_year, start_week, end_week, game_type):
#     """Enter the search range for passing stats and return results."""
#     # display_categories()
#
#     for year in range(start_year, (end_year + 1)):
#         for week in range(start_week, (end_week + 1)):
#             schedule_url(year, game_type, week)
#
#
# # Start Year, End Year, Start, Week, End Week, Game Type('PRE', "REG',
# # or 'POST')
# # player_loop(2017, 2017, 16, 17, 'REG')
#
#
# def display_players(passers):
#     """Print the formatted passing players to the console."""
#     with open(passers, 'r') as ViewFileOpen:
#         data = ViewFileOpen.read()
#
#     pprint(data)
#
#
# display_players('passing_players.txt')


url = ('http://www.nfl.com/liveupdate/game-center/2017012200'
                       '/2017012200_gtd.json')
resp = urllib.request.urlopen(url)
data = json.loads(resp.read().decode())
pprint(data)