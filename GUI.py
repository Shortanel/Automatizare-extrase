import tkinter as tk

class DataModel:
    def __init__(self):
        self.name_data = ['', '', '', '']
        self.artist_code_data = ''
        self.date_from_data = ['', '']
        self.date_to_data = ['', '']

    def get_data_dict(self):
        return {
            "Name": {
                "LastName": self.name_data[0],
                "FirstName": self.name_data[1],
                "MiddleName": self.name_data[2],
                "Alias": self.name_data[3]
            },
            "Artist_Code": self.artist_code_data,
            "Date": {
                "Date_From": self.date_from_data,
                "Date_To": self.date_to_data
            }
        }

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Automatizare extrase")

        # creating a frame and assigning it to container
        container = tk.Frame(self)
        # specifying the region where the frame is packed in root
        container.pack()

        self.data_model = DataModel()

        self.name_frame = NameFrame(container, self.data_model)
        self.name_frame.pack(pady=10)

        self.artist_code_frame = ArtistCodeFrame(container, self.data_model)
        self.artist_code_frame.pack(pady=10)

        self.date_frame = DateFrame(container, self.data_model)
        self.date_frame.pack(pady=10)

        sendButton = tk.Button(container, text='Cauta', command=self.send_data_and_close)
        sendButton.pack(pady=10)

    def send_data_and_close(self):
        self.data_model.name_data = [entry.get() for entry in self.data_model.name_data]
        self.data_model.artist_code_data = self.data_model.artist_code_data.get()
        self.data_model.date_from_data = [entry.get() for entry in self.data_model.date_from_data]
        self.data_model.date_to_data = [entry.get() for entry in self.data_model.date_to_data]

        # Close the GUI after processing the data
        self.destroy()


class NameFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        label_texts = ["Nume artist", "Prenume artist", "Alt Prenume artist", "Alias artist"]
        entries = []
        for i, label_text in enumerate(label_texts):
            label = tk.Label(self, text=label_text)
            entry = tk.Entry(self)
            label.grid(row=i, column=0, padx=10, pady=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        self.data_model.name_data = entries

class ArtistCodeFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        label = tk.Label(self, text="Cod Artist")
        label.grid(row=0, column=0, padx=10, pady=5)

        artist_code_entry = tk.Entry(self)
        artist_code_entry.grid(row=0, column=1, padx=10, pady=5)

        self.data_model.artist_code_data = artist_code_entry

class DateFrame(tk.Frame):
    def __init__(self, parent, data_model):
        super().__init__(parent)
        self.data_model = data_model
        self.init_ui()

    def init_ui(self):
        month_names = ["iun","dec"]
        
        label_from = tk.Label(self, text="Data From")
        label_from.grid(row=0, column=0, padx=10, pady=5)

        month_from_var = tk.StringVar(self)
        month_from_var.set(month_names[0])  # Default value
        month_from_option = tk.OptionMenu(self, month_from_var, *month_names)
        month_from_option.grid(row=0, column=1, padx=10, pady=5)
        self.data_model.date_from_data[0] = month_from_var

        year_from_spin = tk.Spinbox(self, from_=2000, to=3000, width=5)
        year_from_spin.grid(row=0, column=2, padx=10, pady=5)
        self.data_model.date_from_data[1] = year_from_spin

        label_to = tk.Label(self, text="Data To")
        label_to.grid(row=1, column=0, padx=10, pady=5)

        month_to_var = tk.StringVar(self)
        month_to_var.set(month_names[0])  # Default value
        month_to_option = tk.OptionMenu(self, month_to_var, *month_names)
        month_to_option.grid(row=1, column=1, padx=10, pady=5)
        self.data_model.date_to_data[0] = month_to_var

        year_to_spin = tk.Spinbox(self, from_=2000, to=3000, width=5)
        year_to_spin.grid(row=1, column=2, padx=10, pady=5)
        self.data_model.date_to_data[1] = year_to_spin