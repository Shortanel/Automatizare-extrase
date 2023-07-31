import openpyxl
import datetime

def write_results_to_excel(results, data_dic):
    # Create a new Excel workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Write the column headers to the Excel sheet
    column_headers = [
        "PlaylistId",
        "MelodieId",
        "MembruId",
        "Title",
        "Interpret",
        "Mins",
        "Sec",
        "Denumire",
        "Utilizator",
        "DataS",
        "DataF",
        "uuid",
        "valsec",
        "valsec_Cablu",
        "valsec_Amb",
        "valsec_CP",
        "sursa",
        "domeniu",
        "PlaylistLiniiId"
    ]
    for col_index, header in enumerate(column_headers, 1):
        sheet.cell(row=1, column=col_index, value=header)

    # Write the results to the Excel sheet
    for row_index, row in enumerate(results, 2):
        for col_index, value in enumerate(row, 1):
            sheet.cell(row=row_index, column=col_index, value=value)
            print(value)

    # Save the Excel file
    wb.save(name_excel_file(data_dic))

def name_excel_file(data_dict):

    final_name =''
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d%m%Y")

    name = {
        "LastName": data_dict["Name"]["LastName"],
        "MiddleName": data_dict["Name"]["MiddleName"],
        "FirstName": data_dict["Name"]["FirstName"],
        "Alias": data_dict["Name"]["Alias"]
    }
    states = name_state(name)
    keys_list = list(name.keys())
    for i in states:
        if states[i] ==1:
            final_name += name[keys_list[i]] + ' '
    
    return final_name + '_exx__' + data_dict["Date"]["Date_To"][0] + data_dict["Date"]["Date_To"][1] + '__________vali' + formatted_date + '.xlsx'

def name_state(name):
    c_name = [0,0,0,0]
    keys_list = list(name.keys())


    for p_name in name:
        if name[p_name] != '':
            c_name[keys_list.index(p_name)] = 1

    return c_name
        

