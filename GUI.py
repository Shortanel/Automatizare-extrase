import tkinter as tk

name_data = ['', '', '', '']
artist_code_data = 0
date_from_data =['', '']
date_to_data = ['', '']



class Mainwindow(tk.Tk):

    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Automatizare extrase")

        # creating a frame and assigning it to container
        container = tk.Frame(self)
        # specifying the region where the frame is packed in root
        container.pack()

        labelFrame = tk.LabelFrame(container)
        labelFrame.grid(row=0, column=0)


        # configuring the location of the container using grid
        container.grid_rowconfigure(0)
        container.grid_columnconfigure(0)
    
        sendButton = tk.Button(labelFrame, text= 'Cauta', command= lambda: controller.send_data())
        sendButton.grid(row=3, column= 0)
        NameFrame(labelFrame)
        ArtistCodeFrame(labelFrame)
        DateFrame(labelFrame)

        print(artist_code_data)

def NameFrame(frame):
    labelFrame = tk.LabelFrame(frame, text="Date Personale")
    labelFrame.grid(row=0, column=0, sticky="news", padx=20, pady=20)

    #Last Name   
    last_name_label = tk.Label(labelFrame, text="Nume artist")
    last_name_label.grid(row=0, column=0,padx=30, pady=5)
    last_name_entry = tk.Entry(labelFrame)
    last_name_entry.grid(row=1, column=0,padx=30, pady=5)

    name_data[0] = last_name_entry

    #First Name 
    first_name_label = tk.Label(labelFrame, text="Prenume artist")
    first_name_label.grid(row=0, column=1,padx=30, pady=5)
    first_name_entry = tk.Entry(labelFrame)
    first_name_entry.grid(row=1, column=1,padx=30, pady=5)

    name_data[1] = first_name_entry

    #Middle Name
    middle_name_label = tk.Label(labelFrame, text="Alt Prenume artist")
    middle_name_label.grid(row=0, column=2,padx=30, pady=5)
    middle_name_entry = tk.Entry(labelFrame)
    middle_name_entry.grid(row=1, column=2,padx=30, pady=5)

    name_data[2] = middle_name_entry

    #Alias
    alias_label = tk.Label(labelFrame, text="Alias artist")
    alias_label.grid(row=0, column=3,padx=30, pady=5)
    alias_entry = tk.Entry(labelFrame)
    alias_entry.grid(row=1, column=3,padx=30, pady=5)

    name_data[3] = alias_entry

def ArtistCodeFrame(frame):
    labelFrame = tk.LabelFrame(frame, text="Cod Artist")
    labelFrame.grid(row=1, column=0, padx=20, pady= 20)
    artist_code_entry = tk.Entry(labelFrame)
    artist_code_entry.grid(row=1,column=1, sticky='ew')

    frame.grid_columnconfigure((0,1), weight=1)
    labelFrame.grid_columnconfigure((0, 2), weight=1)

    data = artist_code_entry
    return data

def DateFrame(frame):
    labelFrame = tk.LabelFrame(frame, text="Data")
    labelFrame.grid(row=2, column=0, sticky="nsew",padx=20, pady= 20)
    
    #Month from
    month_from_label = tk.Label(labelFrame, text="Luna")
    month_from_label.grid(row=0, column=0)
    month_from_spin = tk.Spinbox(labelFrame, from_=1, to= 12, width= 5)
    month_from_spin.grid(row=1, column=0,padx=10, pady= 10)

    date_from_data[0] = month_from_spin

    #Year from        
    year_from_label = tk.Label(labelFrame, text="An")
    year_from_label.grid(row=0, column=1)
    year_from_spin = tk.Spinbox(labelFrame, from_=1900, to_=3000, width= 5)
    year_from_spin.grid(row=1, column=1,padx=10, pady= 10)

    date_from_data[1] = year_from_spin


    #Month to
    month_to_label = tk.Label(labelFrame, text="Luna")
    month_to_label.grid(row=0, column=2)
    month_to_spin = tk.Spinbox(labelFrame, from_=1, to= 12, width= 5)
    month_to_spin.grid(row=1, column=2,padx=10, pady= 10)

    date_to_data[0] = month_to_spin
    
    #Year to
    year_to_label = tk.Label(labelFrame, text="An")
    year_to_label.grid(row=0, column=3)
    year_to_spin = tk.Spinbox(labelFrame, from_=1900, to_=3000, width= 5)
    year_to_spin.grid(row=1, column=3 ,padx=10, pady= 10)

    date_to_data[1] = year_to_spin

def send_data():
    
    dict["Name"]["LastName"] = name_data[0]
    dict["Name"]["FirstName"] = name_data[1]
    dict["Name"]["MiddleName"] = name_data[2]
    dict["Name"]["Alias"] = name_data[3]
    dict["Artist_Code"] = str(artist_code_data)
    dict["Date"]["Date_From"][0] = date_from_data[0]
    dict["Date"]["Date_From"][1] = date_from_data[1]
    dict["Date"]["Date_To"][0] = date_from_data[0]
    dict["Date"]["Date_To"][1] = date_from_data[1]

    print(dict["Artist_Code"])

    return dict



