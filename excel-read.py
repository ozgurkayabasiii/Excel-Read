import xlrd

loc = ("./excelname.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
row_count = sheet.nrows
column_count = sheet.ncols

for row in range(1, row_count):
    print(row)
