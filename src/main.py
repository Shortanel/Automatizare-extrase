import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from Database import Database
import Gui
from Excel import ExcelProcessor

def perform_search(data_dict, progress_callback=None):
    try:
        with Database(data_dict) as database:
            results = database.search_data_in_table(data_dict)

        # Call the ExcelProcessor method to handle saving the search results to an Excel file
        ExcelProcessor.process_search_results(results, data_dict)

        if progress_callback:
            progress_callback.emit(100)

        print("Search completed successfully.")
    except Exception as e:
        error_message = "An error occurred: " + str(e)
        print(error_message)
        QMessageBox.critical(None, "Error", error_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    data_model = Gui.DataModel
    excel_thread = Gui.ExcelThread(ExcelProcessor)
    excel_thread.finished.connect(app.quit)

    window = Gui.MainWindow(perform_search, ExcelProcessor)
    window.show()
    sys.exit(app.exec_())