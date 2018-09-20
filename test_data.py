"""test_data module.

Test cases for data module
Classes:
    TestData
"""
import data
import unittest
import pymysql.cursors
import sql_methods

hostname = 'localhost'
username = 'kavach'
password = 'zeitgeist13'
database = 'test_ipldb'
table = 'test_table'


class TestData(unittest.TestCase):
    """TestData class.

    Contains test cases for data module
    """
    def setUp(self):
        self.connection = pymysql.connect(host=hostname,
                                          user=username,
                                          passwd=password,
                                          db=database,
                                          cursorclass=pymysql.cursors.DictCursor)

    def tearDown(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "DROP TABLE " + table
                cursor.execute(sql)
        finally:
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


if __name__ == '__main__':
    unittest.main()
