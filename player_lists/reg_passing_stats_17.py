from pprint import pprint


data = {"games": {"2017091400": {"name": "A.Dalton", "att": 35, "cmp": 20,
                               "yds": 224, "tds": 0, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091700": {"name": "J.Flacco", "att": 34, "cmp": 25, "yds": 217, "tds": 2, "ints": 1, "twopta": 0, "twoptm": 0}, "2017091701": {"name": "C.Newton", "att": 32, "cmp": 20, "yds": 228, "tds": 0, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091702": {"name": "J.Brissett", "att": 37, "cmp": 20, "yds": 216, "tds": 0, "ints": 1, "twopta": 0, "twoptm": 0}, "2017091703": {"name": "B.Bortles", "att": 34, "cmp": 20, "yds": 223, "tds": 1, "ints": 2, "twopta": 1, "twoptm": 0}, "2017091704": {"name": "A.Smith", "att": 28, "cmp": 21, "yds": 251, "tds": 1, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091705": {"name": "D.Brees", "att": 45, "cmp": 27, "yds": 356, "tds": 2, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091706": {"name": "B.Roethlisberger", "att": 35, "cmp": 23, "yds": 243, "tds": 2, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091707": {"name": "R.Fitzpatrick", "att": 1, "cmp": 0, "yds": 0, "tds": 0, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091708": {"name": "P.Rivers", "att": 39, "cmp": 31, "yds": 331, "tds": 1, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091709": {"name": "D.Carr", "att": 28, "cmp": 23, "yds": 230, "tds": 3, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091710": {"name": "T.Siemian", "att": 32, "cmp": 22, "yds": 231, "tds": 4, "ints": 1, "twopta": 0, "twoptm": 0}, "2017091711": {"name": "J.Hekker", "att": 1, "cmp": 1, "yds": 28, "tds": 0, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091712": {"name": "R.Wilson", "att": 39, "cmp": 23, "yds": 198, "tds": 1, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091713": {"name": "M.Ryan", "att": 28, "cmp": 19, "yds": 252, "tds": 1, "ints": 0, "twopta": 0, "twoptm": 0}, "2017091800": {"name": "E.Manning", "att": 32, "cmp": 22, "yds": 239, "tds": 1, "ints": 1, "twopta": 0, "twoptm": 0}}}

json_dict = {}

for games in data["games"]:
    pprint(games)


pprint(data)