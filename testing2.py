"""
Returns the score of every game in the year and week range selected.
"""


import requests, bs4


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
    parselog(url)


def parselog(file_path):
    handler = requests.get(file_path)
    soup = bs4.BeautifulSoup(handler.text, "lxml")

    # Print week and year
    for week_info in soup.find_all('gms'):
        week_attrs = dict(week_info.attrs)

        print('Week: ', week_attrs['w'], 'Year: ', week_attrs['y'])

    # Print game score and status
    for message in soup.find_all('g'):
        msg_attrs = dict(message.attrs)

        print('Game ID: ', msg_attrs['eid'], 'Gsis ID: ', msg_attrs['gsis'],
              '\n', msg_attrs['v'], msg_attrs['vnn'], msg_attrs['vs'].title(),
              '\t', msg_attrs['h'], msg_attrs['hnn'].title(),
              msg_attrs['hs'], msg_attrs['q'], '\n')


for year in range(2015, 2016):
    for week in range(6, 12):
        schedule_url(year, 'REG', week)
        print('\n')
