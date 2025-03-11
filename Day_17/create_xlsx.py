import xlsxwriter

workbook = xlsxwriter.Workbook('employees.xlsx')
worksheet = workbook.add_worksheet()

employees = (
    ['Name', 'Age'], 
    ['John Smith', 33],
    ['Harold Johnson', 44],
    ['Mary Brown', 25],
    ['James Lee', 37]
)

row = 0

for name, age in employees:
    worksheet.write(row, 0, name)
    worksheet.write(row, 1, age)
    row += 1

    worksheet.write(row, 0, 'Average Age')
    worksheet.write(row, 1, '=AVERAGE(B1:B' + str(row-1)+')')

    workbook.close()