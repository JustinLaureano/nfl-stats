"""
collect all players and stats

step 1: collect raw data and save it
get schedule
get game id
get game data
loop through range

save all data collected in a file i.e. player_stats_17.py

collect  all stats in file
    dict or class
    class DataToDict():
        def __init(self, dictionary):
            for k, v in dictionary.items():
                setattr(self, k, v)

    class Player():
        def __init(self, playerid, name, team):
            self.playerid = playerid
            self.name = name
            self.team = team


    ex dict:
    player_dict = {}
    def collect stats(load file)
        player_dict[name] = item[name]

    home or away
    abbr
    score
    stats
        defense
            ast
            ffum
            int
            name
            sk
            tkl
        fumbles
        kicking
        kickret
        passing
            att
            comp
            ints
            name
            tds
            twopta
            twoptm
            yds
        punting
        puntret
        receiving
            long
            lngtd
            name
            rec
            tds
            twopta
            twoptm
            yds
        rushing
            att
            lng
            tngtd
            name
            tds
            twopta
            twoptm
            yds
        team



    load stats
    loop, add stats to dict
"""

