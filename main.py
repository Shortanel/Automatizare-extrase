import tkinter as tk
from src.Gui import MainWindow
from src import Database as db
from src import Excel

def main():
    # Create and run the GUI
    app = MainWindow()
    app.mainloop()

    # Get data from the GUI's data model
    data_dict = app.data_model.get_data_dict()

    try:
        # Connect to the database using a context manager
        with db(data_dict) as database:
            # Search data in the database using the data_dict
            results = database.search_data_in_table()

            # Save the results to an Excel file using a context manager
            with Excel.create_excel_writer("results.xlsx") as excel_writer:
                Excel.write_results_to_excel(results, data_dict, excel_writer)

        print("Process completed successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
