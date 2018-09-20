import csv

table = 'test_table'

def create_table_populate(csv_path, connection):
    """Method to create table and populate it with values.

    Accepts csv file path and connection object.
    Creates a table in the MySQL database using the connection object.
    Reads the .csv file and creates entries for each value in the table created in the database.

    Arguments:
        csv_path (str): String which contains the path to the .csv file to the data set.
        connection (pymysql.connect object): SQL connector using which we execute all SQL queries.

    Returns:
        None.
    """
    with open(csv_path, 'r') as file_handler:
        csv_reader = csv.reader(file_handler)
        headers = next(csv_reader)
        header_sql_string = ""
        for header in headers:
            header_sql_string += header + " VARCHAR(50), "
        """Strip the extra spaces and commas from the ends of the string."""
        header_sql_string = header_sql_string.strip()
        header_sql_string = header_sql_string.strip(',')
        # print(header_sql_string)

        try:
            with connection.cursor() as cursor:
                """Create table."""
                sql = "CREATE TABLE " + table + " (" + header_sql_string + ")"
                cursor.execute(sql)

                """Loop to traverse through each row in the .csv file."""
                for row in csv_reader:
                    insert_sql_string = ""
                    for value in range(len(headers)):
                        insert_sql_string += "'" + row[value] + "', "
                    """Strip the extra spaces and commas from the ends of the string."""
                    insert_sql_string = insert_sql_string.strip()
                    insert_sql_string = insert_sql_string.strip(',')
                    # print(insert_sql_string)

                    insert_header_sql_string = ""
                    for header in headers:
                        insert_header_sql_string += header + ", "
                    """Strip the extra spaces and commas from the ends of the string."""
                    insert_header_sql_string = insert_header_sql_string.strip()
                    insert_header_sql_string = insert_header_sql_string.strip(',')
                    # print(insert_header_sql_string)

                    """Create entry."""
                    sql = "INSERT INTO " + \
                          table + \
                          " (" + insert_header_sql_string + ") VALUES (" + insert_sql_string + ")"
                    # print(sql)
                    cursor.execute(sql)
            """connection does not autocommit by default, so commit manually to save changes."""
            connection.commit()
        finally:
            pass


def read_records(query, connection):
    """Method to read records from a table in MySQL database.

    :param query: (str) String variable which stores the SQL query to be executed.
    :param connection: (pymysql connection object) SQL connector which is used to communicate with MySQL
    :return: result: (list) List of tuples each tuple containing one row from the SQL output.
    """
    with connection.cursor() as cursor:
        """Read records."""
        cursor.execute(query)
        result = cursor.fetchall()
    return result
