import sql_methods

table = 'test_table'


def matches_per_season(connection):
    sql = "SELECT season, count(*) FROM " + table + " GROUP BY season"
    seasons = sql_methods.read_records(sql, connection)
    matches_per_season_dict = {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0,
                               '2016': 0, '2017': 0}
    """Loop to populate matches_per_season_dict."""
    for season in seasons:
        matches_per_season_dict[season['season']] = int(season['count(*)'])
    return matches_per_season_dict
