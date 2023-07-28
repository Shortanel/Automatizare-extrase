import Gui

send_data = {
    "Name" : {
        "LastName" : "",
        "FirstName" : "",
        "MiddleName" : "",
        "Alias" : "",
    },
    "Artist_Code" : "",
    "Date" : {
        "Date_From" : [0,0],
        "Date_To" : [0,0],
    }
}

if __name__ == "__main__":
    App = Gui.Mainwindow(send_data)
    print(send_data["Artist_Code"])

    App.mainloop()

