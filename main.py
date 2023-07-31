import tkinter as tk
from Gui import MainWindow
from Database import Database as db
import Excel

def main():
    app = MainWindow()

    app.mainloop()

    # After the GUI closes, get the data from the data model in the MainWindow
    data_dict = app.data_model.get_data_dict()
    database = db(data_dict)



    # Search data in the database using the data_dict
    results = database.search_data_in_table()

    # Save the results to an Excel file
    Excel.write_results_to_excel(results, data_dict)

    database.disconnect_cursor()
    database.disconnect_connection()



if __name__ == "__main__":
    main()
