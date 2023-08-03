from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,QPushButton, QFileDialog, 
    QProgressBar, QDialog, QMessageBox, QHBoxLayout, QRadioButton, QComboBox
)
from PyQt5.QtCore import QThread, pyqtSignal
from enum import Enum
import os

# Enum to represent the Name Type (Name or Alias)
class NameType(Enum):
    NAME = 1
    ALIAS = 2

# DataModel class to store user inputs
class DataModel:
    def __init__(self):
        # Initialize data_model with default values
        self.name_data = {
            "Name Type": NameType.NAME,
            "First Name": '',
            "Last Name": '',
            "Alias": ''
        }
        self.artist_code_data = ''
        self.search_table = ''

    def get_data_dict(self):
        # Return the data_model as a dictionary
        return {
            "Name": {
                "LastName": self.name_data['Last Name'],
                "FirstName": self.name_data['First Name'],
                "MiddleName": '',
                "Alias": self.name_data['Alias']
            },
            "Artist_Code": self.artist_code_data,
            "Table": self.search_table
        }

# Main Window class
class MainWindow(QMainWindow):
    def __init__(self, perform_search, excel_processor):
        super().__init__()
        self.setWindowTitle("Processing Data")
        self.data_model = DataModel()
        self.perform_search = perform_search
        self.excel_processor = excel_processor

        # Create a central widget and layout for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create and add the NameFrame, ArtistCodeFrame, and TableFrame widgets to the main layout
        self.name_frame = NameFrame(self.data_model)
        main_layout.addWidget(self.name_frame)

        self.artist_code_frame = ArtistCodeFrame(self.data_model)
        main_layout.addWidget(self.artist_code_frame)

        self.table_frame = TableFrame(self.data_model)
        main_layout.addWidget(self.table_frame)

        # Create a search button to trigger data processing
        search_button = QPushButton("Search", self)
        search_button.clicked.connect(self.on_search_button_clicked)
        main_layout.addWidget(search_button)

    def on_search_button_clicked(self):
        # Get the search table and store the data in the DataModel
        self.name_frame.store_data()
        self.artist_code_frame.store_data()
        self.table_frame.store_data()

        # Call the perform_search function with the data_model as an argument
        self.perform_search(self.data_model.get_data_dict())

        # Show the progress dialog while performing the search
        excel_thread = ExcelThread(self.excel_processor)
        progress_dialog = self.create_progress_dialog(excel_thread)
        excel_thread.start()
        progress_dialog.exec_()

        # After processing is done, show the finished window
        finished_window = self.create_finished_window()
        finished_window.exec_()

    def create_progress_dialog(self, excel_thread):
        progress_dialog = QDialog(self)
        progress_dialog.setWindowTitle("Processing")
        progress_dialog.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout(progress_dialog)

        label = QLabel("Processing... Please wait.")
        layout.addWidget(label)

        progress_bar = QProgressBar()
        progress_bar.setMaximum(0)
        progress_bar.setMaximum(100)
        layout.addWidget(progress_bar)

        excel_thread.progress_signal.connect(progress_bar.setValue)
        excel_thread.finished.connect(progress_dialog.accept)

        return progress_dialog

    def create_finished_window(self):
        finished_window = QDialog(self)
        finished_window.setWindowTitle("Process Completed")
        finished_window.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout(finished_window)

        label = QLabel("Processing completed successfully.")
        layout.addWidget(label)

        open_button = QPushButton("Open File")
        open_button.clicked.connect(self.on_open_button_clicked)
        layout.addWidget(open_button)

        close_button = QPushButton("Close")
        close_button.clicked.connect(finished_window.accept)
        layout.addWidget(close_button)

        return finished_window

    def on_open_button_clicked(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_name:
            self.excel_processor.open_excel_file(file_name)
            

# NameFrame class to handle the Name-related widgets
class NameFrame(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        # Create a layout for the NameFrame
        layout = QVBoxLayout(self)

        # Create a variable to store the Name Type (Name or Alias)
        self.name_type = NameType.NAME

        # Create radio buttons for Name and Alias options
        self.name_radio = QRadioButton("Name", self)
        self.name_radio.setObjectName("name_radio")  # Set object name for styling
        self.name_radio.toggled.connect(self.on_name_type_selected)

        self.alias_radio = QRadioButton("Nickname", self)
        self.alias_radio.setObjectName("alias_radio")  # Set object name for styling
        self.alias_radio.toggled.connect(self.on_name_type_selected)

        # Create the name entry widgets
        self.first_name_label = QLabel("First Name:", self)
        self.first_name_entry = QLineEdit(self)

        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_entry = QLineEdit(self)

        # Create the "Nickname" entry without a label
        self.alias_entry = QLineEdit(self)

        # Create a layout for the radio buttons
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.name_radio)
        radio_layout.addWidget(self.alias_radio)

        # Create a layout for the "First Name" and "Last Name" entries
        name_layout = QVBoxLayout()
        name_layout.addWidget(self.first_name_label)
        name_layout.addWidget(self.first_name_entry)
        name_layout.addWidget(self.last_name_label)
        name_layout.addWidget(self.last_name_entry)

        # Create a layout for the "Nickname" entry
        alias_layout = QVBoxLayout()
        alias_layout.addWidget(self.alias_entry)

        # Create a horizontal layout to align the radio buttons and the name entry widgets
        h_layout = QHBoxLayout()
        h_layout.addLayout(radio_layout)
        h_layout.addLayout(name_layout)
        h_layout.addLayout(alias_layout)

        layout.addLayout(h_layout)

        self.show_name_entries()

    def on_name_type_selected(self):
        selected_type = self.sender()  # Get the selected radio button

        if selected_type == self.name_radio:
            # Show the "Given Name" labels and entries, hide the "Nickname" entry
            self.first_name_label.show()
            self.first_name_entry.show()
            self.last_name_label.show()
            self.last_name_entry.show()
            self.alias_entry.hide()
        else:
            # Show the "Nickname" entry, hide the "Given Name" labels and entries
            self.first_name_label.hide()
            self.first_name_entry.hide()
            self.last_name_label.hide()
            self.last_name_entry.hide()
            self.alias_entry.show()

    def show_name_entries(self):
        # Show the "Given Name" labels and entries by default, hide the "Nickname" entry
        self.first_name_label.show()
        self.first_name_entry.show()
        self.last_name_label.show()
        self.last_name_entry.show()
        self.alias_entry.hide()

    def store_data(self):
        # Store the Name/Alias data in the data_model
        self.data_model.name_data['Name Type'] = self.name_type.value
        if self.name_type == NameType.NAME:
            # Handle empty input for Name entries
            first_name = self.first_name_entry.text()
            last_name = self.last_name_entry.text()
            if not first_name or not last_name:
                self.show_error_message("Please enter both First Name and Last Name.")
            else:
                self.data_model.name_data['First Name'] = first_name
                self.data_model.name_data['Last Name'] = last_name
                self.data_model.name_data['Alias'] = []
        elif self.name_type == NameType.ALIAS:
            # Handle empty input for Alias entry
            alias_entry_text = self.alias_entry.text()
            if not alias_entry_text:
                self.show_error_message("Please enter at least one Alias.")
            else:
                aliases = alias_entry_text.split(',')
                self.data_model.name_data['First Name'] = ''
                self.data_model.name_data['Last Name'] = ''
                self.data_model.name_data['Alias'] = [alias.strip() for alias in aliases]

    def show_error_message(self, error_message):
        QMessageBox.critical(self, "Error", error_message)

# ArtistCodeFrame class to handle the Artist Code entry
class ArtistCodeFrame(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        # Create a layout for the ArtistCodeFrame
        layout = QHBoxLayout(self)

        # Create a label and a QLineEdit for the Artist Code
        label = QLabel("Artist Code:", self)
        layout.addWidget(label)

        self.artist_code_entry = QLineEdit(self)
        layout.addWidget(self.artist_code_entry)

    def store_data(self):
        # Store the artist code in the data_model
        self.data_model.artist_code_data = self.artist_code_entry.text()

# TableFrame class to handle the search table selection
class TableFrame(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        # Create a layout for the TableFrame
        layout = QVBoxLayout(self)

        # Options for the Combobox
        table_options = [
            "Cautari_C_iun2023",
            "Cautari_C_dec2023",
            "PlayList_T42022_T12023",
            "PlayList_T2T3_2023"
        ]

        # Create a label for the Combobox
        label = QLabel("Select Table:", self)

        # Create a Combobox to select the table
        self.table_combobox = QComboBox(self)
        self.table_combobox.setEditable(True)  # Set the Combobox to be editable
        self.table_combobox.addItems(table_options)
        self.table_combobox.currentIndexChanged.connect(self.on_table_selected)

        # Add the label and Combobox to the layout
        layout.addWidget(label)
        layout.addWidget(self.table_combobox)

    def on_table_selected(self, index):
        # Update the data model with the selected table
        selected_table = self.table_combobox.currentText()
        self.data_model.search_table = selected_table
        print(f"Selected table: {selected_table}")

    def store_data(self):
        # Save the changes made to the selected option
        selected_table = self.table_combobox.currentText()
        self.data_model.search_table = selected_table

class ExcelThread(QThread):
    progress_signal = pyqtSignal(int)  # Custom signal to send progress updates

    def __init__(self, excel_module):
        super().__init__()
        self.excel_module = excel_module

    def run(self):
        try:
            # Perform the search and Excel processing in the thread
            self.excel_module.perform_search(self.data_model.get_data_dict(), self.progress_signal)
        except Exception as e:
            print(f"An error occurred in the Excel thread: {str(e)}")