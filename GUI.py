import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Search GUI")

        self.data_model = DataModel()

        self.name_frame = NameFrame(self, self.data_model)
        self.name_frame.pack(pady=10)

        self.artist_code_frame = ArtistCodeFrame(self, self.data_model)
        self.artist_code_frame.pack(pady=10)

        self.table_frame = TableFrame(self, self.data_model)
        self.table_frame.pack(pady=10)

        search_button = tk.Button(self, text='Search', command=self.save_data)
        search_button.pack(pady=10)

    def save_data(self):
        # Get the search table and store the data in the DataModel
        self.name_frame.store_data()
        self.artist_code_frame.store_data()

        self.destroy()

class DataModel:
    def __init__(self):
        self.name_data = ['', '', '', '']
        self.artist_code_data = ''
        self.search_table = ''
    
    def get_data_dict(self):
        return {
            "Name": {
                "LastName": self.name_data[0],
                "FirstName": self.name_data[1],
                "MiddleName": self.name_data[2],
                "Alias": self.name_data[3]
            },
            "Artist_Code": self.artist_code_data,
            "Table": self.search_table
        }

class NameFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        label_texts = ["Last Name", "First Name", "Middle Name", "Alias"]
        self.entries = []
        for i, label_text in enumerate(label_texts):
            label = tk.Label(self, text=label_text)
            entry = tk.Entry(self)
            label.grid(row=i, column=0, padx=10, pady=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

    def store_data(self):
        self.data_model.name_data = [entry.get() for entry in self.entries]

class ArtistCodeFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        label = tk.Label(self, text="Artist Code")
        label.grid(row=0, column=0, padx=10, pady=5)

        self.artist_code_entry = tk.Entry(self)
        self.artist_code_entry.grid(row=0, column=1, padx=10, pady=5)

    def store_data(self):
        self.data_model.artist_code_data = self.artist_code_entry.get()

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

        label = tk.Label(self, text="Select Table:")
        label.pack(side=tk.LEFT, padx=10, pady=5)

        # Create a Combobox to select the table
        self.table_combobox = ttk.Combobox(self, values=table_options)
        self.table_combobox.pack(side=tk.LEFT, padx=10, pady=5)
        self.table_combobox.set("Select a table")  # Set a default text

        # Bind the Combobox selection to update the data model
        self.table_combobox.bind("<<ComboboxSelected>>", self.on_table_selected)

        save_button = tk.Button(self, text="Save Changes", command=self.save_changes)
        save_button.pack(side=tk.LEFT, padx=10, pady=5)

    def on_table_selected(self, event):
        # Update the data model with the selected table
        selected_table = event.widget.get()
        self.data_model.search_table = selected_table
        print(f"Selected table: {selected_table}")

    def save_changes(self):
        # Save the changes made to the selected option
        selected_table = self.table_combobox.get()
        self.data_model.search_table = selected_table