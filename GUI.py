import tkinter as tk

class Gui:

    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Automatizare extrase")
        self.window.resizable(False, False)
        self.window.config(bg="white")

        self.frame = tk.Frame(self.window)
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def get_lastname(self):
        return self.last_name_entry.get()

    def get_firstname(self):
        return self.first_name_entry.get()

    def get_middlename(self):
        return self.middle_name_entry.get()

    def get_alias(self):
        return self.alias_name_entry.get()

    def get_artistcode(self):
        return self.artist_name_entry.get()

    def get_monthfrom(self):
        return self.month_from_entry.get()

    def get_yearfrom(self):
        return self.year_from_entry.get()

    def get_monthto(self):
        return self.month_to_entry.get()
    
    def get_yearto(self):
        return self.year_to_entry.get()
    
    def create_name_frame(frame):
        name_frame = tk.LabelFrame(frame, text="Date Artist")
        name_frame.grid(row= 0, column=0, padx=20, pady=20)
    
    def create_data_frame(frame):
        data_frame = tk.LabelFrame(frame, text = "Date",)
        data_frame.grid(row= 1, column=0, sticky= 'news', padx=20, pady=20)

    def create_artcode_frame(frame):
        artist_code_frame = tk.LabelFrame(frame, text='Cod Artist')
        artist_code_frame.grid(row=0, column=0,sticky='news', padx=30, pady= 20)
        artist_code_entry = tk.Entry(artist_code_frame)
        artist_code_entry.grid(row=0, column=0)

    def create_date_frame(frame):
        date_frame = tk.LabelFrame(frame, text='Intervalul de timp')
        date_frame.grid(row=0, column=2,sticky='news', padx=30, pady= 10)

    def create_lastname_lb(frame,self):
        last_name_label = tk.Label(frame, text="Nume artist")
        last_name_label.grid(row=0, column=0)
        self.last_name_entry = tk.Entry(frame)
        self.last_name_entry.grid(row=1, column=0)
    
    def create_firstname_lb(frame,self):
        first_name_label = tk.Label(frame, text="Nume artist")
        first_name_label.grid(row=0, column=0)
        self.first_name_entry = tk.Entry(frame)
        self.first_name_entry.grid(row=1, column=0)
    
    def create_middlename_lb(frame,self):
        middle_name_label = tk.Label(frame, text="Nume artist")
        middle_name_label.grid(row=0, column=0)
        self.middle_name_entry = tk.Entry(frame)
        self.middle_name_entry.grid(row=1, column=0)
    
    def create_middlename_lb(frame,self):
        middle_name_label = tk.Label(frame, text="Nume artist")
        middle_name_label.grid(row=0, column=0)
        self.middle_name_entry = tk.Entry(frame)
        self.middle_name_entry.grid(row=1, column=0)
    
    def create_middlename_lb(frame,self):
        middle_name_label = tk.Label(frame, text="Nume artist")
        middle_name_label.grid(row=0, column=0)
        self.middle_name_entry = tk.Entry(frame)
        self.middle_name_entry.grid(row=1, column=0)

    def create_button(frame,self):
       button = tk.Button(frame, text="Genereaza", command= self.send_data)
       button.grid(row=3, column=0, sticky='news', padx=20, pady=10)

    def send_data(self):
        data = [self.get_lastname,
                self.get_firstname, 
                self.get_middlename,
                self.get_alias,
                self.get_artistcode,
                self.get_monthfrom,
                self.get_yearfrom,
                self.get_monthto,
                self.get_yearto]
        return data 

    def interface(self):
        self.create_name_frame(self.frame)
        self.create_data_frame(self.frame)
        self.create_artcode_frame(self.frame)