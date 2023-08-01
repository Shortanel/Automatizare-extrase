import pypyodbc as odc

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'SERVER-REP'
DATABASE_NAME = 'CredidamNew'

class Database:
    def __init__(self, data_dict):
        
        connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
        uid=valieanache;
        pwd=vali2023!;
    """
        self.data_dict = data_dict
        self.connection = odc.connect(connection_string)
        self.cursor = self.connection.cursor()
    
    def disconnect_connection(self):
        self.connection.close()

    def disconnect_cursor(self):
        self.cursor.close()
    
    def get_data_dict(self):
        return self.data_dict 

    def search_data_in_table(self):
        cursor = self.cursor

        data_dir = self.get_data_dict()
        # Get the table name from the data_dict
        table_name = data_dir["Table"]


        # Modify the SQL statement to search for rows with MembruId = Artist_Code
        sql = f"""SELECT * FROM {table_name} WHERE [MembruId] = ?"""

        # Execute the query with the Artist_Code parameter
        artist_code = data_dir["Artist_Code"]
        cursor.execute(sql, (artist_code,))

        results = cursor.fetchall()
        
        return results




        

