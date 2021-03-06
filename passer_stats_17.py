import json
import bs4
import requests
import urllib.request
from pprint import pprint

stats_passing = {}


def schedule_url(year, stype, week):
    """
    Returns the NFL.com XML schedule URL. `year` should be an
    integer, `stype` should be one of the strings `PRE`, `REG` or
    `POST`, and `gsis_week` should be a value in the range
    `[0, 17]`.
    """
    xmlurl = 'http://www.nfl.com/ajax/scorestrip?'
    if stype == 'POST':
        week += 17
        if week == 21:  # NFL.com you so silly
            week += 1
    url = '%sseason=%d&seasonType=%s&week=%d' % (xmlurl, year, stype, week)
    get_game_id(url)


def get_game_id(url):
    """Returns the game ID for each unique game."""
    handler = requests.get(url)
    soup = bs4.BeautifulSoup(handler.text, "lxml")

    # Get game id from nfl.com
    for message in soup.find_all('g'):
        msg_attrs = dict(message.attrs)
        game_id = msg_attrs['eid']
        get_game_data(game_id)


def get_game_data(game_id):
    """Return the unique game ID."""
    json_url = 'http://www.nfl.com/liveupdate/game-center/'
    url = '%s%s/%s_gtd.json' % (json_url, game_id, game_id)
    resp = urllib.request.urlopen(url)
    get_players(resp, game_id)


def get_players(resp, game_id):
    """Collect the passing players for the game."""
    data = json.loads(resp.read().decode())
    passing_stats = {**data[game_id]['away']['stats']['passing'],
                     **data[game_id]['home']['stats']['passing']}

    for name, item in passing_stats.items():
        stats_passing[game_id] = item


def save_players(filename):
    """Save the player dictionary to a new file"""
    players = {'games': stats_passing}

    with open(filename, 'a') as file:
        file.write(json.dumps(players))


def player_loop(start_year, end_year, start_week, end_week, game_type):
    """Enter the search range for passing stats and return results."""
    # display_categories()

    for year in range(start_year, (end_year + 1)):
        for week in range(start_week, (end_week + 1)):
            schedule_url(year, game_type, week)

    filename = 'player_lists/reg_passing_stats_17.py'
    save_players(filename)


# Start Year, End Year, Start, Week, End Week, Game Type('PRE', "REG',
# or 'POST')
player_loop(2017, 2017, 2, 2, 'REG')


##############################################################################

#
# def display_players(passers):
#     """Print the formatted passing players to the console."""
#     with open(passers, 'r') as ViewFileOpen:
#         data = ViewFileOpen.read()
#         stuff = json.loads(data)
#         pprint(stuff)
#         #
#         # pprint(data)
#
#
# display_players('player_lists/reg_passing_stats_17')