import sql_methods

table = 'test_table'
deliveries_table = 'test_deliveries'


def matches_per_season(connection):
    sql = "SELECT season, count(*) FROM " + table + " GROUP BY season"
    seasons = sql_methods.read_records(sql, connection)
    matches_per_season_dict = {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0,
                               '2016': 0, '2017': 0}
    """Loop to populate matches_per_season_dict."""
    for season in seasons:
        matches_per_season_dict[season['season']] = int(season['count(*)'])
    return matches_per_season_dict


def matches_won_per_team_per_season(connection):
    sql = "SELECT season, winner, count(winner) AS wins FROM (SELECT * FROM {0} WHERE winner!='') AS result " \
          "GROUP BY winner, season ORDER BY season".format(table)
    result = sql_methods.read_records(sql, connection)
    matches_won_per_team_per_season_dict = {}
    for win_record in result:
        matches_won_per_team_per_season_dict[win_record['winner']] = {'2008': 0, '2009': 0, '2010': 0, '2011': 0,
                                                                      '2012': 0, '2013': 0, '2014': 0, '2015': 0,
                                                                      '2016': 0, '2017': 0}
    for win_record in result:
        matches_won_per_team_per_season_dict[win_record['winner']][win_record['season']] = int(win_record['wins'])
    return matches_won_per_team_per_season_dict


def extra_runs_per_team_in_2016(connection):
    sql = "SELECT bowling_team, SUM(extra_runs) FROM " + table + " INNER JOIN " + deliveries_table + " ON " + table + \
          ".id = " + deliveries_table + ".match_id WHERE " + table + ".season = '2016' group by " + deliveries_table + \
          ".bowling_team"
    result = sql_methods.read_records(sql, connection)
    extra_runs_per_team_in_2016_dict = {}
    for team in result:
        extra_runs_per_team_in_2016_dict[team['bowling_team']] = int(team['SUM(extra_runs)'])
    return extra_runs_per_team_in_2016_dict


def top_economical_bowlers_in_2015(connection):
    sql = "SELECT bowler, 6*SUM(total_runs)/COUNT(*) AS economy FROM {0} INNER JOIN {1} ON {0}.id = {1}.match_id " \
          "WHERE {0}.season = '2015' GROUP BY {1}.bowler ORDER BY economy LIMIT 10".format(table, deliveries_table)
    result = sql_methods.read_records(sql, connection)
    bowler_economy = {}
    for bowler in result:
        bowler_economy[bowler['bowler']] = round(bowler['economy'], 1)
    return bowler_economy


def bowler_economy_per_season(connection):
    sql = "SELECT season, 6*SUM(total_runs)/COUNT(*) AS economy FROM {0} INNER JOIN {1} " \
          "ON {0}.id={1}.match_id GROUP BY {0}.season".format(table, deliveries_table)
    result = sql_methods.read_records(sql, connection)
    economy_per_season_dict = {'2008': 0.0, '2009': 0.0, '2010': 0.0, '2011': 0.0, '2012': 0.0, '2013': 0.0,
                               '2014': 0.0, '2015': 0.0, '2016': 0.0, '2017': 0.0}
    for season in result:
        economy_per_season_dict[season['season']] = round(season['economy'], 1)
    return economy_per_season_dict
