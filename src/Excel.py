import openpyxl
import datetime

def write_results_to_excel(results, data_dict):
    # Create a new Excel workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active

    user_name = get_full_name(data_dict["Name"])
    table_name = data_dict["Table"]

    define_sheet_structure(sheet, results)
    concatenate_data(sheet)
    values_with_rows_dict = get_values_with_rows(sheet)
    mark_duplicates(values_with_rows_dict, sheet)


    # Save the Excel file
    wb.save(name_excel_file(table_name, user_name))

def name_excel_file(table_name, user_name):
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d%m%Y")

    # Extract the month and year from the table name
    month_year_string = table_name.split("_")[-1]

    # Extract the first three characters as the month
    month_string = month_year_string[:3].lower()

    # Extract the last four characters as the year
    year_string = month_year_string[-4:]

    final_name = f"{user_name}_exx__{month_string}{year_string}__________vali_{formatted_date}.xlsx"

    return final_name

def get_full_name(name_data):
    name_parts = [name_data[key] for key in name_data if name_data[key]]
    return " ".join(name_parts)

def define_sheet_structure(sheet, results):
     # Write the column headers to the Excel sheet
    column_headers = [
        "Functii",
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
        "PlaylistLiniiId",
        "Unicitate"
    ]
    for col_index, header in enumerate(column_headers, 1):
        sheet.cell(row=1, column=col_index, value=header)

    # Write the results to the Excel sheet
    for row_index, row in enumerate(results, 2):
        for col_index, value in enumerate(row, 2):
            sheet.cell(row=row_index, column=col_index, value=value)

def concatenate_data(sheet):
    columns_to_concatenate = [3, 7, 8, 9, 11, 12, 18, 19]

    # Iterate through all rows (excluding the first row) and concatenate cell values for the specified columns
    for row in sheet.iter_rows(min_row=2):
        concatenated_strings = ''
        for col_index in columns_to_concatenate:
            concatenated_strings += str(row[col_index-1].value)

        sheet.cell(row=row[0].row, column=21, value=concatenated_strings)

def get_values_with_rows(sheet):
    values_with_rows = {}

    for row_number, row in enumerate(sheet.iter_rows(min_row=2, min_col=21, values_only=True), start=2):
        cell_value = row[0]
        if cell_value not in values_with_rows:
            values_with_rows[cell_value] = [row_number]
        else:
            values_with_rows[cell_value].append(row_number)

    return values_with_rows

def mark_duplicates(values_with_rows, sheet):
    for rows in values_with_rows.values():
        if len(rows) >= 2:
            for row in rows[1:]:
                sheet.cell(row=row, column=1, value="Duplicat")