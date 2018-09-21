"""test_data module.

Test cases for data module
Classes:
    TestData
"""
import data
import unittest
import sql_methods


table = 'test_table'
deliveries_table = 'test_deliveries'


class TestData(unittest.TestCase):
    """TestData class.

    Contains test cases for data module
    """
    def setUp(self):
        """Set up pymysql connector variable"""
        self.connection = sql_methods.connect_db()

    def tearDown(self):
        """Delete all tables from the database"""
        sql_methods.delete_table(self.connection)
        self.connection.close()

    def test_matches_per_season(self):
        """test_matches_per_season method.

        Contains test cases for matches_per_season method of data module.
        Prints OK if all test cases PASS, else prints which test cases FAIL.

        Arguments:
            self (TestData object)

        Returns:
            None.
        """

        """First test case."""
        expected_output = {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0,
                           '2016': 5, '2017': 4}
        sql_methods.create_table_populate('resources/problem_1/test_1.csv', self.connection)
        calculated_output = data.matches_per_season(self.connection)
        self.assertEqual(expected_output, calculated_output)

        """Second test case."""
        sql_methods.delete_table(self.connection)
        expected_output = {'2008': 1, '2009': 0, '2010': 0, '2011': 0, '2012': 1, '2013': 0, '2014': 0,
                           '2015': 0, '2016': 4, '2017': 3}
        sql_methods.create_table_populate('resources/problem_1/test_2.csv', self.connection)
        calculated_output = data.matches_per_season(self.connection)
        self.assertEqual(expected_output, calculated_output)

    def test_matches_won_per_team_per_season(self):
        """Unit test method for matches_won_per_team_per_season method

        Contains test cases for said method of data module.
        Prints OK if all test cases PASS, else prints which test cases FAIL.

        :return: None
        """

        """First test case."""
        expected_output = {'Chennai Super Kings': {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                                                   '2014': 0, '2015': 0, '2016': 3, '2017': 1},
                           'Mumbai Indians': {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                                              '2014': 0, '2015': 0, '2016': 2, '2017': 3}}
        sql_methods.create_table_populate('resources/problem_2/test_1.csv', self.connection)
        calculated_output = data.matches_won_per_team_per_season(self.connection)
        self.assertEqual(expected_output, calculated_output)

        """second test case."""
        sql_methods.delete_table(self.connection)
        expected_output = {'Chennai Super Kings': {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                                                   '2014': 0, '2015': 0, '2016': 2, '2017': 1},
                           'Deccan Chargers': {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                                               '2014': 0, '2015': 0, '2016': 1, '2017': 0},
                           'Kolkata Knight Riders': {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                                                     '2014': 0, '2015': 0, '2016': 0, '2017': 1},
                           'Mumbai Indians': {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                                              '2014': 0, '2015': 0, '2016': 2, '2017': 2}}
        sql_methods.create_table_populate('resources/problem_2/test_2.csv', self.connection)
        calculated_output = data.matches_won_per_team_per_season(self.connection)
        self.assertEqual(expected_output, calculated_output)

    def test_extra_runs_per_team_in_2016(self):
        """Unit test method for extra_runs_per_team_in_2016 method.

        Contains test cases for said method of data module.
        Prints OK if all test cases PASS, else prints which test case FAILS.

        :return: None
        """

        """First test case."""
        expected_output = {'Mumbai Indians': 3, 'Gujarat Lions': 0, 'Rising Pune Supergiants': 1}
        sql_methods.create_table_populate('resources/matches.csv', self.connection)
        sql_methods.create_table_populate('resources/problem_3/test_1.csv', self.connection, deliveries_table)
        calculated_output = data.extra_runs_per_team_in_2016(self.connection)
        self.assertEqual(expected_output, calculated_output)

        """Second test case."""
        sql_methods.delete_table(self.connection)
        expected_output = {}
        sql_methods.create_table_populate('resources/matches.csv', self.connection)
        sql_methods.create_table_populate('resources/problem_3/test_2.csv', self.connection, deliveries_table)
        calculated_output = data.extra_runs_per_team_in_2016(self.connection)
        self.assertEqual(expected_output, calculated_output)

    def test_top_economical_bowlers_in_2015(self):
        """Unit test method for top_economical_bowlers_in_2015 method.

        Contains test cases for said method of data module.
        Prints OK if all test cases PASS, else prints which test case FAILS.

        :return: None
        """

        """First test case."""
        expected_output = {'RA Jadeja': 6.0, 'DJ Bravo': 36.0, 'SP Narine': 0.0, 'AD Russell': 6.0, 'PP Chawla': 0.0}
        sql_methods.create_table_populate('resources/matches.csv', self.connection)
        sql_methods.create_table_populate('resources/problem_4/test_1.csv', self.connection, deliveries_table)
        calculated_output = data.top_economical_bowlers_in_2015(self.connection)
        self.assertEqual(expected_output, calculated_output)

        """Second test case."""
        sql_methods.delete_table(self.connection)
        expected_output = {}
        sql_methods.create_table_populate('resources/matches.csv', self.connection)
        sql_methods.create_table_populate('resources/problem_4/test_2.csv', self.connection, deliveries_table)
        calculated_output = data.top_economical_bowlers_in_2015(self.connection)
        self.assertEqual(expected_output, calculated_output)

    def test_bowler_economy_per_season(self):
        """Unit test method for bowler_economy_per_season method.

        Contains test cases for said method of data module.
        Prints OK if all test cases PASS, else prints which test case FAILS.

        :return: None
        """

        """First test case."""
        expected_output = {'2008': 0.0, '2009': 0.0, '2010': 6.0, '2011': 0.0, '2012': 0.0, '2013': 0.0, '2014': 0.0,
                           '2015': 8.6, '2016': 9.0, '2017': 6.0}
        sql_methods.create_table_populate('resources/matches.csv', self.connection)
        sql_methods.create_table_populate('resources/problem_5/test_1.csv', self.connection, deliveries_table)
        calculated_output = data.bowler_economy_per_season(self.connection)
        self.assertEqual(expected_output, calculated_output)


if __name__ == '__main__':
    unittest.main()
