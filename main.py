import tkinter as tk
from Gui import MainWindow
from Database import Database as db
import Excel

def main():
    app = MainWindow()
    app.mainloop()
    data_dict = app.data_model.get_data_dict()
    database = db(data_dict)

    # Search data in the database using the data_dict
    results = database.search_data_in_table()

    # Save the results to an Excel file
    Excel.write_results_to_excel(results, data_dict)

    database.disconnect_cursor()
    database.disconnect_connection()
    print("finish")

if __name__ == "__main__":
    main()
