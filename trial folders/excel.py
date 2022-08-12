from openpyxl import Workbook

wb = Workbook()
ws = wb.worksheets[0]

your_list = [5,7,8]
row_number = 3
your_column = 3
for i, value in enumerate(your_list, start=row_number):
    ws.cell(row=i, column=your_column).value = value

wb.save("column_values.xlsx")