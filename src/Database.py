import pyodbc as odbc
import os

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'SERVER-REP'
DATABASE_NAME = 'CredidamNew'
USERNAME = 'valieanache'
PASSWORD = 'vali2023!'

class Database:
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.connection_string = self.get_connection_string()

    def get_connection_string(self):
        # Use environment variables to store sensitive information
        driver = os.environ.get('DB_DRIVER', DRIVER_NAME)
        server = os.environ.get('DB_SERVER', SERVER_NAME)
        database = os.environ.get('DB_DATABASE', DATABASE_NAME)
        uid = os.environ.get('DB_USERNAME', USERNAME)
        pwd = os.environ.get('DB_PASSWORD', PASSWORD)

        connection_string = f"""
            DRIVER={{{driver}}};
            SERVER={server};
            DATABASE={database};
            Trust_Connection=yes;
            uid={uid};
            pwd={pwd};
        """
        return connection_string

    def connect(self):
        self.connection = odbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def get_data_dict(self):
        return self.data_dict

    def search_data_in_table(self, data_dict):
        cursor = self.cursor

        data_dir = data_dict
        # Get the table name from the data_dict
        table_name = data_dir["Table"]

        # Use parameterized query to prevent SQL injection
        sql = f"SELECT * FROM {table_name} WHERE [MembruId] = ?"

        # Execute the query with the Artist_Code parameter
        artist_code = data_dir["Artist_Code"]
        cursor.execute(sql, artist_code)

        results = cursor.fetchall()

        return results

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()