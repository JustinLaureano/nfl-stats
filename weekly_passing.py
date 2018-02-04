import json
import bs4
import requests
import urllib.request


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


def get_game_id(file_path):
    """Returns the game ID for each unique game."""
    handler = requests.get(file_path)
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
    get_passing_stats(resp, game_id)


def get_passing_stats(resp, game_id):
    """Collect the passing stats for the game."""
    data = json.loads(resp.read().decode())
    passing_stats = {**data[game_id]['away']['stats']['passing'],
                     **data[game_id]['home']['stats']['passing']}
    display_passing_stats(passing_stats)


def display_passing_stats(passing_stats):
    """Print the formatted passing stats to the console."""
    for name, item in passing_stats.items():
        print('{}  {:<18}{:>5}{:>5}{:>5}{:>4}{:>5}'.format(name,
                                                           item['name'], item['cmp'], item['att'], item['yds'],
                                                           item['tds'], item['ints']))


def display_categories():
    """Display the categories for the stats being displayed."""
    print('{}\n{}   {:<18}{:>5}{:>5}{:>5}{:>4}{:>5}\n'.format('Weekly '
      'Passing Stats', 'Player ID', 'Name', 'CMP', 'ATT', 'YDS', 'TDS',
      'INTS'))


def display_week(game_type, year, week):
    """Display the week that the stats are for."""
    if game_type == 'PRE':
        print('Year {}   Preseason Week {}'.format(year, week))
    elif game_type == 'REG':
        print('Year {}   Week {}'.format(year, week))
    elif game_type == "POST":
        post_season = ['None', 'Wild Card', 'Divisional Round', 'Conference '
                                                                'Championship', 'Super Bowl']
        print('Year {}   {}'.format(year, post_season[week]))


def search_loop(start_year, end_year, start_week, end_week, game_type):
    """Enter the search range for passing stats and return results."""
    display_categories()

    for year in range(start_year, (end_year + 1)):
        for week in range(start_week, (end_week + 1)):
            display_week(game_type, year, week)
            schedule_url(year, game_type, week)
            print('\n')


# Start Year, End Year, Start, Week, End Week, Game Type('PRE', "REG',
# or 'POST')
search_loop(2016, 2016, 1, 4, 'POST')
