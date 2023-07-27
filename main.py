import tkinter as tk 
import os
import openpyxl 
import pyodbc as odbc

def enter_data():
    #Artist info entered
    lastname = last_name_entry.get()
    firstname = first_name_entry.get()
    middlename = middle_name_entry.get()
    alias = alias_entry.get()
    artistcode =artist_code_entry.get()
    monthfrom = month_from_spin.get()
    yearfrom = year_from_spin.get()
    monthto = month_to_spin.get()
    yearto = year_to_spin.get()

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'SERVER-REP'
DATABASE_NAME = 'CredidamNew'


connection_string = f"""
                    DRIVER={{{DRIVER_NAME}}};
                    SERVER={SERVER_NAME};
                    DATABASE={DATABASE_NAME};
                    Trust_Connection=no; 
                    uid=valieanache;
                    pwd=vali2023!;
"""
conn = odbc.connect(connection_string)
print(conn)

window = tk.Tk()
window.title("Automatizare extrase")

frame = tk.Frame(window)
frame.pack()

#Artist data frame
name_data_frame = tk.LabelFrame(frame, text="Date Artist")
name_data_frame.grid(row= 0, column=0, padx=20, pady=20)

    #Last Name
last_name_label = tk.Label(name_data_frame, text="Nume artist")
last_name_label.grid(row=0, column=0)
last_name_entry = tk.Entry(name_data_frame)
last_name_entry.grid(row=1, column=0)

    #First Name
first_name_label = tk.Label(name_data_frame, text="Prenume artist")
first_name_label.grid(row=0, column=1)
first_name_entry = tk.Entry(name_data_frame)
first_name_entry.grid(row=1, column=1)

    #Middle Name
middle_name_label = tk.Label(name_data_frame, text="Alt prenume artist")
middle_name_label.grid(row=0, column=2)
middle_name_entry = tk.Entry(name_data_frame)
middle_name_entry.grid(row=1, column=2)

    #Alias
alias_label = tk.Label(name_data_frame, text="Alias artist")
alias_label.grid(row=0, column=4)
alias_entry = tk.Entry(name_data_frame)
alias_entry.grid(row=1, column=4)

#Useful data frame
data_frame = tk.LabelFrame(frame, text = "Date",)
data_frame.grid(row= 1, column=0, sticky= 'news', padx=20, pady=20)

    #Artist code frame
artist_code_frame = tk.LabelFrame(data_frame, text='Cod Artist')
artist_code_frame.grid(row=0, column=0,sticky='news', padx=30, pady= 20)
artist_code_entry = tk.Entry(artist_code_frame)
artist_code_entry.grid(row=0, column=0)

    #Date frame
date_frame = tk.LabelFrame(data_frame, text='Intervalul de timp')
date_frame.grid(row=0, column=2,sticky='news', padx=30, pady= 10)

        #Month from
month_from_label = tk.Label(date_frame, text="Luna")
month_from_label.grid(row=0, column=0)
month_from_spin = tk.Spinbox(date_frame, from_=1, to= 12, width= 5)
month_from_spin.grid(row=1, column=0)

        #Year from
year_from_label = tk.Label(date_frame, text="An")
year_from_label.grid(row=0, column=1)
year_from_spin = tk.Spinbox(date_frame, from_=1900, to_=3000, width= 5)
year_from_spin.grid(row=1, column=1)

        #Month to
month_to_label = tk.Label(date_frame, text="Luna")
month_to_label.grid(row=0, column=2)
month_to_spin = tk.Spinbox(date_frame, from_=1, to= 12, width= 5)
month_to_spin.grid(row=1, column=2)

        #Year to
year_to_label = tk.Label(date_frame, text="An")
year_to_label.grid(row=0, column=3)
year_to_spin = tk.Spinbox(date_frame, from_=1900, to_=3000, width= 5)
year_to_spin.grid(row=1, column=3)



for widget in name_data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in artist_code_frame.winfo_children():
    widget.grid_configure(padx= 10, pady=5)

#for widget in date_frame.winfo_children():
    #widget.grid_configure(padx=5, pady=1)

#for widget in data_frame.winfo_children():
    #widget.grid_configure(padx=10, pady=5)

#Button
button = tk.Button(frame, text="Genereaza", command= enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=")

window.mainloop()

