import data
import sql_methods
import matplotlib.pyplot as plt

deliveries_table = 'test_deliveries'


def plot_matches_per_season():
    connection = sql_methods.connect_db()
    sql_methods.create_table_populate('resources/matches.csv', connection)
    matches_per_season = data.matches_per_season(connection)
    sql_methods.delete_table(connection)
    connection.close()
    plt.bar(list(matches_per_season.keys()), list(matches_per_season.values()))
    plt.xlabel('Seasons')
    plt.ylabel('Matches played')
    plt.title('Matches played per season')
    plt.show()


def plot_matches_won_per_team_per_season():
    connection = sql_methods.connect_db()
    sql_methods.create_table_populate('resources/matches.csv', connection)
    matches_won_per_team_per_season = data.matches_won_per_team_per_season(connection)
    sql_methods.delete_table(connection)
    connection.close()
    team_total = None

    for team_name in matches_won_per_team_per_season.keys():
        if team_total is None:
            team_total = matches_won_per_team_per_season[team_name].values()
        else:
            team_total = [int(x) + int(y) for x, y in zip(matches_won_per_team_per_season[team_name].values(), team_total)]

    for team_name in matches_won_per_team_per_season.keys():
        plt.bar(range(len(matches_won_per_team_per_season[team_name].keys())), team_total, label=team_name)
        team_total = [int(y) - int(x) for x, y in zip(matches_won_per_team_per_season[team_name].values(), team_total)]

    plt.xticks(range(len(matches_won_per_team_per_season[team_name].keys())), matches_won_per_team_per_season[team_name].keys())
    plt.legend(loc="upper right", fontsize="x-small", bbox_to_anchor=(1.12, 1))
    plt.title("Matches won by each team over years")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.show()


def plot_extra_runs_per_team_in_2016():
    connection = sql_methods.connect_db()
    sql_methods.create_table_populate('resources/matches.csv', connection)
    sql_methods.create_table_populate('resources/deliveries.csv', connection, deliveries_table)
    extra_runs_per_team = data.extra_runs_per_team_in_2016(connection)
    sql_methods.delete_table(connection)
    connection.close()
    print(extra_runs_per_team)
    plt.bar(list(extra_runs_per_team.keys()), list(extra_runs_per_team.values()))
    plt.xlabel('Teams')
    plt.ylabel('Extra runs conceded')
    plt.title('Extra runs conceded per team in 2016 season')
    plt.show()


def plot_top_economical_bowlers_in_2015():
    connection = sql_methods.connect_db()
    sql_methods.create_table_populate('resources/matches.csv', connection)
    sql_methods.create_table_populate('resources/deliveries.csv', connection, deliveries_table)
    bowler_economy = data.top_economical_bowlers_in_2015(connection)
    sql_methods.delete_table(connection)
    connection.close()
    plt.bar(list(bowler_economy.keys()), list(bowler_economy.values()))
    plt.xlabel('Bowlers')
    plt.ylabel('Bowling Economy')
    plt.title('Top economical bowlers of 2015 season')
    plt.show()


def plot_bowler_economy_per_season():
    connection = sql_methods.connect_db()
    sql_methods.create_table_populate('resources/matches.csv', connection)
    sql_methods.create_table_populate('resources/deliveries.csv', connection, deliveries_table)
    bowler_economy_per_season = data.bowler_economy_per_season(connection)
    sql_methods.delete_table(connection)
    connection.close()
    plt.bar(list(bowler_economy_per_season.keys()), list(bowler_economy_per_season.values()))
    plt.xlabel('Seasons')
    plt.ylabel('Average bowling Economy')
    plt.title('Average bowling economy per season')
    plt.show()
