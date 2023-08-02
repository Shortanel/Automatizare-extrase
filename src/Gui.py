import tkinter as tk
from tkinter import ttk, messagebox

from enum import Enum

# Enum to represent the Name Type (Name or Alias)
class NameType(Enum):
    NAME = 1
    ALIAS = 2

# Main Window class
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Processing Data")

        # Create a data model to store user inputs
        self.data_model = DataModel()

        # Create and pack the NameFrame, ArtistCodeFrame, and TableFrame widgets
        self.name_frame = NameFrame(self, self.data_model)
        self.name_frame.pack(pady=10)

        self.artist_code_frame = ArtistCodeFrame(self, self.data_model)
        self.artist_code_frame.pack(pady=10)

        self.table_frame = TableFrame(self, self.data_model)
        self.table_frame.pack(pady=10)

        # Create a search button to trigger data saving
        search_button = tk.Button(self, text='Search', command=self.save_data)
        search_button.pack(pady=10)

    def save_data(self):
        # Get the search table and store the data in the DataModel
        self.name_frame.store_data()
        self.artist_code_frame.store_data()
        self.table_frame.store_data()

        # You can access the data_model dictionary here and perform any operations you need
        data_dict = self.data_model.get_data_dict()
        print(data_dict)

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

# NameFrame class to handle the Name-related widgets
class NameFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        # Create a variable to store the Name Type (Name or Alias)
        self.name_type = tk.IntVar(value=NameType.NAME.value)

        # Create radio buttons for Name and Alias options
        name_radio = tk.Radiobutton(self, text="Name", variable=self.name_type, value=NameType.NAME.value, command=self.on_name_type_selected)
        name_radio.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        alias_radio = tk.Radiobutton(self, text="Alias", variable=self.name_type, value=NameType.ALIAS.value, command=self.on_name_type_selected)
        alias_radio.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Create the name entry widgets
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(row=0, column=2, padx=10, pady=2, sticky="w")
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(row=1, column=2, padx=10, pady=2, sticky="w")
        self.alias_entry = tk.Entry(self)
        self.alias_entry.grid(row=0, column=2, padx=10, pady=2, sticky="w")

        self.show_name_entries()

    def on_name_type_selected(self):
        # Handle the Name/Alias selection
        selected_type = NameType(self.name_type.get())
        if selected_type == NameType.NAME:
            self.show_name_entries()
        elif selected_type == NameType.ALIAS:
            self.hide_name_entries()

    def show_name_entries(self):
        # Show the Name entry fields
        self.first_name_entry.grid(row=0, column=2, padx=10, pady=2, sticky="w")
        self.last_name_entry.grid(row=1, column=2, padx=10, pady=2, sticky="w")
        self.alias_entry.grid_forget()

    def hide_name_entries(self):
        # Show the Alias entry field
        self.first_name_entry.grid_forget()
        self.last_name_entry.grid_forget()
        self.alias_entry.grid(row=0, column=2, padx=10, pady=2, sticky="w")

    def store_data(self):
        # Store the Name/Alias data in the data_model
        self.data_model.name_data['Name Type'] = self.name_type.get()
        if self.name_type.get() == NameType.NAME.value:
            # Handle empty input for Name entries
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            if not first_name or not last_name:
                tk.messagebox.showerror("Error", "Please enter both First Name and Last Name.")
            else:
                self.data_model.name_data['First Name'] = first_name
                self.data_model.name_data['Last Name'] = last_name
                self.data_model.name_data['Alias'] = []
        elif self.name_type.get() == NameType.ALIAS.value:
            # Handle empty input for Alias entry
            alias_entry_text = self.alias_entry.get()
            if not alias_entry_text:
                tk.messagebox.showerror("Error", "Please enter at least one Alias.")
            else:
                aliases = alias_entry_text.split(',')
                self.data_model.name_data['First Name'] = ''
                self.data_model.name_data['Last Name'] = ''
                self.data_model.name_data['Alias'] = [alias.strip() for alias in aliases]

# ArtistCodeFrame class to handle the Artist Code entry
class ArtistCodeFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        # Create a label and an Entry widget for the Artist Code
        label = tk.Label(self, text="Artist Code")
        label.pack(side=tk.LEFT, padx=10, pady=5)

        # Validate the input to allow only numeric characters
        vcmd = (self.register(self.validate_artist_code), '%P')
        self.artist_code_entry = tk.Entry(self, validate='key', validatecommand=vcmd)
        self.artist_code_entry.pack(side=tk.LEFT, padx=10, pady=5)

    def validate_artist_code(self, input_text):
        try:
            # Check if the input contains only numeric characters
            if not input_text.isdigit():
                # Raise a ValueError if the input is not numeric
                raise ValueError("Invalid input: Artist Code must contain only numeric characters.")
            return True
        except ValueError as e:
            # Show an error message to the user in case of invalid input
            tk.messagebox.showerror("Error", str(e))
            return False

    def store_data(self):
        # Store the artist code in the data_model
        self.data_model.artist_code_data = self.artist_code_entry.get()

# TableFrame class to handle the search table selection
class TableFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        # Options for the Combobox
        table_options = [
            "Cautari_C_iun2023",
            "Cautari_C_dec2023",
            "PlayList_T42022_T12023",
            "PlayList_T2T3_2023"
        ]

        # Create a label for the Combobox
        label = tk.Label(self, text="Select Table:", anchor=tk.W)
        label.pack(side=tk.LEFT, padx=10, pady=5)

        # Create a Combobox to select the table
        self.table_combobox = ttk.Combobox(self, values=table_options)
        self.table_combobox.pack(side=tk.LEFT, padx=10, pady=5)
        self.table_combobox.set(table_options[0])  # Set the first option as default

        # Bind the FocusOut event to update the data model when the combobox loses focus
        self.table_combobox.bind("<FocusOut>", self.on_table_selected)

    def on_table_selected(self, event):
        # Update the data model with the selected table
        selected_table = self.table_combobox.get()
        self.data_model.search_table = selected_table
        print(f"Selected table: {selected_table}")

    def store_data(self):
        # Save the changes made to the selected option
        selected_table = self.table_combobox.get()
        self.data_model.search_table = selected_table

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
